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

from . import remote_identity_groups_pb2 as remote__identity__groups__pb2


class RemoteIdentityGroupsStub(object):
    """A RemoteIdentityGroup is a named grouping of Remote Identities for Accounts.
    An Account's relationship to a RemoteIdentityGroup is defined via RemoteIdentity objects.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/v1.RemoteIdentityGroups/Get',
                request_serializer=remote__identity__groups__pb2.RemoteIdentityGroupGetRequest.SerializeToString,
                response_deserializer=remote__identity__groups__pb2.RemoteIdentityGroupGetResponse.FromString,
                )
        self.List = channel.unary_unary(
                '/v1.RemoteIdentityGroups/List',
                request_serializer=remote__identity__groups__pb2.RemoteIdentityGroupListRequest.SerializeToString,
                response_deserializer=remote__identity__groups__pb2.RemoteIdentityGroupListResponse.FromString,
                )


class RemoteIdentityGroupsServicer(object):
    """A RemoteIdentityGroup is a named grouping of Remote Identities for Accounts.
    An Account's relationship to a RemoteIdentityGroup is defined via RemoteIdentity objects.
    """

    def Get(self, request, context):
        """// Create registers a new RemoteIdentityGroup.
        rpc Create(RemoteIdentityGroupCreateRequest) returns (RemoteIdentityGroupCreateResponse) {
        option (v1.method_options).method = "post";
        option (v1.method_options).url = "/v1/remote-identity-groups";
        }

        Get reads one RemoteIdentityGroup by ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """// Update replaces all the fields of a RemoteIdentityGroup by ID.
        rpc Update(RemoteIdentityGroupUpdateRequest) returns (RemoteIdentityGroupUpdateResponse) {
        option (v1.method_options).method = "put";
        option (v1.method_options).url = "/v1/remote-identity-groups/{id}";
        }

        // Delete removes a RemoteIdentityGroup by ID.
        rpc Delete(RemoteIdentityGroupDeleteRequest) returns (RemoteIdentityGroupDeleteResponse) {
        option (v1.method_options).method = "delete";
        option (v1.method_options).url = "/v1/remote-identity-groups/{id}";
        }

        List gets a list of RemoteIdentityGroups matching a given set of criteria.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RemoteIdentityGroupsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=remote__identity__groups__pb2.RemoteIdentityGroupGetRequest.FromString,
                    response_serializer=remote__identity__groups__pb2.RemoteIdentityGroupGetResponse.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=remote__identity__groups__pb2.RemoteIdentityGroupListRequest.FromString,
                    response_serializer=remote__identity__groups__pb2.RemoteIdentityGroupListResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'v1.RemoteIdentityGroups', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RemoteIdentityGroups(object):
    """A RemoteIdentityGroup is a named grouping of Remote Identities for Accounts.
    An Account's relationship to a RemoteIdentityGroup is defined via RemoteIdentity objects.
    """

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
        return grpc.experimental.unary_unary(request, target, '/v1.RemoteIdentityGroups/Get',
            remote__identity__groups__pb2.RemoteIdentityGroupGetRequest.SerializeToString,
            remote__identity__groups__pb2.RemoteIdentityGroupGetResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/v1.RemoteIdentityGroups/List',
            remote__identity__groups__pb2.RemoteIdentityGroupListRequest.SerializeToString,
            remote__identity__groups__pb2.RemoteIdentityGroupListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
