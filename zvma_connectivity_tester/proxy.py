from .base import BaseConnectivityTester
from .base import bcolors

class ProxyTester(BaseConnectivityTester):
    def __init__(self, specific_config):
        super().__init__(specific_config)
        """self.measurement_id = specific_config.get('measurement_id')
        self.api_secret = specific_config.get('api_secret')
        """
        
    def test_connection(self):
        """
        Test connectivity and if there are any proxy servers in the middle.
        """
        
