import grpc
from . import svc
from . import plumbing

class Client:
    def __init__(self, addr):
        try:
            channel = grpc.insecure_channel(addr)
            self.nodes = svc.Nodes(channel)
        except Exception as e:
            raise plumbing.error_to_porcelain(e) from e