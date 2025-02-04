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
# source: spec.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import options_pb2 as options__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nspec.proto\x12\x02v1\x1a\roptions.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"<\n\x12\x41lreadyExistsError\x12\x1a\n\x06\x65ntity\x18\x01 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:\n\xfa\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x06\"7\n\rNotFoundError\x12\x1a\n\x06\x65ntity\x18\x01 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:\n\xfa\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x05\"\x1d\n\x0f\x42\x61\x64RequestError:\n\xfa\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x03\"!\n\x13\x41uthenticationError:\n\xfa\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x10\"\x1d\n\x0fPermissionError:\n\xfa\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x07\"\x1b\n\rInternalError:\n\xfa\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\r\"u\n\x0eRateLimitError\x12W\n\nrate_limit\x18\x01 \x01(\x0b\x32\x15.v1.RateLimitMetadataB,\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway:\n\xfa\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x08\"G\n\x15\x43reateRequestMetadata\x12.\n\x0c\x66ulfillments\x18\x01 \x01(\x0b\x32\x18.v1.FulfillmentsMetadata\"$\n\x16\x43reateResponseMetadata:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"u\n\x12GetRequestMetadata\x12/\n\x0bsnapshot_at\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\x0c\x66ulfillments\x18\x02 \x01(\x0b\x32\x18.v1.FulfillmentsMetadata\"!\n\x13GetResponseMetadata:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"G\n\x15UpdateRequestMetadata\x12.\n\x0c\x66ulfillments\x18\x01 \x01(\x0b\x32\x18.v1.FulfillmentsMetadata\"$\n\x16UpdateResponseMetadata:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"G\n\x15\x44\x65leteRequestMetadata\x12.\n\x0c\x66ulfillments\x18\x01 \x01(\x0b\x32\x18.v1.FulfillmentsMetadata\"$\n\x16\x44\x65leteResponseMetadata:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"\xb5\x01\n\x13ListRequestMetadata\x12\x0e\n\x06\x63ursor\x18\x01 \x01(\t\x12\x0c\n\x04page\x18\x02 \x01(\x05\x12\r\n\x05limit\x18\x03 \x01(\x05\x12\x10\n\x08order_by\x18\x04 \x01(\t\x12/\n\x0bsnapshot_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\x0c\x66ulfillments\x18\x06 \x01(\x0b\x32\x18.v1.FulfillmentsMetadata\">\n\x14ListResponseMetadata\x12\x13\n\x0bnext_cursor\x18\x01 \x01(\t\x12\x11\n\x05total\x18\x02 \x01(\x05\x42\x02\x18\x01\"\xaf\x01\n\x11RateLimitMetadata\x12\x19\n\x05limit\x18\x01 \x01(\x03\x42\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x1d\n\tremaining\x18\x02 \x01(\x03\x42\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x38\n\x08reset_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x1a\n\x06\x62ucket\x18\x04 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"H\n\x16GenericRequestMetadata\x12.\n\x0c\x66ulfillments\x18\x01 \x01(\x0b\x32\x18.v1.FulfillmentsMetadata\"%\n\x17GenericResponseMetadata:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"=\n\x14RequirementsMetadata\x12%\n\x0crequirements\x18\x01 \x03(\x0b\x32\x0f.v1.Requirement\"=\n\x14\x46ulfillmentsMetadata\x12%\n\x0c\x66ulfillments\x18\x01 \x03(\x0b\x32\x0f.v1.Fulfillment\"*\n\x0bRequirement\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"B\n\x0b\x46ulfillment\x12$\n\x0brequirement\x18\x01 \x01(\x0b\x32\x0f.v1.Requirement\x12\r\n\x05value\x18\x02 \x01(\tBR\n\x19\x63om.strongdm.api.plumbingZ5github.com/strongdm/strongdm-sdk-go/v3/internal/v1;v1b\x06proto3')



