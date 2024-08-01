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
# source: workflows.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fworkflows.proto\x12\x02v1\x1a\roptions.proto\x1a\nspec.proto\"l\n\x15WorkflowCreateRequest\x12\'\n\x04meta\x18\x01 \x01(\x0b\x32\x19.v1.CreateRequestMetadata\x12*\n\x08workflow\x18\x02 \x01(\x0b\x32\x0c.v1.WorkflowB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xd3\x01\n\x16WorkflowCreateResponse\x12(\n\x04meta\x18\x01 \x01(\x0b\x32\x1a.v1.CreateResponseMetadata\x12*\n\x08workflow\x18\x02 \x01(\x0b\x32\x0c.v1.WorkflowB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12W\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB,\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"R\n\x12WorkflowGetRequest\x12$\n\x04meta\x18\x01 \x01(\x0b\x32\x16.v1.GetRequestMetadata\x12\x16\n\x02id\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xd9\x01\n\x13WorkflowGetResponse\x12\x31\n\x04meta\x18\x01 \x01(\x0b\x32\x17.v1.GetResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12*\n\x08workflow\x18\x02 \x01(\x0b\x32\x0c.v1.WorkflowB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12W\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB,\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"l\n\x15WorkflowUpdateRequest\x12\'\n\x04meta\x18\x01 \x01(\x0b\x32\x19.v1.UpdateRequestMetadata\x12*\n\x08workflow\x18\x02 \x01(\x0b\x32\x0c.v1.WorkflowB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xd3\x01\n\x16WorkflowUpdateResponse\x12(\n\x04meta\x18\x01 \x01(\x0b\x32\x1a.v1.UpdateResponseMetadata\x12*\n\x08workflow\x18\x02 \x01(\x0b\x32\x0c.v1.WorkflowB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12W\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB,\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"X\n\x15WorkflowDeleteRequest\x12\'\n\x04meta\x18\x01 \x01(\x0b\x32\x19.v1.DeleteRequestMetadata\x12\x16\n\x02id\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xbf\x01\n\x16WorkflowDeleteResponse\x12(\n\x04meta\x18\x01 \x01(\x0b\x32\x1a.v1.DeleteResponseMetadata\x12\x16\n\x02id\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12W\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB,\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"X\n\x13WorkflowListRequest\x12%\n\x04meta\x18\x01 \x01(\x0b\x32\x17.v1.ListRequestMetadata\x12\x1a\n\x06\x66ilter\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xd0\x01\n\x14WorkflowListResponse\x12&\n\x04meta\x18\x01 \x01(\x0b\x32\x18.v1.ListResponseMetadata\x12+\n\tworkflows\x18\x02 \x03(\x0b\x32\x0c.v1.WorkflowB\n\xf2\xf8\xb3\x07\x05\xb8\xf3\xb3\x07\x01\x12W\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB,\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"\xf5\x04\n\x08Workflow\x12\x16\n\x02id\x18\x01 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x1d\n\x04name\x18\x02 \x01(\tB\x0f\xf2\xf8\xb3\x07\n\xb0\xf3\xb3\x07\x01\xc0\xf3\xb3\x07\x01\x12\x1f\n\x0b\x64\x65scription\x18\x03 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x1f\n\x06weight\x18\x04 \x01(\x03\x42\x0f\xf2\xf8\xb3\x07\n\xb0\xf3\xb3\x07\x01\xd0\xf4\xb3\x07\x01\x12\x1e\n\nauto_grant\x18\x05 \x01(\x08\x42\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x1b\n\x07\x65nabled\x18\x06 \x01(\x08\x42\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x32\n\x0frequires_reason\x18\x07 \x01(\x08\x42\x19\xf2\xf8\xb3\x07\x14\xb0\xf3\xb3\x07\x01\xb2\xf4\xb3\x07\ngo_private\x12\xf2\x01\n\x0c\x61\x63\x63\x65ss_rules\x18\x08 \x01(\tB\xdb\x01\xf2\xf8\xb3\x07\xd5\x01\xb0\xf3\xb3\x07\x01\xca\xf3\xb3\x07\xa9\x01\xea\xf3\xb3\x07\x0c\x61\x63\x63\x65ss_rules\xf2\xf3\xb3\x07\x11\n\x02go\x12\x0b\x41\x63\x63\x65ssRules\xf2\xf3\xb3\x07\x19\n\ngo_private\x12\x0b\x41\x63\x63\x65ssRules\xf2\xf3\xb3\x07\x1b\n\x0cgo_terraform\x12\x0b\x41\x63\x63\x65ssRules\xf2\xf3\xb3\x07\x18\n\x04java\x12\x10List<AccessRule>\xf2\xf3\xb3\x07\"\n\x0cjson_gateway\x12\x12models.AccessRules\xba\xf4\xb3\x07\x17\x61\x63\x63\x65ssRulesDiffSuppress\xd0\xf4\xb3\x07\x01\x12$\n\x10\x61pproval_flow_id\x18\t \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:d\xfa\xf8\xb3\x07_\xa8\xf3\xb3\x07\x01\xc2\xf3\xb3\x07O\xa2\xf3\xb3\x07!tf_examples/workflow_resource.txt\xaa\xf3\xb3\x07$tf_examples/workflow_data_source.txt\xd2\xf3\xb3\x07\x01*2\xb2\x04\n\tWorkflows\x12\x66\n\x06\x43reate\x12\x19.v1.WorkflowCreateRequest\x1a\x1a.v1.WorkflowCreateResponse\"%\x82\xf9\xb3\x07\t\xa2\xf3\xb3\x07\x04post\x82\xf9\xb3\x07\x12\xaa\xf3\xb3\x07\r/v1/workflows\x12`\n\x03Get\x12\x16.v1.WorkflowGetRequest\x1a\x17.v1.WorkflowGetResponse\"(\x82\xf9\xb3\x07\x08\xa2\xf3\xb3\x07\x03get\x82\xf9\xb3\x07\x16\xaa\xf3\xb3\x07\x11/v1/workflow/{id}\x12h\n\x06\x44\x65lete\x12\x19.v1.WorkflowDeleteRequest\x1a\x1a.v1.WorkflowDeleteResponse\"\'\x82\xf9\xb3\x07\x0b\xa2\xf3\xb3\x07\x06\x64\x65lete\x82\xf9\xb3\x07\x12\xaa\xf3\xb3\x07\r/v1/workflows\x12\x65\n\x06Update\x12\x19.v1.WorkflowUpdateRequest\x1a\x1a.v1.WorkflowUpdateResponse\"$\x82\xf9\xb3\x07\x08\xa2\xf3\xb3\x07\x03put\x82\xf9\xb3\x07\x12\xaa\xf3\xb3\x07\r/v1/workflows\x12_\n\x04List\x12\x17.v1.WorkflowListRequest\x1a\x18.v1.WorkflowListResponse\"$\x82\xf9\xb3\x07\x08\xa2\xf3\xb3\x07\x03get\x82\xf9\xb3\x07\x12\xaa\xf3\xb3\x07\r/v1/workflows\x1a)\xca\xf9\xb3\x07\r\xc2\xf9\xb3\x07\x08Workflow\xca\xf9\xb3\x07\x08\xd2\xf9\xb3\x07\x03\x61w-\xca\xf9\xb3\x07\x05\xe8\xf9\xb3\x07\x01\x42\x65\n\x19\x63om.strongdm.api.plumbingB\x11WorkflowsPlumbingZ5github.com/strongdm/strongdm-sdk-go/v3/internal/v1;v1b\x06proto3')



