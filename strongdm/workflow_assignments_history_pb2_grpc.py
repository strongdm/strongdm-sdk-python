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

from . import workflow_assignments_history_pb2 as workflow__assignments__history__pb2


class WorkflowAssignmentsHistoryStub(object):
    """WorkflowAssignmentsHistory provides records of all changes to the state of a WorkflowAssignment.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.List = channel.unary_unary(
                '/v1.WorkflowAssignmentsHistory/List',
                request_serializer=workflow__assignments__history__pb2.WorkflowAssignmentsHistoryListRequest.SerializeToString,
                response_deserializer=workflow__assignments__history__pb2.WorkflowAssignmentsHistoryListResponse.FromString,
                )


class WorkflowAssignmentsHistoryServicer(object):
    """WorkflowAssignmentsHistory provides records of all changes to the state of a WorkflowAssignment.
    """

    def List(self, request, context):
        """List gets a list of WorkflowAssignmentsHistory records matching a given set of criteria.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_WorkflowAssignmentsHistoryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=workflow__assignments__history__pb2.WorkflowAssignmentsHistoryListRequest.FromString,
                    response_serializer=workflow__assignments__history__pb2.WorkflowAssignmentsHistoryListResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'v1.WorkflowAssignmentsHistory', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class WorkflowAssignmentsHistory(object):
    """WorkflowAssignmentsHistory provides records of all changes to the state of a WorkflowAssignment.
    """

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
        return grpc.experimental.unary_unary(request, target, '/v1.WorkflowAssignmentsHistory/List',
            workflow__assignments__history__pb2.WorkflowAssignmentsHistoryListRequest.SerializeToString,
            workflow__assignments__history__pb2.WorkflowAssignmentsHistoryListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
