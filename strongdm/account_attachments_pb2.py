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
# source: account_attachments.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x61\x63\x63ount_attachments.proto\x12\x02v1\x1a\roptions.proto\x1a\nspec.proto\"\x9b\x01\n\x1e\x41\x63\x63ountAttachmentCreateRequest\x12\'\n\x04meta\x18\x01 \x01(\x0b\x32\x19.v1.CreateRequestMetadata\x12=\n\x12\x61\x63\x63ount_attachment\x18\x02 \x01(\x0b\x32\x15.v1.AccountAttachmentB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:\x11\xfa\xf8\xb3\x07\x0c\xba\xf3\xb3\x07\x07options\"\xfb\x01\n\x1f\x41\x63\x63ountAttachmentCreateResponse\x12\x34\n\x04meta\x18\x01 \x01(\x0b\x32\x1a.v1.CreateResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12=\n\x12\x61\x63\x63ount_attachment\x18\x02 \x01(\x0b\x32\x15.v1.AccountAttachmentB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12W\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB,\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"[\n\x1b\x41\x63\x63ountAttachmentGetRequest\x12$\n\x04meta\x18\x01 \x01(\x0b\x32\x16.v1.GetRequestMetadata\x12\x16\n\x02id\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xf5\x01\n\x1c\x41\x63\x63ountAttachmentGetResponse\x12\x31\n\x04meta\x18\x01 \x01(\x0b\x32\x17.v1.GetResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12=\n\x12\x61\x63\x63ount_attachment\x18\x02 \x01(\x0b\x32\x15.v1.AccountAttachmentB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12W\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB,\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"a\n\x1e\x41\x63\x63ountAttachmentDeleteRequest\x12\'\n\x04meta\x18\x01 \x01(\x0b\x32\x19.v1.DeleteRequestMetadata\x12\x16\n\x02id\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xbc\x01\n\x1f\x41\x63\x63ountAttachmentDeleteResponse\x12\x34\n\x04meta\x18\x01 \x01(\x0b\x32\x1a.v1.DeleteResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12W\n\nrate_limit\x18\x02 \x01(\x0b\x32\x15.v1.RateLimitMetadataB,\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"a\n\x1c\x41\x63\x63ountAttachmentListRequest\x12%\n\x04meta\x18\x01 \x01(\x0b\x32\x17.v1.ListRequestMetadata\x12\x1a\n\x06\x66ilter\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xe0\x01\n\x1d\x41\x63\x63ountAttachmentListResponse\x12&\n\x04meta\x18\x01 \x01(\x0b\x32\x18.v1.ListResponseMetadata\x12>\n\x13\x61\x63\x63ount_attachments\x18\x02 \x03(\x0b\x32\x15.v1.AccountAttachmentB\n\xf2\xf8\xb3\x07\x05\xb8\xf3\xb3\x07\x01\x12W\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB,\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway\"\xe6\x01\n\x11\x41\x63\x63ountAttachment\x12\x16\n\x02id\x18\x01 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12#\n\naccount_id\x18\x02 \x01(\tB\x0f\xf2\xf8\xb3\x07\n\xb0\xf3\xb3\x07\x01\xc0\xf3\xb3\x07\x01\x12 \n\x07role_id\x18\x03 \x01(\tB\x0f\xf2\xf8\xb3\x07\n\xb0\xf3\xb3\x07\x01\xc0\xf3\xb3\x07\x01:r\xfa\xf8\xb3\x07m\xa8\xf3\xb3\x07\x01\xc2\xf3\xb3\x07\x63\xa2\xf3\xb3\x07+tf_examples/account_attachment_resource.txt\xaa\xf3\xb3\x07.tf_examples/account_attachment_data_source.txt2\xcb\x04\n\x12\x41\x63\x63ountAttachments\x12\x82\x01\n\x06\x43reate\x12\".v1.AccountAttachmentCreateRequest\x1a#.v1.AccountAttachmentCreateResponse\"/\x82\xf9\xb3\x07\t\xa2\xf3\xb3\x07\x04post\x82\xf9\xb3\x07\x1c\xaa\xf3\xb3\x07\x17/v1/account-attachments\x12}\n\x03Get\x12\x1f.v1.AccountAttachmentGetRequest\x1a .v1.AccountAttachmentGetResponse\"3\x82\xf9\xb3\x07\x08\xa2\xf3\xb3\x07\x03get\x82\xf9\xb3\x07!\xaa\xf3\xb3\x07\x1c/v1/account-attachments/{id}\x12\x89\x01\n\x06\x44\x65lete\x12\".v1.AccountAttachmentDeleteRequest\x1a#.v1.AccountAttachmentDeleteResponse\"6\x82\xf9\xb3\x07\x0b\xa2\xf3\xb3\x07\x06\x64\x65lete\x82\xf9\xb3\x07!\xaa\xf3\xb3\x07\x1c/v1/account-attachments/{id}\x12{\n\x04List\x12 .v1.AccountAttachmentListRequest\x1a!.v1.AccountAttachmentListResponse\".\x82\xf9\xb3\x07\x08\xa2\xf3\xb3\x07\x03get\x82\xf9\xb3\x07\x1c\xaa\xf3\xb3\x07\x17/v1/account-attachments\x1a(\xca\xf9\xb3\x07\x16\xc2\xf9\xb3\x07\x11\x41\x63\x63ountAttachment\xca\xf9\xb3\x07\x08\xd2\xf9\xb3\x07\x03\x61\x61-Bn\n\x19\x63om.strongdm.api.plumbingB\x1a\x41\x63\x63ountAttachmentsPlumbingZ5github.com/strongdm/strongdm-sdk-go/v3/internal/v1;v1b\x06proto3')