_WORKFLOWCREATEREQUEST = DESCRIPTOR.message_types_by_name['WorkflowCreateRequest']
_WORKFLOWCREATERESPONSE = DESCRIPTOR.message_types_by_name['WorkflowCreateResponse']
_WORKFLOWGETREQUEST = DESCRIPTOR.message_types_by_name['WorkflowGetRequest']
_WORKFLOWGETRESPONSE = DESCRIPTOR.message_types_by_name['WorkflowGetResponse']
_WORKFLOWUPDATEREQUEST = DESCRIPTOR.message_types_by_name['WorkflowUpdateRequest']
_WORKFLOWUPDATERESPONSE = DESCRIPTOR.message_types_by_name['WorkflowUpdateResponse']
_WORKFLOWDELETEREQUEST = DESCRIPTOR.message_types_by_name['WorkflowDeleteRequest']
_WORKFLOWDELETERESPONSE = DESCRIPTOR.message_types_by_name['WorkflowDeleteResponse']
_WORKFLOWLISTREQUEST = DESCRIPTOR.message_types_by_name['WorkflowListRequest']
_WORKFLOWLISTRESPONSE = DESCRIPTOR.message_types_by_name['WorkflowListResponse']
_WORKFLOW = DESCRIPTOR.message_types_by_name['Workflow']
WorkflowCreateRequest = _reflection.GeneratedProtocolMessageType('WorkflowCreateRequest', (_message.Message,), {
  'DESCRIPTOR' : _WORKFLOWCREATEREQUEST,
  '__module__' : 'workflows_pb2'
  # @@protoc_insertion_point(class_scope:v1.WorkflowCreateRequest)
  })
