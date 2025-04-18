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
# source: account_grants.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from . import options_pb2 as options__pb2
from . import spec_pb2 as spec__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14\x61\x63\x63ount_grants.proto\x12\x02v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\roptions.proto\x1a\nspec.proto\"y\n\x19\x41\x63\x63ountGrantCreateRequest\x12\'\n\x04meta\x18\x01 \x01(\x0b\x32\x19.v1.CreateRequestMetadata\x12\x33\n\raccount_grant\x18\x02 \x01(\x0b\x32\x10.v1.AccountGrantB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xec\x01\n\x1a\x41\x63\x63ountGrantCreateResponse\x12\x34\n\x04meta\x18\x01 \x01(\x0b\x32\x1a.v1.CreateResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x33\n\raccount_grant\x18\x02 \x01(\x0b\x32\x10.v1.AccountGrantB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12W\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB,\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"V\n\x16\x41\x63\x63ountGrantGetRequest\x12$\n\x04meta\x18\x01 \x01(\x0b\x32\x16.v1.GetRequestMetadata\x12\x16\n\x02id\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xe6\x01\n\x17\x41\x63\x63ountGrantGetResponse\x12\x31\n\x04meta\x18\x01 \x01(\x0b\x32\x17.v1.GetResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x33\n\raccount_grant\x18\x02 \x01(\x0b\x32\x10.v1.AccountGrantB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12W\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB,\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"\\\n\x19\x41\x63\x63ountGrantDeleteRequest\x12\'\n\x04meta\x18\x01 \x01(\x0b\x32\x19.v1.DeleteRequestMetadata\x12\x16\n\x02id\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xb7\x01\n\x1a\x41\x63\x63ountGrantDeleteResponse\x12\x34\n\x04meta\x18\x01 \x01(\x0b\x32\x1a.v1.DeleteResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12W\n\nrate_limit\x18\x02 \x01(\x0b\x32\x15.v1.RateLimitMetadataB,\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"\\\n\x17\x41\x63\x63ountGrantListRequest\x12%\n\x04meta\x18\x01 \x01(\x0b\x32\x17.v1.ListRequestMetadata\x12\x1a\n\x06\x66ilter\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xd1\x01\n\x18\x41\x63\x63ountGrantListResponse\x12&\n\x04meta\x18\x01 \x01(\x0b\x32\x18.v1.ListResponseMetadata\x12\x34\n\x0e\x61\x63\x63ount_grants\x18\x02 \x03(\x0b\x32\x10.v1.AccountGrantB\n\xf2\xf8\xb3\x07\x05\xb8\xf3\xb3\x07\x01\x12W\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB,\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway\"\xfc\x03\n\x0c\x41\x63\x63ountGrant\x12\x16\n\x02id\x18\x01 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12$\n\x0bresource_id\x18\x02 \x01(\tB\x0f\xf2\xf8\xb3\x07\n\xb0\xf3\xb3\x07\x01\xc0\xf3\xb3\x07\x01\x12#\n\naccount_id\x18\x03 \x01(\tB\x0f\xf2\xf8\xb3\x07\n\xb0\xf3\xb3\x07\x01\xc0\xf3\xb3\x07\x01\x12:\n\nstart_from\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12;\n\x0bvalid_until\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\xe5\x01\n\x0b\x61\x63\x63\x65ss_rule\x18\x06 \x01(\tB\xcf\x01\xf2\xf8\xb3\x07\xc9\x01\xb0\xf3\xb3\x07\x01\xca\xf3\xb3\x07\x9e\x01\xea\xf3\xb3\x07\x0b\x61\x63\x63\x65ss_rule\xf2\xf3\xb3\x07\x10\n\x02go\x12\nAccessRule\xf2\xf3\xb3\x07\x18\n\ngo_private\x12\nAccessRule\xf2\xf3\xb3\x07\x1a\n\x0cgo_terraform\x12\nAccessRule\xf2\xf3\xb3\x07\x12\n\x04java\x12\nAccessRule\xf2\xf3\xb3\x07!\n\x0cjson_gateway\x12\x11models.AccessRule\xba\xf4\xb3\x07\x16\x61\x63\x63\x65ssRuleDiffSuppress\xd0\xf4\xb3\x07\x01:(\xfa\xf8\xb3\x07#\xa8\xf3\xb3\x07\x01\xd2\xf3\xb3\x07\x01*\xd2\xf3\xb3\x07\x13!terraform-provider2\xab\x04\n\rAccountGrants\x12s\n\x06\x43reate\x12\x1d.v1.AccountGrantCreateRequest\x1a\x1e.v1.AccountGrantCreateResponse\"*\x82\xf9\xb3\x07\t\xa2\xf3\xb3\x07\x04post\x82\xf9\xb3\x07\x17\xaa\xf3\xb3\x07\x12/v1/account-grants\x12n\n\x03Get\x12\x1a.v1.AccountGrantGetRequest\x1a\x1b.v1.AccountGrantGetResponse\".\x82\xf9\xb3\x07\x08\xa2\xf3\xb3\x07\x03get\x82\xf9\xb3\x07\x1c\xaa\xf3\xb3\x07\x17/v1/account-grants/{id}\x12z\n\x06\x44\x65lete\x12\x1d.v1.AccountGrantDeleteRequest\x1a\x1e.v1.AccountGrantDeleteResponse\"1\x82\xf9\xb3\x07\x0b\xa2\xf3\xb3\x07\x06\x64\x65lete\x82\xf9\xb3\x07\x1c\xaa\xf3\xb3\x07\x17/v1/account-grants/{id}\x12l\n\x04List\x12\x1b.v1.AccountGrantListRequest\x1a\x1c.v1.AccountGrantListResponse\")\x82\xf9\xb3\x07\x08\xa2\xf3\xb3\x07\x03get\x82\xf9\xb3\x07\x17\xaa\xf3\xb3\x07\x12/v1/account-grants\x1aK\xca\xf9\xb3\x07\x11\xc2\xf9\xb3\x07\x0c\x41\x63\x63ountGrant\xca\xf9\xb3\x07\x08\xd2\xf9\xb3\x07\x03\x61g-\xca\xf9\xb3\x07\x06\xca\xf9\xb3\x07\x01*\xca\xf9\xb3\x07\x18\xca\xf9\xb3\x07\x13!terraform-providerBi\n\x19\x63om.strongdm.api.plumbingB\x15\x41\x63\x63ountGrantsPlumbingZ5github.com/strongdm/strongdm-sdk-go/v3/internal/v1;v1b\x06proto3')



_ACCOUNTGRANTCREATEREQUEST = DESCRIPTOR.message_types_by_name['AccountGrantCreateRequest']
_ACCOUNTGRANTCREATERESPONSE = DESCRIPTOR.message_types_by_name['AccountGrantCreateResponse']
_ACCOUNTGRANTGETREQUEST = DESCRIPTOR.message_types_by_name['AccountGrantGetRequest']
_ACCOUNTGRANTGETRESPONSE = DESCRIPTOR.message_types_by_name['AccountGrantGetResponse']
_ACCOUNTGRANTDELETEREQUEST = DESCRIPTOR.message_types_by_name['AccountGrantDeleteRequest']
_ACCOUNTGRANTDELETERESPONSE = DESCRIPTOR.message_types_by_name['AccountGrantDeleteResponse']
_ACCOUNTGRANTLISTREQUEST = DESCRIPTOR.message_types_by_name['AccountGrantListRequest']
_ACCOUNTGRANTLISTRESPONSE = DESCRIPTOR.message_types_by_name['AccountGrantListResponse']
_ACCOUNTGRANT = DESCRIPTOR.message_types_by_name['AccountGrant']
AccountGrantCreateRequest = _reflection.GeneratedProtocolMessageType('AccountGrantCreateRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTGRANTCREATEREQUEST,
  '__module__' : 'account_grants_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountGrantCreateRequest)
  })
_sym_db.RegisterMessage(AccountGrantCreateRequest)

AccountGrantCreateResponse = _reflection.GeneratedProtocolMessageType('AccountGrantCreateResponse', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTGRANTCREATERESPONSE,
  '__module__' : 'account_grants_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountGrantCreateResponse)
  })
_sym_db.RegisterMessage(AccountGrantCreateResponse)

AccountGrantGetRequest = _reflection.GeneratedProtocolMessageType('AccountGrantGetRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTGRANTGETREQUEST,
  '__module__' : 'account_grants_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountGrantGetRequest)
  })
_sym_db.RegisterMessage(AccountGrantGetRequest)

AccountGrantGetResponse = _reflection.GeneratedProtocolMessageType('AccountGrantGetResponse', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTGRANTGETRESPONSE,
  '__module__' : 'account_grants_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountGrantGetResponse)
  })
_sym_db.RegisterMessage(AccountGrantGetResponse)

AccountGrantDeleteRequest = _reflection.GeneratedProtocolMessageType('AccountGrantDeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTGRANTDELETEREQUEST,
  '__module__' : 'account_grants_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountGrantDeleteRequest)
  })
_sym_db.RegisterMessage(AccountGrantDeleteRequest)

AccountGrantDeleteResponse = _reflection.GeneratedProtocolMessageType('AccountGrantDeleteResponse', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTGRANTDELETERESPONSE,
  '__module__' : 'account_grants_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountGrantDeleteResponse)
  })
