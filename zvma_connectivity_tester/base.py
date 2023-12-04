import requests

class BaseConnectivityTester:
    def __init__(self, common_config):
        self.common_config = common_config
        # Initialize common properties like headers, timeout, etc.

    def make_request(self, method, url, **kwargs):
        """
        Make an HTTP request using the given method, URL, and additional kwargs.
        """
        try:
            response = requests.request(method, url, **kwargs)
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            # Handle exceptions or log errors
            return None

    # Other common methods or utility functions

class DNSResolutionResponse:
    def __init__(self, status, ip=None, error_message=None):
        self.status = status
        self.ip = ip
        self.error_message = error_message

    def __str__(self):
        if self.status == "Success":
            return f"Hostname resolved successfully: IP is {self.ip}"
        else:
            return f"Hostname resolution failed: {self.error_message}"

class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKCYAN = '\033[96m'
        OKGREEN = '\033[92m'
        WARNING = '\033[31m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'