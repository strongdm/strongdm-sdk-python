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
# source: options.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\roptions.proto\x12\x02v1\x1a google/protobuf/descriptor.proto\"X\n\x0b\x46ileOptions\x12\x11\n\x07targets\x18\xc4\xc1v \x03(\t:6\xfa\xf8\xb3\x07\x12\xd2\xf3\xb3\x07\r!json_gateway\xfa\xf8\xb3\x07\x1a\xd2\xf3\xb3\x07\x15!json_gateway_private\"\x85\x01\n\x0eServiceOptions\x12\x13\n\tmain_noun\x18\x98\xbfv \x01(\t\x12\x13\n\tid_prefix\x18\x9a\xbfv \x01(\t\x12\x11\n\x07targets\x18\x99\xbfv \x03(\t:6\xfa\xf8\xb3\x07\x12\xd2\xf3\xb3\x07\r!json_gateway\xfa\xf8\xb3\x07\x1a\xd2\xf3\xb3\x07\x15!json_gateway_private\"\x84\x01\n\rMethodOptions\x12\x10\n\x06method\x18\xb4\xbev \x01(\t\x12\r\n\x03url\x18\xb5\xbev \x01(\t\x12\x1a\n\x10\x64\x65precation_date\x18\xb6\xbev \x01(\t:6\xfa\xf8\xb3\x07\x12\xd2\xf3\xb3\x07\r!json_gateway\xfa\xf8\xb3\x07\x1a\xd2\xf3\xb3\x07\x15!json_gateway_private\"\xec\x01\n\x0eMessageOptions\x12\x13\n\tporcelain\x18\xb5\xbev \x01(\x08\x12\x0f\n\x05\x65rror\x18\xb6\xbev \x01(\x05\x12\x17\n\roptions_field\x18\xb7\xbev \x01(\t\x12\x11\n\x07targets\x18\xba\xbev \x03(\t\x12+\n\x0eterraform_docs\x18\xb8\xbev \x01(\x0b\x32\x11.v1.TerraformDocs\x12#\n\x06\x63ustom\x18\xb9\xbev \x01(\x0b\x32\x11.v1.CustomOptions:6\xfa\xf8\xb3\x07\x12\xd2\xf3\xb3\x07\r!json_gateway\xfa\xf8\xb3\x07\x1a\xd2\xf3\xb3\x07\x15!json_gateway_private\"_\n\x0cOneofOptions\x12\x17\n\rcommon_fields\x18\x85\xbfv \x03(\t:6\xfa\xf8\xb3\x07\x12\xd2\xf3\xb3\x07\r!json_gateway\xfa\xf8\xb3\x07\x1a\xd2\xf3\xb3\x07\x15!json_gateway_private\"\x82\x04\n\x0c\x46ieldOptions\x12\x13\n\tporcelain\x18\xb6\xbev \x01(\x08\x12\x12\n\x08iterable\x18\xb7\xbev \x01(\x08\x12\x12\n\x08required\x18\xb8\xbev \x01(\x08\x12\x14\n\nwrite_only\x18\xbd\xbev \x01(\x08\x12\x13\n\tread_only\x18\xc3\xbev \x01(\x08\x12\x17\n\ris_credential\x18\xc4\xbev \x01(\x08\x12\x11\n\x07targets\x18\xc6\xbev \x03(\t\x12\x1d\n\x13terraform_force_new\x18\xbc\xbev \x01(\x08\x12\x1d\n\x13terraform_sensitive\x18\xbe\xbev \x01(\x08\x12&\n\x1cterraform_diff_suppress_func\x18\xc7\xbev \x01(\t\x12\x1c\n\x12terraform_computed\x18\xca\xbev \x01(\x08\x12#\n\x06\x63ustom\x18\xb9\xbev \x01(\x0b\x32\x11.v1.CustomOptions\x12\x44\n\x12read_only_override\x18\xc0\xbev \x03(\x0b\x32&.v1.FieldOptions.ReadOnlyOverrideEntry\x1a\x37\n\x15ReadOnlyOverrideEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x08:\x02\x38\x01:6\xfa\xf8\xb3\x07\x12\xd2\xf3\xb3\x07\r!json_gateway\xfa\xf8\xb3\x07\x1a\xd2\xf3\xb3\x07\x15!json_gateway_private\"\x9a\x05\n\rCustomOptions\x12\x13\n\tconverter\x18\xbd\xbev \x01(\t\x12O\n\x17porcelain_type_override\x18\xbe\xbev \x03(\x0b\x32,.v1.CustomOptions.PorcelainTypeOverrideEntry\x12O\n\x17porcelain_name_override\x18\xc8\xbev \x03(\x0b\x32,.v1.CustomOptions.PorcelainNameOverrideEntry\x12\x42\n\x10\x63omment_override\x18\xd3\xbev \x03(\x0b\x32&.v1.CustomOptions.CommentOverrideEntry\x12H\n\x13\x64\x65precated_override\x18\xc0\xbev \x03(\x0b\x32).v1.CustomOptions.DeprecatedOverrideEntry\x12\x1d\n\x13terraform_elem_type\x18\xbf\xbev \x01(\t\x1a<\n\x1aPorcelainTypeOverrideEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a<\n\x1aPorcelainNameOverrideEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x36\n\x14\x43ommentOverrideEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x39\n\x17\x44\x65precatedOverrideEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x08:\x02\x38\x01:6\xfa\xf8\xb3\x07\x12\xd2\xf3\xb3\x07\r!json_gateway\xfa\xf8\xb3\x07\x1a\xd2\xf3\xb3\x07\x15!json_gateway_private\"\x8c\x01\n\rTerraformDocs\x12\x1f\n\x15resource_example_path\x18\xb4\xbev \x01(\t\x12\"\n\x18\x64\x61ta_source_example_path\x18\xb5\xbev \x01(\t:6\xfa\xf8\xb3\x07\x12\xd2\xf3\xb3\x07\r!json_gateway\xfa\xf8\xb3\x07\x1a\xd2\xf3\xb3\x07\x15!json_gateway_private:E\n\x0c\x66ile_options\x12\x1c.google.protobuf.FileOptions\x18\xa8\xc2v \x01(\x0b\x32\x0f.v1.FileOptions:N\n\x0fservice_options\x12\x1f.google.protobuf.ServiceOptions\x18\x99\xbfv \x01(\x0b\x32\x12.v1.ServiceOptions:K\n\x0emethod_options\x12\x1e.google.protobuf.MethodOptions\x18\x90\xbfv \x01(\x0b\x32\x11.v1.MethodOptions:N\n\x0fmessage_options\x12\x1f.google.protobuf.MessageOptions\x18\x8f\xbfv \x01(\x0b\x32\x12.v1.MessageOptions:H\n\roneof_options\x12\x1d.google.protobuf.OneofOptions\x18\x85\xbfv \x01(\x0b\x32\x10.v1.OneofOptions:H\n\rfield_options\x12\x1d.google.protobuf.FieldOptions\x18\x8e\xbfv \x01(\x0b\x32\x10.v1.FieldOptionsBU\n\x1c\x63om.strongdm.api.v1.plumbingZ5github.com/strongdm/strongdm-sdk-go/v2/internal/v1;v1b\x06proto3')