_sym_db.RegisterMessage(AccountGrantDeleteResponse)

AccountGrantListRequest = _reflection.GeneratedProtocolMessageType('AccountGrantListRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTGRANTLISTREQUEST,
  '__module__' : 'account_grants_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountGrantListRequest)
  })
_sym_db.RegisterMessage(AccountGrantListRequest)

AccountGrantListResponse = _reflection.GeneratedProtocolMessageType('AccountGrantListResponse', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTGRANTLISTRESPONSE,
  '__module__' : 'account_grants_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountGrantListResponse)
  })
_sym_db.RegisterMessage(AccountGrantListResponse)

AccountGrant = _reflection.GeneratedProtocolMessageType('AccountGrant', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTGRANT,
  '__module__' : 'account_grants_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountGrant)
  })
_sym_db.RegisterMessage(AccountGrant)

_ACCOUNTGRANTS = DESCRIPTOR.services_by_name['AccountGrants']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031com.strongdm.api.plumbingB\025AccountGrantsPlumbingZ5github.com/strongdm/strongdm-sdk-go/v3/internal/v1;v1'
  _ACCOUNTGRANTCREATEREQUEST.fields_by_name['account_grant']._options = None
  _ACCOUNTGRANTCREATEREQUEST.fields_by_name['account_grant']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACCOUNTGRANTCREATERESPONSE.fields_by_name['meta']._options = None
  _ACCOUNTGRANTCREATERESPONSE.fields_by_name['meta']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACCOUNTGRANTCREATERESPONSE.fields_by_name['account_grant']._options = None
  _ACCOUNTGRANTCREATERESPONSE.fields_by_name['account_grant']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACCOUNTGRANTCREATERESPONSE.fields_by_name['rate_limit']._options = None
  _ACCOUNTGRANTCREATERESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\022\262\364\263\007\r!json_gateway'
  _ACCOUNTGRANTCREATERESPONSE._options = None
  _ACCOUNTGRANTCREATERESPONSE._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _ACCOUNTGRANTGETREQUEST.fields_by_name['id']._options = None
  _ACCOUNTGRANTGETREQUEST.fields_by_name['id']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACCOUNTGRANTGETRESPONSE.fields_by_name['meta']._options = None
  _ACCOUNTGRANTGETRESPONSE.fields_by_name['meta']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACCOUNTGRANTGETRESPONSE.fields_by_name['account_grant']._options = None
  _ACCOUNTGRANTGETRESPONSE.fields_by_name['account_grant']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACCOUNTGRANTGETRESPONSE.fields_by_name['rate_limit']._options = None
  _ACCOUNTGRANTGETRESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\022\262\364\263\007\r!json_gateway'
  _ACCOUNTGRANTGETRESPONSE._options = None
  _ACCOUNTGRANTGETRESPONSE._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _ACCOUNTGRANTDELETEREQUEST.fields_by_name['id']._options = None
  _ACCOUNTGRANTDELETEREQUEST.fields_by_name['id']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACCOUNTGRANTDELETERESPONSE.fields_by_name['meta']._options = None
  _ACCOUNTGRANTDELETERESPONSE.fields_by_name['meta']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACCOUNTGRANTDELETERESPONSE.fields_by_name['rate_limit']._options = None
  _ACCOUNTGRANTDELETERESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\022\262\364\263\007\r!json_gateway'
  _ACCOUNTGRANTDELETERESPONSE._options = None
  _ACCOUNTGRANTDELETERESPONSE._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _ACCOUNTGRANTLISTREQUEST.fields_by_name['filter']._options = None
  _ACCOUNTGRANTLISTREQUEST.fields_by_name['filter']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACCOUNTGRANTLISTRESPONSE.fields_by_name['account_grants']._options = None
  _ACCOUNTGRANTLISTRESPONSE.fields_by_name['account_grants']._serialized_options = b'\362\370\263\007\005\270\363\263\007\001'
  _ACCOUNTGRANTLISTRESPONSE.fields_by_name['rate_limit']._options = None
  _ACCOUNTGRANTLISTRESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\022\262\364\263\007\r!json_gateway'
  _ACCOUNTGRANT.fields_by_name['id']._options = None
  _ACCOUNTGRANT.fields_by_name['id']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACCOUNTGRANT.fields_by_name['resource_id']._options = None
  _ACCOUNTGRANT.fields_by_name['resource_id']._serialized_options = b'\362\370\263\007\n\260\363\263\007\001\300\363\263\007\001'
  _ACCOUNTGRANT.fields_by_name['account_id']._options = None
  _ACCOUNTGRANT.fields_by_name['account_id']._serialized_options = b'\362\370\263\007\n\260\363\263\007\001\300\363\263\007\001'
  _ACCOUNTGRANT.fields_by_name['start_from']._options = None
  _ACCOUNTGRANT.fields_by_name['start_from']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACCOUNTGRANT.fields_by_name['valid_until']._options = None
  _ACCOUNTGRANT.fields_by_name['valid_until']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACCOUNTGRANT.fields_by_name['access_rule']._options = None
  _ACCOUNTGRANT.fields_by_name['access_rule']._serialized_options = b'\362\370\263\007\311\001\260\363\263\007\001\312\363\263\007\236\001\352\363\263\007\013access_rule\362\363\263\007\020\n\002go\022\nAccessRule\362\363\263\007\030\n\ngo_private\022\nAccessRule\362\363\263\007\032\n\014go_terraform\022\nAccessRule\362\363\263\007\022\n\004java\022\nAccessRule\362\363\263\007!\n\014json_gateway\022\021models.AccessRule\272\364\263\007\026accessRuleDiffSuppress\320\364\263\007\001'
  _ACCOUNTGRANT._options = None
  _ACCOUNTGRANT._serialized_options = b'\372\370\263\007#\250\363\263\007\001\322\363\263\007\001*\322\363\263\007\023!terraform-provider'
  _ACCOUNTGRANTS._options = None
  _ACCOUNTGRANTS._serialized_options = b'\312\371\263\007\021\302\371\263\007\014AccountGrant\312\371\263\007\010\322\371\263\007\003ag-\312\371\263\007\006\312\371\263\007\001*\312\371\263\007\030\312\371\263\007\023!terraform-provider'
  _ACCOUNTGRANTS.methods_by_name['Create']._options = None
  _ACCOUNTGRANTS.methods_by_name['Create']._serialized_options = b'\202\371\263\007\t\242\363\263\007\004post\202\371\263\007\027\252\363\263\007\022/v1/account-grants'
  _ACCOUNTGRANTS.methods_by_name['Get']._options = None
  _ACCOUNTGRANTS.methods_by_name['Get']._serialized_options = b'\202\371\263\007\010\242\363\263\007\003get\202\371\263\007\034\252\363\263\007\027/v1/account-grants/{id}'
  _ACCOUNTGRANTS.methods_by_name['Delete']._options = None
  _ACCOUNTGRANTS.methods_by_name['Delete']._serialized_options = b'\202\371\263\007\013\242\363\263\007\006delete\202\371\263\007\034\252\363\263\007\027/v1/account-grants/{id}'
  _ACCOUNTGRANTS.methods_by_name['List']._options = None
  _ACCOUNTGRANTS.methods_by_name['List']._serialized_options = b'\202\371\263\007\010\242\363\263\007\003get\202\371\263\007\027\252\363\263\007\022/v1/account-grants'
  _ACCOUNTGRANTCREATEREQUEST._serialized_start=88
  _ACCOUNTGRANTCREATEREQUEST._serialized_end=209
  _ACCOUNTGRANTCREATERESPONSE._serialized_start=212
  _ACCOUNTGRANTCREATERESPONSE._serialized_end=448
  _ACCOUNTGRANTGETREQUEST._serialized_start=450
  _ACCOUNTGRANTGETREQUEST._serialized_end=536
  _ACCOUNTGRANTGETRESPONSE._serialized_start=539
  _ACCOUNTGRANTGETRESPONSE._serialized_end=769
  _ACCOUNTGRANTDELETEREQUEST._serialized_start=771
  _ACCOUNTGRANTDELETEREQUEST._serialized_end=863
  _ACCOUNTGRANTDELETERESPONSE._serialized_start=866
  _ACCOUNTGRANTDELETERESPONSE._serialized_end=1049
  _ACCOUNTGRANTLISTREQUEST._serialized_start=1051
  _ACCOUNTGRANTLISTREQUEST._serialized_end=1143
  _ACCOUNTGRANTLISTRESPONSE._serialized_start=1146
  _ACCOUNTGRANTLISTRESPONSE._serialized_end=1355
  _ACCOUNTGRANT._serialized_start=1358
  _ACCOUNTGRANT._serialized_end=1866
  _ACCOUNTGRANTS._serialized_start=1869
  _ACCOUNTGRANTS._serialized_end=2424
# @@protoc_insertion_point(module_scope)
