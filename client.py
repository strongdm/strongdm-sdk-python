import grpc
from . import svc
from . import plumbing

class Client:
    def __init__(self, addr, api_key):
        try:
            channel = grpc.insecure_channel(addr)
            if addr.endswith("443"):
                creds = grpc.ssl_channel_credentials()
                channel = grpc.secure_channel(addr, creds)
            self.nodes = svc.Nodes(channel, api_key)
            self.roles = svc.Roles(channel, api_key)
        except Exception as e:
            raise plumbing.error_to_porcelain(e) from e