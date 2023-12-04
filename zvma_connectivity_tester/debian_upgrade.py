from .base import BaseConnectivityTester

class DebianUpgradeTester(BaseConnectivityTester):
    def __init__(self, specific_config=None):
        # If there's any specific configuration needed, it can be passed and processed here
        super().__init__(specific_config)
        self.urls = [
            "http://httpredir.debian.org/debian",
            "http://security.debian.org/debian-security"
        ]

    def test_connection(self):
        """
        Test connectivity to each of the Debian APT repositories.
        Returns True if all connections are successful, False otherwise.
        """
        all_successful = True
        for url in self.urls:
            response = self.make_request('GET', url)
            if not response or response.status_code != 200:
                all_successful = False
                break
        return all_successful

