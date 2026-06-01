"""
Google Autocomplete API: A Quick Start Example
See more at: https://apify.com/johnvc/google-autocomplete-api?fpr=9n7kx3
Input schema: https://apify.com/johnvc/google-autocomplete-api/input-schema?fpr=9n7kx3

This script shows how to call the Google Autocomplete API on Apify from Python
and read its structured JSON output. It returns the suggestions Google shows as
you type, for each query. Inputs are kept small so your first call stays cheap.

Get your free Apify API key at: https://apify.com?fpr=9n7kx3
"""

import os
from dotenv import load_dotenv
from apify_client import ApifyClient

load_dotenv()

# Initialize the Apify client with your API token (read from .env)
client = ApifyClient(os.getenv("APIFY_API_TOKEN"))

# Build the Actor input.
# Inputs are kept small (one query) to keep this first run inexpensive:
# you are billed per suggestion returned. Pass more queries to expand a list.
run_input = {
    "queries": ["coffee near"],  # one or more partial queries to autocomplete
    "gl": "us",                  # country for localization
    "hl": "en",                  # interface language
}

# Run the Actor and wait for it to finish
run = client.actor("johnvc/google-autocomplete-api").call(run_input=run_input)
if run is None:
    raise SystemExit("The Actor run did not return a result.")

# Read structured results from the run's default dataset
# (apify-client 3.x returns a Run object; use .default_dataset_id, not run["..."])
items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"Returned {len(items)} suggestion(s).\n")

# Show each suggestion with its rank and source query.
for item in items:
    print(f"{item.get('position')}. [{item.get('query')}] {item.get('value')}")