_ALREADYEXISTSERROR = DESCRIPTOR.message_types_by_name['AlreadyExistsError']
_NOTFOUNDERROR = DESCRIPTOR.message_types_by_name['NotFoundError']
_BADREQUESTERROR = DESCRIPTOR.message_types_by_name['BadRequestError']
_AUTHENTICATIONERROR = DESCRIPTOR.message_types_by_name['AuthenticationError']
_PERMISSIONERROR = DESCRIPTOR.message_types_by_name['PermissionError']
_INTERNALERROR = DESCRIPTOR.message_types_by_name['InternalError']
_RATELIMITERROR = DESCRIPTOR.message_types_by_name['RateLimitError']
_CREATEREQUESTMETADATA = DESCRIPTOR.message_types_by_name['CreateRequestMetadata']
_CREATERESPONSEMETADATA = DESCRIPTOR.message_types_by_name['CreateResponseMetadata']
_GETREQUESTMETADATA = DESCRIPTOR.message_types_by_name['GetRequestMetadata']
_GETRESPONSEMETADATA = DESCRIPTOR.message_types_by_name['GetResponseMetadata']
_UPDATEREQUESTMETADATA = DESCRIPTOR.message_types_by_name['UpdateRequestMetadata']
_UPDATERESPONSEMETADATA = DESCRIPTOR.message_types_by_name['UpdateResponseMetadata']
_DELETEREQUESTMETADATA = DESCRIPTOR.message_types_by_name['DeleteRequestMetadata']
_DELETERESPONSEMETADATA = DESCRIPTOR.message_types_by_name['DeleteResponseMetadata']
_LISTREQUESTMETADATA = DESCRIPTOR.message_types_by_name['ListRequestMetadata']
_LISTRESPONSEMETADATA = DESCRIPTOR.message_types_by_name['ListResponseMetadata']
_RATELIMITMETADATA = DESCRIPTOR.message_types_by_name['RateLimitMetadata']
_GENERICREQUESTMETADATA = DESCRIPTOR.message_types_by_name['GenericRequestMetadata']
_GENERICRESPONSEMETADATA = DESCRIPTOR.message_types_by_name['GenericResponseMetadata']
_REQUIREMENTSMETADATA = DESCRIPTOR.message_types_by_name['RequirementsMetadata']
_FULFILLMENTSMETADATA = DESCRIPTOR.message_types_by_name['FulfillmentsMetadata']
_REQUIREMENT = DESCRIPTOR.message_types_by_name['Requirement']
_FULFILLMENT = DESCRIPTOR.message_types_by_name['Fulfillment']
AlreadyExistsError = _reflection.GeneratedProtocolMessageType('AlreadyExistsError', (_message.Message,), {
  'DESCRIPTOR' : _ALREADYEXISTSERROR,
  '__module__' : 'spec_pb2'
  # @@protoc_insertion_point(class_scope:v1.AlreadyExistsError)
  })
_sym_db.RegisterMessage(AlreadyExistsError)

NotFoundError = _reflection.GeneratedProtocolMessageType('NotFoundError', (_message.Message,), {
  'DESCRIPTOR' : _NOTFOUNDERROR,
  '__module__' : 'spec_pb2'
  # @@protoc_insertion_point(class_scope:v1.NotFoundError)
  })
_sym_db.RegisterMessage(NotFoundError)

BadRequestError = _reflection.GeneratedProtocolMessageType('BadRequestError', (_message.Message,), {
  'DESCRIPTOR' : _BADREQUESTERROR,
  '__module__' : 'spec_pb2'
  # @@protoc_insertion_point(class_scope:v1.BadRequestError)
  })
_sym_db.RegisterMessage(BadRequestError)

AuthenticationError = _reflection.GeneratedProtocolMessageType('AuthenticationError', (_message.Message,), {
  'DESCRIPTOR' : _AUTHENTICATIONERROR,
  '__module__' : 'spec_pb2'
  # @@protoc_insertion_point(class_scope:v1.AuthenticationError)
  })
_sym_db.RegisterMessage(AuthenticationError)

PermissionError = _reflection.GeneratedProtocolMessageType('PermissionError', (_message.Message,), {
  'DESCRIPTOR' : _PERMISSIONERROR,
  '__module__' : 'spec_pb2'
  # @@protoc_insertion_point(class_scope:v1.PermissionError)
  })
_sym_db.RegisterMessage(PermissionError)

InternalError = _reflection.GeneratedProtocolMessageType('InternalError', (_message.Message,), {
  'DESCRIPTOR' : _INTERNALERROR,
  '__module__' : 'spec_pb2'
  # @@protoc_insertion_point(class_scope:v1.InternalError)
  })
_sym_db.RegisterMessage(InternalError)

