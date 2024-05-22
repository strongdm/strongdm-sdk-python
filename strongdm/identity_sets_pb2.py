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
# source: identity_sets.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13identity_sets.proto\x12\x02v1\x1a\roptions.proto\x1a\nspec.proto\"U\n\x15IdentitySetGetRequest\x12$\n\x04meta\x18\x01 \x01(\x0b\x32\x16.v1.GetRequestMetadata\x12\x16\n\x02id\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xe3\x01\n\x16IdentitySetGetResponse\x12\x31\n\x04meta\x18\x01 \x01(\x0b\x32\x17.v1.GetResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x31\n\x0cidentity_set\x18\x02 \x01(\x0b\x32\x0f.v1.IdentitySetB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12W\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB,\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"[\n\x16IdentitySetListRequest\x12%\n\x04meta\x18\x01 \x01(\x0b\x32\x17.v1.ListRequestMetadata\x12\x1a\n\x06\x66ilter\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xce\x01\n\x17IdentitySetListResponse\x12&\n\x04meta\x18\x01 \x01(\x0b\x32\x18.v1.ListResponseMetadata\x12\x32\n\ridentity_sets\x18\x02 \x03(\x0b\x32\x0f.v1.IdentitySetB\n\xf2\xf8\xb3\x07\x05\xb8\xf3\xb3\x07\x01\x12W\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB,\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway\"\xac\x01\n\x0bIdentitySet\x12\x16\n\x02id\x18\x01 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x1d\n\x04name\x18\x02 \x01(\tB\x0f\xf2\xf8\xb3\x07\n\xb0\xf3\xb3\x07\x01\xc0\xf3\xb3\x07\x01:f\xfa\xf8\xb3\x07\x61\xa8\xf3\xb3\x07\x01\xc2\xf3\xb3\x07W\xa2\xf3\xb3\x07%tf_examples/identity_set_resource.txt\xaa\xf3\xb3\x07(tf_examples/identity_set_data_source.txt2\x8a\x02\n\x0cIdentitySets\x12k\n\x03Get\x12\x19.v1.IdentitySetGetRequest\x1a\x1a.v1.IdentitySetGetResponse\"-\x82\xf9\xb3\x07\x08\xa2\xf3\xb3\x07\x03get\x82\xf9\xb3\x07\x1b\xaa\xf3\xb3\x07\x16/v1/identity-sets/{id}\x12i\n\x04List\x12\x1a.v1.IdentitySetListRequest\x1a\x1b.v1.IdentitySetListResponse\"(\x82\xf9\xb3\x07\x08\xa2\xf3\xb3\x07\x03get\x82\xf9\xb3\x07\x16\xaa\xf3\xb3\x07\x11/v1/identity-sets\x1a\"\xca\xf9\xb3\x07\x10\xc2\xf9\xb3\x07\x0bIdentitySet\xca\xf9\xb3\x07\x08\xd2\xf9\xb3\x07\x03ig-Bh\n\x19\x63om.strongdm.api.plumbingB\x14IdentitySetsPlumbingZ5github.com/strongdm/strongdm-sdk-go/v3/internal/v1;v1b\x06proto3')



_IDENTITYSETGETREQUEST = DESCRIPTOR.message_types_by_name['IdentitySetGetRequest']
_IDENTITYSETGETRESPONSE = DESCRIPTOR.message_types_by_name['IdentitySetGetResponse']
_IDENTITYSETLISTREQUEST = DESCRIPTOR.message_types_by_name['IdentitySetListRequest']
_IDENTITYSETLISTRESPONSE = DESCRIPTOR.message_types_by_name['IdentitySetListResponse']
_IDENTITYSET = DESCRIPTOR.message_types_by_name['IdentitySet']
IdentitySetGetRequest = _reflection.GeneratedProtocolMessageType('IdentitySetGetRequest', (_message.Message,), {
  'DESCRIPTOR' : _IDENTITYSETGETREQUEST,
  '__module__' : 'identity_sets_pb2'
  # @@protoc_insertion_point(class_scope:v1.IdentitySetGetRequest)
  })
_sym_db.RegisterMessage(IdentitySetGetRequest)

IdentitySetGetResponse = _reflection.GeneratedProtocolMessageType('IdentitySetGetResponse', (_message.Message,), {
  'DESCRIPTOR' : _IDENTITYSETGETRESPONSE,
  '__module__' : 'identity_sets_pb2'
  # @@protoc_insertion_point(class_scope:v1.IdentitySetGetResponse)
  })
_sym_db.RegisterMessage(IdentitySetGetResponse)

IdentitySetListRequest = _reflection.GeneratedProtocolMessageType('IdentitySetListRequest', (_message.Message,), {
  'DESCRIPTOR' : _IDENTITYSETLISTREQUEST,
  '__module__' : 'identity_sets_pb2'
  # @@protoc_insertion_point(class_scope:v1.IdentitySetListRequest)
  })