FILE_OPTIONS_FIELD_NUMBER = 1941800
file_options = DESCRIPTOR.extensions_by_name['file_options']
SERVICE_OPTIONS_FIELD_NUMBER = 1941401
service_options = DESCRIPTOR.extensions_by_name['service_options']
METHOD_OPTIONS_FIELD_NUMBER = 1941392
method_options = DESCRIPTOR.extensions_by_name['method_options']
MESSAGE_OPTIONS_FIELD_NUMBER = 1941391
message_options = DESCRIPTOR.extensions_by_name['message_options']
ONEOF_OPTIONS_FIELD_NUMBER = 1941381
oneof_options = DESCRIPTOR.extensions_by_name['oneof_options']
FIELD_OPTIONS_FIELD_NUMBER = 1941390
field_options = DESCRIPTOR.extensions_by_name['field_options']

_FILEOPTIONS = DESCRIPTOR.message_types_by_name['FileOptions']
_SERVICEOPTIONS = DESCRIPTOR.message_types_by_name['ServiceOptions']
_METHODOPTIONS = DESCRIPTOR.message_types_by_name['MethodOptions']
_MESSAGEOPTIONS = DESCRIPTOR.message_types_by_name['MessageOptions']
_ONEOFOPTIONS = DESCRIPTOR.message_types_by_name['OneofOptions']
_FIELDOPTIONS = DESCRIPTOR.message_types_by_name['FieldOptions']
_FIELDOPTIONS_READONLYOVERRIDEENTRY = _FIELDOPTIONS.nested_types_by_name['ReadOnlyOverrideEntry']
_CUSTOMOPTIONS = DESCRIPTOR.message_types_by_name['CustomOptions']
_CUSTOMOPTIONS_PORCELAINTYPEOVERRIDEENTRY = _CUSTOMOPTIONS.nested_types_by_name['PorcelainTypeOverrideEntry']
_CUSTOMOPTIONS_PORCELAINNAMEOVERRIDEENTRY = _CUSTOMOPTIONS.nested_types_by_name['PorcelainNameOverrideEntry']
_CUSTOMOPTIONS_COMMENTOVERRIDEENTRY = _CUSTOMOPTIONS.nested_types_by_name['CommentOverrideEntry']
_CUSTOMOPTIONS_DEPRECATEDOVERRIDEENTRY = _CUSTOMOPTIONS.nested_types_by_name['DeprecatedOverrideEntry']
_TERRAFORMDOCS = DESCRIPTOR.message_types_by_name['TerraformDocs']
FileOptions = _reflection.GeneratedProtocolMessageType('FileOptions', (_message.Message,), {
  'DESCRIPTOR' : _FILEOPTIONS,
  '__module__' : 'options_pb2'
  # @@protoc_insertion_point(class_scope:v1.FileOptions)
  })