RateLimitError = _reflection.GeneratedProtocolMessageType('RateLimitError', (_message.Message,), {
  'DESCRIPTOR' : _RATELIMITERROR,
  '__module__' : 'spec_pb2'
  # @@protoc_insertion_point(class_scope:v1.RateLimitError)
  })
_sym_db.RegisterMessage(RateLimitError)

CreateRequestMetadata = _reflection.GeneratedProtocolMessageType('CreateRequestMetadata', (_message.Message,), {
  'DESCRIPTOR' : _CREATEREQUESTMETADATA,
  '__module__' : 'spec_pb2'
  # @@protoc_insertion_point(class_scope:v1.CreateRequestMetadata)
  })
_sym_db.RegisterMessage(CreateRequestMetadata)

CreateResponseMetadata = _reflection.GeneratedProtocolMessageType('CreateResponseMetadata', (_message.Message,), {
  'DESCRIPTOR' : _CREATERESPONSEMETADATA,
  '__module__' : 'spec_pb2'
  # @@protoc_insertion_point(class_scope:v1.CreateResponseMetadata)
  })
_sym_db.RegisterMessage(CreateResponseMetadata)

GetRequestMetadata = _reflection.GeneratedProtocolMessageType('GetRequestMetadata', (_message.Message,), {
  'DESCRIPTOR' : _GETREQUESTMETADATA,
  '__module__' : 'spec_pb2'
  # @@protoc_insertion_point(class_scope:v1.GetRequestMetadata)
  })
_sym_db.RegisterMessage(GetRequestMetadata)

GetResponseMetadata = _reflection.GeneratedProtocolMessageType('GetResponseMetadata', (_message.Message,), {
  'DESCRIPTOR' : _GETRESPONSEMETADATA,
  '__module__' : 'spec_pb2'
  # @@protoc_insertion_point(class_scope:v1.GetResponseMetadata)
  })
_sym_db.RegisterMessage(GetResponseMetadata)

UpdateRequestMetadata = _reflection.GeneratedProtocolMessageType('UpdateRequestMetadata', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEREQUESTMETADATA,
  '__module__' : 'spec_pb2'
  # @@protoc_insertion_point(class_scope:v1.UpdateRequestMetadata)
  })
_sym_db.RegisterMessage(UpdateRequestMetadata)

UpdateResponseMetadata = _reflection.GeneratedProtocolMessageType('UpdateResponseMetadata', (_message.Message,), {
  'DESCRIPTOR' : _UPDATERESPONSEMETADATA,
  '__module__' : 'spec_pb2'
  # @@protoc_insertion_point(class_scope:v1.UpdateResponseMetadata)
  })
_sym_db.RegisterMessage(UpdateResponseMetadata)

DeleteRequestMetadata = _reflection.GeneratedProtocolMessageType('DeleteRequestMetadata', (_message.Message,), {
  'DESCRIPTOR' : _DELETEREQUESTMETADATA,
  '__module__' : 'spec_pb2'
  # @@protoc_insertion_point(class_scope:v1.DeleteRequestMetadata)
  })
_sym_db.RegisterMessage(DeleteRequestMetadata)

DeleteResponseMetadata = _reflection.GeneratedProtocolMessageType('DeleteResponseMetadata', (_message.Message,), {
  'DESCRIPTOR' : _DELETERESPONSEMETADATA,
  '__module__' : 'spec_pb2'
  # @@protoc_insertion_point(class_scope:v1.DeleteResponseMetadata)
  })
_sym_db.RegisterMessage(DeleteResponseMetadata)

ListRequestMetadata = _reflection.GeneratedProtocolMessageType('ListRequestMetadata', (_message.Message,), {
  'DESCRIPTOR' : _LISTREQUESTMETADATA,
  '__module__' : 'spec_pb2'
  # @@protoc_insertion_point(class_scope:v1.ListRequestMetadata)
  })
_sym_db.RegisterMessage(ListRequestMetadata)

ListResponseMetadata = _reflection.GeneratedProtocolMessageType('ListResponseMetadata', (_message.Message,), {
  'DESCRIPTOR' : _LISTRESPONSEMETADATA,
  '__module__' : 'spec_pb2'
  # @@protoc_insertion_point(class_scope:v1.ListResponseMetadata)
  })
