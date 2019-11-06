import grpc
import v1_plumbing as plumbing
import v1_models as models

from nodes_pb2 import *
from nodes_pb2_grpc import *
from spec_pb2 import *


# Nodes are proxies in strongDM responsible to communicate with servers
# (relays) and clients (gateways).
class Nodes:
    def __init__(self, channel):
        self.stub = NodesStub(channel)
    
    # Create registers a new node.
    def create(self, nodes):
        req = NodeCreateRequest()
        req.nodes.extend(plumbing.repeated_node_to_plumbing(nodes))

        # begin
        plumbing_response = self.stub.Create(req)
        #rescue => exception
        #    raise Plumbing::error_to_porcelain(exception)
        #end
        resp = models.NodeCreateResponse()
        resp.meta = plumbing.create_response_metadata_to_porcelain(plumbing_response.meta)
        resp.nodes = plumbing.repeated_node_to_porcelain(plumbing_response.nodes)
        resp.tokens = plumbing.repeated_token_to_porcelain(plumbing_response.tokens)
        return resp
    
    # Get reads one node by ID.
    def get(self, id):
        req = NodeGetRequest()
        req.id = id

        # begin
        plumbing_response = self.stub.Get(req)
        #rescue => exception
        #    raise Plumbing::error_to_porcelain(exception)
        #end
        resp = models.NodeGetResponse()
        resp.meta = plumbing.get_response_metadata_to_porcelain(plumbing_response.meta)
        resp.node = plumbing.node_to_porcelain(plumbing_response.node)
        return resp
    
    # Update patches a node by ID.
    def update(self, id, node):
        req = NodeUpdateRequest()
        req.id = id
        req.node.CopyFrom(plumbing.node_to_plumbing(node))

        # begin
        plumbing_response = self.stub.Update(req)
        #rescue => exception
        #    raise Plumbing::error_to_porcelain(exception)
        #end
        resp = models.NodeUpdateResponse()
        resp.meta = plumbing.update_response_metadata_to_porcelain(plumbing_response.meta)
        resp.node = plumbing.node_to_porcelain(plumbing_response.node)
        return resp
    
    # Delete removes a node by ID.
    def delete(self, id):
        req = NodeDeleteRequest()
        req.id = id

        # begin
        plumbing_response = self.stub.Delete(req)
        #rescue => exception
        #    raise Plumbing::error_to_porcelain(exception)
        #end
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
                plumbing_response = svc.stub.List(req)
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

        # begin
        plumbing_response = self.stub.BatchUpdate(req)
        #rescue => exception
        #    raise Plumbing::error_to_porcelain(exception)
        #end
        resp = models.NodeBatchUpdateResponse()
        resp.meta = plumbing.batch_update_response_metadata_to_porcelain(plumbing_response.meta)
        resp.nodes = plumbing.repeated_node_to_porcelain(plumbing_response.nodes)
        return resp
    
    # BatchDelete is a batched Delete call.
    def batch_delete(self, ids):
        req = NodeBatchDeleteRequest()
        req.ids.extend(ids)

        # begin
        plumbing_response = self.stub.BatchDelete(req)
        #rescue => exception
        #    raise Plumbing::error_to_porcelain(exception)
        #end
        resp = models.NodeBatchDeleteResponse()
        resp.meta = plumbing.batch_delete_response_metadata_to_porcelain(plumbing_response.meta)
        return resp
    
