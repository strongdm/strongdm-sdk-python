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
# source: account_permissions.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x61\x63\x63ount_permissions.proto\x12\x02v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\roptions.proto\x1a\nspec.proto\"a\n\x1c\x41\x63\x63ountPermissionListRequest\x12%\n\x04meta\x18\x01 \x01(\x0b\x32\x17.v1.ListRequestMetadata\x12\x1a\n\x06\x66ilter\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xd8\x01\n\x1d\x41\x63\x63ountPermissionListResponse\x12&\n\x04meta\x18\x01 \x01(\x0b\x32\x18.v1.ListResponseMetadata\x12\x36\n\x0bpermissions\x18\x02 \x03(\x0b\x32\x15.v1.AccountPermissionB\n\xf2\xf8\xb3\x07\x05\xb8\xf3\xb3\x07\x01\x12W\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB,\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway\"\xd5\x01\n\x11\x41\x63\x63ountPermission\x12\x1e\n\naccount_id\x18\x01 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12:\n\ngranted_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x1e\n\npermission\x18\x03 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x19\n\x05scope\x18\x04 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x1d\n\tscoped_id\x18\x05 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\x32\xae\x01\n\x12\x41\x63\x63ountPermissions\x12{\n\x04List\x12 .v1.AccountPermissionListRequest\x1a!.v1.AccountPermissionListResponse\".\x82\xf9\xb3\x07\x08\xa2\xf3\xb3\x07\x03get\x82\xf9\xb3\x07\x1c\xaa\xf3\xb3\x07\x17/v1/account-permissions\x1a\x1b\xca\xf9\xb3\x07\x16\xc2\xf9\xb3\x07\x11\x41\x63\x63ountPermissionBn\n\x19\x63om.strongdm.api.plumbingB\x1a\x41\x63\x63ountPermissionsPlumbingZ5github.com/strongdm/strongdm-sdk-go/v3/internal/v1;v1b\x06proto3')



_ACCOUNTPERMISSIONLISTREQUEST = DESCRIPTOR.message_types_by_name['AccountPermissionListRequest']
_ACCOUNTPERMISSIONLISTRESPONSE = DESCRIPTOR.message_types_by_name['AccountPermissionListResponse']
_ACCOUNTPERMISSION = DESCRIPTOR.message_types_by_name['AccountPermission']
AccountPermissionListRequest = _reflection.GeneratedProtocolMessageType('AccountPermissionListRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTPERMISSIONLISTREQUEST,
  '__module__' : 'account_permissions_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountPermissionListRequest)
  })
_sym_db.RegisterMessage(AccountPermissionListRequest)

AccountPermissionListResponse = _reflection.GeneratedProtocolMessageType('AccountPermissionListResponse', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTPERMISSIONLISTRESPONSE,
  '__module__' : 'account_permissions_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountPermissionListResponse)
  })
_sym_db.RegisterMessage(AccountPermissionListResponse)

AccountPermission = _reflection.GeneratedProtocolMessageType('AccountPermission', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTPERMISSION,
  '__module__' : 'account_permissions_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountPermission)
  })
_sym_db.RegisterMessage(AccountPermission)

_ACCOUNTPERMISSIONS = DESCRIPTOR.services_by_name['AccountPermissions']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031com.strongdm.api.plumbingB\032AccountPermissionsPlumbingZ5github.com/strongdm/strongdm-sdk-go/v3/internal/v1;v1'
  _ACCOUNTPERMISSIONLISTREQUEST.fields_by_name['filter']._options = None
  _ACCOUNTPERMISSIONLISTREQUEST.fields_by_name['filter']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACCOUNTPERMISSIONLISTRESPONSE.fields_by_name['permissions']._options = None
  _ACCOUNTPERMISSIONLISTRESPONSE.fields_by_name['permissions']._serialized_options = b'\362\370\263\007\005\270\363\263\007\001'
  _ACCOUNTPERMISSIONLISTRESPONSE.fields_by_name['rate_limit']._options = None
  _ACCOUNTPERMISSIONLISTRESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\022\262\364\263\007\r!json_gateway'
  _ACCOUNTPERMISSION.fields_by_name['account_id']._options = None
  _ACCOUNTPERMISSION.fields_by_name['account_id']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACCOUNTPERMISSION.fields_by_name['granted_at']._options = None
  _ACCOUNTPERMISSION.fields_by_name['granted_at']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACCOUNTPERMISSION.fields_by_name['permission']._options = None
  _ACCOUNTPERMISSION.fields_by_name['permission']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACCOUNTPERMISSION.fields_by_name['scope']._options = None
  _ACCOUNTPERMISSION.fields_by_name['scope']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACCOUNTPERMISSION.fields_by_name['scoped_id']._options = None
  _ACCOUNTPERMISSION.fields_by_name['scoped_id']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACCOUNTPERMISSION._options = None
  _ACCOUNTPERMISSION._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _ACCOUNTPERMISSIONS._options = None
  _ACCOUNTPERMISSIONS._serialized_options = b'\312\371\263\007\026\302\371\263\007\021AccountPermission'
  _ACCOUNTPERMISSIONS.methods_by_name['List']._options = None
  _ACCOUNTPERMISSIONS.methods_by_name['List']._serialized_options = b'\202\371\263\007\010\242\363\263\007\003get\202\371\263\007\034\252\363\263\007\027/v1/account-permissions'
  _ACCOUNTPERMISSIONLISTREQUEST._serialized_start=93
  _ACCOUNTPERMISSIONLISTREQUEST._serialized_end=190
  _ACCOUNTPERMISSIONLISTRESPONSE._serialized_start=193
  _ACCOUNTPERMISSIONLISTRESPONSE._serialized_end=409
  _ACCOUNTPERMISSION._serialized_start=412
  _ACCOUNTPERMISSION._serialized_end=625
  _ACCOUNTPERMISSIONS._serialized_start=628
  _ACCOUNTPERMISSIONS._serialized_end=802
# @@protoc_insertion_point(module_scope)
