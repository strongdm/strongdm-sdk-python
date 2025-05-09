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
# source: approval_workflow_approvers.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import options_pb2 as options__pb2
from . import spec_pb2 as spec__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!approval_workflow_approvers.proto\x12\x02v1\x1a\roptions.proto\x1a\nspec.proto\"\x9e\x01\n%ApprovalWorkflowApproverCreateRequest\x12\'\n\x04meta\x18\x01 \x01(\x0b\x32\x19.v1.CreateRequestMetadata\x12L\n\x1a\x61pproval_workflow_approver\x18\x02 \x01(\x0b\x32\x1c.v1.ApprovalWorkflowApproverB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\x85\x02\n&ApprovalWorkflowApproverCreateResponse\x12(\n\x04meta\x18\x01 \x01(\x0b\x32\x1a.v1.CreateResponseMetadata\x12L\n\x1a\x61pproval_workflow_approver\x18\x02 \x01(\x0b\x32\x1c.v1.ApprovalWorkflowApproverB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12W\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB,\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"b\n\"ApprovalWorkflowApproverGetRequest\x12$\n\x04meta\x18\x01 \x01(\x0b\x32\x16.v1.GetRequestMetadata\x12\x16\n\x02id\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\x8b\x02\n#ApprovalWorkflowApproverGetResponse\x12\x31\n\x04meta\x18\x01 \x01(\x0b\x32\x17.v1.GetResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12L\n\x1a\x61pproval_workflow_approver\x18\x02 \x01(\x0b\x32\x1c.v1.ApprovalWorkflowApproverB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12W\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB,\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"h\n%ApprovalWorkflowApproverDeleteRequest\x12\'\n\x04meta\x18\x01 \x01(\x0b\x32\x19.v1.DeleteRequestMetadata\x12\x16\n\x02id\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xcf\x01\n&ApprovalWorkflowApproverDeleteResponse\x12(\n\x04meta\x18\x01 \x01(\x0b\x32\x1a.v1.DeleteResponseMetadata\x12\x16\n\x02id\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12W\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB,\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"h\n#ApprovalWorkflowApproverListRequest\x12%\n\x04meta\x18\x01 \x01(\x0b\x32\x17.v1.ListRequestMetadata\x12\x1a\n\x06\x66ilter\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\x82\x02\n$ApprovalWorkflowApproverListResponse\x12&\n\x04meta\x18\x01 \x01(\x0b\x32\x18.v1.ListResponseMetadata\x12M\n\x1b\x61pproval_workflow_approvers\x18\x02 \x03(\x0b\x32\x1c.v1.ApprovalWorkflowApproverB\n\xf2\xf8\xb3\x07\x05\xb8\xf3\xb3\x07\x01\x12W\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB,\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"\xbc\x02\n\x18\x41pprovalWorkflowApprover\x12\x16\n\x02id\x18\x01 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12)\n\x10\x61pproval_flow_id\x18\x02 \x01(\tB\x0f\xf2\xf8\xb3\x07\n\xb0\xf3\xb3\x07\x01\xc0\xf3\xb3\x07\x01\x12)\n\x10\x61pproval_step_id\x18\x03 \x01(\tB\x0f\xf2\xf8\xb3\x07\n\xb0\xf3\xb3\x07\x01\xc0\xf3\xb3\x07\x01\x12\x1e\n\naccount_id\x18\x04 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x1b\n\x07role_id\x18\x05 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12I\n\treference\x18\x06 \x01(\tB6\xf2\xf8\xb3\x07\x31\xb0\xf3\xb3\x07\x01\x98\xf4\xb3\x07\x01\xb2\xf4\xb3\x07\x01*\xb2\xf4\xb3\x07\x13!terraform-provider\xb2\xf4\xb3\x07\x04!cli:*\x18\x01\xfa\xf8\xb3\x07#\xa8\xf3\xb3\x07\x01\xd2\xf3\xb3\x07\x01*\xd2\xf3\xb3\x07\x13!terraform-provider2\xe3\x05\n\x19\x41pprovalWorkflowApprovers\x12\x98\x01\n\x06\x43reate\x12).v1.ApprovalWorkflowApproverCreateRequest\x1a*.v1.ApprovalWorkflowApproverCreateResponse\"7\x82\xf9\xb3\x07\t\xa2\xf3\xb3\x07\x04post\x82\xf9\xb3\x07$\xaa\xf3\xb3\x07\x1f/v1/approval-workflow-approvers\x12\x92\x01\n\x03Get\x12&.v1.ApprovalWorkflowApproverGetRequest\x1a\'.v1.ApprovalWorkflowApproverGetResponse\":\x82\xf9\xb3\x07\x08\xa2\xf3\xb3\x07\x03get\x82\xf9\xb3\x07(\xaa\xf3\xb3\x07#/v1/approval-workflow-approver/{id}\x12\x9a\x01\n\x06\x44\x65lete\x12).v1.ApprovalWorkflowApproverDeleteRequest\x1a*.v1.ApprovalWorkflowApproverDeleteResponse\"9\x82\xf9\xb3\x07\x0b\xa2\xf3\xb3\x07\x06\x64\x65lete\x82\xf9\xb3\x07$\xaa\xf3\xb3\x07\x1f/v1/approval-workflow-approvers\x12\x91\x01\n\x04List\x12\'.v1.ApprovalWorkflowApproverListRequest\x1a(.v1.ApprovalWorkflowApproverListResponse\"6\x82\xf9\xb3\x07\x08\xa2\xf3\xb3\x07\x03get\x82\xf9\xb3\x07$\xaa\xf3\xb3\x07\x1f/v1/approval-workflow-approvers\x1a\x65\x88\x02\x01\xca\xf9\xb3\x07\x1d\xc2\xf9\xb3\x07\x18\x41pprovalWorkflowApprover\xca\xf9\xb3\x07\t\xd2\xf9\xb3\x07\x04\x61\x66\x61-\xca\xf9\xb3\x07\x05\xe8\xf9\xb3\x07\x01\xca\xf9\xb3\x07\x06\xca\xf9\xb3\x07\x01*\xca\xf9\xb3\x07\x18\xca\xf9\xb3\x07\x13!terraform-providerBu\n\x19\x63om.strongdm.api.plumbingB!ApprovalWorkflowApproversPlumbingZ5github.com/strongdm/strongdm-sdk-go/v3/internal/v1;v1b\x06proto3')



