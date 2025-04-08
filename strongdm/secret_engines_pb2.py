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
# source: secret_engines.proto
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
from . import secret_stores_pb2 as secret__stores__pb2
from . import secret_engine_types_pb2 as secret__engine__types__pb2
from . import secret_engine_policy_pb2 as secret__engine__policy__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14secret_engines.proto\x12\x02v1\x1a\roptions.proto\x1a\nspec.proto\x1a\x13secret_stores.proto\x1a\x19secret_engine_types.proto\x1a\x1asecret_engine_policy.proto\"h\n\x17SecretEngineListRequest\x12%\n\x04meta\x18\x01 \x01(\x0b\x32\x17.v1.ListRequestMetadata\x12\x1a\n\x06\x66ilter\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"\xdd\x01\n\x18SecretEngineListResponse\x12&\n\x04meta\x18\x01 \x01(\x0b\x32\x18.v1.ListResponseMetadata\x12\x34\n\x0esecret_engines\x18\x02 \x03(\x0b\x32\x10.v1.SecretEngineB\n\xf2\xf8\xb3\x07\x05\xb8\xf3\xb3\x07\x01\x12W\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB,\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"b\n\x16SecretEngineGetRequest\x12$\n\x04meta\x18\x01 \x01(\x0b\x32\x16.v1.GetRequestMetadata\x12\x16\n\x02id\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"\xe6\x01\n\x17SecretEngineGetResponse\x12\x31\n\x04meta\x18\x01 \x01(\x0b\x32\x17.v1.GetResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x33\n\rsecret_engine\x18\x02 \x01(\x0b\x32\x10.v1.SecretEngineB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12W\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB,\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"\x85\x01\n\x19SecretEngineCreateRequest\x12\'\n\x04meta\x18\x01 \x01(\x0b\x32\x19.v1.CreateRequestMetadata\x12\x33\n\rsecret_engine\x18\x02 \x01(\x0b\x32\x10.v1.SecretEngineB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"\xec\x01\n\x1aSecretEngineCreateResponse\x12\x34\n\x04meta\x18\x01 \x01(\x0b\x32\x1a.v1.CreateResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x33\n\rsecret_engine\x18\x02 \x01(\x0b\x32\x10.v1.SecretEngineB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12W\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB,\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"\x91\x01\n\x19SecretEngineUpdateRequest\x12\'\n\x04meta\x18\x01 \x01(\x0b\x32\x19.v1.UpdateRequestMetadata\x12\n\n\x02id\x18\x02 \x01(\t\x12\x33\n\rsecret_engine\x18\x03 \x01(\x0b\x32\x10.v1.SecretEngineB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"\xec\x01\n\x1aSecretEngineUpdateResponse\x12\x34\n\x04meta\x18\x01 \x01(\x0b\x32\x1a.v1.UpdateResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x33\n\rsecret_engine\x18\x02 \x01(\x0b\x32\x10.v1.SecretEngineB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12W\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB,\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"h\n\x19SecretEngineDeleteRequest\x12\'\n\x04meta\x18\x01 \x01(\x0b\x32\x19.v1.UpdateRequestMetadata\x12\x16\n\x02id\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"\xab\x01\n\x1aSecretEngineDeleteResponse\x12(\n\x04meta\x18\x01 \x01(\x0b\x32\x1a.v1.DeleteResponseMetadata\x12W\n\nrate_limit\x18\x02 \x01(\x0b\x32\x15.v1.RateLimitMetadataB,\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"p\n\x13GenerateKeysRequest\x12\'\n\x04meta\x18\x01 \x01(\x0b\x32\x19.v1.UpdateRequestMetadata\x12$\n\x10secret_engine_id\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"\xa5\x01\n\x14GenerateKeysResponse\x12(\n\x04meta\x18\x01 \x01(\x0b\x32\x1a.v1.UpdateResponseMetadata\x12W\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB,\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"l\n\x12HealthcheckRequest\x12$\n\x04meta\x18\x01 \x01(\x0b\x32\x16.v1.GetRequestMetadata\x12$\n\x10secret_engine_id\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"X\n\x11HealthcheckStatus\x12\x1b\n\x07node_id\x18\x01 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x1a\n\x06status\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"\xd3\x01\n\x13HealthcheckResponse\x12$\n\x04meta\x18\x01 \x01(\x0b\x32\x16.v1.GetRequestMetadata\x12W\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB,\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway\x12\x31\n\x06status\x18\x02 \x03(\x0b\x32\x15.v1.HealthcheckStatusB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"\xad\x01\n\x19SecretEngineRotateRequest\x12\'\n\x04meta\x18\x01 \x01(\x0b\x32\x19.v1.UpdateRequestMetadata\x12\x16\n\x02id\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x43\n\x0fpassword_policy\x18\x03 \x01(\x0b\x32\x1e.v1.SecretEnginePasswordPolicyB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"\xaa\x01\n\x1aSecretEngineRotateResponse\x12\'\n\x04meta\x18\x01 \x01(\x0b\x32\x19.v1.UpdateRequestMetadata\x12W\n\nrate_limit\x18\x02 \x01(\x0b\x32\x15.v1.RateLimitMetadataB,\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\x32\xa2\t\n\rSecretEngines\x12l\n\x04List\x12\x1b.v1.SecretEngineListRequest\x1a\x1c.v1.SecretEngineListResponse\")\x82\xf9\xb3\x07\x08\xa2\xf3\xb3\x07\x03get\x82\xf9\xb3\x07\x17\xaa\xf3\xb3\x07\x12/v1/secret-engines\x12n\n\x03Get\x12\x1a.v1.SecretEngineGetRequest\x1a\x1b.v1.SecretEngineGetResponse\".\x82\xf9\xb3\x07\x08\xa2\xf3\xb3\x07\x03get\x82\xf9\xb3\x07\x1c\xaa\xf3\xb3\x07\x17/v1/secret-engines/{id}\x12s\n\x06\x43reate\x12\x1d.v1.SecretEngineCreateRequest\x1a\x1e.v1.SecretEngineCreateResponse\"*\x82\xf9\xb3\x07\t\xa2\xf3\xb3\x07\x04post\x82\xf9\xb3\x07\x17\xaa\xf3\xb3\x07\x12/v1/secret-engines\x12w\n\x06Update\x12\x1d.v1.SecretEngineUpdateRequest\x1a\x1e.v1.SecretEngineUpdateResponse\".\x82\xf9\xb3\x07\x08\xa2\xf3\xb3\x07\x03put\x82\xf9\xb3\x07\x1c\xaa\xf3\xb3\x07\x17/v1/secret-engines/{id}\x12z\n\x06\x44\x65lete\x12\x1d.v1.SecretEngineDeleteRequest\x1a\x1e.v1.SecretEngineDeleteResponse\"1\x82\xf9\xb3\x07\x0b\xa2\xf3\xb3\x07\x06\x64\x65lete\x82\xf9\xb3\x07\x1c\xaa\xf3\xb3\x07\x17/v1/secret-engines/{id}\x12~\n\x10ListSecretStores\x12\x1a.v1.SecretStoreListRequest\x1a\x1b.v1.SecretStoreListResponse\"1\x82\xf9\xb3\x07\x08\xa2\xf3\xb3\x07\x03get\x82\xf9\xb3\x07\x1f\xaa\xf3\xb3\x07\x1a/v1/secret-engines-stores/\x12\x8d\x01\n\x0cGenerateKeys\x12\x17.v1.GenerateKeysRequest\x1a\x18.v1.GenerateKeysResponse\"J\x82\xf9\xb3\x07\x08\xa2\xf3\xb3\x07\x03put\x82\xf9\xb3\x07\x38\xaa\xf3\xb3\x07\x33/v1/secret-engines/{secret_engine_id}/generate-keys\x12\x88\x01\n\x0bHealthcheck\x12\x16.v1.HealthcheckRequest\x1a\x17.v1.HealthcheckResponse\"H\x82\xf9\xb3\x07\x08\xa2\xf3\xb3\x07\x03put\x82\xf9\xb3\x07\x36\xaa\xf3\xb3\x07\x31/v1/secret-engines/{secret_engine_id}/healthcheck\x12~\n\x06Rotate\x12\x1d.v1.SecretEngineRotateRequest\x1a\x1e.v1.SecretEngineRotateResponse\"5\x82\xf9\xb3\x07\x08\xa2\xf3\xb3\x07\x03put\x82\xf9\xb3\x07#\xaa\xf3\xb3\x07\x1e/v1/secret-engines/{id}/rotate\x1a.\xca\xf9\xb3\x07\x11\xc2\xf9\xb3\x07\x0cSecretEngine\xca\xf9\xb3\x07\t\xd2\xf9\xb3\x07\x04\x65ng-\xca\xf9\xb3\x07\x05\xd8\xf9\xb3\x07\x01\x42i\n\x19\x63om.strongdm.api.plumbingB\x15SecretEnginesPlumbingZ5github.com/strongdm/strongdm-sdk-go/v3/internal/v1;v1b\x06proto3')



_SECRETENGINELISTREQUEST = DESCRIPTOR.message_types_by_name['SecretEngineListRequest']
_SECRETENGINELISTRESPONSE = DESCRIPTOR.message_types_by_name['SecretEngineListResponse']
_SECRETENGINEGETREQUEST = DESCRIPTOR.message_types_by_name['SecretEngineGetRequest']
_SECRETENGINEGETRESPONSE = DESCRIPTOR.message_types_by_name['SecretEngineGetResponse']
_SECRETENGINECREATEREQUEST = DESCRIPTOR.message_types_by_name['SecretEngineCreateRequest']
_SECRETENGINECREATERESPONSE = DESCRIPTOR.message_types_by_name['SecretEngineCreateResponse']
_SECRETENGINEUPDATEREQUEST = DESCRIPTOR.message_types_by_name['SecretEngineUpdateRequest']
_SECRETENGINEUPDATERESPONSE = DESCRIPTOR.message_types_by_name['SecretEngineUpdateResponse']
_SECRETENGINEDELETEREQUEST = DESCRIPTOR.message_types_by_name['SecretEngineDeleteRequest']
_SECRETENGINEDELETERESPONSE = DESCRIPTOR.message_types_by_name['SecretEngineDeleteResponse']
_GENERATEKEYSREQUEST = DESCRIPTOR.message_types_by_name['GenerateKeysRequest']
_GENERATEKEYSRESPONSE = DESCRIPTOR.message_types_by_name['GenerateKeysResponse']
_HEALTHCHECKREQUEST = DESCRIPTOR.message_types_by_name['HealthcheckRequest']
_HEALTHCHECKSTATUS = DESCRIPTOR.message_types_by_name['HealthcheckStatus']
_HEALTHCHECKRESPONSE = DESCRIPTOR.message_types_by_name['HealthcheckResponse']
_SECRETENGINEROTATEREQUEST = DESCRIPTOR.message_types_by_name['SecretEngineRotateRequest']
_SECRETENGINEROTATERESPONSE = DESCRIPTOR.message_types_by_name['SecretEngineRotateResponse']
SecretEngineListRequest = _reflection.GeneratedProtocolMessageType('SecretEngineListRequest', (_message.Message,), {
  'DESCRIPTOR' : _SECRETENGINELISTREQUEST,
  '__module__' : 'secret_engines_pb2'
  # @@protoc_insertion_point(class_scope:v1.SecretEngineListRequest)
  })
_sym_db.RegisterMessage(SecretEngineListRequest)

SecretEngineListResponse = _reflection.GeneratedProtocolMessageType('SecretEngineListResponse', (_message.Message,), {
  'DESCRIPTOR' : _SECRETENGINELISTRESPONSE,
  '__module__' : 'secret_engines_pb2'
  # @@protoc_insertion_point(class_scope:v1.SecretEngineListResponse)
  })
_sym_db.RegisterMessage(SecretEngineListResponse)

SecretEngineGetRequest = _reflection.GeneratedProtocolMessageType('SecretEngineGetRequest', (_message.Message,), {
  'DESCRIPTOR' : _SECRETENGINEGETREQUEST,
  '__module__' : 'secret_engines_pb2'
  # @@protoc_insertion_point(class_scope:v1.SecretEngineGetRequest)
  })
_sym_db.RegisterMessage(SecretEngineGetRequest)

SecretEngineGetResponse = _reflection.GeneratedProtocolMessageType('SecretEngineGetResponse', (_message.Message,), {
  'DESCRIPTOR' : _SECRETENGINEGETRESPONSE,
  '__module__' : 'secret_engines_pb2'
  # @@protoc_insertion_point(class_scope:v1.SecretEngineGetResponse)
  })
_sym_db.RegisterMessage(SecretEngineGetResponse)

SecretEngineCreateRequest = _reflection.GeneratedProtocolMessageType('SecretEngineCreateRequest', (_message.Message,), {
  'DESCRIPTOR' : _SECRETENGINECREATEREQUEST,
  '__module__' : 'secret_engines_pb2'
  # @@protoc_insertion_point(class_scope:v1.SecretEngineCreateRequest)
  })
_sym_db.RegisterMessage(SecretEngineCreateRequest)

SecretEngineCreateResponse = _reflection.GeneratedProtocolMessageType('SecretEngineCreateResponse', (_message.Message,), {
  'DESCRIPTOR' : _SECRETENGINECREATERESPONSE,
  '__module__' : 'secret_engines_pb2'
  # @@protoc_insertion_point(class_scope:v1.SecretEngineCreateResponse)
  })
_sym_db.RegisterMessage(SecretEngineCreateResponse)

SecretEngineUpdateRequest = _reflection.GeneratedProtocolMessageType('SecretEngineUpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _SECRETENGINEUPDATEREQUEST,
  '__module__' : 'secret_engines_pb2'
  # @@protoc_insertion_point(class_scope:v1.SecretEngineUpdateRequest)
  })
_sym_db.RegisterMessage(SecretEngineUpdateRequest)

SecretEngineUpdateResponse = _reflection.GeneratedProtocolMessageType('SecretEngineUpdateResponse', (_message.Message,), {
  'DESCRIPTOR' : _SECRETENGINEUPDATERESPONSE,
  '__module__' : 'secret_engines_pb2'
  # @@protoc_insertion_point(class_scope:v1.SecretEngineUpdateResponse)
  })
_sym_db.RegisterMessage(SecretEngineUpdateResponse)

SecretEngineDeleteRequest = _reflection.GeneratedProtocolMessageType('SecretEngineDeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _SECRETENGINEDELETEREQUEST,
  '__module__' : 'secret_engines_pb2'
  # @@protoc_insertion_point(class_scope:v1.SecretEngineDeleteRequest)
  })
_sym_db.RegisterMessage(SecretEngineDeleteRequest)

SecretEngineDeleteResponse = _reflection.GeneratedProtocolMessageType('SecretEngineDeleteResponse', (_message.Message,), {
  'DESCRIPTOR' : _SECRETENGINEDELETERESPONSE,
  '__module__' : 'secret_engines_pb2'
  # @@protoc_insertion_point(class_scope:v1.SecretEngineDeleteResponse)
  })
_sym_db.RegisterMessage(SecretEngineDeleteResponse)

GenerateKeysRequest = _reflection.GeneratedProtocolMessageType('GenerateKeysRequest', (_message.Message,), {
  'DESCRIPTOR' : _GENERATEKEYSREQUEST,
  '__module__' : 'secret_engines_pb2'
  # @@protoc_insertion_point(class_scope:v1.GenerateKeysRequest)
  })
_sym_db.RegisterMessage(GenerateKeysRequest)

GenerateKeysResponse = _reflection.GeneratedProtocolMessageType('GenerateKeysResponse', (_message.Message,), {
  'DESCRIPTOR' : _GENERATEKEYSRESPONSE,
  '__module__' : 'secret_engines_pb2'
  # @@protoc_insertion_point(class_scope:v1.GenerateKeysResponse)
  })
_sym_db.RegisterMessage(GenerateKeysResponse)

HealthcheckRequest = _reflection.GeneratedProtocolMessageType('HealthcheckRequest', (_message.Message,), {
  'DESCRIPTOR' : _HEALTHCHECKREQUEST,
  '__module__' : 'secret_engines_pb2'
  # @@protoc_insertion_point(class_scope:v1.HealthcheckRequest)
  })
_sym_db.RegisterMessage(HealthcheckRequest)

HealthcheckStatus = _reflection.GeneratedProtocolMessageType('HealthcheckStatus', (_message.Message,), {
  'DESCRIPTOR' : _HEALTHCHECKSTATUS,
  '__module__' : 'secret_engines_pb2'
  # @@protoc_insertion_point(class_scope:v1.HealthcheckStatus)
  })
_sym_db.RegisterMessage(HealthcheckStatus)

HealthcheckResponse = _reflection.GeneratedProtocolMessageType('HealthcheckResponse', (_message.Message,), {
  'DESCRIPTOR' : _HEALTHCHECKRESPONSE,
  '__module__' : 'secret_engines_pb2'
  # @@protoc_insertion_point(class_scope:v1.HealthcheckResponse)
  })
_sym_db.RegisterMessage(HealthcheckResponse)

SecretEngineRotateRequest = _reflection.GeneratedProtocolMessageType('SecretEngineRotateRequest', (_message.Message,), {
  'DESCRIPTOR' : _SECRETENGINEROTATEREQUEST,
  '__module__' : 'secret_engines_pb2'
  # @@protoc_insertion_point(class_scope:v1.SecretEngineRotateRequest)
  })
_sym_db.RegisterMessage(SecretEngineRotateRequest)

SecretEngineRotateResponse = _reflection.GeneratedProtocolMessageType('SecretEngineRotateResponse', (_message.Message,), {
  'DESCRIPTOR' : _SECRETENGINEROTATERESPONSE,
  '__module__' : 'secret_engines_pb2'
  # @@protoc_insertion_point(class_scope:v1.SecretEngineRotateResponse)
  })
_sym_db.RegisterMessage(SecretEngineRotateResponse)

_SECRETENGINES = DESCRIPTOR.services_by_name['SecretEngines']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031com.strongdm.api.plumbingB\025SecretEnginesPlumbingZ5github.com/strongdm/strongdm-sdk-go/v3/internal/v1;v1'
  _SECRETENGINELISTREQUEST.fields_by_name['filter']._options = None
  _SECRETENGINELISTREQUEST.fields_by_name['filter']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _SECRETENGINELISTREQUEST._options = None
  _SECRETENGINELISTREQUEST._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _SECRETENGINELISTRESPONSE.fields_by_name['secret_engines']._options = None
  _SECRETENGINELISTRESPONSE.fields_by_name['secret_engines']._serialized_options = b'\362\370\263\007\005\270\363\263\007\001'
  _SECRETENGINELISTRESPONSE.fields_by_name['rate_limit']._options = None
  _SECRETENGINELISTRESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\022\262\364\263\007\r!json_gateway'
  _SECRETENGINELISTRESPONSE._options = None
  _SECRETENGINELISTRESPONSE._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _SECRETENGINEGETREQUEST.fields_by_name['id']._options = None
  _SECRETENGINEGETREQUEST.fields_by_name['id']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _SECRETENGINEGETREQUEST._options = None
  _SECRETENGINEGETREQUEST._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _SECRETENGINEGETRESPONSE.fields_by_name['meta']._options = None
  _SECRETENGINEGETRESPONSE.fields_by_name['meta']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _SECRETENGINEGETRESPONSE.fields_by_name['secret_engine']._options = None
  _SECRETENGINEGETRESPONSE.fields_by_name['secret_engine']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _SECRETENGINEGETRESPONSE.fields_by_name['rate_limit']._options = None
  _SECRETENGINEGETRESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\022\262\364\263\007\r!json_gateway'
  _SECRETENGINEGETRESPONSE._options = None
  _SECRETENGINEGETRESPONSE._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _SECRETENGINECREATEREQUEST.fields_by_name['secret_engine']._options = None
  _SECRETENGINECREATEREQUEST.fields_by_name['secret_engine']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _SECRETENGINECREATEREQUEST._options = None
  _SECRETENGINECREATEREQUEST._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _SECRETENGINECREATERESPONSE.fields_by_name['meta']._options = None
  _SECRETENGINECREATERESPONSE.fields_by_name['meta']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _SECRETENGINECREATERESPONSE.fields_by_name['secret_engine']._options = None
  _SECRETENGINECREATERESPONSE.fields_by_name['secret_engine']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _SECRETENGINECREATERESPONSE.fields_by_name['rate_limit']._options = None
  _SECRETENGINECREATERESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\022\262\364\263\007\r!json_gateway'
  _SECRETENGINECREATERESPONSE._options = None
  _SECRETENGINECREATERESPONSE._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _SECRETENGINEUPDATEREQUEST.fields_by_name['secret_engine']._options = None
  _SECRETENGINEUPDATEREQUEST.fields_by_name['secret_engine']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _SECRETENGINEUPDATEREQUEST._options = None
  _SECRETENGINEUPDATEREQUEST._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _SECRETENGINEUPDATERESPONSE.fields_by_name['meta']._options = None
  _SECRETENGINEUPDATERESPONSE.fields_by_name['meta']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _SECRETENGINEUPDATERESPONSE.fields_by_name['secret_engine']._options = None
  _SECRETENGINEUPDATERESPONSE.fields_by_name['secret_engine']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _SECRETENGINEUPDATERESPONSE.fields_by_name['rate_limit']._options = None
  _SECRETENGINEUPDATERESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\022\262\364\263\007\r!json_gateway'
  _SECRETENGINEUPDATERESPONSE._options = None
  _SECRETENGINEUPDATERESPONSE._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _SECRETENGINEDELETEREQUEST.fields_by_name['id']._options = None
  _SECRETENGINEDELETEREQUEST.fields_by_name['id']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _SECRETENGINEDELETEREQUEST._options = None
  _SECRETENGINEDELETEREQUEST._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _SECRETENGINEDELETERESPONSE.fields_by_name['rate_limit']._options = None
  _SECRETENGINEDELETERESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\022\262\364\263\007\r!json_gateway'
  _SECRETENGINEDELETERESPONSE._options = None
  _SECRETENGINEDELETERESPONSE._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _GENERATEKEYSREQUEST.fields_by_name['secret_engine_id']._options = None
  _GENERATEKEYSREQUEST.fields_by_name['secret_engine_id']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _GENERATEKEYSREQUEST._options = None
  _GENERATEKEYSREQUEST._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _GENERATEKEYSRESPONSE.fields_by_name['rate_limit']._options = None
  _GENERATEKEYSRESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\022\262\364\263\007\r!json_gateway'
  _GENERATEKEYSRESPONSE._options = None
  _GENERATEKEYSRESPONSE._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _HEALTHCHECKREQUEST.fields_by_name['secret_engine_id']._options = None
  _HEALTHCHECKREQUEST.fields_by_name['secret_engine_id']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _HEALTHCHECKREQUEST._options = None
  _HEALTHCHECKREQUEST._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _HEALTHCHECKSTATUS.fields_by_name['node_id']._options = None
  _HEALTHCHECKSTATUS.fields_by_name['node_id']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _HEALTHCHECKSTATUS.fields_by_name['status']._options = None
  _HEALTHCHECKSTATUS.fields_by_name['status']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _HEALTHCHECKSTATUS._options = None
  _HEALTHCHECKSTATUS._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _HEALTHCHECKRESPONSE.fields_by_name['rate_limit']._options = None
  _HEALTHCHECKRESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\022\262\364\263\007\r!json_gateway'
  _HEALTHCHECKRESPONSE.fields_by_name['status']._options = None
  _HEALTHCHECKRESPONSE.fields_by_name['status']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _HEALTHCHECKRESPONSE._options = None
  _HEALTHCHECKRESPONSE._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _SECRETENGINEROTATEREQUEST.fields_by_name['id']._options = None
  _SECRETENGINEROTATEREQUEST.fields_by_name['id']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _SECRETENGINEROTATEREQUEST.fields_by_name['password_policy']._options = None
  _SECRETENGINEROTATEREQUEST.fields_by_name['password_policy']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _SECRETENGINEROTATEREQUEST._options = None
  _SECRETENGINEROTATEREQUEST._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _SECRETENGINEROTATERESPONSE.fields_by_name['rate_limit']._options = None
  _SECRETENGINEROTATERESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\022\262\364\263\007\r!json_gateway'
  _SECRETENGINEROTATERESPONSE._options = None
  _SECRETENGINEROTATERESPONSE._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _SECRETENGINES._options = None
  _SECRETENGINES._serialized_options = b'\312\371\263\007\021\302\371\263\007\014SecretEngine\312\371\263\007\t\322\371\263\007\004eng-\312\371\263\007\005\330\371\263\007\001'
  _SECRETENGINES.methods_by_name['List']._options = None
  _SECRETENGINES.methods_by_name['List']._serialized_options = b'\202\371\263\007\010\242\363\263\007\003get\202\371\263\007\027\252\363\263\007\022/v1/secret-engines'
  _SECRETENGINES.methods_by_name['Get']._options = None
  _SECRETENGINES.methods_by_name['Get']._serialized_options = b'\202\371\263\007\010\242\363\263\007\003get\202\371\263\007\034\252\363\263\007\027/v1/secret-engines/{id}'
  _SECRETENGINES.methods_by_name['Create']._options = None
  _SECRETENGINES.methods_by_name['Create']._serialized_options = b'\202\371\263\007\t\242\363\263\007\004post\202\371\263\007\027\252\363\263\007\022/v1/secret-engines'
  _SECRETENGINES.methods_by_name['Update']._options = None
  _SECRETENGINES.methods_by_name['Update']._serialized_options = b'\202\371\263\007\010\242\363\263\007\003put\202\371\263\007\034\252\363\263\007\027/v1/secret-engines/{id}'
  _SECRETENGINES.methods_by_name['Delete']._options = None
  _SECRETENGINES.methods_by_name['Delete']._serialized_options = b'\202\371\263\007\013\242\363\263\007\006delete\202\371\263\007\034\252\363\263\007\027/v1/secret-engines/{id}'
  _SECRETENGINES.methods_by_name['ListSecretStores']._options = None
  _SECRETENGINES.methods_by_name['ListSecretStores']._serialized_options = b'\202\371\263\007\010\242\363\263\007\003get\202\371\263\007\037\252\363\263\007\032/v1/secret-engines-stores/'
  _SECRETENGINES.methods_by_name['GenerateKeys']._options = None
  _SECRETENGINES.methods_by_name['GenerateKeys']._serialized_options = b'\202\371\263\007\010\242\363\263\007\003put\202\371\263\0078\252\363\263\0073/v1/secret-engines/{secret_engine_id}/generate-keys'
  _SECRETENGINES.methods_by_name['Healthcheck']._options = None
  _SECRETENGINES.methods_by_name['Healthcheck']._serialized_options = b'\202\371\263\007\010\242\363\263\007\003put\202\371\263\0076\252\363\263\0071/v1/secret-engines/{secret_engine_id}/healthcheck'
  _SECRETENGINES.methods_by_name['Rotate']._options = None
  _SECRETENGINES.methods_by_name['Rotate']._serialized_options = b'\202\371\263\007\010\242\363\263\007\003put\202\371\263\007#\252\363\263\007\036/v1/secret-engines/{id}/rotate'
  _SECRETENGINELISTREQUEST._serialized_start=131
  _SECRETENGINELISTREQUEST._serialized_end=235
  _SECRETENGINELISTRESPONSE._serialized_start=238
  _SECRETENGINELISTRESPONSE._serialized_end=459
  _SECRETENGINEGETREQUEST._serialized_start=461
  _SECRETENGINEGETREQUEST._serialized_end=559
  _SECRETENGINEGETRESPONSE._serialized_start=562
  _SECRETENGINEGETRESPONSE._serialized_end=792
  _SECRETENGINECREATEREQUEST._serialized_start=795
  _SECRETENGINECREATEREQUEST._serialized_end=928
  _SECRETENGINECREATERESPONSE._serialized_start=931
  _SECRETENGINECREATERESPONSE._serialized_end=1167
  _SECRETENGINEUPDATEREQUEST._serialized_start=1170
  _SECRETENGINEUPDATEREQUEST._serialized_end=1315
  _SECRETENGINEUPDATERESPONSE._serialized_start=1318
  _SECRETENGINEUPDATERESPONSE._serialized_end=1554
  _SECRETENGINEDELETEREQUEST._serialized_start=1556
  _SECRETENGINEDELETEREQUEST._serialized_end=1660
  _SECRETENGINEDELETERESPONSE._serialized_start=1663
  _SECRETENGINEDELETERESPONSE._serialized_end=1834
  _GENERATEKEYSREQUEST._serialized_start=1836
  _GENERATEKEYSREQUEST._serialized_end=1948
  _GENERATEKEYSRESPONSE._serialized_start=1951
  _GENERATEKEYSRESPONSE._serialized_end=2116
  _HEALTHCHECKREQUEST._serialized_start=2118
  _HEALTHCHECKREQUEST._serialized_end=2226
  _HEALTHCHECKSTATUS._serialized_start=2228
  _HEALTHCHECKSTATUS._serialized_end=2316
  _HEALTHCHECKRESPONSE._serialized_start=2319
  _HEALTHCHECKRESPONSE._serialized_end=2530
  _SECRETENGINEROTATEREQUEST._serialized_start=2533
  _SECRETENGINEROTATEREQUEST._serialized_end=2706
  _SECRETENGINEROTATERESPONSE._serialized_start=2709
  _SECRETENGINEROTATERESPONSE._serialized_end=2879
  _SECRETENGINES._serialized_start=2882
  _SECRETENGINES._serialized_end=4068
# @@protoc_insertion_point(module_scope)
