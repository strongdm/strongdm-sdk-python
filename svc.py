import grpc
from . import plumbing
from . import models

from .options_pb2 import *
from .options_pb2_grpc import *
from .drivers_pb2 import *
from .drivers_pb2_grpc import *
from .spec_pb2 import *
from .spec_pb2_grpc import *
from .nodes_pb2 import *
from .nodes_pb2_grpc import *
from .resources_pb2 import *
from .resources_pb2_grpc import *
from .role_attachments_pb2 import *
from .role_attachments_pb2_grpc import *
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
            plumbing_response = self.stub.Create(
                req,
                metadata=self.parent.get_metadata('Nodes.Create', req),
                timeout=timeout)
        except Exception as e:
            raise plumbing.error_to_porcelain(e) from e
        resp = models.NodeCreateResponse()
        resp.meta = plumbing.create_response_metadata_to_porcelain(
            plumbing_response.meta)
        resp.node = plumbing.node_to_porcelain(plumbing_response.node)
        resp.token = plumbing_response.token
        resp.rate_limit = plumbing.rate_limit_metadata_to_porcelain(
            plumbing_response.rate_limit)
        return resp

    # Get reads one Node by ID.
    def get(self, id, timeout=None):
        req = NodeGetRequest()
        req.id = id
        try:
            plumbing_response = self.stub.Get(
                req,
                metadata=self.parent.get_metadata('Nodes.Get', req),
                timeout=timeout)
        except Exception as e:
            raise plumbing.error_to_porcelain(e) from e
        resp = models.NodeGetResponse()
        resp.meta = plumbing.get_response_metadata_to_porcelain(
            plumbing_response.meta)
        resp.node = plumbing.node_to_porcelain(plumbing_response.node)
        resp.rate_limit = plumbing.rate_limit_metadata_to_porcelain(
            plumbing_response.rate_limit)
        return resp

    # Update patches a Node by ID.
    def update(self, node, timeout=None):
        req = NodeUpdateRequest()
        req.node.CopyFrom(plumbing.node_to_plumbing(node))
        try:
            plumbing_response = self.stub.Update(
                req,
                metadata=self.parent.get_metadata('Nodes.Update', req),
                timeout=timeout)
        except Exception as e:
            raise plumbing.error_to_porcelain(e) from e
        resp = models.NodeUpdateResponse()
        resp.meta = plumbing.update_response_metadata_to_porcelain(
            plumbing_response.meta)
        resp.node = plumbing.node_to_porcelain(plumbing_response.node)
        resp.rate_limit = plumbing.rate_limit_metadata_to_porcelain(
            plumbing_response.rate_limit)
        return resp

    # Delete removes a Node by ID.
    def delete(self, id, timeout=None):
        req = NodeDeleteRequest()
        req.id = id
        try:
            plumbing_response = self.stub.Delete(
                req,
                metadata=self.parent.get_metadata('Nodes.Delete', req),
                timeout=timeout)
        except Exception as e:
            raise plumbing.error_to_porcelain(e) from e
        resp = models.NodeDeleteResponse()
        resp.meta = plumbing.delete_response_metadata_to_porcelain(
            plumbing_response.meta)
        resp.rate_limit = plumbing.rate_limit_metadata_to_porcelain(
            plumbing_response.rate_limit)
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
                    plumbing_response = svc.stub.List(
                        req,
                        metadata=svc.parent.get_metadata('Nodes.List', req),
                        timeout=timeout)
                except Exception as e:
                    raise plumbing.error_to_porcelain(e) from e
                for plumbing_item in plumbing_response.nodes:

                    yield plumbing.node_to_porcelain(plumbing_item)
                if plumbing_response.meta.next_cursor == '':
                    break
                req.meta.cursor = plumbing_response.meta.next_cursor

        return generator(self, req)