_APPROVALWORKFLOWAPPROVERCREATEREQUEST = DESCRIPTOR.message_types_by_name['ApprovalWorkflowApproverCreateRequest']
_APPROVALWORKFLOWAPPROVERCREATERESPONSE = DESCRIPTOR.message_types_by_name['ApprovalWorkflowApproverCreateResponse']
_APPROVALWORKFLOWAPPROVERGETREQUEST = DESCRIPTOR.message_types_by_name['ApprovalWorkflowApproverGetRequest']
_APPROVALWORKFLOWAPPROVERGETRESPONSE = DESCRIPTOR.message_types_by_name['ApprovalWorkflowApproverGetResponse']
_APPROVALWORKFLOWAPPROVERDELETEREQUEST = DESCRIPTOR.message_types_by_name['ApprovalWorkflowApproverDeleteRequest']
_APPROVALWORKFLOWAPPROVERDELETERESPONSE = DESCRIPTOR.message_types_by_name['ApprovalWorkflowApproverDeleteResponse']
_APPROVALWORKFLOWAPPROVERLISTREQUEST = DESCRIPTOR.message_types_by_name['ApprovalWorkflowApproverListRequest']
_APPROVALWORKFLOWAPPROVERLISTRESPONSE = DESCRIPTOR.message_types_by_name['ApprovalWorkflowApproverListResponse']
_APPROVALWORKFLOWAPPROVER = DESCRIPTOR.message_types_by_name['ApprovalWorkflowApprover']
ApprovalWorkflowApproverCreateRequest = _reflection.GeneratedProtocolMessageType('ApprovalWorkflowApproverCreateRequest', (_message.Message,), {
  'DESCRIPTOR' : _APPROVALWORKFLOWAPPROVERCREATEREQUEST,
  '__module__' : 'approval_workflow_approvers_pb2'
  # @@protoc_insertion_point(class_scope:v1.ApprovalWorkflowApproverCreateRequest)
  })
_sym_db.RegisterMessage(ApprovalWorkflowApproverCreateRequest)

ApprovalWorkflowApproverCreateResponse = _reflection.GeneratedProtocolMessageType('ApprovalWorkflowApproverCreateResponse', (_message.Message,), {
  'DESCRIPTOR' : _APPROVALWORKFLOWAPPROVERCREATERESPONSE,
  '__module__' : 'approval_workflow_approvers_pb2'
  # @@protoc_insertion_point(class_scope:v1.ApprovalWorkflowApproverCreateResponse)
  })
