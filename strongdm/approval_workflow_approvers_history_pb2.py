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
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: approval_workflow_approvers_history.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from . import approval_workflow_approvers_pb2 as approval__workflow__approvers__pb2
from . import options_pb2 as options__pb2
from . import spec_pb2 as spec__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)approval_workflow_approvers_history.proto\x12\x02v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a!approval_workflow_approvers.proto\x1a\roptions.proto\x1a\nspec.proto\"\x99\x01\n*ApprovalWorkflowApproverHistoryListRequest\x12%\n\x04meta\x18\x01 \x01(\x0b\x32\x17.v1.ListRequestMetadata\x12\x1a\n\x06\x66ilter\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:(\xfa\xf8\xb3\x07\x06\xd2\xf3\xb3\x07\x01*\xfa\xf8\xb3\x07\x18\xd2\xf3\xb3\x07\x13!terraform-provider\"\x9a\x02\n+ApprovalWorkflowApproverHistoryListResponse\x12&\n\x04meta\x18\x01 \x01(\x0b\x32\x18.v1.ListResponseMetadata\x12@\n\x07history\x18\x02 \x03(\x0b\x32#.v1.ApprovalWorkflowApproverHistoryB\n\xf2\xf8\xb3\x07\x05\xb8\xf3\xb3\x07\x01\x12W\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB,\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway:(\xfa\xf8\xb3\x07\x06\xd2\xf3\xb3\x07\x01*\xfa\xf8\xb3\x07\x18\xd2\xf3\xb3\x07\x13!terraform-provider\"\xbb\x02\n\x1f\x41pprovalWorkflowApproverHistory\x12\x1f\n\x0b\x61\x63tivity_id\x18\x01 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x39\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12L\n\x1a\x61pproval_workflow_approver\x18\x03 \x01(\x0b\x32\x1c.v1.ApprovalWorkflowApproverB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12:\n\ndeleted_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:2\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\xfa\xf8\xb3\x07\x06\xd2\xf3\xb3\x07\x01*\xfa\xf8\xb3\x07\x18\xd2\xf3\xb3\x07\x13!terraform-provider2\xb3\x02\n ApprovalWorkflowApproversHistory\x12\xa7\x01\n\x04List\x12..v1.ApprovalWorkflowApproverHistoryListRequest\x1a/.v1.ApprovalWorkflowApproverHistoryListResponse\">\x82\xf9\xb3\x07\x08\xa2\xf3\xb3\x07\x03get\x82\xf9\xb3\x07,\xaa\xf3\xb3\x07\'/v1/approval-workflow-approvers-history\x1a\x65\xca\xf9\xb3\x07$\xc2\xf9\xb3\x07\x1f\x41pprovalWorkflowApproverHistory\xca\xf9\xb3\x07\x05\xd8\xf9\xb3\x07\x01\xca\xf9\xb3\x07\x06\xca\xf9\xb3\x07\x01*\xca\xf9\xb3\x07\x18\xca\xf9\xb3\x07\x13!terraform-provider\xca\xf9\xb3\x07\x05\xe8\xf9\xb3\x07\x01\x42\xa4\x01\n\x19\x63om.strongdm.api.plumbingB(ApprovalWorkflowApproversHistoryPlumbingZ5github.com/strongdm/strongdm-sdk-go/v3/internal/v1;v1\xc2\x92\xb4\x07\x06\xa2\x8c\xb4\x07\x01*\xc2\x92\xb4\x07\x18\xa2\x8c\xb4\x07\x13!terraform-providerb\x06proto3')



_APPROVALWORKFLOWAPPROVERHISTORYLISTREQUEST = DESCRIPTOR.message_types_by_name['ApprovalWorkflowApproverHistoryListRequest']
_APPROVALWORKFLOWAPPROVERHISTORYLISTRESPONSE = DESCRIPTOR.message_types_by_name['ApprovalWorkflowApproverHistoryListResponse']
_APPROVALWORKFLOWAPPROVERHISTORY = DESCRIPTOR.message_types_by_name['ApprovalWorkflowApproverHistory']
ApprovalWorkflowApproverHistoryListRequest = _reflection.GeneratedProtocolMessageType('ApprovalWorkflowApproverHistoryListRequest', (_message.Message,), {
  'DESCRIPTOR' : _APPROVALWORKFLOWAPPROVERHISTORYLISTREQUEST,
  '__module__' : 'approval_workflow_approvers_history_pb2'
  # @@protoc_insertion_point(class_scope:v1.ApprovalWorkflowApproverHistoryListRequest)
  })
_sym_db.RegisterMessage(ApprovalWorkflowApproverHistoryListRequest)

ApprovalWorkflowApproverHistoryListResponse = _reflection.GeneratedProtocolMessageType('ApprovalWorkflowApproverHistoryListResponse', (_message.Message,), {
  'DESCRIPTOR' : _APPROVALWORKFLOWAPPROVERHISTORYLISTRESPONSE,
  '__module__' : 'approval_workflow_approvers_history_pb2'
  # @@protoc_insertion_point(class_scope:v1.ApprovalWorkflowApproverHistoryListResponse)
  })
_sym_db.RegisterMessage(ApprovalWorkflowApproverHistoryListResponse)

