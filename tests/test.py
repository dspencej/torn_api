import os
import time
import unittest
import logging
import coloredlogs
from datetime import datetime
from torn_api import TornAPIClient

# Set up timestamped log directory.
timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
log_dir = os.path.join("logs", timestamp)
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, "logs.txt")

# Configure logging format.
LOG_FORMAT = "%(asctime)s [%(levelname)s] %(message)s"

# Configure colored console logging.
coloredlogs.install(level="DEBUG", fmt=LOG_FORMAT)

# Create file handler.
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter(LOG_FORMAT)
file_handler.setFormatter(formatter)

# Attach file handler to the root logger.
logger = logging.getLogger()
logger.addHandler(file_handler)

DELAY = 0.5  # Delay in seconds between API calls

class TestTornAPIClientIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.api_key = os.environ.get("TORN_API_KEY")
        if not cls.api_key:
            raise unittest.SkipTest("TORN_API_KEY environment variable not set")
        cls.client = TornAPIClient(api_key=cls.api_key)

        # Get basic user data and extract IDs from it.
        try:
            logging.debug("Fetching basic user data from /user endpoint")
            cls.user_data = cls.client.get_user(selections="basic")
            logging.debug("User data retrieved: %s", cls.user_data)
            time.sleep(DELAY)
        except Exception as e:
            raise unittest.SkipTest("Failed to fetch user data: " + str(e))

        # Extract the user id (try common keys)
        cls.user_id = cls.user_data.get("player_id") or cls.user_data.get("id")
        logging.debug("Extracted user_id: %s", cls.user_id)
        # Extract the faction id from user data if available.
        cls.faction_id = None
        if "faction" in cls.user_data and isinstance(cls.user_data["faction"], dict):
            cls.faction_id = cls.user_data["faction"].get("faction_id")
        logging.debug("Extracted faction_id: %s", cls.faction_id)

        # For racing endpoints, attempt to fetch a race id.
        try:
            logging.debug("Fetching racing races data")
            racing_data = cls.client.get_racing_races(selections="default")
            logging.debug("Racing data retrieved: %s", racing_data)
            if isinstance(racing_data, dict) and "races" in racing_data and racing_data["races"]:
                cls.race_id = racing_data["races"][0].get("race_id")
            else:
                cls.race_id = None
            time.sleep(DELAY)
        except Exception as e:
            logging.exception("Error fetching racing races data")
            cls.race_id = None
        logging.debug("Extracted race_id: %s", cls.race_id)

        # For forum endpoints, attempt to fetch a thread id.
        try:
            logging.debug("Fetching forum threads data")
            forum_data = cls.client.get_forum_threads(selections="default")
            logging.debug("Forum data retrieved: %s", forum_data)
            if isinstance(forum_data, dict) and "threads" in forum_data and forum_data["threads"]:
                cls.thread_id = forum_data["threads"][0].get("thread_id")
            else:
                cls.thread_id = None
            time.sleep(DELAY)
        except Exception as e:
            logging.exception("Error fetching forum threads data")
            cls.thread_id = None
        logging.debug("Extracted thread_id: %s", cls.thread_id)

    def check_response(self, response):
        """Basic check: response should be a dictionary."""
        self.assertIsInstance(response, dict)

    def run_test(self, endpoint_callable, *args, **kwargs):
        """Helper to run an endpoint call with try/except, logging, and a delay after the call."""
        try:
            logging.debug("Testing endpoint: %s with args: %s, kwargs: %s", endpoint_callable, args, kwargs)
            result = endpoint_callable(*args, **kwargs)
            self.check_response(result)
            logging.debug("Endpoint %s returned valid response: %s", endpoint_callable, result)
        except Exception as e:
            logging.exception("Error calling endpoint %s with args: %s, kwargs: %s", endpoint_callable, args, kwargs)
            raise
        finally:
            time.sleep(DELAY)

    # --- User Endpoints ---
    def test_user_endpoints(self):
        self.run_test(self.client.get_user_attacks, selections="default")
        self.run_test(self.client.get_user_attacksfull, selections="default")
        self.run_test(self.client.get_user_bounties, selections="default")
        self.run_test(self.client.get_user_calendar)
        self.run_test(self.client.get_user_enlistedcars, selections="default")
        self.run_test(self.client.get_user_factionbalance, selections="default")
        self.run_test(self.client.get_user_forumfeed, selections="default")
        self.run_test(self.client.get_user_forumfriends, selections="default")
        self.run_test(self.client.get_user_forumposts, selections="default")
        self.run_test(self.client.get_user_forumsubscribedthreads, selections="default")
        self.run_test(self.client.get_user_forumthreads, selections="default")
        self.run_test(self.client.get_user_hof, selections="default")
        self.run_test(self.client.get_user_itemmarket, selections="default")
        self.run_test(self.client.get_user_jobranks, selections="default")
        self.run_test(self.client.get_user_organizedcrime, selections="default")
        self.run_test(self.client.get_user_personalstats, selections="default")
        self.run_test(self.client.get_user_races, selections="default")
        self.run_test(self.client.get_user_revives, selections="default")
        self.run_test(self.client.get_user_revivesFull, selections="default")
        self.run_test(self.client.get_user_lookup, selections="default")
        self.run_test(self.client.get_user_timestamp)
        self.run_test(self.client.get_user, selections="default")

        if self.user_id:
            self.run_test(self.client.get_user_bounties_by_id, self.user_id, selections="default")
            self.run_test(self.client.get_user_crimes, 1, selections="default")
            self.run_test(self.client.get_user_forumposts_by_id, self.user_id, selections="default")
            self.run_test(self.client.get_user_forumthreads_by_id, self.user_id, selections="default")
            self.run_test(self.client.get_user_hof_by_id, self.user_id, selections="default")
            self.run_test(self.client.get_user_personalstats_by_id, self.user_id, selections="default")
        else:
            self.skipTest("User ID not found in user data.")

    # --- Faction Endpoints ---
    def test_faction_endpoints(self):
        self.run_test(self.client.get_faction_applications, selections="default")
        self.run_test(self.client.get_faction_attacks, selections="default")
        self.run_test(self.client.get_faction_attacksfull, selections="default")
        self.run_test(self.client.get_faction_chain, selections="default")
        self.run_test(self.client.get_faction_chains, selections="default")
        self.run_test(self.client.get_faction_chainreport, selections="default")
        self.run_test(self.client.get_faction_crimes, selections="default")
        self.run_test(self.client.get_faction_lookup, selections="default")
        self.run_test(self.client.get_faction_timestamp)
        self.run_test(self.client.get_faction, selections="default")

        if self.faction_id:
            self.run_test(self.client.get_faction_basic, faction_id=self.faction_id, selections="default")
            self.run_test(self.client.get_faction_chain, faction_id=self.faction_id, selections="default")
            self.run_test(self.client.get_faction_chains, faction_id=self.faction_id, selections="default")
            self.run_test(self.client.get_faction_hof, faction_id=self.faction_id, selections="default")
            self.run_test(self.client.get_faction_members, faction_id=self.faction_id, selections="default")
            self.run_test(self.client.get_faction_rankedwars, faction_id=self.faction_id, selections="default")
            self.run_test(self.client.get_faction_rankedwarreport, faction_id=self.faction_id, selections="default")
            self.run_test(self.client.get_faction_wars, faction_id=self.faction_id, selections="default")
        else:
            self.skipTest("Faction ID not found in user data.")

    # --- Market Endpoints ---
    def test_market_endpoints(self):
        self.run_test(self.client.get_market_lookup, selections="default")
        self.run_test(self.client.get_market_timestamp)
        self.run_test(self.client.get_market, selections="default")
        logging.debug("Skipping market item endpoint test due to lack of automatic item extraction.")
        self.skipTest("Market item endpoint test skipped.")

    # --- Racing Endpoints ---
    def test_racing_endpoints(self):
        self.run_test(self.client.get_racing_cars, selections="default")
        self.run_test(self.client.get_racing_carupgrades, selections="default")
        self.run_test(self.client.get_racing_races, selections="default")
        self.run_test(self.client.get_racing_tracks, selections="default")
        self.run_test(self.client.get_racing_lookup, selections="default")
        self.run_test(self.client.get_racing_timestamp)
        self.run_test(self.client.get_racing, selections="default")
        if self.race_id:
            self.run_test(self.client.get_racing_race, race_id=self.race_id, selections="default")
        else:
            self.skipTest("No race ID found from racing races data.")
        self.run_test(self.client.get_racing_records, track_id=1, selections="default")

    # --- Forum Endpoints ---
    def test_forum_endpoints(self):
        self.run_test(self.client.get_forum_categories, selections="default")
        self.run_test(self.client.get_forum_threads, selections="default")
        self.run_test(self.client.get_forum_lookup, selections="default")
        self.run_test(self.client.get_forum_timestamp)
        self.run_test(self.client.get_forum, selections="default")
        if self.thread_id:
            self.run_test(self.client.get_forum_posts, thread_id=self.thread_id, selections="default")
            self.run_test(self.client.get_forum_thread, thread_id=self.thread_id, selections="default")
        else:
            self.skipTest("No forum thread ID found from forum threads data.")

    # --- Torn Endpoints ---
    def test_torn_endpoints(self):
        self.run_test(self.client.get_torn_attacklog, selections="default")
        self.run_test(self.client.get_torn_bounties, selections="default")
        self.run_test(self.client.get_torn_calendar, selections="default")
        self.run_test(self.client.get_torn_crimes, selections="default")
        self.run_test(self.client.get_torn_factionhof, selections="default")
        self.run_test(self.client.get_torn_hof, selections="default")
        self.run_test(self.client.get_torn_itemammo, selections="default")
        self.run_test(self.client.get_torn_itemmods, selections="default")
        self.run_test(self.client.get_torn_items, selections="default")
        self.run_test(self.client.get_torn_logcategories, selections="default")
        self.run_test(self.client.get_torn_logtypes, selections="default")
        self.run_test(self.client.get_torn_lookup, selections="default")
        self.run_test(self.client.get_torn_timestamp)
        self.run_test(self.client.get_torn, selections="default")

if __name__ == '__main__':
    unittest.main()
