import os
import unittest

from dagster_quickstart.assets import hackernews_top_stories
from dagster_quickstart.configurations import HNStoriesConfig
from unittest import mock


@mock.patch("requests.get")
def test_hackernews_top_stories(mock_get):
    mock_response = mock.Mock()
    mock_response.json.return_value = {
        "title": "Mock Title",
        "by": "John Smith",
        "url": "www.example.com",
    }
    mock_get.return_value = mock_response

    config = HNStoriesConfig(
        hn_top_story_ids_path="dagster_quickstart_tests/hackernews_top_story_ids.json",
        hn_top_stories_path="dagster_quickstart_tests/hackernews_top_stories.csv",
    )

    materialized_results = hackernews_top_stories(config)

    assert materialized_results.metadata.get("num_records") == 10

    os.remove("dagster_quickstart_tests/hackernews_top_stories.csv")


if __name__ == "__main__":
    unittest.main()