_sym_db.RegisterMessage(IdentitySetListRequest)

IdentitySetListResponse = _reflection.GeneratedProtocolMessageType('IdentitySetListResponse', (_message.Message,), {
  'DESCRIPTOR' : _IDENTITYSETLISTRESPONSE,
  '__module__' : 'identity_sets_pb2'
  # @@protoc_insertion_point(class_scope:v1.IdentitySetListResponse)
  })
_sym_db.RegisterMessage(IdentitySetListResponse)

IdentitySet = _reflection.GeneratedProtocolMessageType('IdentitySet', (_message.Message,), {
  'DESCRIPTOR' : _IDENTITYSET,
  '__module__' : 'identity_sets_pb2'
  # @@protoc_insertion_point(class_scope:v1.IdentitySet)
  })
_sym_db.RegisterMessage(IdentitySet)

_IDENTITYSETS = DESCRIPTOR.services_by_name['IdentitySets']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031com.strongdm.api.plumbingB\024IdentitySetsPlumbingZ5github.com/strongdm/strongdm-sdk-go/v3/internal/v1;v1'
  _IDENTITYSETGETREQUEST.fields_by_name['id']._options = None
  _IDENTITYSETGETREQUEST.fields_by_name['id']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _IDENTITYSETGETRESPONSE.fields_by_name['meta']._options = None
  _IDENTITYSETGETRESPONSE.fields_by_name['meta']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _IDENTITYSETGETRESPONSE.fields_by_name['identity_set']._options = None
  _IDENTITYSETGETRESPONSE.fields_by_name['identity_set']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _IDENTITYSETGETRESPONSE.fields_by_name['rate_limit']._options = None
  _IDENTITYSETGETRESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\022\262\364\263\007\r!json_gateway'
  _IDENTITYSETGETRESPONSE._options = None
  _IDENTITYSETGETRESPONSE._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _IDENTITYSETLISTREQUEST.fields_by_name['filter']._options = None
  _IDENTITYSETLISTREQUEST.fields_by_name['filter']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _IDENTITYSETLISTRESPONSE.fields_by_name['identity_sets']._options = None
  _IDENTITYSETLISTRESPONSE.fields_by_name['identity_sets']._serialized_options = b'\362\370\263\007\005\270\363\263\007\001'
  _IDENTITYSETLISTRESPONSE.fields_by_name['rate_limit']._options = None
  _IDENTITYSETLISTRESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\022\262\364\263\007\r!json_gateway'
  _IDENTITYSET.fields_by_name['id']._options = None
  _IDENTITYSET.fields_by_name['id']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _IDENTITYSET.fields_by_name['name']._options = None
  _IDENTITYSET.fields_by_name['name']._serialized_options = b'\362\370\263\007\n\260\363\263\007\001\300\363\263\007\001'
  _IDENTITYSET._options = None
  _IDENTITYSET._serialized_options = b'\372\370\263\007a\250\363\263\007\001\302\363\263\007W\242\363\263\007%tf_examples/identity_set_resource.txt\252\363\263\007(tf_examples/identity_set_data_source.txt'
  _IDENTITYSETS._options = None
  _IDENTITYSETS._serialized_options = b'\312\371\263\007\020\302\371\263\007\013IdentitySet\312\371\263\007\010\322\371\263\007\003ig-'
  _IDENTITYSETS.methods_by_name['Get']._options = None
  _IDENTITYSETS.methods_by_name['Get']._serialized_options = b'\202\371\263\007\010\242\363\263\007\003get\202\371\263\007\033\252\363\263\007\026/v1/identity-sets/{id}'
  _IDENTITYSETS.methods_by_name['List']._options = None
  _IDENTITYSETS.methods_by_name['List']._serialized_options = b'\202\371\263\007\010\242\363\263\007\003get\202\371\263\007\026\252\363\263\007\021/v1/identity-sets'
  _IDENTITYSETGETREQUEST._serialized_start=54
  _IDENTITYSETGETREQUEST._serialized_end=139
  _IDENTITYSETGETRESPONSE._serialized_start=142
  _IDENTITYSETGETRESPONSE._serialized_end=369
  _IDENTITYSETLISTREQUEST._serialized_start=371
  _IDENTITYSETLISTREQUEST._serialized_end=462
  _IDENTITYSETLISTRESPONSE._serialized_start=465
  _IDENTITYSETLISTRESPONSE._serialized_end=671
  _IDENTITYSET._serialized_start=674
  _IDENTITYSET._serialized_end=846
  _IDENTITYSETS._serialized_start=849
  _IDENTITYSETS._serialized_end=1115
# @@protoc_insertion_point(module_scope)