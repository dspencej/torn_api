import requests

class TornAPIClient:
    """
    A Python client for the Torn API v2.

    Usage:
        client = TornAPIClient(api_key="YOUR_API_KEY")
        attacks = client.get_user_attacks(selections="profile,stats")
    """
    BASE_URL = "https://api.torn.com/v2"

    def __init__(self, api_key: str):
        """
        Initialize the Torn API client with your API key.
        """
        self.api_key = api_key
        self.session = requests.Session()

    def _request(self, path: str, params: dict = None):
        """
        Internal method to send a GET request to the Torn API.
        """
        if params is None:
            params = {}
        # Always include the API key in the parameters.
        params["key"] = self.api_key
        url = f"{self.BASE_URL}{path}"
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    # --- User Endpoints ---
    def get_user_attacks(self, selections: str = "default"):
        """Get your detailed attacks."""
        return self._request("/user/attacks", {"selections": selections})

    def get_user_attacksfull(self, selections: str = "default"):
        """Get your simplified attacks."""
        return self._request("/user/attacksfull", {"selections": selections})

    def get_user_bounties(self, selections: str = "default"):
        """Get bounties placed on you."""
        return self._request("/user/bounties", {"selections": selections})

    def get_user_bounties_by_id(self, user_id: int, selections: str = "default"):
        """Get bounties placed on a specific user."""
        return self._request(f"/user/{user_id}/bounties", {"selections": selections})

    def get_user_calendar(self):
        """Get your competition's event start time."""
        return self._request("/user/calendar")

    def get_user_crimes(self, crime_id: int, selections: str = "default"):
        """Get your crime statistics for a given crime."""
        return self._request(f"/user/{crime_id}/crimes", {"selections": selections})

    def get_user_enlistedcars(self, selections: str = "default"):
        """Get user enlisted cars."""
        return self._request("/user/enlistedcars", {"selections": selections})

    def get_user_factionbalance(self, selections: str = "default"):
        """Get your current faction balance."""
        return self._request("/user/factionbalance", {"selections": selections})

    def get_user_forumfeed(self, selections: str = "default"):
        """Get updates on your forum threads and posts."""
        return self._request("/user/forumfeed", {"selections": selections})

    def get_user_forumfriends(self, selections: str = "default"):
        """Get updates on your friends' activity in the forum."""
        return self._request("/user/forumfriends", {"selections": selections})

    def get_user_forumposts(self, selections: str = "default"):
        """Get your forum posts."""
        return self._request("/user/forumposts", {"selections": selections})

    def get_user_forumposts_by_id(self, user_id: int, selections: str = "default"):
        """Get forum posts for a specific player."""
        return self._request(f"/user/{user_id}/forumposts", {"selections": selections})

    def get_user_forumsubscribedthreads(self, selections: str = "default"):
        """Get updates on threads you are subscribed to."""
        return self._request("/user/forumsubscribedthreads", {"selections": selections})

    def get_user_forumthreads(self, selections: str = "default"):
        """Get your forum threads."""
        return self._request("/user/forumthreads", {"selections": selections})

    def get_user_forumthreads_by_id(self, user_id: int, selections: str = "default"):
        """Get forum threads for a specific player."""
        return self._request(f"/user/{user_id}/forumthreads", {"selections": selections})

    def get_user_hof(self, selections: str = "default"):
        """Get your hall of fame rankings."""
        return self._request("/user/hof", {"selections": selections})

    def get_user_hof_by_id(self, user_id: int, selections: str = "default"):
        """Get hall of fame rankings for a specific player."""
        return self._request(f"/user/{user_id}/hof", {"selections": selections})

    def get_user_itemmarket(self, selections: str = "default"):
        """Get your item market listings."""
        return self._request("/user/itemmarket", {"selections": selections})

    def get_user_jobranks(self, selections: str = "default"):
        """Get your starter job positions."""
        return self._request("/user/jobranks", {"selections": selections})

    def get_user_organizedcrime(self, selections: str = "default"):
        """Get your current ongoing organized crime."""
        return self._request("/user/organizedcrime", {"selections": selections})

    def get_user_personalstats(self, selections: str = "default"):
        """Get your personal stats."""
        return self._request("/user/personalstats", {"selections": selections})

    def get_user_personalstats_by_id(self, user_id: int, selections: str = "default"):
        """Get personal stats for a specific player."""
        return self._request(f"/user/{user_id}/personalstats", {"selections": selections})

    def get_user_races(self, selections: str = "default"):
        """Get user races."""
        return self._request("/user/races", {"selections": selections})

    def get_user_revives(self, selections: str = "default"):
        """Get your detailed revives."""
        return self._request("/user/revives", {"selections": selections})

    def get_user_revivesFull(self, selections: str = "default"):
        """Get your simplified revives."""
        return self._request("/user/revivesFull", {"selections": selections})

    def get_user_lookup(self, selections: str = "default"):
        """Get all available user selections."""
        return self._request("/user/lookup", {"selections": selections})

    def get_user_timestamp(self):
        """Get the current server time for the user section."""
        return self._request("/user/timestamp")

    def get_user(self, selections: str = "default"):
        """Get any User selection."""
        return self._request("/user", {"selections": selections})

    # --- Faction Endpoints ---
    def get_faction_applications(self, selections: str = "default"):
        """Get your faction's applications."""
        return self._request("/faction/applications", {"selections": selections})

    def get_faction_attacks(self, selections: str = "default"):
        """Get your faction's detailed attacks."""
        return self._request("/faction/attacks", {"selections": selections})

    def get_faction_attacksfull(self, selections: str = "default"):
        """Get your faction's simplified attacks."""
        return self._request("/faction/attacksfull", {"selections": selections})

    def get_faction_basic(self, faction_id: int = None, selections: str = "default"):
        """Get basic faction details. If faction_id is provided, retrieves details for that faction."""
        path = f"/faction/{faction_id}/basic" if faction_id else "/faction/basic"
        return self._request(path, {"selections": selections})

    def get_faction_chain(self, faction_id: int = None, selections: str = "default"):
        """Get your faction's current chain."""
        path = f"/faction/{faction_id}/chain" if faction_id else "/faction/chain"
        return self._request(path, {"selections": selections})

    def get_faction_chains(self, faction_id: int = None, selections: str = "default"):
        """Get a list of completed chains. If faction_id is provided, retrieves for that faction."""
        path = f"/faction/{faction_id}/chains" if faction_id else "/faction/chains"
        return self._request(path, {"selections": selections})

    def get_faction_chainreport(self, chain_id: int = None, selections: str = "default"):
        """Get your faction's latest chain report or for a specific chain if chain_id is provided."""
        path = f"/faction/{chain_id}/chainreport" if chain_id else "/faction/chainreport"
        return self._request(path, {"selections": selections})

    def get_faction_crimes(self, selections: str = "default"):
        """Get your faction's organized crimes."""
        return self._request("/faction/crimes", {"selections": selections})

    def get_faction_hof(self, faction_id: int = None, selections: str = "default"):
        """Get your faction's hall of fame rankings, or for a specific faction if faction_id is provided."""
        path = f"/faction/{faction_id}/hof" if faction_id else "/faction/hof"
        return self._request(path, {"selections": selections})

    def get_faction_members(self, faction_id: int = None, selections: str = "default"):
        """Get a list of faction members. If faction_id is provided, retrieves members for that faction."""
        path = f"/faction/{faction_id}/members" if faction_id else "/faction/members"
        return self._request(path, {"selections": selections})

    def get_faction_news(self, selections: str = "default"):
        """Get your faction's news details."""
        return self._request("/faction/news", {"selections": selections})

    def get_faction_rankedwars(self, faction_id: int = None, selections: str = "default"):
        """Get ranked wars. If faction_id is provided, retrieves for that faction."""
        path = f"/faction/{faction_id}/rankedwars" if faction_id else "/faction/rankedwars"
        return self._request(path, {"selections": selections})

    def get_faction_rankedwarreport(self, faction_id: int, selections: str = "default"):
        """Get ranked war details for a specific faction."""
        return self._request(f"/faction/{faction_id}/rankedwarreport", {"selections": selections})

    def get_faction_revives(self, selections: str = "default"):
        """Get your faction's detailed revives."""
        return self._request("/faction/revives", {"selections": selections})

    def get_faction_revivesFull(self, selections: str = "default"):
        """Get your faction's simplified revives."""
        return self._request("/faction/revivesFull", {"selections": selections})

    def get_faction_wars(self, faction_id: int = None, selections: str = "default"):
        """Get your faction's wars & pacts details, or for a specific faction if faction_id is provided."""
        path = f"/faction/{faction_id}/wars" if faction_id else "/faction/wars"
        return self._request(path, {"selections": selections})

    def get_faction_lookup(self, selections: str = "default"):
        """Get all available faction selections."""
        return self._request("/faction/lookup", {"selections": selections})

    def get_faction_timestamp(self):
        """Get the current server time for the faction section."""
        return self._request("/faction/timestamp")

    def get_faction(self, selections: str = "default"):
        """Get any Faction selection."""
        return self._request("/faction", {"selections": selections})

    # --- Market Endpoints ---
    def get_market_itemmarket(self, item_id: int, selections: str = "default"):
        """Get item market listings for a specific item."""
        return self._request(f"/market/{item_id}/itemmarket", {"selections": selections})

    def get_market_lookup(self, selections: str = "default"):
        """Get all available market selections."""
        return self._request("/market/lookup", {"selections": selections})

    def get_market_timestamp(self):
        """Get the current server time for the market section."""
        return self._request("/market/timestamp")

    def get_market(self, selections: str = "default"):
        """Get any Market selection."""
        return self._request("/market", {"selections": selections})

    # --- Racing Endpoints ---
    def get_racing_cars(self, selections: str = "default"):
        """Get cars and their racing stats."""
        return self._request("/racing/cars", {"selections": selections})

    def get_racing_carupgrades(self, selections: str = "default"):
        """Get all possible car upgrades."""
        return self._request("/racing/carupgrades", {"selections": selections})

    def get_racing_races(self, selections: str = "default"):
        """Get races."""
        return self._request("/racing/races", {"selections": selections})

    def get_racing_race(self, race_id: int, selections: str = "default"):
        """Get specific race details for a given race."""
        return self._request(f"/racing/{race_id}/race", {"selections": selections})

    def get_racing_records(self, track_id: int, selections: str = "default"):
        """Get track records for a specific track."""
        return self._request(f"/racing/{track_id}/records", {"selections": selections})

    def get_racing_tracks(self, selections: str = "default"):
        """Get race tracks and descriptions."""
        return self._request("/racing/tracks", {"selections": selections})

    def get_racing_lookup(self, selections: str = "default"):
        """Get all available racing selections."""
        return self._request("/racing/lookup", {"selections": selections})

    def get_racing_timestamp(self):
        """Get the current server time for the racing section."""
        return self._request("/racing/timestamp")

    def get_racing(self, selections: str = "default"):
        """Get any Racing selection."""
        return self._request("/racing", {"selections": selections})

    # --- Forum Endpoints ---
    def get_forum_categories(self, selections: str = "default"):
        """Get publicly available forum categories."""
        return self._request("/forum/categories", {"selections": selections})

    def get_forum_posts(self, thread_id: int, selections: str = "default"):
        """Get specific forum thread posts."""
        return self._request(f"/forum/{thread_id}/posts", {"selections": selections})

    def get_forum_thread(self, thread_id: int, selections: str = "default"):
        """Get specific thread details."""
        return self._request(f"/forum/{thread_id}/thread", {"selections": selections})

    def get_forum_threads(self, selections: str = "default"):
        """Get threads across all forum categories."""
        return self._request("/forum/threads", {"selections": selections})

    def get_forum_threads_by_category(self, category_ids: str, selections: str = "default"):
        """
        Get threads for specific public forum category or categories.
        'category_ids' can be a comma-separated list of IDs.
        """
        return self._request(f"/forum/{category_ids}/threads", {"selections": selections})

    def get_forum_lookup(self, selections: str = "default"):
        """Get all available forum selections."""
        return self._request("/forum/lookup", {"selections": selections})

    def get_forum_timestamp(self):
        """Get the current server time for the forum section."""
        return self._request("/forum/timestamp")

    def get_forum(self, selections: str = "default"):
        """Get any Forum selection."""
        return self._request("/forum", {"selections": selections})

    # --- Torn Endpoints ---
    def get_torn_attacklog(self, selections: str = "default"):
        """Get attack log details."""
        return self._request("/torn/attacklog", {"selections": selections})

    def get_torn_bounties(self, selections: str = "default"):
        """Get bounties."""
        return self._request("/torn/bounties", {"selections": selections})

    def get_torn_calendar(self, selections: str = "default"):
        """Get calendar information."""
        return self._request("/torn/calendar", {"selections": selections})

    def get_torn_crimes(self, selections: str = "default"):
        """Get crimes information."""
        return self._request("/torn/crimes", {"selections": selections})

    def get_torn_factionhof(self, selections: str = "default"):
        """Get faction hall of fame positions for a specific category."""
        return self._request("/torn/factionhof", {"selections": selections})

    def get_torn_hof(self, selections: str = "default"):
        """Get player hall of fame positions for a specific category."""
        return self._request("/torn/hof", {"selections": selections})

    def get_torn_itemammo(self, selections: str = "default"):
        """Get information about ammo."""
        return self._request("/torn/itemammo", {"selections": selections})

    def get_torn_itemmods(self, selections: str = "default"):
        """Get information about weapon upgrades."""
        return self._request("/torn/itemmods", {"selections": selections})

    def get_torn_items(self, selections: str = "default"):
        """Get information about items."""
        return self._request("/torn/items", {"selections": selections})

    def get_torn_items_by_ids(self, ids: str, selections: str = "default"):
        """
        Get information about items by IDs.
        'ids' should be a comma-separated string of item IDs.
        """
        return self._request(f"/torn/{ids}/items", {"selections": selections})

    def get_torn_logcategories(self, selections: str = "default"):
        """Get available log categories."""
        return self._request("/torn/logcategories", {"selections": selections})

    def get_torn_logtypes(self, selections: str = "default"):
        """Get all available log ids."""
        return self._request("/torn/logtypes", {"selections": selections})

    def get_torn_logtypes_by_category(self, log_category_id: int, selections: str = "default"):
        """Get available log ids for a specific log category."""
        return self._request(f"/torn/{log_category_id}/logtypes", {"selections": selections})

    def get_torn_subcrimes(self, crime_id: int, selections: str = "default"):
        """Get subcrimes information for a given crime."""
        return self._request(f"/torn/{crime_id}/subcrimes", {"selections": selections})

    def get_torn_lookup(self, selections: str = "default"):
        """Get all available torn selections."""
        return self._request("/torn/lookup", {"selections": selections})

    def get_torn_timestamp(self):
        """Get the current server time for the torn section."""
        return self._request("/torn/timestamp")

    def get_torn(self, selections: str = "default"):
        """Get any Torn selection."""
        return self._request("/torn", {"selections": selections})
