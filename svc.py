import grpc
from . import plumbing
from . import models

from .options_pb2 import *
from .options_pb2_grpc import *
from .spec_pb2 import *
from .spec_pb2_grpc import *
from .nodes_pb2 import *
from .nodes_pb2_grpc import *


# Nodes are proxies in strongDM responsible to communicate with servers
# (relays) and clients (gateways).
class Nodes:
    def __init__(self, channel):
        self.stub = NodesStub(channel)
    
    # Create registers a new node.
    def create(self, nodes):
        req = NodeCreateRequest()
        req.nodes.extend(plumbing.repeated_node_to_plumbing(nodes))
        try:
            plumbing_response = self.stub.Create(req)
        except Exception as e:
            raise plumbing.error_to_porcelain(e) from e
        resp = models.NodeCreateResponse()
        resp.meta = plumbing.create_response_metadata_to_porcelain(plumbing_response.meta)
        resp.nodes = plumbing.repeated_node_to_porcelain(plumbing_response.nodes)
        resp.tokens = plumbing.repeated_token_to_porcelain(plumbing_response.tokens)
        return resp
    
    # Get reads one node by ID.
    def get(self, id):
        req = NodeGetRequest()
        req.id = id
        try:
            plumbing_response = self.stub.Get(req)
        except Exception as e:
            raise plumbing.error_to_porcelain(e) from e
        resp = models.NodeGetResponse()
        resp.meta = plumbing.get_response_metadata_to_porcelain(plumbing_response.meta)
        resp.node = plumbing.node_to_porcelain(plumbing_response.node)
        return resp
    
    # Update patches a node by ID.
    def update(self, id, node):
        req = NodeUpdateRequest()
        req.id = id
        req.node.CopyFrom(plumbing.node_to_plumbing(node))
        try:
            plumbing_response = self.stub.Update(req)
        except Exception as e:
            raise plumbing.error_to_porcelain(e) from e
        resp = models.NodeUpdateResponse()
        resp.meta = plumbing.update_response_metadata_to_porcelain(plumbing_response.meta)
        resp.node = plumbing.node_to_porcelain(plumbing_response.node)
        return resp
    
    # Delete removes a node by ID.
    def delete(self, id):
        req = NodeDeleteRequest()
        req.id = id
        try:
            plumbing_response = self.stub.Delete(req)
        except Exception as e:
            raise plumbing.error_to_porcelain(e) from e
        resp = models.NodeDeleteResponse()
        resp.meta = plumbing.delete_response_metadata_to_porcelain(plumbing_response.meta)
        return resp
    
    # List is a batched Get call.
    def list(self, filter):
        req = NodeListRequest()
        req.meta.CopyFrom(ListRequestMetadata())
        req.filter = filter
        resp = models.NodeListResponse()
        def generator(svc, req):
            while True:
                try:
                    plumbing_response = svc.stub.List(req)
                except Exception as e:
                    raise plumbing.error_to_porcelain(e) from e
                for plumbing_item in plumbing_response.nodes:
                    
                    yield plumbing.node_to_porcelain(plumbing_item)
                if plumbing_response.meta.next_page == '':
                    break
                req.meta.page = plumbing_response.meta.next_page
        resp.nodes = generator(self, req)
        return resp
    
    # BatchUpdate is a batched Update call.
    def batch_update(self, nodes):
        req = NodeBatchUpdateRequest()
        req.nodes.extend(plumbing.repeated_node_to_plumbing(nodes))
        try:
            plumbing_response = self.stub.BatchUpdate(req)
        except Exception as e:
            raise plumbing.error_to_porcelain(e) from e
        resp = models.NodeBatchUpdateResponse()
        resp.meta = plumbing.batch_update_response_metadata_to_porcelain(plumbing_response.meta)
        resp.nodes = plumbing.repeated_node_to_porcelain(plumbing_response.nodes)
        return resp
    
    # BatchDelete is a batched Delete call.
    def batch_delete(self, ids):
        req = NodeBatchDeleteRequest()
        req.ids.extend(ids)
        try:
            plumbing_response = self.stub.BatchDelete(req)
        except Exception as e:
            raise plumbing.error_to_porcelain(e) from e
        resp = models.NodeBatchDeleteResponse()
        resp.meta = plumbing.batch_delete_response_metadata_to_porcelain(plumbing_response.meta)
        return resp
    
