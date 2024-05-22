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

from . import identity_sets_pb2 as identity__sets__pb2


class IdentitySetsStub(object):
    """A IdentitySet is a named grouping of Identity Aliases for Accounts.
    An Account's relationship to a IdentitySet is defined via IdentityAlias objects.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/v1.IdentitySets/Get',
                request_serializer=identity__sets__pb2.IdentitySetGetRequest.SerializeToString,
                response_deserializer=identity__sets__pb2.IdentitySetGetResponse.FromString,
                )
        self.List = channel.unary_unary(
                '/v1.IdentitySets/List',
                request_serializer=identity__sets__pb2.IdentitySetListRequest.SerializeToString,
                response_deserializer=identity__sets__pb2.IdentitySetListResponse.FromString,
                )


class IdentitySetsServicer(object):
    """A IdentitySet is a named grouping of Identity Aliases for Accounts.
    An Account's relationship to a IdentitySet is defined via IdentityAlias objects.
    """

    def Get(self, request, context):
        """// Create registers a new IdentitySet.
        rpc Create(IdentitySetCreateRequest) returns (IdentitySetCreateResponse) {
        option (v1.method_options).method = "post";
        option (v1.method_options).url = "/v1/identity-sets";
        }

        Get reads one IdentitySet by ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """// Update replaces all the fields of a IdentitySet by ID.
        rpc Update(IdentitySetUpdateRequest) returns (IdentitySetUpdateResponse) {
        option (v1.method_options).method = "put";
        option (v1.method_options).url = "/v1/identity-sets/{id}";
        }

        // Delete removes a IdentitySet by ID.
        rpc Delete(IdentitySetDeleteRequest) returns (IdentitySetDeleteResponse) {
        option (v1.method_options).method = "delete";
        option (v1.method_options).url = "/v1/identity-sets/{id}";
        }

        List gets a list of IdentitySets matching a given set of criteria.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_IdentitySetsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=identity__sets__pb2.IdentitySetGetRequest.FromString,
                    response_serializer=identity__sets__pb2.IdentitySetGetResponse.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=identity__sets__pb2.IdentitySetListRequest.FromString,
                    response_serializer=identity__sets__pb2.IdentitySetListResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'v1.IdentitySets', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class IdentitySets(object):
    """A IdentitySet is a named grouping of Identity Aliases for Accounts.
    An Account's relationship to a IdentitySet is defined via IdentityAlias objects.
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
        return grpc.experimental.unary_unary(request, target, '/v1.IdentitySets/Get',
            identity__sets__pb2.IdentitySetGetRequest.SerializeToString,
            identity__sets__pb2.IdentitySetGetResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/v1.IdentitySets/List',
            identity__sets__pb2.IdentitySetListRequest.SerializeToString,
            identity__sets__pb2.IdentitySetListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)