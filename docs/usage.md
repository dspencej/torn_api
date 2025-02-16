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
