# Copyright 2020 StrongDM Inc
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# 
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import workflow_roles_pb2 as workflow__roles__pb2


class WorkflowRolesStub(object):
    """WorkflowRole links a role to a workflow. The linked roles indicate which roles a user must be a part of
    to request access to a resource via the workflow.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
                '/v1.WorkflowRoles/Create',
                request_serializer=workflow__roles__pb2.WorkflowRolesCreateRequest.SerializeToString,
                response_deserializer=workflow__roles__pb2.WorkflowRolesCreateResponse.FromString,
                )
        self.Get = channel.unary_unary(
                '/v1.WorkflowRoles/Get',
                request_serializer=workflow__roles__pb2.WorkflowRoleGetRequest.SerializeToString,
                response_deserializer=workflow__roles__pb2.WorkflowRoleGetResponse.FromString,
                )
        self.Delete = channel.unary_unary(
                '/v1.WorkflowRoles/Delete',
                request_serializer=workflow__roles__pb2.WorkflowRolesDeleteRequest.SerializeToString,
                response_deserializer=workflow__roles__pb2.WorkflowRolesDeleteResponse.FromString,
                )
        self.List = channel.unary_unary(
                '/v1.WorkflowRoles/List',
                request_serializer=workflow__roles__pb2.WorkflowRolesListRequest.SerializeToString,
                response_deserializer=workflow__roles__pb2.WorkflowRolesListResponse.FromString,
                )


class WorkflowRolesServicer(object):
    """WorkflowRole links a role to a workflow. The linked roles indicate which roles a user must be a part of
    to request access to a resource via the workflow.
    """

    def Create(self, request, context):
        """Create creates a new workflow role
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """Get reads one workflow role by ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Delete deletes a workflow role
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Lists existing workflow roles.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_WorkflowRolesServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=workflow__roles__pb2.WorkflowRolesCreateRequest.FromString,
                    response_serializer=workflow__roles__pb2.WorkflowRolesCreateResponse.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=workflow__roles__pb2.WorkflowRoleGetRequest.FromString,
                    response_serializer=workflow__roles__pb2.WorkflowRoleGetResponse.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=workflow__roles__pb2.WorkflowRolesDeleteRequest.FromString,
                    response_serializer=workflow__roles__pb2.WorkflowRolesDeleteResponse.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=workflow__roles__pb2.WorkflowRolesListRequest.FromString,
                    response_serializer=workflow__roles__pb2.WorkflowRolesListResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'v1.WorkflowRoles', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class WorkflowRoles(object):
    """WorkflowRole links a role to a workflow. The linked roles indicate which roles a user must be a part of
    to request access to a resource via the workflow.
    """

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/v1.WorkflowRoles/Create',
            workflow__roles__pb2.WorkflowRolesCreateRequest.SerializeToString,
            workflow__roles__pb2.WorkflowRolesCreateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/v1.WorkflowRoles/Get',
            workflow__roles__pb2.WorkflowRoleGetRequest.SerializeToString,
            workflow__roles__pb2.WorkflowRoleGetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/v1.WorkflowRoles/Delete',
            workflow__roles__pb2.WorkflowRolesDeleteRequest.SerializeToString,
            workflow__roles__pb2.WorkflowRolesDeleteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/v1.WorkflowRoles/List',
            workflow__roles__pb2.WorkflowRolesListRequest.SerializeToString,
            workflow__roles__pb2.WorkflowRolesListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
