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
# source: policies_history.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from . import policies_pb2 as policies__pb2
from . import options_pb2 as options__pb2
from . import spec_pb2 as spec__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16policies_history.proto\x12\x02v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x0epolicies.proto\x1a\roptions.proto\x1a\nspec.proto\"\x89\x01\n\x1aPoliciesHistoryListRequest\x12%\n\x04meta\x18\x01 \x01(\x0b\x32\x17.v1.ListRequestMetadata\x12\x1a\n\x06\x66ilter\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:(\xfa\xf8\xb3\x07\x06\xd2\xf3\xb3\x07\x01*\xfa\xf8\xb3\x07\x18\xd2\xf3\xb3\x07\x13!terraform-provider\"\x95\x02\n\x1bPoliciesHistoryListResponse\x12&\n\x04meta\x18\x01 \x01(\x0b\x32\x18.v1.ListResponseMetadata\x12.\n\x07history\x18\x02 \x03(\x0b\x32\x11.v1.PolicyHistoryB\n\xf2\xf8\xb3\x07\x05\xb8\xf3\xb3\x07\x01\x12t\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataBI\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway\xf2\xf8\xb3\x07\x18\xb2\xf4\xb3\x07\x13!terraform-provider:(\xfa\xf8\xb3\x07\x06\xd2\xf3\xb3\x07\x01*\xfa\xf8\xb3\x07\x18\xd2\xf3\xb3\x07\x13!terraform-provider\"\xf9\x01\n\rPolicyHistory\x12\x1f\n\x0b\x61\x63tivity_id\x18\x01 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x39\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12&\n\x06policy\x18\x03 \x01(\x0b\x32\n.v1.PolicyB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12:\n\ndeleted_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:(\xfa\xf8\xb3\x07#\xa8\xf3\xb3\x07\x01\xd2\xf3\xb3\x07\x01*\xd2\xf3\xb3\x07\x13!terraform-provider2\xea\x01\n\x0fPoliciesHistory\x12t\n\x04List\x12\x1e.v1.PoliciesHistoryListRequest\x1a\x1f.v1.PoliciesHistoryListResponse\"+\x82\xf9\xb3\x07\x08\xa2\xf3\xb3\x07\x03get\x82\xf9\xb3\x07\x19\xaa\xf3\xb3\x07\x14/v1/policies-history\x1a\x61\xca\xf9\xb3\x07\x12\xc2\xf9\xb3\x07\rPolicyHistory\xca\xf9\xb3\x07\x05\xd8\xf9\xb3\x07\x01\xca\xf9\xb3\x07\x06\xca\xf9\xb3\x07\x01*\xca\xf9\xb3\x07\x18\xca\xf9\xb3\x07\x13!terraform-provider\xca\xf9\xb3\x07\t\xca\xf9\xb3\x07\x04!cli\xca\xf9\xb3\x07\x05\xe8\xf9\xb3\x07\x01\x42\x93\x01\n\x19\x63om.strongdm.api.plumbingB\x17PoliciesHistoryPlumbingZ5github.com/strongdm/strongdm-sdk-go/v3/internal/v1;v1\xc2\x92\xb4\x07\x06\xa2\x8c\xb4\x07\x01*\xc2\x92\xb4\x07\x18\xa2\x8c\xb4\x07\x13!terraform-providerb\x06proto3')



_POLICIESHISTORYLISTREQUEST = DESCRIPTOR.message_types_by_name['PoliciesHistoryListRequest']
_POLICIESHISTORYLISTRESPONSE = DESCRIPTOR.message_types_by_name['PoliciesHistoryListResponse']
_POLICYHISTORY = DESCRIPTOR.message_types_by_name['PolicyHistory']
PoliciesHistoryListRequest = _reflection.GeneratedProtocolMessageType('PoliciesHistoryListRequest', (_message.Message,), {
  'DESCRIPTOR' : _POLICIESHISTORYLISTREQUEST,
  '__module__' : 'policies_history_pb2'
  # @@protoc_insertion_point(class_scope:v1.PoliciesHistoryListRequest)
  })
_sym_db.RegisterMessage(PoliciesHistoryListRequest)

