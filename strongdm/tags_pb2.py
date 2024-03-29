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
# source: tags.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import options_pb2 as options__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ntags.proto\x12\x02v1\x1a\roptions.proto\"\xda\x02\n\x04Tags\x12\x1c\n\x05pairs\x18\x01 \x03(\x0b\x32\r.v1.Tags.Pair\x1a\x42\n\x04Pair\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x1d\xfa\xf8\xb3\x07\x18\xd2\xf3\xb3\x07\x01*\xd2\xf3\xb3\x07\r!json_gateway:\xef\x01\xfa\xf8\xb3\x07\xe9\x01\xca\xf3\xb3\x07\xcb\x01\xea\xf3\xb3\x07\x04tags\xf2\xf3\xb3\x07\n\n\x02go\x12\x04Tags\xf2\xf3\xb3\x07\x12\n\ngo_private\x12\x04Tags\xf2\xf3\xb3\x07\x14\n\x0cgo_terraform\x12\x04Tags\xf2\xf3\xb3\x07%\n\x04java\x12\x1djava.util.Map<String, String>\xf2\xf3\xb3\x07\x1d\n\x12terraform-provider\x12\x07TypeMap\xf2\xf3\xb3\x07!\n\x0cjson_gateway\x12\x11map[string]string\xfa\xf3\xb3\x07\x0ctagsElemType\xd2\xf3\xb3\x07\x01*\xd2\xf3\xb3\x07\r!json_gateway\"F\n\x03Tag\x12\x18\n\x04name\x18\x01 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x19\n\x05value\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\x42`\n\x19\x63om.strongdm.api.plumbingB\x0cTagsPlumbingZ5github.com/strongdm/strongdm-sdk-go/v3/internal/v1;v1b\x06proto3')



_TAGS = DESCRIPTOR.message_types_by_name['Tags']
_TAGS_PAIR = _TAGS.nested_types_by_name['Pair']
_TAG = DESCRIPTOR.message_types_by_name['Tag']
Tags = _reflection.GeneratedProtocolMessageType('Tags', (_message.Message,), {

  'Pair' : _reflection.GeneratedProtocolMessageType('Pair', (_message.Message,), {
    'DESCRIPTOR' : _TAGS_PAIR,
    '__module__' : 'tags_pb2'
    # @@protoc_insertion_point(class_scope:v1.Tags.Pair)
    })
  ,
  'DESCRIPTOR' : _TAGS,
  '__module__' : 'tags_pb2'
  # @@protoc_insertion_point(class_scope:v1.Tags)
  })
_sym_db.RegisterMessage(Tags)
_sym_db.RegisterMessage(Tags.Pair)

Tag = _reflection.GeneratedProtocolMessageType('Tag', (_message.Message,), {
  'DESCRIPTOR' : _TAG,
  '__module__' : 'tags_pb2'
  # @@protoc_insertion_point(class_scope:v1.Tag)
  })
_sym_db.RegisterMessage(Tag)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031com.strongdm.api.plumbingB\014TagsPlumbingZ5github.com/strongdm/strongdm-sdk-go/v3/internal/v1;v1'
  _TAGS_PAIR._options = None
  _TAGS_PAIR._serialized_options = b'\372\370\263\007\030\322\363\263\007\001*\322\363\263\007\r!json_gateway'
  _TAGS._options = None
  _TAGS._serialized_options = b'\372\370\263\007\351\001\312\363\263\007\313\001\352\363\263\007\004tags\362\363\263\007\n\n\002go\022\004Tags\362\363\263\007\022\n\ngo_private\022\004Tags\362\363\263\007\024\n\014go_terraform\022\004Tags\362\363\263\007%\n\004java\022\035java.util.Map<String, String>\362\363\263\007\035\n\022terraform-provider\022\007TypeMap\362\363\263\007!\n\014json_gateway\022\021map[string]string\372\363\263\007\014tagsElemType\322\363\263\007\001*\322\363\263\007\r!json_gateway'
  _TAG.fields_by_name['name']._options = None
  _TAG.fields_by_name['name']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _TAG.fields_by_name['value']._options = None
  _TAG.fields_by_name['value']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _TAG._options = None
  _TAG._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _TAGS._serialized_start=34
  _TAGS._serialized_end=380
  _TAGS_PAIR._serialized_start=72
  _TAGS_PAIR._serialized_end=138
  _TAG._serialized_start=382
  _TAG._serialized_end=452
# @@protoc_insertion_point(module_scope)
