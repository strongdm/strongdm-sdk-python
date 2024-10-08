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
# source: policies.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0epolicies.proto\x12\x02v1\x1a\roptions.proto\x1a\nspec.proto\"f\n\x13PolicyCreateRequest\x12\'\n\x04meta\x18\x01 \x01(\x0b\x32\x19.v1.CreateRequestMetadata\x12&\n\x06policy\x18\x02 \x01(\x0b\x32\n.v1.PolicyB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xcd\x01\n\x14PolicyCreateResponse\x12(\n\x04meta\x18\x01 \x01(\x0b\x32\x1a.v1.CreateResponseMetadata\x12&\n\x06policy\x18\x02 \x01(\x0b\x32\n.v1.PolicyB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12W\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB,\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"r\n\x13PolicyUpdateRequest\x12\'\n\x04meta\x18\x01 \x01(\x0b\x32\x19.v1.UpdateRequestMetadata\x12\n\n\x02id\x18\x02 \x01(\t\x12&\n\x06policy\x18\x03 \x01(\x0b\x32\n.v1.PolicyB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xcd\x01\n\x14PolicyUpdateResponse\x12(\n\x04meta\x18\x01 \x01(\x0b\x32\x1a.v1.UpdateResponseMetadata\x12&\n\x06policy\x18\x02 \x01(\x0b\x32\n.v1.PolicyB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12W\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB,\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"V\n\x13PolicyDeleteRequest\x12\'\n\x04meta\x18\x01 \x01(\x0b\x32\x19.v1.DeleteRequestMetadata\x12\x16\n\x02id\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xa5\x01\n\x14PolicyDeleteResponse\x12(\n\x04meta\x18\x01 \x01(\x0b\x32\x1a.v1.DeleteResponseMetadata\x12W\n\nrate_limit\x18\x02 \x01(\x0b\x32\x15.v1.RateLimitMetadataB,\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"P\n\x10PolicyGetRequest\x12$\n\x04meta\x18\x01 \x01(\x0b\x32\x16.v1.GetRequestMetadata\x12\x16\n\x02id\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xd3\x01\n\x11PolicyGetResponse\x12\x31\n\x04meta\x18\x01 \x01(\x0b\x32\x17.v1.GetResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12&\n\x06policy\x18\x02 \x01(\x0b\x32\n.v1.PolicyB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12W\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB,\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"V\n\x11PolicyListRequest\x12%\n\x04meta\x18\x01 \x01(\x0b\x32\x17.v1.ListRequestMetadata\x12\x1a\n\x06\x66ilter\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xcb\x01\n\x12PolicyListResponse\x12&\n\x04meta\x18\x01 \x01(\x0b\x32\x18.v1.ListResponseMetadata\x12(\n\x08policies\x18\x02 \x03(\x0b\x32\n.v1.PolicyB\n\xf2\xf8\xb3\x07\x05\xb8\xf3\xb3\x07\x01\x12W\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB,\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"\xd8\x01\n\x06Policy\x12\x16\n\x02id\x18\x01 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x1d\n\x04name\x18\x02 \x01(\tB\x0f\xf2\xf8\xb3\x07\n\xb0\xf3\xb3\x07\x01\xc0\xf3\xb3\x07\x01\x12\x1f\n\x0b\x64\x65scription\x18\x03 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x1a\n\x06policy\x18\x04 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:Z\xfa\xf8\xb3\x07U\xa8\xf3\xb3\x07\x01\xc2\xf3\xb3\x07K\xa2\xf3\xb3\x07\x1ftf_examples/policy_resource.txt\xaa\xf3\xb3\x07\"tf_examples/policy_data_source.txt2\xba\x04\n\x08Policies\x12\x61\n\x06\x43reate\x12\x17.v1.PolicyCreateRequest\x1a\x18.v1.PolicyCreateResponse\"$\x82\xf9\xb3\x07\t\xa2\xf3\xb3\x07\x04post\x82\xf9\xb3\x07\x11\xaa\xf3\xb3\x07\x0c/v1/policies\x12h\n\x06\x44\x65lete\x12\x17.v1.PolicyDeleteRequest\x1a\x18.v1.PolicyDeleteResponse\"+\x82\xf9\xb3\x07\x0b\xa2\xf3\xb3\x07\x06\x64\x65lete\x82\xf9\xb3\x07\x16\xaa\xf3\xb3\x07\x11/v1/policies/{id}\x12\x65\n\x06Update\x12\x17.v1.PolicyUpdateRequest\x1a\x18.v1.PolicyUpdateResponse\"(\x82\xf9\xb3\x07\x08\xa2\xf3\xb3\x07\x03put\x82\xf9\xb3\x07\x16\xaa\xf3\xb3\x07\x11/v1/policies/{id}\x12\\\n\x03Get\x12\x14.v1.PolicyGetRequest\x1a\x15.v1.PolicyGetResponse\"(\x82\xf9\xb3\x07\x08\xa2\xf3\xb3\x07\x03get\x82\xf9\xb3\x07\x16\xaa\xf3\xb3\x07\x11/v1/policies/{id}\x12Z\n\x04List\x12\x15.v1.PolicyListRequest\x1a\x16.v1.PolicyListResponse\"#\x82\xf9\xb3\x07\x08\xa2\xf3\xb3\x07\x03get\x82\xf9\xb3\x07\x11\xaa\xf3\xb3\x07\x0c/v1/policies\x1a@\xca\xf9\xb3\x07\x0b\xc2\xf9\xb3\x07\x06Policy\xca\xf9\xb3\x07\x08\xd2\xf9\xb3\x07\x03po-\xca\xf9\xb3\x07\x06\xca\xf9\xb3\x07\x01*\xca\xf9\xb3\x07\t\xca\xf9\xb3\x07\x04!cli\xca\xf9\xb3\x07\x05\xe8\xf9\xb3\x07\x01\x42\x64\n\x19\x63om.strongdm.api.plumbingB\x10PoliciesPlumbingZ5github.com/strongdm/strongdm-sdk-go/v3/internal/v1;v1b\x06proto3')