_sym_db.RegisterMessage(FileOptions)

ServiceOptions = _reflection.GeneratedProtocolMessageType('ServiceOptions', (_message.Message,), {
  'DESCRIPTOR' : _SERVICEOPTIONS,
  '__module__' : 'options_pb2'
  # @@protoc_insertion_point(class_scope:v1.ServiceOptions)
  })
_sym_db.RegisterMessage(ServiceOptions)

MethodOptions = _reflection.GeneratedProtocolMessageType('MethodOptions', (_message.Message,), {
  'DESCRIPTOR' : _METHODOPTIONS,
  '__module__' : 'options_pb2'
  # @@protoc_insertion_point(class_scope:v1.MethodOptions)
  })
_sym_db.RegisterMessage(MethodOptions)

MessageOptions = _reflection.GeneratedProtocolMessageType('MessageOptions', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGEOPTIONS,
  '__module__' : 'options_pb2'
  # @@protoc_insertion_point(class_scope:v1.MessageOptions)
  })
_sym_db.RegisterMessage(MessageOptions)

OneofOptions = _reflection.GeneratedProtocolMessageType('OneofOptions', (_message.Message,), {
  'DESCRIPTOR' : _ONEOFOPTIONS,
  '__module__' : 'options_pb2'
  # @@protoc_insertion_point(class_scope:v1.OneofOptions)
  })
_sym_db.RegisterMessage(OneofOptions)

FieldOptions = _reflection.GeneratedProtocolMessageType('FieldOptions', (_message.Message,), {

  'ReadOnlyOverrideEntry' : _reflection.GeneratedProtocolMessageType('ReadOnlyOverrideEntry', (_message.Message,), {
    'DESCRIPTOR' : _FIELDOPTIONS_READONLYOVERRIDEENTRY,
    '__module__' : 'options_pb2'
    # @@protoc_insertion_point(class_scope:v1.FieldOptions.ReadOnlyOverrideEntry)
    })
  ,
  'DESCRIPTOR' : _FIELDOPTIONS,
  '__module__' : 'options_pb2'
  # @@protoc_insertion_point(class_scope:v1.FieldOptions)
  })
_sym_db.RegisterMessage(FieldOptions)
_sym_db.RegisterMessage(FieldOptions.ReadOnlyOverrideEntry)

