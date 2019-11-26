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


# Nodes are proxies in the strongDM network. They come in two flavors: relays,
# which communicate with resources, and gateways, which communicate with
# clients.
class Nodes:
    def __init__(self, channel, client):
        self.parent = client
        self.stub = NodesStub(channel)
    
    # Create registers a new Node.
    def create(self, node, timeout=None):
        req = NodeCreateRequest()
        req.node.CopyFrom(plumbing.node_to_plumbing(node))
        try:
            plumbing_response = self.stub.Create(req, metadata=[('authorization', self.parent.api_key)], timeout=timeout)
        except Exception as e:
            raise plumbing.error_to_porcelain(e) from e
        resp = models.NodeCreateResponse()
        resp.meta = plumbing.create_response_metadata_to_porcelain(plumbing_response.meta)
        resp.node = plumbing.node_to_porcelain(plumbing_response.node)
        resp.token = plumbing_response.token
        return resp
    
    # Get reads one Node by ID.
    def get(self, id, timeout=None):
        req = NodeGetRequest()
        req.id = id
        try:
            plumbing_response = self.stub.Get(req, metadata=[('authorization', self.parent.api_key)], timeout=timeout)
        except Exception as e:
            raise plumbing.error_to_porcelain(e) from e
        resp = models.NodeGetResponse()
        resp.meta = plumbing.get_response_metadata_to_porcelain(plumbing_response.meta)
        resp.node = plumbing.node_to_porcelain(plumbing_response.node)
        return resp
    
    # Update patches a Node by ID.
    def update(self, node, timeout=None):
        req = NodeUpdateRequest()
        req.node.CopyFrom(plumbing.node_to_plumbing(node))
        try:
            plumbing_response = self.stub.Update(req, metadata=[('authorization', self.parent.api_key)], timeout=timeout)
        except Exception as e:
            raise plumbing.error_to_porcelain(e) from e
        resp = models.NodeUpdateResponse()
        resp.meta = plumbing.update_response_metadata_to_porcelain(plumbing_response.meta)
        resp.node = plumbing.node_to_porcelain(plumbing_response.node)
        return resp
    
    # Delete removes a Node by ID.
    def delete(self, id, timeout=None):
        req = NodeDeleteRequest()
        req.id = id
        try:
            plumbing_response = self.stub.Delete(req, metadata=[('authorization', self.parent.api_key)], timeout=timeout)
        except Exception as e:
            raise plumbing.error_to_porcelain(e) from e
        resp = models.NodeDeleteResponse()
        resp.meta = plumbing.delete_response_metadata_to_porcelain(plumbing_response.meta)
        return resp
    
    # List gets a list of Nodes matching a given set of criteria.
    def list(self, filter, timeout=None):
        req = NodeListRequest()
        req.meta.CopyFrom(ListRequestMetadata())
        page_size_option = self.parent._test_options.get('PageSize')
        if isinstance(page_size_option, int):
            req.meta.limit = page_size_option
        req.filter = filter
        def generator(svc, req):
            while True:
                try:
                    plumbing_response = svc.stub.List(req, metadata=[('authorization', svc.parent.api_key)], timeout=timeout)
                except Exception as e:
                    raise plumbing.error_to_porcelain(e) from e
                for plumbing_item in plumbing_response.nodes:
                    
                    yield plumbing.node_to_porcelain(plumbing_item)
                if plumbing_response.meta.next_cursor == '':
                    break
                req.meta.cursor = plumbing_response.meta.next_cursor
        return generator(self, req)
    

# Roles are tools for controlling user access to resources. Each Role holds a
# list of resources which they grant access to. Composite roles are a special
# type of Role which have no resource associations of their own, but instead
# grant access to the combined resources associated with a set of child roles.
# Each user can be a member of one Role or composite role.
class Roles:
    def __init__(self, channel, client):
        self.parent = client
        self.stub = RolesStub(channel)
    
    # Create registers a new Role.
    def create(self, role, timeout=None):
        req = RoleCreateRequest()
        req.role.CopyFrom(plumbing.role_to_plumbing(role))
        try:
            plumbing_response = self.stub.Create(req, metadata=[('authorization', self.parent.api_key)], timeout=timeout)
        except Exception as e:
            raise plumbing.error_to_porcelain(e) from e
        resp = models.RoleCreateResponse()
        resp.meta = plumbing.create_response_metadata_to_porcelain(plumbing_response.meta)
        resp.role = plumbing.role_to_porcelain(plumbing_response.role)
        return resp
    
    # Get reads one Role by ID.
    def get(self, id, timeout=None):
        req = RoleGetRequest()
        req.id = id
        try:
            plumbing_response = self.stub.Get(req, metadata=[('authorization', self.parent.api_key)], timeout=timeout)
        except Exception as e:
            raise plumbing.error_to_porcelain(e) from e
        resp = models.RoleGetResponse()
        resp.meta = plumbing.get_response_metadata_to_porcelain(plumbing_response.meta)
        resp.role = plumbing.role_to_porcelain(plumbing_response.role)
        return resp
    
    # Update patches a Role by ID.
    def update(self, role, timeout=None):
        req = RoleUpdateRequest()
        req.role.CopyFrom(plumbing.role_to_plumbing(role))
        try:
            plumbing_response = self.stub.Update(req, metadata=[('authorization', self.parent.api_key)], timeout=timeout)
        except Exception as e:
            raise plumbing.error_to_porcelain(e) from e
        resp = models.RoleUpdateResponse()
        resp.meta = plumbing.update_response_metadata_to_porcelain(plumbing_response.meta)
        resp.role = plumbing.role_to_porcelain(plumbing_response.role)
        return resp
    
    # Delete removes a Role by ID.
    def delete(self, id, timeout=None):
        req = RoleDeleteRequest()
        req.id = id
        try:
            plumbing_response = self.stub.Delete(req, metadata=[('authorization', self.parent.api_key)], timeout=timeout)
        except Exception as e:
            raise plumbing.error_to_porcelain(e) from e
        resp = models.RoleDeleteResponse()
        resp.meta = plumbing.delete_response_metadata_to_porcelain(plumbing_response.meta)
        return resp
    
    # List gets a list of Roles matching a given set of criteria.
    def list(self, filter, timeout=None):
        req = RoleListRequest()
        req.meta.CopyFrom(ListRequestMetadata())
        page_size_option = self.parent._test_options.get('PageSize')
        if isinstance(page_size_option, int):
            req.meta.limit = page_size_option
        req.filter = filter
        def generator(svc, req):
            while True:
                try:
                    plumbing_response = svc.stub.List(req, metadata=[('authorization', svc.parent.api_key)], timeout=timeout)
                except Exception as e:
                    raise plumbing.error_to_porcelain(e) from e
                for plumbing_item in plumbing_response.roles:
                    
                    yield plumbing.role_to_porcelain(plumbing_item)
                if plumbing_response.meta.next_cursor == '':
                    break
                req.meta.cursor = plumbing_response.meta.next_cursor
        return generator(self, req)
    
