import grpc
from . import svc
from . import plumbing

# Client is a strongDM API client.
class Client:
    # Creates a new strongDM API client. The `addr` parameter expects a hostname/port tuple.
    def __init__(self, addr, api_key):
        self.api_key = api_key
        try:
            channel = grpc.insecure_channel(addr)
            if addr.endswith("443"):
                creds = grpc.ssl_channel_credentials()
                channel = grpc.secure_channel(addr, creds)
            self.nodes = svc.Nodes(channel, self)
            self.roles = svc.Roles(channel, self)
        except Exception as e:
            raise plumbing.error_to_porcelain(e) from e
        self._test_options = {}