CustomOptions = _reflection.GeneratedProtocolMessageType('CustomOptions', (_message.Message,), {

  'PorcelainTypeOverrideEntry' : _reflection.GeneratedProtocolMessageType('PorcelainTypeOverrideEntry', (_message.Message,), {
    'DESCRIPTOR' : _CUSTOMOPTIONS_PORCELAINTYPEOVERRIDEENTRY,
    '__module__' : 'options_pb2'
    # @@protoc_insertion_point(class_scope:v1.CustomOptions.PorcelainTypeOverrideEntry)
    })
  ,

  'PorcelainNameOverrideEntry' : _reflection.GeneratedProtocolMessageType('PorcelainNameOverrideEntry', (_message.Message,), {
    'DESCRIPTOR' : _CUSTOMOPTIONS_PORCELAINNAMEOVERRIDEENTRY,
    '__module__' : 'options_pb2'
    # @@protoc_insertion_point(class_scope:v1.CustomOptions.PorcelainNameOverrideEntry)
    })
  ,

  'CommentOverrideEntry' : _reflection.GeneratedProtocolMessageType('CommentOverrideEntry', (_message.Message,), {
    'DESCRIPTOR' : _CUSTOMOPTIONS_COMMENTOVERRIDEENTRY,
    '__module__' : 'options_pb2'
    # @@protoc_insertion_point(class_scope:v1.CustomOptions.CommentOverrideEntry)
    })
  ,

  'DeprecatedOverrideEntry' : _reflection.GeneratedProtocolMessageType('DeprecatedOverrideEntry', (_message.Message,), {
    'DESCRIPTOR' : _CUSTOMOPTIONS_DEPRECATEDOVERRIDEENTRY,
    '__module__' : 'options_pb2'
    # @@protoc_insertion_point(class_scope:v1.CustomOptions.DeprecatedOverrideEntry)
    })
  ,
  'DESCRIPTOR' : _CUSTOMOPTIONS,
  '__module__' : 'options_pb2'
  # @@protoc_insertion_point(class_scope:v1.CustomOptions)
  })
_sym_db.RegisterMessage(CustomOptions)
_sym_db.RegisterMessage(CustomOptions.PorcelainTypeOverrideEntry)
_sym_db.RegisterMessage(CustomOptions.PorcelainNameOverrideEntry)
_sym_db.RegisterMessage(CustomOptions.CommentOverrideEntry)
_sym_db.RegisterMessage(CustomOptions.DeprecatedOverrideEntry)

TerraformDocs = _reflection.GeneratedProtocolMessageType('TerraformDocs', (_message.Message,), {
  'DESCRIPTOR' : _TERRAFORMDOCS,
  '__module__' : 'options_pb2'
  # @@protoc_insertion_point(class_scope:v1.TerraformDocs)
  })
_sym_db.RegisterMessage(TerraformDocs)

