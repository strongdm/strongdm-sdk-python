# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import role_attachments_pb2 as role__attachments__pb2


class RoleAttachmentsStub(object):
  """RoleAttachments represent relationships between composite roles and the roles
  that make up those composite roles. When a composite role is attached to another
  role, the permissions granted to members of the composite role are augmented to
  include the permissions granted to members of the attached role.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Create = channel.unary_unary(
        '/v1.RoleAttachments/Create',
        request_serializer=role__attachments__pb2.RoleAttachmentCreateRequest.SerializeToString,
        response_deserializer=role__attachments__pb2.RoleAttachmentCreateResponse.FromString,
        )
    self.Get = channel.unary_unary(
        '/v1.RoleAttachments/Get',
        request_serializer=role__attachments__pb2.RoleAttachmentGetRequest.SerializeToString,
        response_deserializer=role__attachments__pb2.RoleAttachmentGetResponse.FromString,
        )
    self.Delete = channel.unary_unary(
        '/v1.RoleAttachments/Delete',
        request_serializer=role__attachments__pb2.RoleAttachmentDeleteRequest.SerializeToString,
        response_deserializer=role__attachments__pb2.RoleAttachmentDeleteResponse.FromString,
        )
    self.List = channel.unary_unary(
        '/v1.RoleAttachments/List',
        request_serializer=role__attachments__pb2.RoleAttachmentListRequest.SerializeToString,
        response_deserializer=role__attachments__pb2.RoleAttachmentListResponse.FromString,
        )


class RoleAttachmentsServicer(object):
  """RoleAttachments represent relationships between composite roles and the roles
  that make up those composite roles. When a composite role is attached to another
  role, the permissions granted to members of the composite role are augmented to
  include the permissions granted to members of the attached role.
  """

  def Create(self, request, context):
    """Create registers a new RoleAttachment.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Get(self, request, context):
    """Get reads one RoleAttachment by ID.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Delete(self, request, context):
    """Delete removes a RoleAttachment by ID.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def List(self, request, context):
    """List gets a list of RoleAttachments matching a given set of criteria.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_RoleAttachmentsServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Create': grpc.unary_unary_rpc_method_handler(
          servicer.Create,
          request_deserializer=role__attachments__pb2.RoleAttachmentCreateRequest.FromString,
          response_serializer=role__attachments__pb2.RoleAttachmentCreateResponse.SerializeToString,
      ),
      'Get': grpc.unary_unary_rpc_method_handler(
          servicer.Get,
          request_deserializer=role__attachments__pb2.RoleAttachmentGetRequest.FromString,
          response_serializer=role__attachments__pb2.RoleAttachmentGetResponse.SerializeToString,
      ),
      'Delete': grpc.unary_unary_rpc_method_handler(
          servicer.Delete,
          request_deserializer=role__attachments__pb2.RoleAttachmentDeleteRequest.FromString,
          response_serializer=role__attachments__pb2.RoleAttachmentDeleteResponse.SerializeToString,
      ),
      'List': grpc.unary_unary_rpc_method_handler(
          servicer.List,
          request_deserializer=role__attachments__pb2.RoleAttachmentListRequest.FromString,
          response_serializer=role__attachments__pb2.RoleAttachmentListResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'v1.RoleAttachments', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
