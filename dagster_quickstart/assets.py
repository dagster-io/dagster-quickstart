import json
import requests
import re

import pandas as pd

from dagster import (
    MaterializeResult,
    MetadataValue,
    asset,
)
from dagster_quickstart.configurations import NaptanConfig

def make_point(lng,lat):
  return json.dumps({'type':'Point','coordinates':[float(lng),float(lat)]})

def bq_names(raw_name):
  bq_name = re.sub(r'\W+', '', raw_name)
  return bq_name

@asset
def get_naptan(config: NaptanConfig):
    """Get Naptan dataset."""
    naptan = requests.get("https://naptan.api.dft.gov.uk/v1/access-nodes?dataFormat=CSV").content.decode('utf-8')

    with open(config.raw_path, "w") as f:
        f.write(naptan)
        
@asset(deps=[get_naptan])
def enrich_naptan(config: NaptanConfig) -> MaterializeResult:
    """Enrich Naptan dataset with GeoJson."""
    df = pd.read_csv(config.raw_path, dtype = 'str')
    df['geom'] = df.apply(lambda x: make_point(x['Longitude'], x['Latitude']), axis=1)
    df.rename(columns=bq_names).head()
    df.to_csv(config.enriched_path, index = False)

    return MaterializeResult(
        metadata={
            "preview": MetadataValue.md(str(df.head().to_markdown())),
        }
    )