_sym_db.RegisterMessage(ApprovalWorkflowApproverCreateResponse)

ApprovalWorkflowApproverGetRequest = _reflection.GeneratedProtocolMessageType('ApprovalWorkflowApproverGetRequest', (_message.Message,), {
  'DESCRIPTOR' : _APPROVALWORKFLOWAPPROVERGETREQUEST,
  '__module__' : 'approval_workflow_approvers_pb2'
  # @@protoc_insertion_point(class_scope:v1.ApprovalWorkflowApproverGetRequest)
  })
_sym_db.RegisterMessage(ApprovalWorkflowApproverGetRequest)

ApprovalWorkflowApproverGetResponse = _reflection.GeneratedProtocolMessageType('ApprovalWorkflowApproverGetResponse', (_message.Message,), {
  'DESCRIPTOR' : _APPROVALWORKFLOWAPPROVERGETRESPONSE,
  '__module__' : 'approval_workflow_approvers_pb2'
  # @@protoc_insertion_point(class_scope:v1.ApprovalWorkflowApproverGetResponse)
  })
_sym_db.RegisterMessage(ApprovalWorkflowApproverGetResponse)

ApprovalWorkflowApproverDeleteRequest = _reflection.GeneratedProtocolMessageType('ApprovalWorkflowApproverDeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _APPROVALWORKFLOWAPPROVERDELETEREQUEST,
  '__module__' : 'approval_workflow_approvers_pb2'
  # @@protoc_insertion_point(class_scope:v1.ApprovalWorkflowApproverDeleteRequest)
  })
_sym_db.RegisterMessage(ApprovalWorkflowApproverDeleteRequest)

ApprovalWorkflowApproverDeleteResponse = _reflection.GeneratedProtocolMessageType('ApprovalWorkflowApproverDeleteResponse', (_message.Message,), {
  'DESCRIPTOR' : _APPROVALWORKFLOWAPPROVERDELETERESPONSE,
  '__module__' : 'approval_workflow_approvers_pb2'
  # @@protoc_insertion_point(class_scope:v1.ApprovalWorkflowApproverDeleteResponse)
  })
_sym_db.RegisterMessage(ApprovalWorkflowApproverDeleteResponse)

ApprovalWorkflowApproverListRequest = _reflection.GeneratedProtocolMessageType('ApprovalWorkflowApproverListRequest', (_message.Message,), {
  'DESCRIPTOR' : _APPROVALWORKFLOWAPPROVERLISTREQUEST,
  '__module__' : 'approval_workflow_approvers_pb2'
  # @@protoc_insertion_point(class_scope:v1.ApprovalWorkflowApproverListRequest)
  })
_sym_db.RegisterMessage(ApprovalWorkflowApproverListRequest)

ApprovalWorkflowApproverListResponse = _reflection.GeneratedProtocolMessageType('ApprovalWorkflowApproverListResponse', (_message.Message,), {
  'DESCRIPTOR' : _APPROVALWORKFLOWAPPROVERLISTRESPONSE,
  '__module__' : 'approval_workflow_approvers_pb2'
  # @@protoc_insertion_point(class_scope:v1.ApprovalWorkflowApproverListResponse)
  })
_sym_db.RegisterMessage(ApprovalWorkflowApproverListResponse)

ApprovalWorkflowApprover = _reflection.GeneratedProtocolMessageType('ApprovalWorkflowApprover', (_message.Message,), {
  'DESCRIPTOR' : _APPROVALWORKFLOWAPPROVER,
  '__module__' : 'approval_workflow_approvers_pb2'
  # @@protoc_insertion_point(class_scope:v1.ApprovalWorkflowApprover)
  })
_sym_db.RegisterMessage(ApprovalWorkflowApprover)

