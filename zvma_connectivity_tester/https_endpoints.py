from .base import BaseConnectivityTester
from .base import bcolors

class HttpsEndpointTester(BaseConnectivityTester):
    DEFAULT_ENDPOINTS = [
        {'url': 'https://httpredir.debian.org', 'name': 'Debian Package mirror'},
        {'url': 'https://security.debian.org', 'name': 'Debian Security mirror'},
        {'url': 'https://pypi.org', 'name': 'Python Packages'},
        {'url': 'http://ppa.launchpad.net/ansible/ansible/ubuntu', 'name': 'Ansible PPA'},
        {'url': 'https://zapps-registry.zerto.com', 'name': 'Zerto Docker Registry'},
        {'url': 'https://zvml-upgrade.s3.amazonaws.com', 'name': 'Zerto Upgrade S3 Repo'},
        {'url': 'https://keyserver.ubuntu.com', 'name': 'Debian Apt Keyserver'},
        {'url': 'https://zertodownloads.s3.amazonaws.com', 'name': 'Zerto S3 Downloads Repo'},
        {'url': 'https://zertodownloads.s3us-east-1.amazonaws.com', 'name': 'Zerto S3 East US Downloads Repo'},
        {'url': 'https://zlogs-us.s3.amazonaws.com', 'name': 'Zerto Log Server US'},
        {'url': 'https://zlogs-emea.s3.amazonaws.com', 'name': 'Zerto Log Server EU'},
        {'url': 'https://autologs.zerto.com', 'name': 'Zerto Log Server'},
        {'url': 'https://ch3.zerto.com', 'name': 'Zerto Call Home'},
        {'url': 'https://zapps.zerto.com', 'name': 'Zerto License Validation'},
        {'url': 'https://zerto-mobile-data.zerto.com', 'name': 'Zerto Analytics'},
        {'url': 'https://zerto-msgs-for-sites.saas.zerto.com', 'name': 'Zerto Remote Log Collector'},
        {'url': 'https://zvm-control.api.zerto.com', 'name': 'Zerto ZVM Feature Control'},
        {'url': 'https://api.snapcraft.io', 'name': 'Snap Packages'},
        {'url': 'https://k8s.gcr.io', 'name': 'Kubernetes Container Repo'},
    ]

    def __init__(self, endpoints=None):
        """
        :param endpoints: An optional list of dictionaries, each containing a 'url' and a 'name'.
                          If not provided, default endpoints will be used.
        """
        super().__init__(None)  # Assuming no specific config needed for base class
        self.endpoints = endpoints if endpoints is not None else self.DEFAULT_ENDPOINTS


    #def test_endpoints(self):
    #    """
    #    Test each HTTPS endpoint. 
    #    Returns True if all are successful, False if any fail, 
    #    and prints the names of failing endpoints.
    #    """
    #    all_successful = True
    #    for endpoint in self.endpoints:
    #        url = endpoint['url']
    #        name = endpoint['name']
    #        response = self.make_request('GET', url)
    #        if not response or response.status_code != 200:
    #            print(f"{bcolors.WARNING}Failed to connect to {name} at {url}{bcolors.ENDC} Response Code: {response.status_code}")
    #            all_successful = False
    #        else:
    ##            print(f"{bcolors.OKGREEN}Successfully connected to {name} at {url}{bcolors.ENDC}")
    #    return all_successful


    def test_endpoints(self):
        """
        Test each HTTPS endpoint. 
        Returns True if all are successful, False if any fail, 
        and prints the names of failing endpoints.
        """
        all_successful = True
        for endpoint in self.endpoints:
            url = endpoint['url']
            name = endpoint['name']
            response = self.make_request('GET', url)
            
            if response is None or response.status_code != 200:
                print(f"{bcolors.WARNING}Failed to connect to {name} at {url}{bcolors.ENDC}", end="")
                if response:
                    print(f" Response Code: {response.status_code}")
                else:
                    print(" No response received.")
                all_successful = False
            else:
                print(f"{bcolors.OKGREEN}Successfully connected to {name} at {url}{bcolors.ENDC}")

        return all_successful