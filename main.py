# main.py
from zvma_connectivity_tester.dns import DnsTester
from zvma_connectivity_tester.google_analytics import GoogleAnalyticsConnector  
from zvma_connectivity_tester.https_endpoints import HttpsEndpointTester
from zvma_connectivity_tester.debian_upgrade import DebianUpgradeTester
from zvma_connectivity_tester.base import bcolors
# Import other service connectors as needed

def main():
    tester = DnsTester()
    if tester.test_hosts():
        print(f"{bcolors.OKGREEN}Successfully resolved all hosts.{bcolors.ENDC}")
    else:
        print(f"{bcolors.WARNING}Failed to resolve one or more hosts.{bcolors.ENDC}")

    # Define specific configurations for each service
    ga_config = {
    'measurement_id': 'G-0SC41XSFDN',
    'api_secret': 'KKKozOveRR25YiQ6Ai-vUQ',
    }

    ga_connector = GoogleAnalyticsConnector(ga_config)

    # Example usage for Google Analytics
    if ga_connector.test_connection():
        print(f"{bcolors.OKGREEN}Successfully connected to Google Analytics service.{bcolors.ENDC}")
    else:
        print(f"{bcolors.WARNING}Failed to connect to Google Analytics service.{bcolors.ENDC}")

    debian_tester = DebianUpgradeTester()
    if debian_tester.test_connection():
        print(f"{bcolors.OKGREEN}Successfully connected to all Debian APT repositories.{bcolors.ENDC}")
    else:
        print(f"{bcolors.WARNING}Failed to connect to one or more Debian APT repositories.{bcolors.ENDC}")

    tester = HttpsEndpointTester()
    if tester.test_endpoints():
        print(f"{bcolors.OKGREEN}Successfully connected to all default endpoints.{bcolors.ENDC}")
    else:
        print(f"{bcolors.WARNING}Failed to connect to one or more default endpoints.{bcolors.ENDC}")


if __name__ == "__main__":
    main()