PoliciesHistoryListResponse = _reflection.GeneratedProtocolMessageType('PoliciesHistoryListResponse', (_message.Message,), {
  'DESCRIPTOR' : _POLICIESHISTORYLISTRESPONSE,
  '__module__' : 'policies_history_pb2'
  # @@protoc_insertion_point(class_scope:v1.PoliciesHistoryListResponse)
  })
_sym_db.RegisterMessage(PoliciesHistoryListResponse)

PolicyHistory = _reflection.GeneratedProtocolMessageType('PolicyHistory', (_message.Message,), {
  'DESCRIPTOR' : _POLICYHISTORY,
  '__module__' : 'policies_history_pb2'
  # @@protoc_insertion_point(class_scope:v1.PolicyHistory)
  })
_sym_db.RegisterMessage(PolicyHistory)

_POLICIESHISTORY = DESCRIPTOR.services_by_name['PoliciesHistory']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031com.strongdm.api.plumbingB\027PoliciesHistoryPlumbingZ5github.com/strongdm/strongdm-sdk-go/v3/internal/v1;v1\302\222\264\007\006\242\214\264\007\001*\302\222\264\007\030\242\214\264\007\023!terraform-provider'
  _POLICIESHISTORYLISTREQUEST.fields_by_name['filter']._options = None
  _POLICIESHISTORYLISTREQUEST.fields_by_name['filter']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _POLICIESHISTORYLISTREQUEST._options = None
  _POLICIESHISTORYLISTREQUEST._serialized_options = b'\372\370\263\007\006\322\363\263\007\001*\372\370\263\007\030\322\363\263\007\023!terraform-provider'
  _POLICIESHISTORYLISTRESPONSE.fields_by_name['history']._options = None
  _POLICIESHISTORYLISTRESPONSE.fields_by_name['history']._serialized_options = b'\362\370\263\007\005\270\363\263\007\001'
  _POLICIESHISTORYLISTRESPONSE.fields_by_name['rate_limit']._options = None
  _POLICIESHISTORYLISTRESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\022\262\364\263\007\r!json_gateway\362\370\263\007\030\262\364\263\007\023!terraform-provider'
  _POLICIESHISTORYLISTRESPONSE._options = None
  _POLICIESHISTORYLISTRESPONSE._serialized_options = b'\372\370\263\007\006\322\363\263\007\001*\372\370\263\007\030\322\363\263\007\023!terraform-provider'
  _POLICYHISTORY.fields_by_name['activity_id']._options = None
  _POLICYHISTORY.fields_by_name['activity_id']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _POLICYHISTORY.fields_by_name['timestamp']._options = None
  _POLICYHISTORY.fields_by_name['timestamp']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _POLICYHISTORY.fields_by_name['policy']._options = None
  _POLICYHISTORY.fields_by_name['policy']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _POLICYHISTORY.fields_by_name['deleted_at']._options = None
  _POLICYHISTORY.fields_by_name['deleted_at']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _POLICYHISTORY._options = None
  _POLICYHISTORY._serialized_options = b'\372\370\263\007#\250\363\263\007\001\322\363\263\007\001*\322\363\263\007\023!terraform-provider'
  _POLICIESHISTORY._options = None
  _POLICIESHISTORY._serialized_options = b'\312\371\263\007\022\302\371\263\007\rPolicyHistory\312\371\263\007\005\330\371\263\007\001\312\371\263\007\006\312\371\263\007\001*\312\371\263\007\030\312\371\263\007\023!terraform-provider\312\371\263\007\t\312\371\263\007\004!cli\312\371\263\007\005\350\371\263\007\001'
  _POLICIESHISTORY.methods_by_name['List']._options = None
  _POLICIESHISTORY.methods_by_name['List']._serialized_options = b'\202\371\263\007\010\242\363\263\007\003get\202\371\263\007\031\252\363\263\007\024/v1/policies-history'
  _POLICIESHISTORYLISTREQUEST._serialized_start=107
  _POLICIESHISTORYLISTREQUEST._serialized_end=244
  _POLICIESHISTORYLISTRESPONSE._serialized_start=247
  _POLICIESHISTORYLISTRESPONSE._serialized_end=524
  _POLICYHISTORY._serialized_start=527
  _POLICYHISTORY._serialized_end=776
  _POLICIESHISTORY._serialized_start=779
  _POLICIESHISTORY._serialized_end=1013
# @@protoc_insertion_point(module_scope)