_sym_db.RegisterMessage(WorkflowCreateRequest)

WorkflowCreateResponse = _reflection.GeneratedProtocolMessageType('WorkflowCreateResponse', (_message.Message,), {
  'DESCRIPTOR' : _WORKFLOWCREATERESPONSE,
  '__module__' : 'workflows_pb2'
  # @@protoc_insertion_point(class_scope:v1.WorkflowCreateResponse)
  })
_sym_db.RegisterMessage(WorkflowCreateResponse)

WorkflowGetRequest = _reflection.GeneratedProtocolMessageType('WorkflowGetRequest', (_message.Message,), {
  'DESCRIPTOR' : _WORKFLOWGETREQUEST,
  '__module__' : 'workflows_pb2'
  # @@protoc_insertion_point(class_scope:v1.WorkflowGetRequest)
  })
_sym_db.RegisterMessage(WorkflowGetRequest)

WorkflowGetResponse = _reflection.GeneratedProtocolMessageType('WorkflowGetResponse', (_message.Message,), {
  'DESCRIPTOR' : _WORKFLOWGETRESPONSE,
  '__module__' : 'workflows_pb2'
  # @@protoc_insertion_point(class_scope:v1.WorkflowGetResponse)
  })
_sym_db.RegisterMessage(WorkflowGetResponse)

WorkflowUpdateRequest = _reflection.GeneratedProtocolMessageType('WorkflowUpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _WORKFLOWUPDATEREQUEST,
  '__module__' : 'workflows_pb2'
  # @@protoc_insertion_point(class_scope:v1.WorkflowUpdateRequest)
  })
_sym_db.RegisterMessage(WorkflowUpdateRequest)

WorkflowUpdateResponse = _reflection.GeneratedProtocolMessageType('WorkflowUpdateResponse', (_message.Message,), {
  'DESCRIPTOR' : _WORKFLOWUPDATERESPONSE,
  '__module__' : 'workflows_pb2'
  # @@protoc_insertion_point(class_scope:v1.WorkflowUpdateResponse)
  })
_sym_db.RegisterMessage(WorkflowUpdateResponse)

WorkflowDeleteRequest = _reflection.GeneratedProtocolMessageType('WorkflowDeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _WORKFLOWDELETEREQUEST,
  '__module__' : 'workflows_pb2'
  # @@protoc_insertion_point(class_scope:v1.WorkflowDeleteRequest)
  })
_sym_db.RegisterMessage(WorkflowDeleteRequest)

WorkflowDeleteResponse = _reflection.GeneratedProtocolMessageType('WorkflowDeleteResponse', (_message.Message,), {
  'DESCRIPTOR' : _WORKFLOWDELETERESPONSE,
  '__module__' : 'workflows_pb2'
  # @@protoc_insertion_point(class_scope:v1.WorkflowDeleteResponse)
  })
_sym_db.RegisterMessage(WorkflowDeleteResponse)

WorkflowListRequest = _reflection.GeneratedProtocolMessageType('WorkflowListRequest', (_message.Message,), {
  'DESCRIPTOR' : _WORKFLOWLISTREQUEST,
  '__module__' : 'workflows_pb2'
  # @@protoc_insertion_point(class_scope:v1.WorkflowListRequest)
  })
_sym_db.RegisterMessage(WorkflowListRequest)

WorkflowListResponse = _reflection.GeneratedProtocolMessageType('WorkflowListResponse', (_message.Message,), {
  'DESCRIPTOR' : _WORKFLOWLISTRESPONSE,
  '__module__' : 'workflows_pb2'
  # @@protoc_insertion_point(class_scope:v1.WorkflowListResponse)
  })
_sym_db.RegisterMessage(WorkflowListResponse)

Workflow = _reflection.GeneratedProtocolMessageType('Workflow', (_message.Message,), {
  'DESCRIPTOR' : _WORKFLOW,
  '__module__' : 'workflows_pb2'
  # @@protoc_insertion_point(class_scope:v1.Workflow)
  })
_sym_db.RegisterMessage(Workflow)