_POLICYCREATEREQUEST = DESCRIPTOR.message_types_by_name['PolicyCreateRequest']
_POLICYCREATERESPONSE = DESCRIPTOR.message_types_by_name['PolicyCreateResponse']
_POLICYUPDATEREQUEST = DESCRIPTOR.message_types_by_name['PolicyUpdateRequest']
_POLICYUPDATERESPONSE = DESCRIPTOR.message_types_by_name['PolicyUpdateResponse']
_POLICYDELETEREQUEST = DESCRIPTOR.message_types_by_name['PolicyDeleteRequest']
_POLICYDELETERESPONSE = DESCRIPTOR.message_types_by_name['PolicyDeleteResponse']
_POLICYGETREQUEST = DESCRIPTOR.message_types_by_name['PolicyGetRequest']
_POLICYGETRESPONSE = DESCRIPTOR.message_types_by_name['PolicyGetResponse']
_POLICYLISTREQUEST = DESCRIPTOR.message_types_by_name['PolicyListRequest']
_POLICYLISTRESPONSE = DESCRIPTOR.message_types_by_name['PolicyListResponse']
_POLICY = DESCRIPTOR.message_types_by_name['Policy']
PolicyCreateRequest = _reflection.GeneratedProtocolMessageType('PolicyCreateRequest', (_message.Message,), {
  'DESCRIPTOR' : _POLICYCREATEREQUEST,
  '__module__' : 'policies_pb2'
  # @@protoc_insertion_point(class_scope:v1.PolicyCreateRequest)
  })
_sym_db.RegisterMessage(PolicyCreateRequest)

PolicyCreateResponse = _reflection.GeneratedProtocolMessageType('PolicyCreateResponse', (_message.Message,), {
  'DESCRIPTOR' : _POLICYCREATERESPONSE,
  '__module__' : 'policies_pb2'
  # @@protoc_insertion_point(class_scope:v1.PolicyCreateResponse)
  })
_sym_db.RegisterMessage(PolicyCreateResponse)

PolicyUpdateRequest = _reflection.GeneratedProtocolMessageType('PolicyUpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _POLICYUPDATEREQUEST,
  '__module__' : 'policies_pb2'
  # @@protoc_insertion_point(class_scope:v1.PolicyUpdateRequest)
  })
_sym_db.RegisterMessage(PolicyUpdateRequest)

PolicyUpdateResponse = _reflection.GeneratedProtocolMessageType('PolicyUpdateResponse', (_message.Message,), {
  'DESCRIPTOR' : _POLICYUPDATERESPONSE,
  '__module__' : 'policies_pb2'
  # @@protoc_insertion_point(class_scope:v1.PolicyUpdateResponse)
  })
_sym_db.RegisterMessage(PolicyUpdateResponse)

PolicyDeleteRequest = _reflection.GeneratedProtocolMessageType('PolicyDeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _POLICYDELETEREQUEST,
  '__module__' : 'policies_pb2'
  # @@protoc_insertion_point(class_scope:v1.PolicyDeleteRequest)
  })