class Resources:
    def __init__(self, channel, client):
        self.parent = client
        self.stub = ResourcesStub(channel)

    # Create registers a new Resource.
    def create(self, driver, timeout=None):
        req = ResourceCreateRequest()
        req.driver.CopyFrom(plumbing.driver_to_plumbing(driver))
        try:
            plumbing_response = self.stub.Create(
                req,
                metadata=self.parent.get_metadata('Resources.Create', req),
                timeout=timeout)
        except Exception as e:
            raise plumbing.error_to_porcelain(e) from e
        resp = models.ResourceCreateResponse()
        resp.meta = plumbing.create_response_metadata_to_porcelain(
            plumbing_response.meta)
        resp.resource = plumbing.resource_to_porcelain(
            plumbing_response.resource)
        resp.rate_limit = plumbing.rate_limit_metadata_to_porcelain(
            plumbing_response.rate_limit)
        return resp

    # Get reads one Resource by ID.
    def get(self, id, timeout=None):
        req = ResourceGetRequest()
        req.id = id
        try:
            plumbing_response = self.stub.Get(
                req,
                metadata=self.parent.get_metadata('Resources.Get', req),
                timeout=timeout)
        except Exception as e:
            raise plumbing.error_to_porcelain(e) from e
        resp = models.ResourceGetResponse()
        resp.meta = plumbing.get_response_metadata_to_porcelain(
            plumbing_response.meta)
        resp.resource = plumbing.resource_to_porcelain(
            plumbing_response.resource)
        resp.rate_limit = plumbing.rate_limit_metadata_to_porcelain(
            plumbing_response.rate_limit)
        return resp

    # Update patches a Resource by ID.
    def update(self, resource, timeout=None):
        req = ResourceUpdateRequest()
        req.resource.CopyFrom(plumbing.resource_to_plumbing(resource))
        try:
            plumbing_response = self.stub.Update(
                req,
                metadata=self.parent.get_metadata('Resources.Update', req),
                timeout=timeout)
        except Exception as e:
            raise plumbing.error_to_porcelain(e) from e
        resp = models.ResourceUpdateResponse()
        resp.meta = plumbing.update_response_metadata_to_porcelain(
            plumbing_response.meta)
        resp.resource = plumbing.resource_to_porcelain(
            plumbing_response.resource)
        resp.rate_limit = plumbing.rate_limit_metadata_to_porcelain(
            plumbing_response.rate_limit)
        return resp

    # Delete removes a Resource by ID.
    def delete(self, id, timeout=None):
        req = ResourceDeleteRequest()
        req.id = id
        try:
            plumbing_response = self.stub.Delete(
                req,
                metadata=self.parent.get_metadata('Resources.Delete', req),
                timeout=timeout)
        except Exception as e:
            raise plumbing.error_to_porcelain(e) from e
        resp = models.ResourceDeleteResponse()
        resp.meta = plumbing.delete_response_metadata_to_porcelain(
            plumbing_response.meta)
        resp.rate_limit = plumbing.rate_limit_metadata_to_porcelain(
            plumbing_response.rate_limit)
        return resp

    # List gets a list of Resources matching a given set of criteria.
    def list(self, filter, timeout=None):
        req = ResourceListRequest()
        req.meta.CopyFrom(ListRequestMetadata())
        page_size_option = self.parent._test_options.get('PageSize')
        if isinstance(page_size_option, int):
            req.meta.limit = page_size_option
        req.filter = filter

        def generator(svc, req):
            while True:
                try:
                    plumbing_response = svc.stub.List(
                        req,
                        metadata=svc.parent.get_metadata(
                            'Resources.List', req),
                        timeout=timeout)
                except Exception as e:
                    raise plumbing.error_to_porcelain(e) from e
                for plumbing_item in plumbing_response.resources:

                    yield plumbing.resource_to_porcelain(plumbing_item)
                if plumbing_response.meta.next_cursor == '':
                    break
                req.meta.cursor = plumbing_response.meta.next_cursor

        return generator(self, req)


