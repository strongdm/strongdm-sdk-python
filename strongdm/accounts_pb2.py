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
# source: accounts.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from . import options_pb2 as options__pb2
from . import spec_pb2 as spec__pb2
from . import tags_pb2 as tags__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0e\x61\x63\x63ounts.proto\x12\x02v1\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\roptions.proto\x1a\nspec.proto\x1a\ntags.proto\"i\n\x14\x41\x63\x63ountCreateRequest\x12\'\n\x04meta\x18\x01 \x01(\x0b\x32\x19.v1.CreateRequestMetadata\x12(\n\x07\x61\x63\x63ount\x18\x02 \x01(\x0b\x32\x0b.v1.AccountB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xf8\x02\n\x15\x41\x63\x63ountCreateResponse\x12\x34\n\x04meta\x18\x01 \x01(\x0b\x32\x1a.v1.CreateResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12(\n\x07\x61\x63\x63ount\x18\x02 \x01(\x0b\x32\x0b.v1.AccountB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x1e\n\x05token\x18\x03 \x01(\tB\x0f\xf2\xf8\xb3\x07\n\xb0\xf3\xb3\x07\x01\xf0\xf3\xb3\x07\x01\x12W\n\nrate_limit\x18\x04 \x01(\x0b\x32\x15.v1.RateLimitMetadataB,\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway\x12<\n\naccess_key\x18\x05 \x01(\tB(\xf2\xf8\xb3\x07#\xb0\xf3\xb3\x07\x01\xb2\xf4\xb3\x07\x01*\xb2\xf4\xb3\x07\x13!terraform-provider\x12<\n\nsecret_key\x18\x06 \x01(\tB(\xf2\xf8\xb3\x07#\xb0\xf3\xb3\x07\x01\xb2\xf4\xb3\x07\x01*\xb2\xf4\xb3\x07\x13!terraform-provider:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"Q\n\x11\x41\x63\x63ountGetRequest\x12$\n\x04meta\x18\x01 \x01(\x0b\x32\x16.v1.GetRequestMetadata\x12\x16\n\x02id\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xd6\x01\n\x12\x41\x63\x63ountGetResponse\x12\x31\n\x04meta\x18\x01 \x01(\x0b\x32\x17.v1.GetResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12(\n\x07\x61\x63\x63ount\x18\x02 \x01(\x0b\x32\x0b.v1.AccountB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12W\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB,\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"u\n\x14\x41\x63\x63ountUpdateRequest\x12\'\n\x04meta\x18\x01 \x01(\x0b\x32\x19.v1.UpdateRequestMetadata\x12\n\n\x02id\x18\x02 \x01(\t\x12(\n\x07\x61\x63\x63ount\x18\x03 \x01(\x0b\x32\x0b.v1.AccountB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xdc\x01\n\x15\x41\x63\x63ountUpdateResponse\x12\x34\n\x04meta\x18\x01 \x01(\x0b\x32\x1a.v1.UpdateResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12(\n\x07\x61\x63\x63ount\x18\x02 \x01(\x0b\x32\x0b.v1.AccountB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12W\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB,\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"W\n\x14\x41\x63\x63ountDeleteRequest\x12\'\n\x04meta\x18\x01 \x01(\x0b\x32\x19.v1.DeleteRequestMetadata\x12\x16\n\x02id\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xb2\x01\n\x15\x41\x63\x63ountDeleteResponse\x12\x34\n\x04meta\x18\x01 \x01(\x0b\x32\x1a.v1.DeleteResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12W\n\nrate_limit\x18\x02 \x01(\x0b\x32\x15.v1.RateLimitMetadataB,\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"W\n\x12\x41\x63\x63ountListRequest\x12%\n\x04meta\x18\x01 \x01(\x0b\x32\x17.v1.ListRequestMetadata\x12\x1a\n\x06\x66ilter\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xc1\x01\n\x13\x41\x63\x63ountListResponse\x12&\n\x04meta\x18\x01 \x01(\x0b\x32\x18.v1.ListResponseMetadata\x12)\n\x08\x61\x63\x63ounts\x18\x02 \x03(\x0b\x32\x0b.v1.AccountB\n\xf2\xf8\xb3\x07\x05\xb8\xf3\xb3\x07\x01\x12W\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB,\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway\"\x94\x02\n\x07\x41\x63\x63ount\x12$\n\x04user\x18\x01 \x01(\x0b\x32\x08.v1.UserB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01H\x00\x12*\n\x07service\x18\x02 \x01(\x0b\x32\x0b.v1.ServiceB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01H\x00\x12&\n\x05token\x18\x03 \x01(\x0b\x32\t.v1.TokenB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01H\x00:a\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\xfa\xf8\xb3\x07R\xc2\xf3\xb3\x07M\xa2\xf3\xb3\x07 tf_examples/account_resource.txt\xaa\xf3\xb3\x07#tf_examples/account_data_source.txtB,\n\x07\x61\x63\x63ount\x12!\xaa\xf8\xb3\x07\x0e\xaa\xf8\xb3\x07\tsuspended\xaa\xf8\xb3\x07\t\xaa\xf8\xb3\x07\x04tags\"\x92\x08\n\x04User\x12\x16\n\x02id\x18\x01 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x1e\n\x05\x65mail\x18\x02 \x01(\tB\x0f\xf2\xf8\xb3\x07\n\xb0\xf3\xb3\x07\x01\xc0\xf3\xb3\x07\x01\x12#\n\nfirst_name\x18\x03 \x01(\tB\x0f\xf2\xf8\xb3\x07\n\xb0\xf3\xb3\x07\x01\xc0\xf3\xb3\x07\x01\x12\"\n\tlast_name\x18\x04 \x01(\tB\x0f\xf2\xf8\xb3\x07\n\xb0\xf3\xb3\x07\x01\xc0\xf3\xb3\x07\x01\x12*\n\tsuspended\x18\x05 \x01(\x08\x42\x17\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway\x12\"\n\x04tags\x18\x06 \x01(\x0b\x32\x08.v1.TagsB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x36\n\x10permission_level\x18\x07 \x01(\tB\x1c\xf2\xf8\xb3\x07\x17\x98\xf4\xb3\x07\x01\xb2\xf4\xb3\x07\r!json_gateway\x12#\n\nmanaged_by\x18\x08 \x01(\tB\x0f\xf2\xf8\xb3\x07\n\xb0\xf3\xb3\x07\x01\x98\xf4\xb3\x07\x01\x12\x1f\n\x0b\x65xternal_id\x18\t \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\xdb\x01\n\x0bsuspendedRO\x18\n \x01(\x08\x42\xc5\x01\xf2\xf8\xb3\x07\xbf\x01\xb0\xf3\xb3\x07\x01\xca\xf3\xb3\x07\xaf\x01\xc2\xf4\xb3\x07\x0f\n\x02go\x12\tSuspended\xc2\xf4\xb3\x07\x10\n\x03\x63li\x12\tsuspended\xc2\xf4\xb3\x07\x11\n\x04ruby\x12\tsuspended\xc2\xf4\xb3\x07\x13\n\x06python\x12\tsuspended\xc2\xf4\xb3\x07\x11\n\x04java\x12\tSuspended\xc2\xf4\xb3\x07\x1f\n\x12terraform-provider\x12\tsuspended\xc2\xf4\xb3\x07\x19\n\x0cjson_gateway\x12\tsuspended\x98\xf4\xb3\x07\x01\x12\x90\x02\n\x12permission_levelRW\x18\x0b \x01(\tB\xf3\x01\xf2\xf8\xb3\x07\xed\x01\xb0\xf3\xb3\x07\x01\xca\xf3\xb3\x07\xdd\x01\xc2\xf4\xb3\x07\x15\n\x02go\x12\x0fPermissionLevel\xc2\xf4\xb3\x07\x17\n\x03\x63li\x12\x10permission-level\xc2\xf4\xb3\x07\x18\n\x04ruby\x12\x10permission_level\xc2\xf4\xb3\x07\x1a\n\x06python\x12\x10permission_level\xc2\xf4\xb3\x07\x17\n\x04java\x12\x0fPermissionLevel\xc2\xf4\xb3\x07&\n\x12terraform-provider\x12\x10permission_level\xc2\xf4\xb3\x07\x1f\n\x0cjson_gateway\x12\x0fpermissionLevel\xd0\xf4\xb3\x07\x01\x12?\n\x08password\x18\x0c \x01(\tB-\xf2\xf8\xb3\x07(\xb0\xf3\xb3\x07\x01\xe8\xf3\xb3\x07\x01\xb2\xf4\xb3\x07\x01*\xb2\xf4\xb3\x07\x13!terraform-provider\x12#\n\x04SCIM\x18\r \x01(\tB\x15\xf2\xf8\xb3\x07\x10\xb0\xf3\xb3\x07\x01\x98\xf4\xb3\x07\x01\xb2\xf4\xb3\x07\x01*\x12$\n\nmanager_id\x18\x0e \x01(\tB\x10\xf2\xf8\xb3\x07\x0b\xb0\xf3\xb3\x07\x01\xb2\xf4\xb3\x07\x01*\x12\x32\n\x13resolved_manager_id\x18\x0f \x01(\tB\x15\xf2\xf8\xb3\x07\x10\xb0\xf3\xb3\x07\x01\x98\xf4\xb3\x07\x01\xb2\xf4\xb3\x07\x01*:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"\x8f\x01\n\x07Service\x12\x16\n\x02id\x18\x01 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x1d\n\x04name\x18\x02 \x01(\tB\x0f\xf2\xf8\xb3\x07\n\xb0\xf3\xb3\x07\x01\xc0\xf3\xb3\x07\x01\x12\x1d\n\tsuspended\x18\x03 \x01(\x08\x42\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\"\n\x04tags\x18\x04 \x01(\x0b\x32\x08.v1.TagsB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"\x81\x03\n\x05Token\x12\x16\n\x02id\x18\x01 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x1d\n\x04name\x18\x02 \x01(\tB\x0f\xf2\xf8\xb3\x07\n\xb0\xf3\xb3\x07\x01\xc0\xf3\xb3\x07\x01\x12\x1d\n\tsuspended\x18\x03 \x01(\x08\x42\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\"\n\x04tags\x18\x04 \x01(\x0b\x32\x08.v1.TagsB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x37\n\x07rekeyed\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x38\n\x08\x64\x65\x61\x64line\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12 \n\x0c\x61\x63\x63ount_type\x18\x07 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x1f\n\x0bpermissions\x18\x08 \x03(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x37\n\x08\x64uration\x18\t \x01(\x0b\x32\x19.google.protobuf.DurationB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:\x0f\xfa\xf8\xb3\x07\n\xa8\xf3\xb3\x07\x01\xd8\xf3\xb3\x07\x01\x32\xba\x04\n\x08\x41\x63\x63ounts\x12\x63\n\x06\x43reate\x12\x18.v1.AccountCreateRequest\x1a\x19.v1.AccountCreateResponse\"$\x82\xf9\xb3\x07\t\xa2\xf3\xb3\x07\x04post\x82\xf9\xb3\x07\x11\xaa\xf3\xb3\x07\x0c/v1/accounts\x12^\n\x03Get\x12\x15.v1.AccountGetRequest\x1a\x16.v1.AccountGetResponse\"(\x82\xf9\xb3\x07\x08\xa2\xf3\xb3\x07\x03get\x82\xf9\xb3\x07\x16\xaa\xf3\xb3\x07\x11/v1/accounts/{id}\x12g\n\x06Update\x12\x18.v1.AccountUpdateRequest\x1a\x19.v1.AccountUpdateResponse\"(\x82\xf9\xb3\x07\x08\xa2\xf3\xb3\x07\x03put\x82\xf9\xb3\x07\x16\xaa\xf3\xb3\x07\x11/v1/accounts/{id}\x12j\n\x06\x44\x65lete\x12\x18.v1.AccountDeleteRequest\x1a\x19.v1.AccountDeleteResponse\"+\x82\xf9\xb3\x07\x0b\xa2\xf3\xb3\x07\x06\x64\x65lete\x82\xf9\xb3\x07\x16\xaa\xf3\xb3\x07\x11/v1/accounts/{id}\x12\\\n\x04List\x12\x16.v1.AccountListRequest\x1a\x17.v1.AccountListResponse\"#\x82\xf9\xb3\x07\x08\xa2\xf3\xb3\x07\x03get\x82\xf9\xb3\x07\x11\xaa\xf3\xb3\x07\x0c/v1/accounts\x1a\x36\xca\xf9\xb3\x07\x0c\xc2\xf9\xb3\x07\x07\x41\x63\x63ount\xca\xf9\xb3\x07\x07\xd2\xf9\xb3\x07\x02\x61-\xca\xf9\xb3\x07\x06\xca\xf9\xb3\x07\x01*\xca\xf9\xb3\x07\t\xca\xf9\xb3\x07\x04!cliBd\n\x19\x63om.strongdm.api.plumbingB\x10\x41\x63\x63ountsPlumbingZ5github.com/strongdm/strongdm-sdk-go/v3/internal/v1;v1b\x06proto3')



_ACCOUNTCREATEREQUEST = DESCRIPTOR.message_types_by_name['AccountCreateRequest']
_ACCOUNTCREATERESPONSE = DESCRIPTOR.message_types_by_name['AccountCreateResponse']
_ACCOUNTGETREQUEST = DESCRIPTOR.message_types_by_name['AccountGetRequest']
_ACCOUNTGETRESPONSE = DESCRIPTOR.message_types_by_name['AccountGetResponse']
_ACCOUNTUPDATEREQUEST = DESCRIPTOR.message_types_by_name['AccountUpdateRequest']
_ACCOUNTUPDATERESPONSE = DESCRIPTOR.message_types_by_name['AccountUpdateResponse']
_ACCOUNTDELETEREQUEST = DESCRIPTOR.message_types_by_name['AccountDeleteRequest']
_ACCOUNTDELETERESPONSE = DESCRIPTOR.message_types_by_name['AccountDeleteResponse']
_ACCOUNTLISTREQUEST = DESCRIPTOR.message_types_by_name['AccountListRequest']
_ACCOUNTLISTRESPONSE = DESCRIPTOR.message_types_by_name['AccountListResponse']
_ACCOUNT = DESCRIPTOR.message_types_by_name['Account']
_USER = DESCRIPTOR.message_types_by_name['User']
_SERVICE = DESCRIPTOR.message_types_by_name['Service']
_TOKEN = DESCRIPTOR.message_types_by_name['Token']
AccountCreateRequest = _reflection.GeneratedProtocolMessageType('AccountCreateRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTCREATEREQUEST,
  '__module__' : 'accounts_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountCreateRequest)
  })
_sym_db.RegisterMessage(AccountCreateRequest)

AccountCreateResponse = _reflection.GeneratedProtocolMessageType('AccountCreateResponse', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTCREATERESPONSE,
  '__module__' : 'accounts_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountCreateResponse)
  })
_sym_db.RegisterMessage(AccountCreateResponse)

AccountGetRequest = _reflection.GeneratedProtocolMessageType('AccountGetRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTGETREQUEST,
  '__module__' : 'accounts_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountGetRequest)
  })
