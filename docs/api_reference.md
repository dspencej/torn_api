# API Reference

This section describes the available methods on the `TornAPIClient`.

## User Endpoints

- **get_user_attacks(selections: str = "default")**  
  Retrieve detailed attack information.

- **get_user_attacksfull(selections: str = "default")**  
  Retrieve simplified attack information.

- **get_user_bounties(selections: str = "default")**  
  Retrieve bounties placed on the user.

- **get_user_bounties_by_id(user_id: int, selections: str = "default")**  
  Retrieve bounties for a specific user.

- **get_user_calendar()**  
  Retrieve the competition's event start time.

- *(… and more. See the source code in `src/torn_api/client.py` for a full list of methods.)*

## Faction Endpoints

- **get_faction_applications(selections: str = "default")**  
  Retrieve faction applications.

- **get_faction_attacks(selections: str = "default")**  
  Retrieve detailed faction attack information.

- *(… additional faction methods)*

## Market, Racing, Forum, and Torn Endpoints

Each group of endpoints follows a similar pattern. For detailed information on each method, please refer to the source code.

> **Note:** The API is read-only. Make sure your selections match the access level of your API key.