_sym_db.RegisterMessage(ListResponseMetadata)

RateLimitMetadata = _reflection.GeneratedProtocolMessageType('RateLimitMetadata', (_message.Message,), {
  'DESCRIPTOR' : _RATELIMITMETADATA,
  '__module__' : 'spec_pb2'
  # @@protoc_insertion_point(class_scope:v1.RateLimitMetadata)
  })
_sym_db.RegisterMessage(RateLimitMetadata)

GenericRequestMetadata = _reflection.GeneratedProtocolMessageType('GenericRequestMetadata', (_message.Message,), {
  'DESCRIPTOR' : _GENERICREQUESTMETADATA,
  '__module__' : 'spec_pb2'
  # @@protoc_insertion_point(class_scope:v1.GenericRequestMetadata)
  })
_sym_db.RegisterMessage(GenericRequestMetadata)

GenericResponseMetadata = _reflection.GeneratedProtocolMessageType('GenericResponseMetadata', (_message.Message,), {
  'DESCRIPTOR' : _GENERICRESPONSEMETADATA,
  '__module__' : 'spec_pb2'
  # @@protoc_insertion_point(class_scope:v1.GenericResponseMetadata)
  })
_sym_db.RegisterMessage(GenericResponseMetadata)

RequirementsMetadata = _reflection.GeneratedProtocolMessageType('RequirementsMetadata', (_message.Message,), {
  'DESCRIPTOR' : _REQUIREMENTSMETADATA,
  '__module__' : 'spec_pb2'
  # @@protoc_insertion_point(class_scope:v1.RequirementsMetadata)
  })
_sym_db.RegisterMessage(RequirementsMetadata)

FulfillmentsMetadata = _reflection.GeneratedProtocolMessageType('FulfillmentsMetadata', (_message.Message,), {
  'DESCRIPTOR' : _FULFILLMENTSMETADATA,
  '__module__' : 'spec_pb2'
  # @@protoc_insertion_point(class_scope:v1.FulfillmentsMetadata)
  })
_sym_db.RegisterMessage(FulfillmentsMetadata)

Requirement = _reflection.GeneratedProtocolMessageType('Requirement', (_message.Message,), {
  'DESCRIPTOR' : _REQUIREMENT,
  '__module__' : 'spec_pb2'
  # @@protoc_insertion_point(class_scope:v1.Requirement)
  })
_sym_db.RegisterMessage(Requirement)

Fulfillment = _reflection.GeneratedProtocolMessageType('Fulfillment', (_message.Message,), {
  'DESCRIPTOR' : _FULFILLMENT,
  '__module__' : 'spec_pb2'
  # @@protoc_insertion_point(class_scope:v1.Fulfillment)
  })
