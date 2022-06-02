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
# source: role_attachments.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16role_attachments.proto\x12\x02v1\x1a\roptions.proto\x1a\nspec.proto\"\x83\x01\n\x1bRoleAttachmentCreateRequest\x12\'\n\x04meta\x18\x01 \x01(\x0b\x32\x19.v1.CreateRequestMetadata\x12\x37\n\x0frole_attachment\x18\x02 \x01(\x0b\x32\x12.v1.RoleAttachmentB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:\x02\x18\x01\"\xd8\x02\n\x1cRoleAttachmentCreateResponse\x12\x34\n\x04meta\x18\x01 \x01(\x0b\x32\x1a.v1.CreateResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x37\n\x0frole_attachment\x18\x02 \x01(\x0b\x32\x12.v1.RoleAttachmentB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\xba\x01\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB\x8e\x01\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x0e\xb2\xf4\xb3\x07\t!jopenapi\xf2\xf8\xb3\x07\x16\xb2\xf4\xb3\x07\x11!jopenapi_private\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway\xf2\xf8\xb3\x07\x1a\xb2\xf4\xb3\x07\x15!json_gateway_private\xf2\xf8\xb3\x07\x10\xb2\xf4\xb3\x07\x0b!typescript:\x0c\x18\x01\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"\\\n\x18RoleAttachmentGetRequest\x12$\n\x04meta\x18\x01 \x01(\x0b\x32\x16.v1.GetRequestMetadata\x12\x16\n\x02id\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:\x02\x18\x01\"\xd2\x02\n\x19RoleAttachmentGetResponse\x12\x31\n\x04meta\x18\x01 \x01(\x0b\x32\x17.v1.GetResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x37\n\x0frole_attachment\x18\x02 \x01(\x0b\x32\x12.v1.RoleAttachmentB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\xba\x01\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB\x8e\x01\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x0e\xb2\xf4\xb3\x07\t!jopenapi\xf2\xf8\xb3\x07\x16\xb2\xf4\xb3\x07\x11!jopenapi_private\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway\xf2\xf8\xb3\x07\x1a\xb2\xf4\xb3\x07\x15!json_gateway_private\xf2\xf8\xb3\x07\x10\xb2\xf4\xb3\x07\x0b!typescript:\x0c\x18\x01\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"b\n\x1bRoleAttachmentDeleteRequest\x12\'\n\x04meta\x18\x01 \x01(\x0b\x32\x19.v1.DeleteRequestMetadata\x12\x16\n\x02id\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:\x02\x18\x01\"\x9f\x02\n\x1cRoleAttachmentDeleteResponse\x12\x34\n\x04meta\x18\x01 \x01(\x0b\x32\x1a.v1.DeleteResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\xba\x01\n\nrate_limit\x18\x02 \x01(\x0b\x32\x15.v1.RateLimitMetadataB\x8e\x01\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x0e\xb2\xf4\xb3\x07\t!jopenapi\xf2\xf8\xb3\x07\x16\xb2\xf4\xb3\x07\x11!jopenapi_private\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway\xf2\xf8\xb3\x07\x1a\xb2\xf4\xb3\x07\x15!json_gateway_private\xf2\xf8\xb3\x07\x10\xb2\xf4\xb3\x07\x0b!typescript:\x0c\x18\x01\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"b\n\x19RoleAttachmentListRequest\x12%\n\x04meta\x18\x01 \x01(\x0b\x32\x17.v1.ListRequestMetadata\x12\x1a\n\x06\x66ilter\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:\x02\x18\x01\"\xbf\x02\n\x1aRoleAttachmentListResponse\x12&\n\x04meta\x18\x01 \x01(\x0b\x32\x18.v1.ListResponseMetadata\x12\x38\n\x10role_attachments\x18\x02 \x03(\x0b\x32\x12.v1.RoleAttachmentB\n\xf2\xf8\xb3\x07\x05\xb8\xf3\xb3\x07\x01\x12\xba\x01\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB\x8e\x01\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x0e\xb2\xf4\xb3\x07\t!jopenapi\xf2\xf8\xb3\x07\x16\xb2\xf4\xb3\x07\x11!jopenapi_private\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway\xf2\xf8\xb3\x07\x1a\xb2\xf4\xb3\x07\x15!json_gateway_private\xf2\xf8\xb3\x07\x10\xb2\xf4\xb3\x07\x0b!typescript:\x02\x18\x01\"\xef\x01\n\x0eRoleAttachment\x12\x16\n\x02id\x18\x01 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12*\n\x11\x63omposite_role_id\x18\x02 \x01(\tB\x0f\xf2\xf8\xb3\x07\n\xb0\xf3\xb3\x07\x01\xc0\xf3\xb3\x07\x01\x12)\n\x10\x61ttached_role_id\x18\x03 \x01(\tB\x0f\xf2\xf8\xb3\x07\n\xb0\xf3\xb3\x07\x01\xc0\xf3\xb3\x07\x01:n\x18\x01\xfa\xf8\xb3\x07g\xa8\xf3\xb3\x07\x01\xc2\xf3\xb3\x07]\xa2\xf3\xb3\x07(tf_examples/role_attachment_resource.txt\xaa\xf3\xb3\x07+tf_examples/role_attachment_data_source.txt2\x82\x05\n\x0fRoleAttachments\x12\x90\x01\n\x06\x43reate\x12\x1f.v1.RoleAttachmentCreateRequest\x1a .v1.RoleAttachmentCreateResponse\"C\x88\x02\x01\x82\xf9\xb3\x07\t\xa2\xf3\xb3\x07\x04post\x82\xf9\xb3\x07\x19\xaa\xf3\xb3\x07\x14/v1/role-attachments\x82\xf9\xb3\x07\x0f\xb2\xf3\xb3\x07\n2022-06-01\x12\x8b\x01\n\x03Get\x12\x1c.v1.RoleAttachmentGetRequest\x1a\x1d.v1.RoleAttachmentGetResponse\"G\x88\x02\x01\x82\xf9\xb3\x07\x08\xa2\xf3\xb3\x07\x03get\x82\xf9\xb3\x07\x1e\xaa\xf3\xb3\x07\x19/v1/role-attachments/{id}\x82\xf9\xb3\x07\x0f\xb2\xf3\xb3\x07\n2022-06-01\x12\x97\x01\n\x06\x44\x65lete\x12\x1f.v1.RoleAttachmentDeleteRequest\x1a .v1.RoleAttachmentDeleteResponse\"J\x88\x02\x01\x82\xf9\xb3\x07\x0b\xa2\xf3\xb3\x07\x06\x64\x65lete\x82\xf9\xb3\x07\x1e\xaa\xf3\xb3\x07\x19/v1/role-attachments/{id}\x82\xf9\xb3\x07\x0f\xb2\xf3\xb3\x07\n2022-06-01\x12\x89\x01\n\x04List\x12\x1d.v1.RoleAttachmentListRequest\x1a\x1e.v1.RoleAttachmentListResponse\"B\x88\x02\x01\x82\xf9\xb3\x07\x08\xa2\xf3\xb3\x07\x03get\x82\xf9\xb3\x07\x19\xaa\xf3\xb3\x07\x14/v1/role-attachments\x82\xf9\xb3\x07\x0f\xb2\xf3\xb3\x07\n2022-06-01\x1a(\x88\x02\x01\xca\xf9\xb3\x07\x13\xc2\xf9\xb3\x07\x0eRoleAttachment\xca\xf9\xb3\x07\x08\xd2\xf9\xb3\x07\x03ra-Bn\n\x1c\x63om.strongdm.api.v1.plumbingB\x17RoleAttachmentsPlumbingZ5github.com/strongdm/strongdm-sdk-go/v2/internal/v1;v1b\x06proto3')