_ACCOUNTATTACHMENTCREATEREQUEST = DESCRIPTOR.message_types_by_name['AccountAttachmentCreateRequest']
_ACCOUNTATTACHMENTCREATERESPONSE = DESCRIPTOR.message_types_by_name['AccountAttachmentCreateResponse']
_ACCOUNTATTACHMENTGETREQUEST = DESCRIPTOR.message_types_by_name['AccountAttachmentGetRequest']
_ACCOUNTATTACHMENTGETRESPONSE = DESCRIPTOR.message_types_by_name['AccountAttachmentGetResponse']
_ACCOUNTATTACHMENTDELETEREQUEST = DESCRIPTOR.message_types_by_name['AccountAttachmentDeleteRequest']
_ACCOUNTATTACHMENTDELETERESPONSE = DESCRIPTOR.message_types_by_name['AccountAttachmentDeleteResponse']
_ACCOUNTATTACHMENTLISTREQUEST = DESCRIPTOR.message_types_by_name['AccountAttachmentListRequest']
_ACCOUNTATTACHMENTLISTRESPONSE = DESCRIPTOR.message_types_by_name['AccountAttachmentListResponse']
_ACCOUNTATTACHMENT = DESCRIPTOR.message_types_by_name['AccountAttachment']
AccountAttachmentCreateRequest = _reflection.GeneratedProtocolMessageType('AccountAttachmentCreateRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTATTACHMENTCREATEREQUEST,
  '__module__' : 'account_attachments_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountAttachmentCreateRequest)
  })
_sym_db.RegisterMessage(AccountAttachmentCreateRequest)

AccountAttachmentCreateResponse = _reflection.GeneratedProtocolMessageType('AccountAttachmentCreateResponse', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTATTACHMENTCREATERESPONSE,
  '__module__' : 'account_attachments_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountAttachmentCreateResponse)
  })
_sym_db.RegisterMessage(AccountAttachmentCreateResponse)

AccountAttachmentGetRequest = _reflection.GeneratedProtocolMessageType('AccountAttachmentGetRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTATTACHMENTGETREQUEST,
  '__module__' : 'account_attachments_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountAttachmentGetRequest)
  })
_sym_db.RegisterMessage(AccountAttachmentGetRequest)

AccountAttachmentGetResponse = _reflection.GeneratedProtocolMessageType('AccountAttachmentGetResponse', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTATTACHMENTGETRESPONSE,
  '__module__' : 'account_attachments_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountAttachmentGetResponse)
  })
_sym_db.RegisterMessage(AccountAttachmentGetResponse)

AccountAttachmentDeleteRequest = _reflection.GeneratedProtocolMessageType('AccountAttachmentDeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTATTACHMENTDELETEREQUEST,
  '__module__' : 'account_attachments_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountAttachmentDeleteRequest)
  })
_sym_db.RegisterMessage(AccountAttachmentDeleteRequest)

AccountAttachmentDeleteResponse = _reflection.GeneratedProtocolMessageType('AccountAttachmentDeleteResponse', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTATTACHMENTDELETERESPONSE,
  '__module__' : 'account_attachments_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountAttachmentDeleteResponse)
  })