_sym_db.RegisterMessage(PolicyDeleteRequest)

PolicyDeleteResponse = _reflection.GeneratedProtocolMessageType('PolicyDeleteResponse', (_message.Message,), {
  'DESCRIPTOR' : _POLICYDELETERESPONSE,
  '__module__' : 'policies_pb2'
  # @@protoc_insertion_point(class_scope:v1.PolicyDeleteResponse)
  })
_sym_db.RegisterMessage(PolicyDeleteResponse)

PolicyGetRequest = _reflection.GeneratedProtocolMessageType('PolicyGetRequest', (_message.Message,), {
  'DESCRIPTOR' : _POLICYGETREQUEST,
  '__module__' : 'policies_pb2'
  # @@protoc_insertion_point(class_scope:v1.PolicyGetRequest)
  })
_sym_db.RegisterMessage(PolicyGetRequest)

PolicyGetResponse = _reflection.GeneratedProtocolMessageType('PolicyGetResponse', (_message.Message,), {
  'DESCRIPTOR' : _POLICYGETRESPONSE,
  '__module__' : 'policies_pb2'
  # @@protoc_insertion_point(class_scope:v1.PolicyGetResponse)
  })
_sym_db.RegisterMessage(PolicyGetResponse)

PolicyListRequest = _reflection.GeneratedProtocolMessageType('PolicyListRequest', (_message.Message,), {
  'DESCRIPTOR' : _POLICYLISTREQUEST,
  '__module__' : 'policies_pb2'
  # @@protoc_insertion_point(class_scope:v1.PolicyListRequest)
  })
_sym_db.RegisterMessage(PolicyListRequest)

PolicyListResponse = _reflection.GeneratedProtocolMessageType('PolicyListResponse', (_message.Message,), {
  'DESCRIPTOR' : _POLICYLISTRESPONSE,
  '__module__' : 'policies_pb2'
  # @@protoc_insertion_point(class_scope:v1.PolicyListResponse)
  })
_sym_db.RegisterMessage(PolicyListResponse)

Policy = _reflection.GeneratedProtocolMessageType('Policy', (_message.Message,), {
  'DESCRIPTOR' : _POLICY,
  '__module__' : 'policies_pb2'
  # @@protoc_insertion_point(class_scope:v1.Policy)
  })
_sym_db.RegisterMessage(Policy)