_sym_db.RegisterMessage(AccountGetRequest)

AccountGetResponse = _reflection.GeneratedProtocolMessageType('AccountGetResponse', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTGETRESPONSE,
  '__module__' : 'accounts_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountGetResponse)
  })
_sym_db.RegisterMessage(AccountGetResponse)

AccountUpdateRequest = _reflection.GeneratedProtocolMessageType('AccountUpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTUPDATEREQUEST,
  '__module__' : 'accounts_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountUpdateRequest)
  })
_sym_db.RegisterMessage(AccountUpdateRequest)

AccountUpdateResponse = _reflection.GeneratedProtocolMessageType('AccountUpdateResponse', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTUPDATERESPONSE,
  '__module__' : 'accounts_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountUpdateResponse)
  })
_sym_db.RegisterMessage(AccountUpdateResponse)

AccountDeleteRequest = _reflection.GeneratedProtocolMessageType('AccountDeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTDELETEREQUEST,
  '__module__' : 'accounts_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountDeleteRequest)
  })
_sym_db.RegisterMessage(AccountDeleteRequest)

AccountDeleteResponse = _reflection.GeneratedProtocolMessageType('AccountDeleteResponse', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTDELETERESPONSE,
  '__module__' : 'accounts_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountDeleteResponse)
  })
