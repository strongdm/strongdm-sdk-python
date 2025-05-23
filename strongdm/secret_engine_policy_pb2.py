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
# source: secret_engine_policy.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import options_pb2 as options__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1asecret_engine_policy.proto\x12\x02v1\x1a\roptions.proto\"\xf7\x01\n\x1aSecretEnginePasswordPolicy\x12\x1a\n\x06length\x18\x01 \x01(\rB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12&\n\x12\x65xclude_upper_case\x18\x02 \x01(\x08\x42\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x1e\n\nnum_digits\x18\x03 \x01(\rB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x1f\n\x0bnum_symbols\x18\x04 \x01(\rB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12 \n\x0c\x61llow_repeat\x18\x05 \x01(\x08\x42\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12&\n\x12\x65xclude_characters\x18\x06 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"e\n\x12SecretEnginePolicy\x12\x43\n\x0fpassword_policy\x18\x01 \x01(\x0b\x32\x1e.v1.SecretEnginePasswordPolicyB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\x42n\n\x19\x63om.strongdm.api.plumbingB\x1aSecretEnginePolicyPlumbingZ5github.com/strongdm/strongdm-sdk-go/v3/internal/v1;v1b\x06proto3')



_SECRETENGINEPASSWORDPOLICY = DESCRIPTOR.message_types_by_name['SecretEnginePasswordPolicy']
_SECRETENGINEPOLICY = DESCRIPTOR.message_types_by_name['SecretEnginePolicy']
SecretEnginePasswordPolicy = _reflection.GeneratedProtocolMessageType('SecretEnginePasswordPolicy', (_message.Message,), {
  'DESCRIPTOR' : _SECRETENGINEPASSWORDPOLICY,
  '__module__' : 'secret_engine_policy_pb2'
  # @@protoc_insertion_point(class_scope:v1.SecretEnginePasswordPolicy)
  })
_sym_db.RegisterMessage(SecretEnginePasswordPolicy)

SecretEnginePolicy = _reflection.GeneratedProtocolMessageType('SecretEnginePolicy', (_message.Message,), {
  'DESCRIPTOR' : _SECRETENGINEPOLICY,
  '__module__' : 'secret_engine_policy_pb2'
  # @@protoc_insertion_point(class_scope:v1.SecretEnginePolicy)
  })
_sym_db.RegisterMessage(SecretEnginePolicy)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031com.strongdm.api.plumbingB\032SecretEnginePolicyPlumbingZ5github.com/strongdm/strongdm-sdk-go/v3/internal/v1;v1'
  _SECRETENGINEPASSWORDPOLICY.fields_by_name['length']._options = None
  _SECRETENGINEPASSWORDPOLICY.fields_by_name['length']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _SECRETENGINEPASSWORDPOLICY.fields_by_name['exclude_upper_case']._options = None
  _SECRETENGINEPASSWORDPOLICY.fields_by_name['exclude_upper_case']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _SECRETENGINEPASSWORDPOLICY.fields_by_name['num_digits']._options = None
  _SECRETENGINEPASSWORDPOLICY.fields_by_name['num_digits']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _SECRETENGINEPASSWORDPOLICY.fields_by_name['num_symbols']._options = None
  _SECRETENGINEPASSWORDPOLICY.fields_by_name['num_symbols']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _SECRETENGINEPASSWORDPOLICY.fields_by_name['allow_repeat']._options = None
  _SECRETENGINEPASSWORDPOLICY.fields_by_name['allow_repeat']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _SECRETENGINEPASSWORDPOLICY.fields_by_name['exclude_characters']._options = None
  _SECRETENGINEPASSWORDPOLICY.fields_by_name['exclude_characters']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _SECRETENGINEPASSWORDPOLICY._options = None
  _SECRETENGINEPASSWORDPOLICY._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _SECRETENGINEPOLICY.fields_by_name['password_policy']._options = None
  _SECRETENGINEPOLICY.fields_by_name['password_policy']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _SECRETENGINEPOLICY._options = None
  _SECRETENGINEPOLICY._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _SECRETENGINEPASSWORDPOLICY._serialized_start=50
  _SECRETENGINEPASSWORDPOLICY._serialized_end=297
  _SECRETENGINEPOLICY._serialized_start=299
  _SECRETENGINEPOLICY._serialized_end=400
# @@protoc_insertion_point(module_scope)
