import grpc
from . import plumbing
from . import models

from .options_pb2 import *
from .options_pb2_grpc import *
from .spec_pb2 import *
from .spec_pb2_grpc import *
from .nodes_pb2 import *
from .nodes_pb2_grpc import *
from .roles_pb2 import *
from .roles_pb2_grpc import *


# Nodes are proxies in strongDM responsible to communicate with servers
# (relays) and clients (gateways).
class Nodes:
    def __init__(self, channel, api_key):
        self.stub = NodesStub(channel)
        self.api_key = api_key
    
    # Create registers a new node.
    def create(self, node):
        req = NodeCreateRequest()
        req.node.CopyFrom(plumbing.node_to_plumbing(node))
        try:
            plumbing_response = self.stub.Create(req, metadata=[('authorization', self.api_key)])
        except Exception as e:
            raise plumbing.error_to_porcelain(e) from e
        resp = models.NodeCreateResponse()
        resp.meta = plumbing.create_response_metadata_to_porcelain(plumbing_response.meta)
        resp.node = plumbing.node_to_porcelain(plumbing_response.node)
        resp.token = plumbing.token_to_porcelain(plumbing_response.token)
        return resp
    
    # Get reads one node by ID.
    def get(self, id):
        req = NodeGetRequest()
        req.id = id
        try:
            plumbing_response = self.stub.Get(req, metadata=[('authorization', self.api_key)])
        except Exception as e:
            raise plumbing.error_to_porcelain(e) from e
        resp = models.NodeGetResponse()
        resp.meta = plumbing.get_response_metadata_to_porcelain(plumbing_response.meta)
        resp.node = plumbing.node_to_porcelain(plumbing_response.node)
        return resp
    
    # Update patches a node by ID.
    def update(self, node):
        req = NodeUpdateRequest()
        req.node.CopyFrom(plumbing.node_to_plumbing(node))
        try:
            plumbing_response = self.stub.Update(req, metadata=[('authorization', self.api_key)])
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
            plumbing_response = self.stub.Delete(req, metadata=[('authorization', self.api_key)])
        except Exception as e:
            raise plumbing.error_to_porcelain(e) from e
        resp = models.NodeDeleteResponse()
        resp.meta = plumbing.delete_response_metadata_to_porcelain(plumbing_response.meta)
        return resp
    
    # List is a batched Get call.
    def list(self, filter):
        req = NodeListRequest()
        req.meta.CopyFrom(ListRequestMetadata())
        req.meta.limit = 25
        req.filter = filter
        def generator(svc, req):
            while True:
                try:
                    plumbing_response = svc.stub.List(req, metadata=[('authorization', svc.api_key)])
                except Exception as e:
                    raise plumbing.error_to_porcelain(e) from e
                for plumbing_item in plumbing_response.nodes:
                    
                    yield plumbing.node_to_porcelain(plumbing_item)
                if plumbing_response.meta.next_cursor == '':
                    break
                req.meta.cursor = plumbing_response.meta.next_cursor
        return generator(self, req)
    

# Roles are
class Roles:
    def __init__(self, channel, api_key):
        self.stub = RolesStub(channel)
        self.api_key = api_key
    
    # Create registers a new role.
    def create(self, role):
        req = RoleCreateRequest()
        req.role.CopyFrom(plumbing.role_to_plumbing(role))
        try:
            plumbing_response = self.stub.Create(req, metadata=[('authorization', self.api_key)])
        except Exception as e:
            raise plumbing.error_to_porcelain(e) from e
        resp = models.RoleCreateResponse()
        resp.meta = plumbing.create_response_metadata_to_porcelain(plumbing_response.meta)
        resp.role = plumbing.role_to_porcelain(plumbing_response.role)
        return resp
    
    # Get reads one role by ID.
    def get(self, id):
        req = RoleGetRequest()
        req.id = id
        try:
            plumbing_response = self.stub.Get(req, metadata=[('authorization', self.api_key)])
        except Exception as e:
            raise plumbing.error_to_porcelain(e) from e
        resp = models.RoleGetResponse()
        resp.meta = plumbing.get_response_metadata_to_porcelain(plumbing_response.meta)
        resp.role = plumbing.role_to_porcelain(plumbing_response.role)
        return resp
    
    # Update patches a Role by ID.
    def update(self, role):
        req = RoleUpdateRequest()
        req.role.CopyFrom(plumbing.role_to_plumbing(role))
        try:
            plumbing_response = self.stub.Update(req, metadata=[('authorization', self.api_key)])
        except Exception as e:
            raise plumbing.error_to_porcelain(e) from e
        resp = models.RoleUpdateResponse()
        resp.meta = plumbing.update_response_metadata_to_porcelain(plumbing_response.meta)
        resp.role = plumbing.role_to_porcelain(plumbing_response.role)
        return resp
    
    # Delete removes a Role by ID.
    def delete(self, id):
        req = RoleDeleteRequest()
        req.id = id
        try:
            plumbing_response = self.stub.Delete(req, metadata=[('authorization', self.api_key)])
        except Exception as e:
            raise plumbing.error_to_porcelain(e) from e
        resp = models.RoleDeleteResponse()
        resp.meta = plumbing.delete_response_metadata_to_porcelain(plumbing_response.meta)
        return resp
    
    # List is a batched Get call.
    def list(self, filter):
        req = RoleListRequest()
        req.meta.CopyFrom(ListRequestMetadata())
        req.meta.limit = 25
        req.filter = filter
        def generator(svc, req):
            while True:
                try:
                    plumbing_response = svc.stub.List(req, metadata=[('authorization', svc.api_key)])
                except Exception as e:
                    raise plumbing.error_to_porcelain(e) from e
                for plumbing_item in plumbing_response.roles:
                    
                    yield plumbing.role_to_porcelain(plumbing_item)
                if plumbing_response.meta.next_cursor == '':
                    break
                req.meta.cursor = plumbing_response.meta.next_cursor
        return generator(self, req)
    