_sym_db.RegisterMessage(AccountDeleteResponse)

AccountListRequest = _reflection.GeneratedProtocolMessageType('AccountListRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTLISTREQUEST,
  '__module__' : 'accounts_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountListRequest)
  })
_sym_db.RegisterMessage(AccountListRequest)

AccountListResponse = _reflection.GeneratedProtocolMessageType('AccountListResponse', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTLISTRESPONSE,
  '__module__' : 'accounts_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountListResponse)
  })
_sym_db.RegisterMessage(AccountListResponse)

Account = _reflection.GeneratedProtocolMessageType('Account', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNT,
  '__module__' : 'accounts_pb2'
  # @@protoc_insertion_point(class_scope:v1.Account)
  })
_sym_db.RegisterMessage(Account)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {
  'DESCRIPTOR' : _USER,
  '__module__' : 'accounts_pb2'
  # @@protoc_insertion_point(class_scope:v1.User)
  })
_sym_db.RegisterMessage(User)

Service = _reflection.GeneratedProtocolMessageType('Service', (_message.Message,), {
  'DESCRIPTOR' : _SERVICE,
  '__module__' : 'accounts_pb2'
  # @@protoc_insertion_point(class_scope:v1.Service)
  })
_sym_db.RegisterMessage(Service)

