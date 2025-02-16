# Torn API Python Package Documentation

Welcome to the documentation for the Torn API Python package. This package provides a convenient wrapper around Torn's v2 API so that you can easily access player, faction, market, racing, forum, and Torn data.

Use the navigation on the left to explore installation instructions, usage examples, and a complete API reference.

# Installation

To install the package, you can use Poetry. First, clone the repository, then install the dependencies:

```bash
git clone https://github.com/dspencej/torn-api
cd torn-api
poetry install
```

If you are using the package in your own project, simply add it as a dependency.

> **Note:** Ensure you are using Python 3.12 or higher.

# Usage

Below is a simple example of how to use the Torn API Python package:

```python
from torn_api import TornAPIClient

# Initialize the client with your Torn API key.
client = TornAPIClient(api_key="YOUR_API_KEY")

# Fetch basic user data.
user_data = client.get_user(selections="basic")
print("User Data:", user_data)

# Get detailed attacks.
attacks = client.get_user_attacks(selections="default")
print("Attacks:", attacks)
```

For testing purposes, you can run the integration tests which are located in the `tests/` directory. Make sure to set the environment variable `TORN_API_KEY` before running the tests:

```bash
export TORN_API_KEY="your_actual_api_key"
python -m unittest tests/test.py
```
