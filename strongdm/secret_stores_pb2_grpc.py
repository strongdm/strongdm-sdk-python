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

from . import secret_stores_pb2 as secret__stores__pb2


class SecretStoresStub(object):
    """SecretStores are servers where resource secrets (passwords, keys) are stored.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
                '/v1.SecretStores/Create',
                request_serializer=secret__stores__pb2.SecretStoreCreateRequest.SerializeToString,
                response_deserializer=secret__stores__pb2.SecretStoreCreateResponse.FromString,
                )
        self.Get = channel.unary_unary(
                '/v1.SecretStores/Get',
                request_serializer=secret__stores__pb2.SecretStoreGetRequest.SerializeToString,
                response_deserializer=secret__stores__pb2.SecretStoreGetResponse.FromString,
                )
        self.Update = channel.unary_unary(
                '/v1.SecretStores/Update',
                request_serializer=secret__stores__pb2.SecretStoreUpdateRequest.SerializeToString,
                response_deserializer=secret__stores__pb2.SecretStoreUpdateResponse.FromString,
                )
        self.Delete = channel.unary_unary(
                '/v1.SecretStores/Delete',
                request_serializer=secret__stores__pb2.SecretStoreDeleteRequest.SerializeToString,
                response_deserializer=secret__stores__pb2.SecretStoreDeleteResponse.FromString,
                )
        self.List = channel.unary_unary(
                '/v1.SecretStores/List',
                request_serializer=secret__stores__pb2.SecretStoreListRequest.SerializeToString,
                response_deserializer=secret__stores__pb2.SecretStoreListResponse.FromString,
                )


class SecretStoresServicer(object):
    """SecretStores are servers where resource secrets (passwords, keys) are stored.
    """

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """Get reads one SecretStore by ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Update replaces all the fields of a SecretStore by ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Delete removes a SecretStore by ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """List gets a list of SecretStores matching a given set of criteria.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SecretStoresServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=secret__stores__pb2.SecretStoreCreateRequest.FromString,
                    response_serializer=secret__stores__pb2.SecretStoreCreateResponse.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=secret__stores__pb2.SecretStoreGetRequest.FromString,
                    response_serializer=secret__stores__pb2.SecretStoreGetResponse.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=secret__stores__pb2.SecretStoreUpdateRequest.FromString,
                    response_serializer=secret__stores__pb2.SecretStoreUpdateResponse.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=secret__stores__pb2.SecretStoreDeleteRequest.FromString,
                    response_serializer=secret__stores__pb2.SecretStoreDeleteResponse.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=secret__stores__pb2.SecretStoreListRequest.FromString,
                    response_serializer=secret__stores__pb2.SecretStoreListResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'v1.SecretStores', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SecretStores(object):
    """SecretStores are servers where resource secrets (passwords, keys) are stored.
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
        return grpc.experimental.unary_unary(request, target, '/v1.SecretStores/Create',
            secret__stores__pb2.SecretStoreCreateRequest.SerializeToString,
            secret__stores__pb2.SecretStoreCreateResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/v1.SecretStores/Get',
            secret__stores__pb2.SecretStoreGetRequest.SerializeToString,
            secret__stores__pb2.SecretStoreGetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/v1.SecretStores/Update',
            secret__stores__pb2.SecretStoreUpdateRequest.SerializeToString,
            secret__stores__pb2.SecretStoreUpdateResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/v1.SecretStores/Delete',
            secret__stores__pb2.SecretStoreDeleteRequest.SerializeToString,
            secret__stores__pb2.SecretStoreDeleteResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/v1.SecretStores/List',
            secret__stores__pb2.SecretStoreListRequest.SerializeToString,
            secret__stores__pb2.SecretStoreListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
