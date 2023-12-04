import unittest
from unittest.mock import patch
from ..zvma_connectivity_tester.google_analytics import GoogleAnalyticsConnector


class TestGoogleAnalyticsConnector(unittest.TestCase):
    @patch('zvm_connectivity_tester.google_analytics.requests')
    def test_google_analytics_connection(self, mock_requests):
        # Configure the mock to return a response with status code 204
        mock_requests.request.return_value.status_code = 204

        ga_config = {
            'measurement_id': 'test_id',
            'api_secret': 'test_secret',
        }
        connector = GoogleAnalyticsConnector(ga_config)

        self.assertTrue(connector.test_connection())

if __name__ == '__main__':
    unittest.main()