_APPROVALWORKFLOWAPPROVERS = DESCRIPTOR.services_by_name['ApprovalWorkflowApprovers']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031com.strongdm.api.plumbingB!ApprovalWorkflowApproversPlumbingZ5github.com/strongdm/strongdm-sdk-go/v3/internal/v1;v1'
  _APPROVALWORKFLOWAPPROVERCREATEREQUEST.fields_by_name['approval_workflow_approver']._options = None
  _APPROVALWORKFLOWAPPROVERCREATEREQUEST.fields_by_name['approval_workflow_approver']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _APPROVALWORKFLOWAPPROVERCREATERESPONSE.fields_by_name['approval_workflow_approver']._options = None
  _APPROVALWORKFLOWAPPROVERCREATERESPONSE.fields_by_name['approval_workflow_approver']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _APPROVALWORKFLOWAPPROVERCREATERESPONSE.fields_by_name['rate_limit']._options = None
  _APPROVALWORKFLOWAPPROVERCREATERESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\022\262\364\263\007\r!json_gateway'
  _APPROVALWORKFLOWAPPROVERCREATERESPONSE._options = None
  _APPROVALWORKFLOWAPPROVERCREATERESPONSE._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _APPROVALWORKFLOWAPPROVERGETREQUEST.fields_by_name['id']._options = None
  _APPROVALWORKFLOWAPPROVERGETREQUEST.fields_by_name['id']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _APPROVALWORKFLOWAPPROVERGETRESPONSE.fields_by_name['meta']._options = None
  _APPROVALWORKFLOWAPPROVERGETRESPONSE.fields_by_name['meta']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _APPROVALWORKFLOWAPPROVERGETRESPONSE.fields_by_name['approval_workflow_approver']._options = None
  _APPROVALWORKFLOWAPPROVERGETRESPONSE.fields_by_name['approval_workflow_approver']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _APPROVALWORKFLOWAPPROVERGETRESPONSE.fields_by_name['rate_limit']._options = None
  _APPROVALWORKFLOWAPPROVERGETRESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\022\262\364\263\007\r!json_gateway'
  _APPROVALWORKFLOWAPPROVERGETRESPONSE._options = None
  _APPROVALWORKFLOWAPPROVERGETRESPONSE._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _APPROVALWORKFLOWAPPROVERDELETEREQUEST.fields_by_name['id']._options = None
  _APPROVALWORKFLOWAPPROVERDELETEREQUEST.fields_by_name['id']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _APPROVALWORKFLOWAPPROVERDELETERESPONSE.fields_by_name['id']._options = None
  _APPROVALWORKFLOWAPPROVERDELETERESPONSE.fields_by_name['id']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _APPROVALWORKFLOWAPPROVERDELETERESPONSE.fields_by_name['rate_limit']._options = None
  _APPROVALWORKFLOWAPPROVERDELETERESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\022\262\364\263\007\r!json_gateway'
  _APPROVALWORKFLOWAPPROVERDELETERESPONSE._options = None
  _APPROVALWORKFLOWAPPROVERDELETERESPONSE._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _APPROVALWORKFLOWAPPROVERLISTREQUEST.fields_by_name['filter']._options = None
  _APPROVALWORKFLOWAPPROVERLISTREQUEST.fields_by_name['filter']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _APPROVALWORKFLOWAPPROVERLISTRESPONSE.fields_by_name['approval_workflow_approvers']._options = None
  _APPROVALWORKFLOWAPPROVERLISTRESPONSE.fields_by_name['approval_workflow_approvers']._serialized_options = b'\362\370\263\007\005\270\363\263\007\001'
  _APPROVALWORKFLOWAPPROVERLISTRESPONSE.fields_by_name['rate_limit']._options = None
  _APPROVALWORKFLOWAPPROVERLISTRESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\022\262\364\263\007\r!json_gateway'
  _APPROVALWORKFLOWAPPROVERLISTRESPONSE._options = None
  _APPROVALWORKFLOWAPPROVERLISTRESPONSE._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _APPROVALWORKFLOWAPPROVER.fields_by_name['id']._options = None
  _APPROVALWORKFLOWAPPROVER.fields_by_name['id']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _APPROVALWORKFLOWAPPROVER.fields_by_name['approval_flow_id']._options = None
  _APPROVALWORKFLOWAPPROVER.fields_by_name['approval_flow_id']._serialized_options = b'\362\370\263\007\n\260\363\263\007\001\300\363\263\007\001'
  _APPROVALWORKFLOWAPPROVER.fields_by_name['approval_step_id']._options = None
  _APPROVALWORKFLOWAPPROVER.fields_by_name['approval_step_id']._serialized_options = b'\362\370\263\007\n\260\363\263\007\001\300\363\263\007\001'
  _APPROVALWORKFLOWAPPROVER.fields_by_name['account_id']._options = None
  _APPROVALWORKFLOWAPPROVER.fields_by_name['account_id']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _APPROVALWORKFLOWAPPROVER.fields_by_name['role_id']._options = None
  _APPROVALWORKFLOWAPPROVER.fields_by_name['role_id']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _APPROVALWORKFLOWAPPROVER.fields_by_name['reference']._options = None
  _APPROVALWORKFLOWAPPROVER.fields_by_name['reference']._serialized_options = b'\362\370\263\0071\260\363\263\007\001\230\364\263\007\001\262\364\263\007\001*\262\364\263\007\023!terraform-provider\262\364\263\007\004!cli'
  _APPROVALWORKFLOWAPPROVER._options = None
  _APPROVALWORKFLOWAPPROVER._serialized_options = b'\030\001\372\370\263\007#\250\363\263\007\001\322\363\263\007\001*\322\363\263\007\023!terraform-provider'
  _APPROVALWORKFLOWAPPROVERS._options = None
  _APPROVALWORKFLOWAPPROVERS._serialized_options = b'\210\002\001\312\371\263\007\035\302\371\263\007\030ApprovalWorkflowApprover\312\371\263\007\t\322\371\263\007\004afa-\312\371\263\007\005\350\371\263\007\001\312\371\263\007\006\312\371\263\007\001*\312\371\263\007\030\312\371\263\007\023!terraform-provider'
  _APPROVALWORKFLOWAPPROVERS.methods_by_name['Create']._options = None
  _APPROVALWORKFLOWAPPROVERS.methods_by_name['Create']._serialized_options = b'\202\371\263\007\t\242\363\263\007\004post\202\371\263\007$\252\363\263\007\037/v1/approval-workflow-approvers'
  _APPROVALWORKFLOWAPPROVERS.methods_by_name['Get']._options = None
  _APPROVALWORKFLOWAPPROVERS.methods_by_name['Get']._serialized_options = b'\202\371\263\007\010\242\363\263\007\003get\202\371\263\007(\252\363\263\007#/v1/approval-workflow-approver/{id}'
  _APPROVALWORKFLOWAPPROVERS.methods_by_name['Delete']._options = None
  _APPROVALWORKFLOWAPPROVERS.methods_by_name['Delete']._serialized_options = b'\202\371\263\007\013\242\363\263\007\006delete\202\371\263\007$\252\363\263\007\037/v1/approval-workflow-approvers'
  _APPROVALWORKFLOWAPPROVERS.methods_by_name['List']._options = None
  _APPROVALWORKFLOWAPPROVERS.methods_by_name['List']._serialized_options = b'\202\371\263\007\010\242\363\263\007\003get\202\371\263\007$\252\363\263\007\037/v1/approval-workflow-approvers'
  _APPROVALWORKFLOWAPPROVERCREATEREQUEST._serialized_start=69
  _APPROVALWORKFLOWAPPROVERCREATEREQUEST._serialized_end=227
  _APPROVALWORKFLOWAPPROVERCREATERESPONSE._serialized_start=230
  _APPROVALWORKFLOWAPPROVERCREATERESPONSE._serialized_end=491
  _APPROVALWORKFLOWAPPROVERGETREQUEST._serialized_start=493
  _APPROVALWORKFLOWAPPROVERGETREQUEST._serialized_end=591
  _APPROVALWORKFLOWAPPROVERGETRESPONSE._serialized_start=594
  _APPROVALWORKFLOWAPPROVERGETRESPONSE._serialized_end=861
  _APPROVALWORKFLOWAPPROVERDELETEREQUEST._serialized_start=863
  _APPROVALWORKFLOWAPPROVERDELETEREQUEST._serialized_end=967
  _APPROVALWORKFLOWAPPROVERDELETERESPONSE._serialized_start=970
  _APPROVALWORKFLOWAPPROVERDELETERESPONSE._serialized_end=1177
  _APPROVALWORKFLOWAPPROVERLISTREQUEST._serialized_start=1179
  _APPROVALWORKFLOWAPPROVERLISTREQUEST._serialized_end=1283
  _APPROVALWORKFLOWAPPROVERLISTRESPONSE._serialized_start=1286
  _APPROVALWORKFLOWAPPROVERLISTRESPONSE._serialized_end=1544
  _APPROVALWORKFLOWAPPROVER._serialized_start=1547
  _APPROVALWORKFLOWAPPROVER._serialized_end=1863
  _APPROVALWORKFLOWAPPROVERS._serialized_start=1866
  _APPROVALWORKFLOWAPPROVERS._serialized_end=2605
# @@protoc_insertion_point(module_scope)