_ROLEATTACHMENTCREATEREQUEST = DESCRIPTOR.message_types_by_name['RoleAttachmentCreateRequest']
_ROLEATTACHMENTCREATERESPONSE = DESCRIPTOR.message_types_by_name['RoleAttachmentCreateResponse']
_ROLEATTACHMENTGETREQUEST = DESCRIPTOR.message_types_by_name['RoleAttachmentGetRequest']
_ROLEATTACHMENTGETRESPONSE = DESCRIPTOR.message_types_by_name['RoleAttachmentGetResponse']
_ROLEATTACHMENTDELETEREQUEST = DESCRIPTOR.message_types_by_name['RoleAttachmentDeleteRequest']
_ROLEATTACHMENTDELETERESPONSE = DESCRIPTOR.message_types_by_name['RoleAttachmentDeleteResponse']
_ROLEATTACHMENTLISTREQUEST = DESCRIPTOR.message_types_by_name['RoleAttachmentListRequest']
_ROLEATTACHMENTLISTRESPONSE = DESCRIPTOR.message_types_by_name['RoleAttachmentListResponse']
_ROLEATTACHMENT = DESCRIPTOR.message_types_by_name['RoleAttachment']
RoleAttachmentCreateRequest = _reflection.GeneratedProtocolMessageType('RoleAttachmentCreateRequest', (_message.Message,), {
  'DESCRIPTOR' : _ROLEATTACHMENTCREATEREQUEST,
  '__module__' : 'role_attachments_pb2'
  # @@protoc_insertion_point(class_scope:v1.RoleAttachmentCreateRequest)
  })