if _descriptor._USE_C_DESCRIPTORS == False:
  google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(file_options)
  google_dot_protobuf_dot_descriptor__pb2.ServiceOptions.RegisterExtension(service_options)
  google_dot_protobuf_dot_descriptor__pb2.MethodOptions.RegisterExtension(method_options)
  google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(message_options)
  google_dot_protobuf_dot_descriptor__pb2.OneofOptions.RegisterExtension(oneof_options)
  google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(field_options)

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\034com.strongdm.api.v1.plumbingZ5github.com/strongdm/strongdm-sdk-go/v2/internal/v1;v1'
  _FILEOPTIONS._options = None
  _FILEOPTIONS._serialized_options = b'\372\370\263\007\022\322\363\263\007\r!json_gateway\372\370\263\007\032\322\363\263\007\025!json_gateway_private'
  _SERVICEOPTIONS._options = None
  _SERVICEOPTIONS._serialized_options = b'\372\370\263\007\022\322\363\263\007\r!json_gateway\372\370\263\007\032\322\363\263\007\025!json_gateway_private'
  _METHODOPTIONS._options = None
  _METHODOPTIONS._serialized_options = b'\372\370\263\007\022\322\363\263\007\r!json_gateway\372\370\263\007\032\322\363\263\007\025!json_gateway_private'
  _MESSAGEOPTIONS._options = None
  _MESSAGEOPTIONS._serialized_options = b'\372\370\263\007\022\322\363\263\007\r!json_gateway\372\370\263\007\032\322\363\263\007\025!json_gateway_private'
  _ONEOFOPTIONS._options = None
  _ONEOFOPTIONS._serialized_options = b'\372\370\263\007\022\322\363\263\007\r!json_gateway\372\370\263\007\032\322\363\263\007\025!json_gateway_private'
  _FIELDOPTIONS_READONLYOVERRIDEENTRY._options = None
  _FIELDOPTIONS_READONLYOVERRIDEENTRY._serialized_options = b'8\001'
  _FIELDOPTIONS._options = None
  _FIELDOPTIONS._serialized_options = b'\372\370\263\007\022\322\363\263\007\r!json_gateway\372\370\263\007\032\322\363\263\007\025!json_gateway_private'
  _CUSTOMOPTIONS_PORCELAINTYPEOVERRIDEENTRY._options = None
  _CUSTOMOPTIONS_PORCELAINTYPEOVERRIDEENTRY._serialized_options = b'8\001'
  _CUSTOMOPTIONS_PORCELAINNAMEOVERRIDEENTRY._options = None
  _CUSTOMOPTIONS_PORCELAINNAMEOVERRIDEENTRY._serialized_options = b'8\001'
  _CUSTOMOPTIONS_COMMENTOVERRIDEENTRY._options = None
  _CUSTOMOPTIONS_COMMENTOVERRIDEENTRY._serialized_options = b'8\001'
  _CUSTOMOPTIONS_DEPRECATEDOVERRIDEENTRY._options = None
  _CUSTOMOPTIONS_DEPRECATEDOVERRIDEENTRY._serialized_options = b'8\001'
  _CUSTOMOPTIONS._options = None
  _CUSTOMOPTIONS._serialized_options = b'\372\370\263\007\022\322\363\263\007\r!json_gateway\372\370\263\007\032\322\363\263\007\025!json_gateway_private'
  _TERRAFORMDOCS._options = None
  _TERRAFORMDOCS._serialized_options = b'\372\370\263\007\022\322\363\263\007\r!json_gateway\372\370\263\007\032\322\363\263\007\025!json_gateway_private'
  _FILEOPTIONS._serialized_start=55
  _FILEOPTIONS._serialized_end=143
  _SERVICEOPTIONS._serialized_start=146
  _SERVICEOPTIONS._serialized_end=279
  _METHODOPTIONS._serialized_start=282
  _METHODOPTIONS._serialized_end=414
  _MESSAGEOPTIONS._serialized_start=417
  _MESSAGEOPTIONS._serialized_end=653
  _ONEOFOPTIONS._serialized_start=655
  _ONEOFOPTIONS._serialized_end=750
  _FIELDOPTIONS._serialized_start=753
  _FIELDOPTIONS._serialized_end=1267
  _FIELDOPTIONS_READONLYOVERRIDEENTRY._serialized_start=1156
  _FIELDOPTIONS_READONLYOVERRIDEENTRY._serialized_end=1211
  _CUSTOMOPTIONS._serialized_start=1270
  _CUSTOMOPTIONS._serialized_end=1936
  _CUSTOMOPTIONS_PORCELAINTYPEOVERRIDEENTRY._serialized_start=1643
  _CUSTOMOPTIONS_PORCELAINTYPEOVERRIDEENTRY._serialized_end=1703
  _CUSTOMOPTIONS_PORCELAINNAMEOVERRIDEENTRY._serialized_start=1705
  _CUSTOMOPTIONS_PORCELAINNAMEOVERRIDEENTRY._serialized_end=1765
  _CUSTOMOPTIONS_COMMENTOVERRIDEENTRY._serialized_start=1767
  _CUSTOMOPTIONS_COMMENTOVERRIDEENTRY._serialized_end=1821
  _CUSTOMOPTIONS_DEPRECATEDOVERRIDEENTRY._serialized_start=1823
  _CUSTOMOPTIONS_DEPRECATEDOVERRIDEENTRY._serialized_end=1880
  _TERRAFORMDOCS._serialized_start=1939
  _TERRAFORMDOCS._serialized_end=2079
# @@protoc_insertion_point(module_scope)
