from dagster import Config


class NaptanConfig(Config):
    raw_path: str = "Stops.csv"
    enriched_path: str = "EnrichedStops.csv"