_sym_db.RegisterMessage(RoleAttachmentCreateRequest)

RoleAttachmentCreateResponse = _reflection.GeneratedProtocolMessageType('RoleAttachmentCreateResponse', (_message.Message,), {
  'DESCRIPTOR' : _ROLEATTACHMENTCREATERESPONSE,
  '__module__' : 'role_attachments_pb2'
  # @@protoc_insertion_point(class_scope:v1.RoleAttachmentCreateResponse)
  })
_sym_db.RegisterMessage(RoleAttachmentCreateResponse)

RoleAttachmentGetRequest = _reflection.GeneratedProtocolMessageType('RoleAttachmentGetRequest', (_message.Message,), {
  'DESCRIPTOR' : _ROLEATTACHMENTGETREQUEST,
  '__module__' : 'role_attachments_pb2'
  # @@protoc_insertion_point(class_scope:v1.RoleAttachmentGetRequest)
  })
_sym_db.RegisterMessage(RoleAttachmentGetRequest)

RoleAttachmentGetResponse = _reflection.GeneratedProtocolMessageType('RoleAttachmentGetResponse', (_message.Message,), {
  'DESCRIPTOR' : _ROLEATTACHMENTGETRESPONSE,
  '__module__' : 'role_attachments_pb2'
  # @@protoc_insertion_point(class_scope:v1.RoleAttachmentGetResponse)
  })
_sym_db.RegisterMessage(RoleAttachmentGetResponse)

RoleAttachmentDeleteRequest = _reflection.GeneratedProtocolMessageType('RoleAttachmentDeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _ROLEATTACHMENTDELETEREQUEST,
  '__module__' : 'role_attachments_pb2'
  # @@protoc_insertion_point(class_scope:v1.RoleAttachmentDeleteRequest)
  })
_sym_db.RegisterMessage(RoleAttachmentDeleteRequest)

RoleAttachmentDeleteResponse = _reflection.GeneratedProtocolMessageType('RoleAttachmentDeleteResponse', (_message.Message,), {
  'DESCRIPTOR' : _ROLEATTACHMENTDELETERESPONSE,
  '__module__' : 'role_attachments_pb2'
  # @@protoc_insertion_point(class_scope:v1.RoleAttachmentDeleteResponse)
  })
_sym_db.RegisterMessage(RoleAttachmentDeleteResponse)

RoleAttachmentListRequest = _reflection.GeneratedProtocolMessageType('RoleAttachmentListRequest', (_message.Message,), {
  'DESCRIPTOR' : _ROLEATTACHMENTLISTREQUEST,
  '__module__' : 'role_attachments_pb2'
  # @@protoc_insertion_point(class_scope:v1.RoleAttachmentListRequest)
  })
_sym_db.RegisterMessage(RoleAttachmentListRequest)

RoleAttachmentListResponse = _reflection.GeneratedProtocolMessageType('RoleAttachmentListResponse', (_message.Message,), {
  'DESCRIPTOR' : _ROLEATTACHMENTLISTRESPONSE,
  '__module__' : 'role_attachments_pb2'
  # @@protoc_insertion_point(class_scope:v1.RoleAttachmentListResponse)
  })
_sym_db.RegisterMessage(RoleAttachmentListResponse)

RoleAttachment = _reflection.GeneratedProtocolMessageType('RoleAttachment', (_message.Message,), {
  'DESCRIPTOR' : _ROLEATTACHMENT,
  '__module__' : 'role_attachments_pb2'
  # @@protoc_insertion_point(class_scope:v1.RoleAttachment)
  })
_sym_db.RegisterMessage(RoleAttachment)

