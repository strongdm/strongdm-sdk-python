import grpc
import v1_svc as svc

class Client:
    def __init__(self, addr):
        channel = grpc.insecure_channel(addr)
        self.nodes = svc.Nodes(channel)