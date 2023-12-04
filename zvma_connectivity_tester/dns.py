from .base import BaseConnectivityTester
from .base import DNSResolutionResponse
from .base import bcolors
import socket

class DnsTester(BaseConnectivityTester):
    DEFAULT_HOSTS = [
        {'host': 'httpredir.debian.org', 'name': 'Debian Package mirror'},
        {'host': 'security.debian.org', 'name': 'Debian Security mirror'},
        {'host': 'pypi.org', 'name': 'Python Packages'},
        {'host': 'ppa.launchpad.net', 'name': 'Ansible PPA'},
        {'host': 'zapps-registry.zerto.com', 'name': 'Zerto Docker Registry'},
        {'host': 'zvml-upgrade.s3.amazonaws.com', 'name': 'Zerto Upgrade S3 Repo'},
        {'host': 'keyserver.ubuntu.com', 'name': 'Debian Apt Keyserver'},
        {'host': 'zertodownloads.s3.amazonaws.com', 'name': 'Zerto S3 Downloads Repo'},
        {'host': 'autologs.zerto.com', 'name': 'Zerto Call Home'},
        {'host': 'zapps.zerto.com', 'name': 'Zerto License Validation'},
        {'host': 'zerto-mobile-data.zerto.com', 'name': 'Zerto Analytics'},
        {'host': 'zerto-msgs-for-sites.saas.zerto.com', 'name': 'Zerto Remote Log Collector'},
        {'host': 'zvm-control.api.zerto.com', 'name': 'Zerto ZVM Feature Control'},
        {'host': 'api.snapcraft.io', 'name': 'Snap Packages'},
        {'host': 'k8s.gcr.io', 'name': 'Kubernetes Container Repo'},
    ]

    def __init__(self, hosts=None):
        """
        :param endpoints: An optional list of dictionaries, each containing a 'host' and a 'name'.
                          If not provided, default endpoints will be used.
        """
        super().__init__(None)  # Assuming no specific config needed for base class
        self.hosts = hosts if hosts is not None else self.DEFAULT_HOSTS

    def test_hosts(self):
        """
        Test each Hostname. 
        Returns True if all are successful, False if any fail, 
        and prints the names of failing endpoints.
        """
        all_successful = True
        for host in self.hosts:
            ipaddress = None
            hostname = str(host['host'])
            name = str(host['name'])
            dnsinfo = self.resolve_hostname(hostname)
            if dnsinfo.status == "Success":
                print(f"{bcolors.OKGREEN}Successfully resolved {hostname} to {dnsinfo.ip}{bcolors.ENDC}")
            elif dnsinfo.status == "Failed":
                print(f"{bcolors.WARNING}Failed to resolve {hostname}: {dnsinfo.error_message}{bcolors.ENDC}")
        return all_successful

    def resolve_hostname(self, hostname):
        try:
            ip_address = socket.gethostbyname(hostname)
            return DNSResolutionResponse(status="Success", ip=ip_address)
        except socket.gaierror as e:
            return DNSResolutionResponse(status="Failed", error_message=str(e))