_ROLEATTACHMENTS = DESCRIPTOR.services_by_name['RoleAttachments']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\034com.strongdm.api.v1.plumbingB\027RoleAttachmentsPlumbingZ5github.com/strongdm/strongdm-sdk-go/v2/internal/v1;v1'
  _ROLEATTACHMENTCREATEREQUEST.fields_by_name['role_attachment']._options = None
  _ROLEATTACHMENTCREATEREQUEST.fields_by_name['role_attachment']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ROLEATTACHMENTCREATEREQUEST._options = None
  _ROLEATTACHMENTCREATEREQUEST._serialized_options = b'\030\001'
  _ROLEATTACHMENTCREATERESPONSE.fields_by_name['meta']._options = None
  _ROLEATTACHMENTCREATERESPONSE.fields_by_name['meta']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ROLEATTACHMENTCREATERESPONSE.fields_by_name['role_attachment']._options = None
  _ROLEATTACHMENTCREATERESPONSE.fields_by_name['role_attachment']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ROLEATTACHMENTCREATERESPONSE.fields_by_name['rate_limit']._options = None
  _ROLEATTACHMENTCREATERESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\016\262\364\263\007\t!jopenapi\362\370\263\007\026\262\364\263\007\021!jopenapi_private\362\370\263\007\022\262\364\263\007\r!json_gateway\362\370\263\007\032\262\364\263\007\025!json_gateway_private\362\370\263\007\020\262\364\263\007\013!typescript'
  _ROLEATTACHMENTCREATERESPONSE._options = None
  _ROLEATTACHMENTCREATERESPONSE._serialized_options = b'\030\001\372\370\263\007\005\250\363\263\007\001'
  _ROLEATTACHMENTGETREQUEST.fields_by_name['id']._options = None
  _ROLEATTACHMENTGETREQUEST.fields_by_name['id']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ROLEATTACHMENTGETREQUEST._options = None
  _ROLEATTACHMENTGETREQUEST._serialized_options = b'\030\001'
  _ROLEATTACHMENTGETRESPONSE.fields_by_name['meta']._options = None
  _ROLEATTACHMENTGETRESPONSE.fields_by_name['meta']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ROLEATTACHMENTGETRESPONSE.fields_by_name['role_attachment']._options = None
  _ROLEATTACHMENTGETRESPONSE.fields_by_name['role_attachment']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ROLEATTACHMENTGETRESPONSE.fields_by_name['rate_limit']._options = None
  _ROLEATTACHMENTGETRESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\016\262\364\263\007\t!jopenapi\362\370\263\007\026\262\364\263\007\021!jopenapi_private\362\370\263\007\022\262\364\263\007\r!json_gateway\362\370\263\007\032\262\364\263\007\025!json_gateway_private\362\370\263\007\020\262\364\263\007\013!typescript'
  _ROLEATTACHMENTGETRESPONSE._options = None
  _ROLEATTACHMENTGETRESPONSE._serialized_options = b'\030\001\372\370\263\007\005\250\363\263\007\001'
  _ROLEATTACHMENTDELETEREQUEST.fields_by_name['id']._options = None
  _ROLEATTACHMENTDELETEREQUEST.fields_by_name['id']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ROLEATTACHMENTDELETEREQUEST._options = None
  _ROLEATTACHMENTDELETEREQUEST._serialized_options = b'\030\001'
  _ROLEATTACHMENTDELETERESPONSE.fields_by_name['meta']._options = None
  _ROLEATTACHMENTDELETERESPONSE.fields_by_name['meta']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ROLEATTACHMENTDELETERESPONSE.fields_by_name['rate_limit']._options = None
  _ROLEATTACHMENTDELETERESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\016\262\364\263\007\t!jopenapi\362\370\263\007\026\262\364\263\007\021!jopenapi_private\362\370\263\007\022\262\364\263\007\r!json_gateway\362\370\263\007\032\262\364\263\007\025!json_gateway_private\362\370\263\007\020\262\364\263\007\013!typescript'
  _ROLEATTACHMENTDELETERESPONSE._options = None
  _ROLEATTACHMENTDELETERESPONSE._serialized_options = b'\030\001\372\370\263\007\005\250\363\263\007\001'
  _ROLEATTACHMENTLISTREQUEST.fields_by_name['filter']._options = None
  _ROLEATTACHMENTLISTREQUEST.fields_by_name['filter']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ROLEATTACHMENTLISTREQUEST._options = None
  _ROLEATTACHMENTLISTREQUEST._serialized_options = b'\030\001'
  _ROLEATTACHMENTLISTRESPONSE.fields_by_name['role_attachments']._options = None
  _ROLEATTACHMENTLISTRESPONSE.fields_by_name['role_attachments']._serialized_options = b'\362\370\263\007\005\270\363\263\007\001'
  _ROLEATTACHMENTLISTRESPONSE.fields_by_name['rate_limit']._options = None
  _ROLEATTACHMENTLISTRESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\016\262\364\263\007\t!jopenapi\362\370\263\007\026\262\364\263\007\021!jopenapi_private\362\370\263\007\022\262\364\263\007\r!json_gateway\362\370\263\007\032\262\364\263\007\025!json_gateway_private\362\370\263\007\020\262\364\263\007\013!typescript'
  _ROLEATTACHMENTLISTRESPONSE._options = None
  _ROLEATTACHMENTLISTRESPONSE._serialized_options = b'\030\001'
  _ROLEATTACHMENT.fields_by_name['id']._options = None
  _ROLEATTACHMENT.fields_by_name['id']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ROLEATTACHMENT.fields_by_name['composite_role_id']._options = None
  _ROLEATTACHMENT.fields_by_name['composite_role_id']._serialized_options = b'\362\370\263\007\n\260\363\263\007\001\300\363\263\007\001'
  _ROLEATTACHMENT.fields_by_name['attached_role_id']._options = None
  _ROLEATTACHMENT.fields_by_name['attached_role_id']._serialized_options = b'\362\370\263\007\n\260\363\263\007\001\300\363\263\007\001'
  _ROLEATTACHMENT._options = None
  _ROLEATTACHMENT._serialized_options = b'\030\001\372\370\263\007g\250\363\263\007\001\302\363\263\007]\242\363\263\007(tf_examples/role_attachment_resource.txt\252\363\263\007+tf_examples/role_attachment_data_source.txt'
  _ROLEATTACHMENTS._options = None
  _ROLEATTACHMENTS._serialized_options = b'\210\002\001\312\371\263\007\023\302\371\263\007\016RoleAttachment\312\371\263\007\010\322\371\263\007\003ra-'
  _ROLEATTACHMENTS.methods_by_name['Create']._options = None
  _ROLEATTACHMENTS.methods_by_name['Create']._serialized_options = b'\210\002\001\202\371\263\007\t\242\363\263\007\004post\202\371\263\007\031\252\363\263\007\024/v1/role-attachments\202\371\263\007\017\262\363\263\007\n2022-06-01'
  _ROLEATTACHMENTS.methods_by_name['Get']._options = None
  _ROLEATTACHMENTS.methods_by_name['Get']._serialized_options = b'\210\002\001\202\371\263\007\010\242\363\263\007\003get\202\371\263\007\036\252\363\263\007\031/v1/role-attachments/{id}\202\371\263\007\017\262\363\263\007\n2022-06-01'
  _ROLEATTACHMENTS.methods_by_name['Delete']._options = None
  _ROLEATTACHMENTS.methods_by_name['Delete']._serialized_options = b'\210\002\001\202\371\263\007\013\242\363\263\007\006delete\202\371\263\007\036\252\363\263\007\031/v1/role-attachments/{id}\202\371\263\007\017\262\363\263\007\n2022-06-01'
  _ROLEATTACHMENTS.methods_by_name['List']._options = None
  _ROLEATTACHMENTS.methods_by_name['List']._serialized_options = b'\210\002\001\202\371\263\007\010\242\363\263\007\003get\202\371\263\007\031\252\363\263\007\024/v1/role-attachments\202\371\263\007\017\262\363\263\007\n2022-06-01'
  _ROLEATTACHMENTCREATEREQUEST._serialized_start=58
  _ROLEATTACHMENTCREATEREQUEST._serialized_end=189
  _ROLEATTACHMENTCREATERESPONSE._serialized_start=192
  _ROLEATTACHMENTCREATERESPONSE._serialized_end=536
  _ROLEATTACHMENTGETREQUEST._serialized_start=538
  _ROLEATTACHMENTGETREQUEST._serialized_end=630
  _ROLEATTACHMENTGETRESPONSE._serialized_start=633
  _ROLEATTACHMENTGETRESPONSE._serialized_end=971
  _ROLEATTACHMENTDELETEREQUEST._serialized_start=973
  _ROLEATTACHMENTDELETEREQUEST._serialized_end=1071
  _ROLEATTACHMENTDELETERESPONSE._serialized_start=1074
  _ROLEATTACHMENTDELETERESPONSE._serialized_end=1361
  _ROLEATTACHMENTLISTREQUEST._serialized_start=1363
  _ROLEATTACHMENTLISTREQUEST._serialized_end=1461
  _ROLEATTACHMENTLISTRESPONSE._serialized_start=1464
  _ROLEATTACHMENTLISTRESPONSE._serialized_end=1783
  _ROLEATTACHMENT._serialized_start=1786
  _ROLEATTACHMENT._serialized_end=2025
  _ROLEATTACHMENTS._serialized_start=2028
  _ROLEATTACHMENTS._serialized_end=2670
# @@protoc_insertion_point(module_scope)