_sym_db.RegisterMessage(Fulfillment)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031com.strongdm.api.plumbingZ5github.com/strongdm/strongdm-sdk-go/v3/internal/v1;v1'
  _ALREADYEXISTSERROR.fields_by_name['entity']._options = None
  _ALREADYEXISTSERROR.fields_by_name['entity']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ALREADYEXISTSERROR._options = None
  _ALREADYEXISTSERROR._serialized_options = b'\372\370\263\007\005\260\363\263\007\006'
  _NOTFOUNDERROR.fields_by_name['entity']._options = None
  _NOTFOUNDERROR.fields_by_name['entity']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _NOTFOUNDERROR._options = None
  _NOTFOUNDERROR._serialized_options = b'\372\370\263\007\005\260\363\263\007\005'
  _BADREQUESTERROR._options = None
  _BADREQUESTERROR._serialized_options = b'\372\370\263\007\005\260\363\263\007\003'
  _AUTHENTICATIONERROR._options = None
  _AUTHENTICATIONERROR._serialized_options = b'\372\370\263\007\005\260\363\263\007\020'
  _PERMISSIONERROR._options = None
  _PERMISSIONERROR._serialized_options = b'\372\370\263\007\005\260\363\263\007\007'
  _INTERNALERROR._options = None
  _INTERNALERROR._serialized_options = b'\372\370\263\007\005\260\363\263\007\r'
  _RATELIMITERROR.fields_by_name['rate_limit']._options = None
  _RATELIMITERROR.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\022\262\364\263\007\r!json_gateway'
  _RATELIMITERROR._options = None
  _RATELIMITERROR._serialized_options = b'\372\370\263\007\005\260\363\263\007\010'
  _CREATERESPONSEMETADATA._options = None
  _CREATERESPONSEMETADATA._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _GETRESPONSEMETADATA._options = None
  _GETRESPONSEMETADATA._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _UPDATERESPONSEMETADATA._options = None
  _UPDATERESPONSEMETADATA._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _DELETERESPONSEMETADATA._options = None
  _DELETERESPONSEMETADATA._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _LISTRESPONSEMETADATA.fields_by_name['total']._options = None
  _LISTRESPONSEMETADATA.fields_by_name['total']._serialized_options = b'\030\001'
  _RATELIMITMETADATA.fields_by_name['limit']._options = None
  _RATELIMITMETADATA.fields_by_name['limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _RATELIMITMETADATA.fields_by_name['remaining']._options = None
  _RATELIMITMETADATA.fields_by_name['remaining']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _RATELIMITMETADATA.fields_by_name['reset_at']._options = None
  _RATELIMITMETADATA.fields_by_name['reset_at']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _RATELIMITMETADATA.fields_by_name['bucket']._options = None
  _RATELIMITMETADATA.fields_by_name['bucket']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _RATELIMITMETADATA._options = None
  _RATELIMITMETADATA._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _GENERICRESPONSEMETADATA._options = None
  _GENERICRESPONSEMETADATA._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _ALREADYEXISTSERROR._serialized_start=66
  _ALREADYEXISTSERROR._serialized_end=126
  _NOTFOUNDERROR._serialized_start=128
  _NOTFOUNDERROR._serialized_end=183
  _BADREQUESTERROR._serialized_start=185
  _BADREQUESTERROR._serialized_end=214
  _AUTHENTICATIONERROR._serialized_start=216
  _AUTHENTICATIONERROR._serialized_end=249
  _PERMISSIONERROR._serialized_start=251
  _PERMISSIONERROR._serialized_end=280
  _INTERNALERROR._serialized_start=282
  _INTERNALERROR._serialized_end=309
  _RATELIMITERROR._serialized_start=311
  _RATELIMITERROR._serialized_end=428
  _CREATEREQUESTMETADATA._serialized_start=430
  _CREATEREQUESTMETADATA._serialized_end=501
  _CREATERESPONSEMETADATA._serialized_start=503
  _CREATERESPONSEMETADATA._serialized_end=539
  _GETREQUESTMETADATA._serialized_start=541
  _GETREQUESTMETADATA._serialized_end=658
  _GETRESPONSEMETADATA._serialized_start=660
  _GETRESPONSEMETADATA._serialized_end=693
  _UPDATEREQUESTMETADATA._serialized_start=695
  _UPDATEREQUESTMETADATA._serialized_end=766
  _UPDATERESPONSEMETADATA._serialized_start=768
  _UPDATERESPONSEMETADATA._serialized_end=804
  _DELETEREQUESTMETADATA._serialized_start=806
  _DELETEREQUESTMETADATA._serialized_end=877
  _DELETERESPONSEMETADATA._serialized_start=879
  _DELETERESPONSEMETADATA._serialized_end=915
  _LISTREQUESTMETADATA._serialized_start=918
  _LISTREQUESTMETADATA._serialized_end=1099
  _LISTRESPONSEMETADATA._serialized_start=1101
  _LISTRESPONSEMETADATA._serialized_end=1163
  _RATELIMITMETADATA._serialized_start=1166
  _RATELIMITMETADATA._serialized_end=1341
  _GENERICREQUESTMETADATA._serialized_start=1343
  _GENERICREQUESTMETADATA._serialized_end=1415
  _GENERICRESPONSEMETADATA._serialized_start=1417
  _GENERICRESPONSEMETADATA._serialized_end=1454
  _REQUIREMENTSMETADATA._serialized_start=1456
  _REQUIREMENTSMETADATA._serialized_end=1517
  _FULFILLMENTSMETADATA._serialized_start=1519
  _FULFILLMENTSMETADATA._serialized_end=1580
  _REQUIREMENT._serialized_start=1582
  _REQUIREMENT._serialized_end=1624
  _FULFILLMENT._serialized_start=1626
  _FULFILLMENT._serialized_end=1692
# @@protoc_insertion_point(module_scope)
