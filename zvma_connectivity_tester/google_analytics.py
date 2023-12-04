from .base import BaseConnectivityTester

class GoogleAnalyticsConnector(BaseConnectivityTester):
    def __init__(self, specific_config):
        super().__init__(specific_config)
        self.measurement_id = specific_config.get('measurement_id')
        self.api_secret = specific_config.get('api_secret')

    def test_connection(self):
        """
        Test connectivity to Google Analytics 4 by sending a test event.
        """
        url = f"https://www.google-analytics.com/mp/collect?measurement_id={self.measurement_id}&api_secret={self.api_secret}"
        payload = {
            'client_id': '555',  # Example client ID, replace with a relevant value
            'events': [{'name': 'test_event', 'params': {}}]
        }
        headers = {'Content-Type': 'application/json'}

        response = self.make_request('POST', url, json=payload, headers=headers)
        return response is not None and response.status_code == 204