_WORKFLOWS = DESCRIPTOR.services_by_name['Workflows']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031com.strongdm.api.plumbingB\021WorkflowsPlumbingZ5github.com/strongdm/strongdm-sdk-go/v3/internal/v1;v1'
  _WORKFLOWCREATEREQUEST.fields_by_name['workflow']._options = None
  _WORKFLOWCREATEREQUEST.fields_by_name['workflow']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _WORKFLOWCREATERESPONSE.fields_by_name['workflow']._options = None
  _WORKFLOWCREATERESPONSE.fields_by_name['workflow']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _WORKFLOWCREATERESPONSE.fields_by_name['rate_limit']._options = None
  _WORKFLOWCREATERESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\022\262\364\263\007\r!json_gateway'
  _WORKFLOWCREATERESPONSE._options = None
  _WORKFLOWCREATERESPONSE._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _WORKFLOWGETREQUEST.fields_by_name['id']._options = None
  _WORKFLOWGETREQUEST.fields_by_name['id']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _WORKFLOWGETRESPONSE.fields_by_name['meta']._options = None
  _WORKFLOWGETRESPONSE.fields_by_name['meta']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _WORKFLOWGETRESPONSE.fields_by_name['workflow']._options = None
  _WORKFLOWGETRESPONSE.fields_by_name['workflow']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _WORKFLOWGETRESPONSE.fields_by_name['rate_limit']._options = None
  _WORKFLOWGETRESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\022\262\364\263\007\r!json_gateway'
  _WORKFLOWGETRESPONSE._options = None
  _WORKFLOWGETRESPONSE._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _WORKFLOWUPDATEREQUEST.fields_by_name['workflow']._options = None
  _WORKFLOWUPDATEREQUEST.fields_by_name['workflow']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _WORKFLOWUPDATERESPONSE.fields_by_name['workflow']._options = None
  _WORKFLOWUPDATERESPONSE.fields_by_name['workflow']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _WORKFLOWUPDATERESPONSE.fields_by_name['rate_limit']._options = None
  _WORKFLOWUPDATERESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\022\262\364\263\007\r!json_gateway'
  _WORKFLOWUPDATERESPONSE._options = None
  _WORKFLOWUPDATERESPONSE._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _WORKFLOWDELETEREQUEST.fields_by_name['id']._options = None
  _WORKFLOWDELETEREQUEST.fields_by_name['id']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _WORKFLOWDELETERESPONSE.fields_by_name['id']._options = None
  _WORKFLOWDELETERESPONSE.fields_by_name['id']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _WORKFLOWDELETERESPONSE.fields_by_name['rate_limit']._options = None
  _WORKFLOWDELETERESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\022\262\364\263\007\r!json_gateway'
  _WORKFLOWDELETERESPONSE._options = None
  _WORKFLOWDELETERESPONSE._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _WORKFLOWLISTREQUEST.fields_by_name['filter']._options = None
  _WORKFLOWLISTREQUEST.fields_by_name['filter']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _WORKFLOWLISTRESPONSE.fields_by_name['workflows']._options = None
  _WORKFLOWLISTRESPONSE.fields_by_name['workflows']._serialized_options = b'\362\370\263\007\005\270\363\263\007\001'
  _WORKFLOWLISTRESPONSE.fields_by_name['rate_limit']._options = None
  _WORKFLOWLISTRESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\022\262\364\263\007\r!json_gateway'
  _WORKFLOWLISTRESPONSE._options = None
  _WORKFLOWLISTRESPONSE._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _WORKFLOW.fields_by_name['id']._options = None
  _WORKFLOW.fields_by_name['id']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _WORKFLOW.fields_by_name['name']._options = None
  _WORKFLOW.fields_by_name['name']._serialized_options = b'\362\370\263\007\n\260\363\263\007\001\300\363\263\007\001'
  _WORKFLOW.fields_by_name['description']._options = None
  _WORKFLOW.fields_by_name['description']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _WORKFLOW.fields_by_name['weight']._options = None
  _WORKFLOW.fields_by_name['weight']._serialized_options = b'\362\370\263\007\n\260\363\263\007\001\320\364\263\007\001'
  _WORKFLOW.fields_by_name['auto_grant']._options = None
  _WORKFLOW.fields_by_name['auto_grant']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _WORKFLOW.fields_by_name['enabled']._options = None
  _WORKFLOW.fields_by_name['enabled']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _WORKFLOW.fields_by_name['requires_reason']._options = None
  _WORKFLOW.fields_by_name['requires_reason']._serialized_options = b'\362\370\263\007\024\260\363\263\007\001\262\364\263\007\ngo_private'
  _WORKFLOW.fields_by_name['access_rules']._options = None
  _WORKFLOW.fields_by_name['access_rules']._serialized_options = b'\362\370\263\007\325\001\260\363\263\007\001\312\363\263\007\251\001\352\363\263\007\014access_rules\362\363\263\007\021\n\002go\022\013AccessRules\362\363\263\007\031\n\ngo_private\022\013AccessRules\362\363\263\007\033\n\014go_terraform\022\013AccessRules\362\363\263\007\030\n\004java\022\020List<AccessRule>\362\363\263\007\"\n\014json_gateway\022\022models.AccessRules\272\364\263\007\027accessRulesDiffSuppress\320\364\263\007\001'
  _WORKFLOW.fields_by_name['approval_flow_id']._options = None
  _WORKFLOW.fields_by_name['approval_flow_id']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _WORKFLOW._options = None
  _WORKFLOW._serialized_options = b'\372\370\263\007_\250\363\263\007\001\302\363\263\007O\242\363\263\007!tf_examples/workflow_resource.txt\252\363\263\007$tf_examples/workflow_data_source.txt\322\363\263\007\001*'
  _WORKFLOWS._options = None
  _WORKFLOWS._serialized_options = b'\312\371\263\007\r\302\371\263\007\010Workflow\312\371\263\007\010\322\371\263\007\003aw-\312\371\263\007\005\350\371\263\007\001'
  _WORKFLOWS.methods_by_name['Create']._options = None
  _WORKFLOWS.methods_by_name['Create']._serialized_options = b'\202\371\263\007\t\242\363\263\007\004post\202\371\263\007\022\252\363\263\007\r/v1/workflows'
  _WORKFLOWS.methods_by_name['Get']._options = None
  _WORKFLOWS.methods_by_name['Get']._serialized_options = b'\202\371\263\007\010\242\363\263\007\003get\202\371\263\007\026\252\363\263\007\021/v1/workflow/{id}'
  _WORKFLOWS.methods_by_name['Delete']._options = None
  _WORKFLOWS.methods_by_name['Delete']._serialized_options = b'\202\371\263\007\013\242\363\263\007\006delete\202\371\263\007\022\252\363\263\007\r/v1/workflows'
  _WORKFLOWS.methods_by_name['Update']._options = None
  _WORKFLOWS.methods_by_name['Update']._serialized_options = b'\202\371\263\007\010\242\363\263\007\003put\202\371\263\007\022\252\363\263\007\r/v1/workflows'
  _WORKFLOWS.methods_by_name['List']._options = None
  _WORKFLOWS.methods_by_name['List']._serialized_options = b'\202\371\263\007\010\242\363\263\007\003get\202\371\263\007\022\252\363\263\007\r/v1/workflows'
  _WORKFLOWCREATEREQUEST._serialized_start=50
  _WORKFLOWCREATEREQUEST._serialized_end=158
  _WORKFLOWCREATERESPONSE._serialized_start=161
  _WORKFLOWCREATERESPONSE._serialized_end=372
  _WORKFLOWGETREQUEST._serialized_start=374
  _WORKFLOWGETREQUEST._serialized_end=456
  _WORKFLOWGETRESPONSE._serialized_start=459
  _WORKFLOWGETRESPONSE._serialized_end=676
  _WORKFLOWUPDATEREQUEST._serialized_start=678
  _WORKFLOWUPDATEREQUEST._serialized_end=786
  _WORKFLOWUPDATERESPONSE._serialized_start=789
  _WORKFLOWUPDATERESPONSE._serialized_end=1000
  _WORKFLOWDELETEREQUEST._serialized_start=1002
  _WORKFLOWDELETEREQUEST._serialized_end=1090
  _WORKFLOWDELETERESPONSE._serialized_start=1093
  _WORKFLOWDELETERESPONSE._serialized_end=1284
  _WORKFLOWLISTREQUEST._serialized_start=1286
  _WORKFLOWLISTREQUEST._serialized_end=1374
  _WORKFLOWLISTRESPONSE._serialized_start=1377
  _WORKFLOWLISTRESPONSE._serialized_end=1585
  _WORKFLOW._serialized_start=1588
  _WORKFLOW._serialized_end=2217
  _WORKFLOWS._serialized_start=2220
  _WORKFLOWS._serialized_end=2782
# @@protoc_insertion_point(module_scope)