Token = _reflection.GeneratedProtocolMessageType('Token', (_message.Message,), {
  'DESCRIPTOR' : _TOKEN,
  '__module__' : 'accounts_pb2'
  # @@protoc_insertion_point(class_scope:v1.Token)
  })
_sym_db.RegisterMessage(Token)

_ACCOUNTS = DESCRIPTOR.services_by_name['Accounts']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031com.strongdm.api.plumbingB\020AccountsPlumbingZ5github.com/strongdm/strongdm-sdk-go/v3/internal/v1;v1'
  _ACCOUNTCREATEREQUEST.fields_by_name['account']._options = None
  _ACCOUNTCREATEREQUEST.fields_by_name['account']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACCOUNTCREATERESPONSE.fields_by_name['meta']._options = None
  _ACCOUNTCREATERESPONSE.fields_by_name['meta']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACCOUNTCREATERESPONSE.fields_by_name['account']._options = None
  _ACCOUNTCREATERESPONSE.fields_by_name['account']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACCOUNTCREATERESPONSE.fields_by_name['token']._options = None
  _ACCOUNTCREATERESPONSE.fields_by_name['token']._serialized_options = b'\362\370\263\007\n\260\363\263\007\001\360\363\263\007\001'
  _ACCOUNTCREATERESPONSE.fields_by_name['rate_limit']._options = None
  _ACCOUNTCREATERESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\022\262\364\263\007\r!json_gateway'
  _ACCOUNTCREATERESPONSE.fields_by_name['access_key']._options = None
  _ACCOUNTCREATERESPONSE.fields_by_name['access_key']._serialized_options = b'\362\370\263\007#\260\363\263\007\001\262\364\263\007\001*\262\364\263\007\023!terraform-provider'
  _ACCOUNTCREATERESPONSE.fields_by_name['secret_key']._options = None
  _ACCOUNTCREATERESPONSE.fields_by_name['secret_key']._serialized_options = b'\362\370\263\007#\260\363\263\007\001\262\364\263\007\001*\262\364\263\007\023!terraform-provider'
  _ACCOUNTCREATERESPONSE._options = None
  _ACCOUNTCREATERESPONSE._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _ACCOUNTGETREQUEST.fields_by_name['id']._options = None
  _ACCOUNTGETREQUEST.fields_by_name['id']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACCOUNTGETRESPONSE.fields_by_name['meta']._options = None
  _ACCOUNTGETRESPONSE.fields_by_name['meta']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACCOUNTGETRESPONSE.fields_by_name['account']._options = None
  _ACCOUNTGETRESPONSE.fields_by_name['account']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACCOUNTGETRESPONSE.fields_by_name['rate_limit']._options = None
  _ACCOUNTGETRESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\022\262\364\263\007\r!json_gateway'
  _ACCOUNTGETRESPONSE._options = None
  _ACCOUNTGETRESPONSE._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _ACCOUNTUPDATEREQUEST.fields_by_name['account']._options = None
  _ACCOUNTUPDATEREQUEST.fields_by_name['account']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACCOUNTUPDATERESPONSE.fields_by_name['meta']._options = None
  _ACCOUNTUPDATERESPONSE.fields_by_name['meta']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACCOUNTUPDATERESPONSE.fields_by_name['account']._options = None
  _ACCOUNTUPDATERESPONSE.fields_by_name['account']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACCOUNTUPDATERESPONSE.fields_by_name['rate_limit']._options = None
  _ACCOUNTUPDATERESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\022\262\364\263\007\r!json_gateway'
  _ACCOUNTUPDATERESPONSE._options = None
  _ACCOUNTUPDATERESPONSE._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _ACCOUNTDELETEREQUEST.fields_by_name['id']._options = None
  _ACCOUNTDELETEREQUEST.fields_by_name['id']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACCOUNTDELETERESPONSE.fields_by_name['meta']._options = None
  _ACCOUNTDELETERESPONSE.fields_by_name['meta']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACCOUNTDELETERESPONSE.fields_by_name['rate_limit']._options = None
  _ACCOUNTDELETERESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\022\262\364\263\007\r!json_gateway'
  _ACCOUNTDELETERESPONSE._options = None
  _ACCOUNTDELETERESPONSE._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _ACCOUNTLISTREQUEST.fields_by_name['filter']._options = None
  _ACCOUNTLISTREQUEST.fields_by_name['filter']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACCOUNTLISTRESPONSE.fields_by_name['accounts']._options = None
  _ACCOUNTLISTRESPONSE.fields_by_name['accounts']._serialized_options = b'\362\370\263\007\005\270\363\263\007\001'
  _ACCOUNTLISTRESPONSE.fields_by_name['rate_limit']._options = None
  _ACCOUNTLISTRESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\022\262\364\263\007\r!json_gateway'
  _ACCOUNT.oneofs_by_name['account']._options = None
  _ACCOUNT.oneofs_by_name['account']._serialized_options = b'\252\370\263\007\016\252\370\263\007\tsuspended\252\370\263\007\t\252\370\263\007\004tags'
  _ACCOUNT.fields_by_name['user']._options = None
  _ACCOUNT.fields_by_name['user']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACCOUNT.fields_by_name['service']._options = None
  _ACCOUNT.fields_by_name['service']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACCOUNT.fields_by_name['token']._options = None
  _ACCOUNT.fields_by_name['token']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACCOUNT._options = None
  _ACCOUNT._serialized_options = b'\372\370\263\007\005\250\363\263\007\001\372\370\263\007R\302\363\263\007M\242\363\263\007 tf_examples/account_resource.txt\252\363\263\007#tf_examples/account_data_source.txt'
  _USER.fields_by_name['id']._options = None
  _USER.fields_by_name['id']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _USER.fields_by_name['email']._options = None
  _USER.fields_by_name['email']._serialized_options = b'\362\370\263\007\n\260\363\263\007\001\300\363\263\007\001'
  _USER.fields_by_name['first_name']._options = None
  _USER.fields_by_name['first_name']._serialized_options = b'\362\370\263\007\n\260\363\263\007\001\300\363\263\007\001'
  _USER.fields_by_name['last_name']._options = None
  _USER.fields_by_name['last_name']._serialized_options = b'\362\370\263\007\n\260\363\263\007\001\300\363\263\007\001'
  _USER.fields_by_name['suspended']._options = None
  _USER.fields_by_name['suspended']._serialized_options = b'\362\370\263\007\022\262\364\263\007\r!json_gateway'
  _USER.fields_by_name['tags']._options = None
  _USER.fields_by_name['tags']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _USER.fields_by_name['permission_level']._options = None
  _USER.fields_by_name['permission_level']._serialized_options = b'\362\370\263\007\027\230\364\263\007\001\262\364\263\007\r!json_gateway'
  _USER.fields_by_name['managed_by']._options = None
  _USER.fields_by_name['managed_by']._serialized_options = b'\362\370\263\007\n\260\363\263\007\001\230\364\263\007\001'
  _USER.fields_by_name['external_id']._options = None
  _USER.fields_by_name['external_id']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _USER.fields_by_name['suspendedRO']._options = None
  _USER.fields_by_name['suspendedRO']._serialized_options = b'\362\370\263\007\277\001\260\363\263\007\001\312\363\263\007\257\001\302\364\263\007\017\n\002go\022\tSuspended\302\364\263\007\020\n\003cli\022\tsuspended\302\364\263\007\021\n\004ruby\022\tsuspended\302\364\263\007\023\n\006python\022\tsuspended\302\364\263\007\021\n\004java\022\tSuspended\302\364\263\007\037\n\022terraform-provider\022\tsuspended\302\364\263\007\031\n\014json_gateway\022\tsuspended\230\364\263\007\001'
  _USER.fields_by_name['permission_levelRW']._options = None
  _USER.fields_by_name['permission_levelRW']._serialized_options = b'\362\370\263\007\355\001\260\363\263\007\001\312\363\263\007\335\001\302\364\263\007\025\n\002go\022\017PermissionLevel\302\364\263\007\027\n\003cli\022\020permission-level\302\364\263\007\030\n\004ruby\022\020permission_level\302\364\263\007\032\n\006python\022\020permission_level\302\364\263\007\027\n\004java\022\017PermissionLevel\302\364\263\007&\n\022terraform-provider\022\020permission_level\302\364\263\007\037\n\014json_gateway\022\017permissionLevel\320\364\263\007\001'
  _USER.fields_by_name['password']._options = None
  _USER.fields_by_name['password']._serialized_options = b'\362\370\263\007(\260\363\263\007\001\350\363\263\007\001\262\364\263\007\001*\262\364\263\007\023!terraform-provider'
  _USER.fields_by_name['SCIM']._options = None
  _USER.fields_by_name['SCIM']._serialized_options = b'\362\370\263\007\020\260\363\263\007\001\230\364\263\007\001\262\364\263\007\001*'
  _USER.fields_by_name['manager_id']._options = None
  _USER.fields_by_name['manager_id']._serialized_options = b'\362\370\263\007\013\260\363\263\007\001\262\364\263\007\001*'
  _USER.fields_by_name['resolved_manager_id']._options = None
  _USER.fields_by_name['resolved_manager_id']._serialized_options = b'\362\370\263\007\020\260\363\263\007\001\230\364\263\007\001\262\364\263\007\001*'
  _USER._options = None
  _USER._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _SERVICE.fields_by_name['id']._options = None
  _SERVICE.fields_by_name['id']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _SERVICE.fields_by_name['name']._options = None
  _SERVICE.fields_by_name['name']._serialized_options = b'\362\370\263\007\n\260\363\263\007\001\300\363\263\007\001'
  _SERVICE.fields_by_name['suspended']._options = None
  _SERVICE.fields_by_name['suspended']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _SERVICE.fields_by_name['tags']._options = None
  _SERVICE.fields_by_name['tags']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _SERVICE._options = None
  _SERVICE._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _TOKEN.fields_by_name['id']._options = None
  _TOKEN.fields_by_name['id']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _TOKEN.fields_by_name['name']._options = None
  _TOKEN.fields_by_name['name']._serialized_options = b'\362\370\263\007\n\260\363\263\007\001\300\363\263\007\001'
  _TOKEN.fields_by_name['suspended']._options = None
  _TOKEN.fields_by_name['suspended']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _TOKEN.fields_by_name['tags']._options = None
  _TOKEN.fields_by_name['tags']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _TOKEN.fields_by_name['rekeyed']._options = None
  _TOKEN.fields_by_name['rekeyed']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _TOKEN.fields_by_name['deadline']._options = None
  _TOKEN.fields_by_name['deadline']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _TOKEN.fields_by_name['account_type']._options = None
  _TOKEN.fields_by_name['account_type']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _TOKEN.fields_by_name['permissions']._options = None
  _TOKEN.fields_by_name['permissions']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _TOKEN.fields_by_name['duration']._options = None
  _TOKEN.fields_by_name['duration']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _TOKEN._options = None
  _TOKEN._serialized_options = b'\372\370\263\007\n\250\363\263\007\001\330\363\263\007\001'
  _ACCOUNTS._options = None
  _ACCOUNTS._serialized_options = b'\312\371\263\007\014\302\371\263\007\007Account\312\371\263\007\007\322\371\263\007\002a-\312\371\263\007\006\312\371\263\007\001*\312\371\263\007\t\312\371\263\007\004!cli'
  _ACCOUNTS.methods_by_name['Create']._options = None
  _ACCOUNTS.methods_by_name['Create']._serialized_options = b'\202\371\263\007\t\242\363\263\007\004post\202\371\263\007\021\252\363\263\007\014/v1/accounts'
  _ACCOUNTS.methods_by_name['Get']._options = None
  _ACCOUNTS.methods_by_name['Get']._serialized_options = b'\202\371\263\007\010\242\363\263\007\003get\202\371\263\007\026\252\363\263\007\021/v1/accounts/{id}'
  _ACCOUNTS.methods_by_name['Update']._options = None
  _ACCOUNTS.methods_by_name['Update']._serialized_options = b'\202\371\263\007\010\242\363\263\007\003put\202\371\263\007\026\252\363\263\007\021/v1/accounts/{id}'
  _ACCOUNTS.methods_by_name['Delete']._options = None
  _ACCOUNTS.methods_by_name['Delete']._serialized_options = b'\202\371\263\007\013\242\363\263\007\006delete\202\371\263\007\026\252\363\263\007\021/v1/accounts/{id}'
  _ACCOUNTS.methods_by_name['List']._options = None
  _ACCOUNTS.methods_by_name['List']._serialized_options = b'\202\371\263\007\010\242\363\263\007\003get\202\371\263\007\021\252\363\263\007\014/v1/accounts'
  _ACCOUNTCREATEREQUEST._serialized_start=126
  _ACCOUNTCREATEREQUEST._serialized_end=231
  _ACCOUNTCREATERESPONSE._serialized_start=234
  _ACCOUNTCREATERESPONSE._serialized_end=610
  _ACCOUNTGETREQUEST._serialized_start=612
  _ACCOUNTGETREQUEST._serialized_end=693
  _ACCOUNTGETRESPONSE._serialized_start=696
  _ACCOUNTGETRESPONSE._serialized_end=910
  _ACCOUNTUPDATEREQUEST._serialized_start=912
  _ACCOUNTUPDATEREQUEST._serialized_end=1029
  _ACCOUNTUPDATERESPONSE._serialized_start=1032
  _ACCOUNTUPDATERESPONSE._serialized_end=1252
  _ACCOUNTDELETEREQUEST._serialized_start=1254
  _ACCOUNTDELETEREQUEST._serialized_end=1341
  _ACCOUNTDELETERESPONSE._serialized_start=1344
  _ACCOUNTDELETERESPONSE._serialized_end=1522
  _ACCOUNTLISTREQUEST._serialized_start=1524
  _ACCOUNTLISTREQUEST._serialized_end=1611
  _ACCOUNTLISTRESPONSE._serialized_start=1614
  _ACCOUNTLISTRESPONSE._serialized_end=1807
  _ACCOUNT._serialized_start=1810
  _ACCOUNT._serialized_end=2086
  _USER._serialized_start=2089
  _USER._serialized_end=3131
  _SERVICE._serialized_start=3134
  _SERVICE._serialized_end=3277
  _TOKEN._serialized_start=3280
  _TOKEN._serialized_end=3665
  _ACCOUNTS._serialized_start=3668
  _ACCOUNTS._serialized_end=4238
# @@protoc_insertion_point(module_scope)