# RoleAttachments represent relationships between composite roles and the roles
# that make up those composite roles. When a composite role is attached to another
# role, the permissions granted to members of the composite role are augmented to
# include the permissions granted to members of the attached role.
class RoleAttachments:
    def __init__(self, channel, client):
        self.parent = client
        self.stub = RoleAttachmentsStub(channel)

    # Create registers a new RoleAttachment.
    def create(self, role_attachment, timeout=None):
        req = RoleAttachmentCreateRequest()
        req.role_attachment.CopyFrom(
            plumbing.role_attachment_to_plumbing(role_attachment))
        try:
            plumbing_response = self.stub.Create(
                req,
                metadata=self.parent.get_metadata('RoleAttachments.Create',
                                                  req),
                timeout=timeout)
        except Exception as e:
            raise plumbing.error_to_porcelain(e) from e
        resp = models.RoleAttachmentCreateResponse()
        resp.meta = plumbing.create_response_metadata_to_porcelain(
            plumbing_response.meta)
        resp.role_attachment = plumbing.role_attachment_to_porcelain(
            plumbing_response.role_attachment)
        resp.rate_limit = plumbing.rate_limit_metadata_to_porcelain(
            plumbing_response.rate_limit)
        return resp

    # Get reads one RoleAttachment by ID.
    def get(self, id, timeout=None):
        req = RoleAttachmentGetRequest()
        req.id = id
        try:
            plumbing_response = self.stub.Get(
                req,
                metadata=self.parent.get_metadata('RoleAttachments.Get', req),
                timeout=timeout)
        except Exception as e:
            raise plumbing.error_to_porcelain(e) from e
        resp = models.RoleAttachmentGetResponse()
        resp.meta = plumbing.get_response_metadata_to_porcelain(
            plumbing_response.meta)
        resp.role_attachment = plumbing.role_attachment_to_porcelain(
            plumbing_response.role_attachment)
        resp.rate_limit = plumbing.rate_limit_metadata_to_porcelain(
            plumbing_response.rate_limit)
        return resp

    # Delete removes a RoleAttachment by ID.
    def delete(self, id, timeout=None):
        req = RoleAttachmentDeleteRequest()
        req.id = id
        try:
            plumbing_response = self.stub.Delete(
                req,
                metadata=self.parent.get_metadata('RoleAttachments.Delete',
                                                  req),
                timeout=timeout)
        except Exception as e:
            raise plumbing.error_to_porcelain(e) from e
        resp = models.RoleAttachmentDeleteResponse()
        resp.meta = plumbing.delete_response_metadata_to_porcelain(
            plumbing_response.meta)
        resp.rate_limit = plumbing.rate_limit_metadata_to_porcelain(
            plumbing_response.rate_limit)
        return resp

    # List gets a list of RoleAttachments matching a given set of criteria.
    def list(self, filter, timeout=None):
        req = RoleAttachmentListRequest()
        req.meta.CopyFrom(ListRequestMetadata())
        page_size_option = self.parent._test_options.get('PageSize')
        if isinstance(page_size_option, int):
            req.meta.limit = page_size_option
        req.filter = filter

        def generator(svc, req):
            while True:
                try:
                    plumbing_response = svc.stub.List(
                        req,
                        metadata=svc.parent.get_metadata(
                            'RoleAttachments.List', req),
                        timeout=timeout)
                except Exception as e:
                    raise plumbing.error_to_porcelain(e) from e
                for plumbing_item in plumbing_response.role_attachments:

                    yield plumbing.role_attachment_to_porcelain(plumbing_item)
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
            plumbing_response = self.stub.Create(
                req,
                metadata=self.parent.get_metadata('Roles.Create', req),
                timeout=timeout)
        except Exception as e:
            raise plumbing.error_to_porcelain(e) from e
        resp = models.RoleCreateResponse()
        resp.meta = plumbing.create_response_metadata_to_porcelain(
            plumbing_response.meta)
        resp.role = plumbing.role_to_porcelain(plumbing_response.role)
        resp.rate_limit = plumbing.rate_limit_metadata_to_porcelain(
            plumbing_response.rate_limit)
        return resp

    # Get reads one Role by ID.
    def get(self, id, timeout=None):
        req = RoleGetRequest()
        req.id = id
        try:
            plumbing_response = self.stub.Get(
                req,
                metadata=self.parent.get_metadata('Roles.Get', req),
                timeout=timeout)
        except Exception as e:
            raise plumbing.error_to_porcelain(e) from e
        resp = models.RoleGetResponse()
        resp.meta = plumbing.get_response_metadata_to_porcelain(
            plumbing_response.meta)
        resp.role = plumbing.role_to_porcelain(plumbing_response.role)
        resp.rate_limit = plumbing.rate_limit_metadata_to_porcelain(
            plumbing_response.rate_limit)
        return resp

    # Update patches a Role by ID.
    def update(self, role, timeout=None):
        req = RoleUpdateRequest()
        req.role.CopyFrom(plumbing.role_to_plumbing(role))
        try:
            plumbing_response = self.stub.Update(
                req,
                metadata=self.parent.get_metadata('Roles.Update', req),
                timeout=timeout)
        except Exception as e:
            raise plumbing.error_to_porcelain(e) from e
        resp = models.RoleUpdateResponse()
        resp.meta = plumbing.update_response_metadata_to_porcelain(
            plumbing_response.meta)
        resp.role = plumbing.role_to_porcelain(plumbing_response.role)
        resp.rate_limit = plumbing.rate_limit_metadata_to_porcelain(
            plumbing_response.rate_limit)
        return resp

    # Delete removes a Role by ID.
    def delete(self, id, timeout=None):
        req = RoleDeleteRequest()
        req.id = id
        try:
            plumbing_response = self.stub.Delete(
                req,
                metadata=self.parent.get_metadata('Roles.Delete', req),
                timeout=timeout)
        except Exception as e:
            raise plumbing.error_to_porcelain(e) from e
        resp = models.RoleDeleteResponse()
        resp.meta = plumbing.delete_response_metadata_to_porcelain(
            plumbing_response.meta)
        resp.rate_limit = plumbing.rate_limit_metadata_to_porcelain(
            plumbing_response.rate_limit)
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
                    plumbing_response = svc.stub.List(
                        req,
                        metadata=svc.parent.get_metadata('Roles.List', req),
                        timeout=timeout)
                except Exception as e:
                    raise plumbing.error_to_porcelain(e) from e
                for plumbing_item in plumbing_response.roles:

                    yield plumbing.role_to_porcelain(plumbing_item)
                if plumbing_response.meta.next_cursor == '':
                    break
                req.meta.cursor = plumbing_response.meta.next_cursor

        return generator(self, req)