_sym_db.RegisterMessage(AccountAttachmentDeleteResponse)

AccountAttachmentListRequest = _reflection.GeneratedProtocolMessageType('AccountAttachmentListRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTATTACHMENTLISTREQUEST,
  '__module__' : 'account_attachments_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountAttachmentListRequest)
  })
_sym_db.RegisterMessage(AccountAttachmentListRequest)

AccountAttachmentListResponse = _reflection.GeneratedProtocolMessageType('AccountAttachmentListResponse', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTATTACHMENTLISTRESPONSE,
  '__module__' : 'account_attachments_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountAttachmentListResponse)
  })
_sym_db.RegisterMessage(AccountAttachmentListResponse)

AccountAttachment = _reflection.GeneratedProtocolMessageType('AccountAttachment', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTATTACHMENT,
  '__module__' : 'account_attachments_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountAttachment)
  })
_sym_db.RegisterMessage(AccountAttachment)

_ACCOUNTATTACHMENTS = DESCRIPTOR.services_by_name['AccountAttachments']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031com.strongdm.api.plumbingB\032AccountAttachmentsPlumbingZ5github.com/strongdm/strongdm-sdk-go/v3/internal/v1;v1'
  _ACCOUNTATTACHMENTCREATEREQUEST.fields_by_name['account_attachment']._options = None
  _ACCOUNTATTACHMENTCREATEREQUEST.fields_by_name['account_attachment']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACCOUNTATTACHMENTCREATEREQUEST._options = None
  _ACCOUNTATTACHMENTCREATEREQUEST._serialized_options = b'\372\370\263\007\014\272\363\263\007\007options'
  _ACCOUNTATTACHMENTCREATERESPONSE.fields_by_name['meta']._options = None
  _ACCOUNTATTACHMENTCREATERESPONSE.fields_by_name['meta']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACCOUNTATTACHMENTCREATERESPONSE.fields_by_name['account_attachment']._options = None
  _ACCOUNTATTACHMENTCREATERESPONSE.fields_by_name['account_attachment']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACCOUNTATTACHMENTCREATERESPONSE.fields_by_name['rate_limit']._options = None
  _ACCOUNTATTACHMENTCREATERESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\022\262\364\263\007\r!json_gateway'
  _ACCOUNTATTACHMENTCREATERESPONSE._options = None
  _ACCOUNTATTACHMENTCREATERESPONSE._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _ACCOUNTATTACHMENTGETREQUEST.fields_by_name['id']._options = None
  _ACCOUNTATTACHMENTGETREQUEST.fields_by_name['id']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACCOUNTATTACHMENTGETRESPONSE.fields_by_name['meta']._options = None
  _ACCOUNTATTACHMENTGETRESPONSE.fields_by_name['meta']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACCOUNTATTACHMENTGETRESPONSE.fields_by_name['account_attachment']._options = None
  _ACCOUNTATTACHMENTGETRESPONSE.fields_by_name['account_attachment']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACCOUNTATTACHMENTGETRESPONSE.fields_by_name['rate_limit']._options = None
  _ACCOUNTATTACHMENTGETRESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\022\262\364\263\007\r!json_gateway'
  _ACCOUNTATTACHMENTGETRESPONSE._options = None
  _ACCOUNTATTACHMENTGETRESPONSE._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _ACCOUNTATTACHMENTDELETEREQUEST.fields_by_name['id']._options = None
  _ACCOUNTATTACHMENTDELETEREQUEST.fields_by_name['id']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACCOUNTATTACHMENTDELETERESPONSE.fields_by_name['meta']._options = None
  _ACCOUNTATTACHMENTDELETERESPONSE.fields_by_name['meta']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACCOUNTATTACHMENTDELETERESPONSE.fields_by_name['rate_limit']._options = None
  _ACCOUNTATTACHMENTDELETERESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\022\262\364\263\007\r!json_gateway'
  _ACCOUNTATTACHMENTDELETERESPONSE._options = None
  _ACCOUNTATTACHMENTDELETERESPONSE._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _ACCOUNTATTACHMENTLISTREQUEST.fields_by_name['filter']._options = None
  _ACCOUNTATTACHMENTLISTREQUEST.fields_by_name['filter']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACCOUNTATTACHMENTLISTRESPONSE.fields_by_name['account_attachments']._options = None
  _ACCOUNTATTACHMENTLISTRESPONSE.fields_by_name['account_attachments']._serialized_options = b'\362\370\263\007\005\270\363\263\007\001'
  _ACCOUNTATTACHMENTLISTRESPONSE.fields_by_name['rate_limit']._options = None
  _ACCOUNTATTACHMENTLISTRESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\022\262\364\263\007\r!json_gateway'
  _ACCOUNTATTACHMENT.fields_by_name['id']._options = None
  _ACCOUNTATTACHMENT.fields_by_name['id']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACCOUNTATTACHMENT.fields_by_name['account_id']._options = None
  _ACCOUNTATTACHMENT.fields_by_name['account_id']._serialized_options = b'\362\370\263\007\n\260\363\263\007\001\300\363\263\007\001'
  _ACCOUNTATTACHMENT.fields_by_name['role_id']._options = None
  _ACCOUNTATTACHMENT.fields_by_name['role_id']._serialized_options = b'\362\370\263\007\n\260\363\263\007\001\300\363\263\007\001'
  _ACCOUNTATTACHMENT._options = None
  _ACCOUNTATTACHMENT._serialized_options = b'\372\370\263\007m\250\363\263\007\001\302\363\263\007c\242\363\263\007+tf_examples/account_attachment_resource.txt\252\363\263\007.tf_examples/account_attachment_data_source.txt'
  _ACCOUNTATTACHMENTS._options = None
  _ACCOUNTATTACHMENTS._serialized_options = b'\312\371\263\007\026\302\371\263\007\021AccountAttachment\312\371\263\007\010\322\371\263\007\003aa-'
  _ACCOUNTATTACHMENTS.methods_by_name['Create']._options = None
  _ACCOUNTATTACHMENTS.methods_by_name['Create']._serialized_options = b'\202\371\263\007\t\242\363\263\007\004post\202\371\263\007\034\252\363\263\007\027/v1/account-attachments'
  _ACCOUNTATTACHMENTS.methods_by_name['Get']._options = None
  _ACCOUNTATTACHMENTS.methods_by_name['Get']._serialized_options = b'\202\371\263\007\010\242\363\263\007\003get\202\371\263\007!\252\363\263\007\034/v1/account-attachments/{id}'
  _ACCOUNTATTACHMENTS.methods_by_name['Delete']._options = None
  _ACCOUNTATTACHMENTS.methods_by_name['Delete']._serialized_options = b'\202\371\263\007\013\242\363\263\007\006delete\202\371\263\007!\252\363\263\007\034/v1/account-attachments/{id}'
  _ACCOUNTATTACHMENTS.methods_by_name['List']._options = None
  _ACCOUNTATTACHMENTS.methods_by_name['List']._serialized_options = b'\202\371\263\007\010\242\363\263\007\003get\202\371\263\007\034\252\363\263\007\027/v1/account-attachments'
  _ACCOUNTATTACHMENTCREATEREQUEST._serialized_start=61
  _ACCOUNTATTACHMENTCREATEREQUEST._serialized_end=216
  _ACCOUNTATTACHMENTCREATERESPONSE._serialized_start=219
  _ACCOUNTATTACHMENTCREATERESPONSE._serialized_end=470
  _ACCOUNTATTACHMENTGETREQUEST._serialized_start=472
  _ACCOUNTATTACHMENTGETREQUEST._serialized_end=563
  _ACCOUNTATTACHMENTGETRESPONSE._serialized_start=566
  _ACCOUNTATTACHMENTGETRESPONSE._serialized_end=811
  _ACCOUNTATTACHMENTDELETEREQUEST._serialized_start=813
  _ACCOUNTATTACHMENTDELETEREQUEST._serialized_end=910
  _ACCOUNTATTACHMENTDELETERESPONSE._serialized_start=913
  _ACCOUNTATTACHMENTDELETERESPONSE._serialized_end=1101
  _ACCOUNTATTACHMENTLISTREQUEST._serialized_start=1103
  _ACCOUNTATTACHMENTLISTREQUEST._serialized_end=1200
  _ACCOUNTATTACHMENTLISTRESPONSE._serialized_start=1203
  _ACCOUNTATTACHMENTLISTRESPONSE._serialized_end=1427
  _ACCOUNTATTACHMENT._serialized_start=1430
  _ACCOUNTATTACHMENT._serialized_end=1660
  _ACCOUNTATTACHMENTS._serialized_start=1663
  _ACCOUNTATTACHMENTS._serialized_end=2250
# @@protoc_insertion_point(module_scope)
