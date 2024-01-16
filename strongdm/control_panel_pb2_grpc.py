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

from . import control_panel_pb2 as control__panel__pb2


class ControlPanelStub(object):
    """ControlPanel contains all administrative controls.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetSSHCAPublicKey = channel.unary_unary(
                '/v1.ControlPanel/GetSSHCAPublicKey',
                request_serializer=control__panel__pb2.ControlPanelGetSSHCAPublicKeyRequest.SerializeToString,
                response_deserializer=control__panel__pb2.ControlPanelGetSSHCAPublicKeyResponse.FromString,
                )
        self.GetRDPCAPublicKey = channel.unary_unary(
                '/v1.ControlPanel/GetRDPCAPublicKey',
                request_serializer=control__panel__pb2.ControlPanelGetRDPCAPublicKeyRequest.SerializeToString,
                response_deserializer=control__panel__pb2.ControlPanelGetRDPCAPublicKeyResponse.FromString,
                )
        self.VerifyJWT = channel.unary_unary(
                '/v1.ControlPanel/VerifyJWT',
                request_serializer=control__panel__pb2.ControlPanelVerifyJWTRequest.SerializeToString,
                response_deserializer=control__panel__pb2.ControlPanelVerifyJWTResponse.FromString,
                )


class ControlPanelServicer(object):
    """ControlPanel contains all administrative controls.
    """

    def GetSSHCAPublicKey(self, request, context):
        """GetSSHCAPublicKey retrieves the SSH CA public key.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRDPCAPublicKey(self, request, context):
        """GetRDPCAPublicKey retrieves the RDP CA public key.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def VerifyJWT(self, request, context):
        """VerifyJWT reports whether the given JWT token (x-sdm-token) is valid.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ControlPanelServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetSSHCAPublicKey': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSSHCAPublicKey,
                    request_deserializer=control__panel__pb2.ControlPanelGetSSHCAPublicKeyRequest.FromString,
                    response_serializer=control__panel__pb2.ControlPanelGetSSHCAPublicKeyResponse.SerializeToString,
            ),
            'GetRDPCAPublicKey': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRDPCAPublicKey,
                    request_deserializer=control__panel__pb2.ControlPanelGetRDPCAPublicKeyRequest.FromString,
                    response_serializer=control__panel__pb2.ControlPanelGetRDPCAPublicKeyResponse.SerializeToString,
            ),
            'VerifyJWT': grpc.unary_unary_rpc_method_handler(
                    servicer.VerifyJWT,
                    request_deserializer=control__panel__pb2.ControlPanelVerifyJWTRequest.FromString,
                    response_serializer=control__panel__pb2.ControlPanelVerifyJWTResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'v1.ControlPanel', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ControlPanel(object):
    """ControlPanel contains all administrative controls.
    """

    @staticmethod
    def GetSSHCAPublicKey(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/v1.ControlPanel/GetSSHCAPublicKey',
            control__panel__pb2.ControlPanelGetSSHCAPublicKeyRequest.SerializeToString,
            control__panel__pb2.ControlPanelGetSSHCAPublicKeyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetRDPCAPublicKey(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/v1.ControlPanel/GetRDPCAPublicKey',
            control__panel__pb2.ControlPanelGetRDPCAPublicKeyRequest.SerializeToString,
            control__panel__pb2.ControlPanelGetRDPCAPublicKeyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def VerifyJWT(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/v1.ControlPanel/VerifyJWT',
            control__panel__pb2.ControlPanelVerifyJWTRequest.SerializeToString,
            control__panel__pb2.ControlPanelVerifyJWTResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