_POLICIES = DESCRIPTOR.services_by_name['Policies']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031com.strongdm.api.plumbingB\020PoliciesPlumbingZ5github.com/strongdm/strongdm-sdk-go/v3/internal/v1;v1'
  _POLICYCREATEREQUEST.fields_by_name['policy']._options = None
  _POLICYCREATEREQUEST.fields_by_name['policy']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _POLICYCREATERESPONSE.fields_by_name['policy']._options = None
  _POLICYCREATERESPONSE.fields_by_name['policy']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _POLICYCREATERESPONSE.fields_by_name['rate_limit']._options = None
  _POLICYCREATERESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\022\262\364\263\007\r!json_gateway'
  _POLICYCREATERESPONSE._options = None
  _POLICYCREATERESPONSE._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _POLICYUPDATEREQUEST.fields_by_name['policy']._options = None
  _POLICYUPDATEREQUEST.fields_by_name['policy']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _POLICYUPDATERESPONSE.fields_by_name['policy']._options = None
  _POLICYUPDATERESPONSE.fields_by_name['policy']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _POLICYUPDATERESPONSE.fields_by_name['rate_limit']._options = None
  _POLICYUPDATERESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\022\262\364\263\007\r!json_gateway'
  _POLICYUPDATERESPONSE._options = None
  _POLICYUPDATERESPONSE._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _POLICYDELETEREQUEST.fields_by_name['id']._options = None
  _POLICYDELETEREQUEST.fields_by_name['id']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _POLICYDELETERESPONSE.fields_by_name['rate_limit']._options = None
  _POLICYDELETERESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\022\262\364\263\007\r!json_gateway'
  _POLICYDELETERESPONSE._options = None
  _POLICYDELETERESPONSE._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _POLICYGETREQUEST.fields_by_name['id']._options = None
  _POLICYGETREQUEST.fields_by_name['id']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _POLICYGETRESPONSE.fields_by_name['meta']._options = None
  _POLICYGETRESPONSE.fields_by_name['meta']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _POLICYGETRESPONSE.fields_by_name['policy']._options = None
  _POLICYGETRESPONSE.fields_by_name['policy']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _POLICYGETRESPONSE.fields_by_name['rate_limit']._options = None
  _POLICYGETRESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\022\262\364\263\007\r!json_gateway'
  _POLICYGETRESPONSE._options = None
  _POLICYGETRESPONSE._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _POLICYLISTREQUEST.fields_by_name['filter']._options = None
  _POLICYLISTREQUEST.fields_by_name['filter']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _POLICYLISTRESPONSE.fields_by_name['policies']._options = None
  _POLICYLISTRESPONSE.fields_by_name['policies']._serialized_options = b'\362\370\263\007\005\270\363\263\007\001'
  _POLICYLISTRESPONSE.fields_by_name['rate_limit']._options = None
  _POLICYLISTRESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\022\262\364\263\007\r!json_gateway'
  _POLICYLISTRESPONSE._options = None
  _POLICYLISTRESPONSE._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _POLICY.fields_by_name['id']._options = None
  _POLICY.fields_by_name['id']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _POLICY.fields_by_name['name']._options = None
  _POLICY.fields_by_name['name']._serialized_options = b'\362\370\263\007\n\260\363\263\007\001\300\363\263\007\001'
  _POLICY.fields_by_name['description']._options = None
  _POLICY.fields_by_name['description']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _POLICY.fields_by_name['policy']._options = None
  _POLICY.fields_by_name['policy']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _POLICY._options = None
  _POLICY._serialized_options = b'\372\370\263\007U\250\363\263\007\001\302\363\263\007K\242\363\263\007\037tf_examples/policy_resource.txt\252\363\263\007\"tf_examples/policy_data_source.txt'
  _POLICIES._options = None
  _POLICIES._serialized_options = b'\312\371\263\007\013\302\371\263\007\006Policy\312\371\263\007\010\322\371\263\007\003po-\312\371\263\007\006\312\371\263\007\001*\312\371\263\007\t\312\371\263\007\004!cli\312\371\263\007\005\350\371\263\007\001'
  _POLICIES.methods_by_name['Create']._options = None
  _POLICIES.methods_by_name['Create']._serialized_options = b'\202\371\263\007\t\242\363\263\007\004post\202\371\263\007\021\252\363\263\007\014/v1/policies'
  _POLICIES.methods_by_name['Delete']._options = None
  _POLICIES.methods_by_name['Delete']._serialized_options = b'\202\371\263\007\013\242\363\263\007\006delete\202\371\263\007\026\252\363\263\007\021/v1/policies/{id}'
  _POLICIES.methods_by_name['Update']._options = None
  _POLICIES.methods_by_name['Update']._serialized_options = b'\202\371\263\007\010\242\363\263\007\003put\202\371\263\007\026\252\363\263\007\021/v1/policies/{id}'
  _POLICIES.methods_by_name['Get']._options = None
  _POLICIES.methods_by_name['Get']._serialized_options = b'\202\371\263\007\010\242\363\263\007\003get\202\371\263\007\026\252\363\263\007\021/v1/policies/{id}'
  _POLICIES.methods_by_name['List']._options = None
  _POLICIES.methods_by_name['List']._serialized_options = b'\202\371\263\007\010\242\363\263\007\003get\202\371\263\007\021\252\363\263\007\014/v1/policies'
  _POLICYCREATEREQUEST._serialized_start=49
  _POLICYCREATEREQUEST._serialized_end=151
  _POLICYCREATERESPONSE._serialized_start=154
  _POLICYCREATERESPONSE._serialized_end=359
  _POLICYUPDATEREQUEST._serialized_start=361
  _POLICYUPDATEREQUEST._serialized_end=475
  _POLICYUPDATERESPONSE._serialized_start=478
  _POLICYUPDATERESPONSE._serialized_end=683
  _POLICYDELETEREQUEST._serialized_start=685
  _POLICYDELETEREQUEST._serialized_end=771
  _POLICYDELETERESPONSE._serialized_start=774
  _POLICYDELETERESPONSE._serialized_end=939
  _POLICYGETREQUEST._serialized_start=941
  _POLICYGETREQUEST._serialized_end=1021
  _POLICYGETRESPONSE._serialized_start=1024
  _POLICYGETRESPONSE._serialized_end=1235
  _POLICYLISTREQUEST._serialized_start=1237
  _POLICYLISTREQUEST._serialized_end=1323
  _POLICYLISTRESPONSE._serialized_start=1326
  _POLICYLISTRESPONSE._serialized_end=1529
  _POLICY._serialized_start=1532
  _POLICY._serialized_end=1748
  _POLICIES._serialized_start=1751
  _POLICIES._serialized_end=2321
# @@protoc_insertion_point(module_scope)