ApprovalWorkflowApproverHistory = _reflection.GeneratedProtocolMessageType('ApprovalWorkflowApproverHistory', (_message.Message,), {
  'DESCRIPTOR' : _APPROVALWORKFLOWAPPROVERHISTORY,
  '__module__' : 'approval_workflow_approvers_history_pb2'
  # @@protoc_insertion_point(class_scope:v1.ApprovalWorkflowApproverHistory)
  })
_sym_db.RegisterMessage(ApprovalWorkflowApproverHistory)

_APPROVALWORKFLOWAPPROVERSHISTORY = DESCRIPTOR.services_by_name['ApprovalWorkflowApproversHistory']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031com.strongdm.api.plumbingB(ApprovalWorkflowApproversHistoryPlumbingZ5github.com/strongdm/strongdm-sdk-go/v3/internal/v1;v1\302\222\264\007\006\242\214\264\007\001*\302\222\264\007\030\242\214\264\007\023!terraform-provider'
  _APPROVALWORKFLOWAPPROVERHISTORYLISTREQUEST.fields_by_name['filter']._options = None
  _APPROVALWORKFLOWAPPROVERHISTORYLISTREQUEST.fields_by_name['filter']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _APPROVALWORKFLOWAPPROVERHISTORYLISTREQUEST._options = None
  _APPROVALWORKFLOWAPPROVERHISTORYLISTREQUEST._serialized_options = b'\372\370\263\007\006\322\363\263\007\001*\372\370\263\007\030\322\363\263\007\023!terraform-provider'
  _APPROVALWORKFLOWAPPROVERHISTORYLISTRESPONSE.fields_by_name['history']._options = None
  _APPROVALWORKFLOWAPPROVERHISTORYLISTRESPONSE.fields_by_name['history']._serialized_options = b'\362\370\263\007\005\270\363\263\007\001'
  _APPROVALWORKFLOWAPPROVERHISTORYLISTRESPONSE.fields_by_name['rate_limit']._options = None
  _APPROVALWORKFLOWAPPROVERHISTORYLISTRESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\022\262\364\263\007\r!json_gateway'
  _APPROVALWORKFLOWAPPROVERHISTORYLISTRESPONSE._options = None
  _APPROVALWORKFLOWAPPROVERHISTORYLISTRESPONSE._serialized_options = b'\372\370\263\007\006\322\363\263\007\001*\372\370\263\007\030\322\363\263\007\023!terraform-provider'
  _APPROVALWORKFLOWAPPROVERHISTORY.fields_by_name['activity_id']._options = None
  _APPROVALWORKFLOWAPPROVERHISTORY.fields_by_name['activity_id']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _APPROVALWORKFLOWAPPROVERHISTORY.fields_by_name['timestamp']._options = None
  _APPROVALWORKFLOWAPPROVERHISTORY.fields_by_name['timestamp']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _APPROVALWORKFLOWAPPROVERHISTORY.fields_by_name['approval_workflow_approver']._options = None
  _APPROVALWORKFLOWAPPROVERHISTORY.fields_by_name['approval_workflow_approver']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _APPROVALWORKFLOWAPPROVERHISTORY.fields_by_name['deleted_at']._options = None
  _APPROVALWORKFLOWAPPROVERHISTORY.fields_by_name['deleted_at']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _APPROVALWORKFLOWAPPROVERHISTORY._options = None
  _APPROVALWORKFLOWAPPROVERHISTORY._serialized_options = b'\372\370\263\007\005\250\363\263\007\001\372\370\263\007\006\322\363\263\007\001*\372\370\263\007\030\322\363\263\007\023!terraform-provider'
  _APPROVALWORKFLOWAPPROVERSHISTORY._options = None
  _APPROVALWORKFLOWAPPROVERSHISTORY._serialized_options = b'\312\371\263\007$\302\371\263\007\037ApprovalWorkflowApproverHistory\312\371\263\007\005\330\371\263\007\001\312\371\263\007\006\312\371\263\007\001*\312\371\263\007\030\312\371\263\007\023!terraform-provider\312\371\263\007\005\350\371\263\007\001'
  _APPROVALWORKFLOWAPPROVERSHISTORY.methods_by_name['List']._options = None
  _APPROVALWORKFLOWAPPROVERSHISTORY.methods_by_name['List']._serialized_options = b'\202\371\263\007\010\242\363\263\007\003get\202\371\263\007,\252\363\263\007\'/v1/approval-workflow-approvers-history'
  _APPROVALWORKFLOWAPPROVERHISTORYLISTREQUEST._serialized_start=145
  _APPROVALWORKFLOWAPPROVERHISTORYLISTREQUEST._serialized_end=298
  _APPROVALWORKFLOWAPPROVERHISTORYLISTRESPONSE._serialized_start=301
  _APPROVALWORKFLOWAPPROVERHISTORYLISTRESPONSE._serialized_end=583
  _APPROVALWORKFLOWAPPROVERHISTORY._serialized_start=586
  _APPROVALWORKFLOWAPPROVERHISTORY._serialized_end=901
  _APPROVALWORKFLOWAPPROVERSHISTORY._serialized_start=904
  _APPROVALWORKFLOWAPPROVERSHISTORY._serialized_end=1211
# @@protoc_insertion_point(module_scope)
