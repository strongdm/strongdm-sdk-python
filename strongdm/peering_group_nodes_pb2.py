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
# source: peering_group_nodes.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19peering_group_nodes.proto\x12\x02v1\x1a\roptions.proto\x1a\nspec.proto\"\x86\x01\n\x1dPeeringGroupNodeCreateRequest\x12\'\n\x04meta\x18\x01 \x01(\x0b\x32\x19.v1.CreateRequestMetadata\x12<\n\x12peering_group_node\x18\x02 \x01(\x0b\x32\x14.v1.PeeringGroupNodeB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xf9\x01\n\x1ePeeringGroupNodeCreateResponse\x12\x34\n\x04meta\x18\x01 \x01(\x0b\x32\x1a.v1.CreateResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12<\n\x12peering_group_node\x18\x02 \x01(\x0b\x32\x14.v1.PeeringGroupNodeB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12W\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB,\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"Z\n\x1aPeeringGroupNodeGetRequest\x12$\n\x04meta\x18\x01 \x01(\x0b\x32\x16.v1.GetRequestMetadata\x12\x16\n\x02id\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xf3\x01\n\x1bPeeringGroupNodeGetResponse\x12\x31\n\x04meta\x18\x01 \x01(\x0b\x32\x17.v1.GetResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12<\n\x12peering_group_node\x18\x02 \x01(\x0b\x32\x14.v1.PeeringGroupNodeB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12W\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB,\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"`\n\x1dPeeringGroupNodeDeleteRequest\x12\'\n\x04meta\x18\x01 \x01(\x0b\x32\x19.v1.DeleteRequestMetadata\x12\x16\n\x02id\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xbb\x01\n\x1ePeeringGroupNodeDeleteResponse\x12\x34\n\x04meta\x18\x01 \x01(\x0b\x32\x1a.v1.DeleteResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12W\n\nrate_limit\x18\x02 \x01(\x0b\x32\x15.v1.RateLimitMetadataB,\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"`\n\x1bPeeringGroupNodeListRequest\x12%\n\x04meta\x18\x01 \x01(\x0b\x32\x17.v1.ListRequestMetadata\x12\x1a\n\x06\x66ilter\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xde\x01\n\x1cPeeringGroupNodeListResponse\x12&\n\x04meta\x18\x01 \x01(\x0b\x32\x18.v1.ListResponseMetadata\x12=\n\x13peering_group_nodes\x18\x02 \x03(\x0b\x32\x14.v1.PeeringGroupNodeB\n\xf2\xf8\xb3\x07\x05\xb8\xf3\xb3\x07\x01\x12W\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB,\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway\"{\n\x10PeeringGroupNode\x12\x16\n\x02id\x18\x01 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12 \n\x07node_id\x18\x03 \x01(\tB\x0f\xf2\xf8\xb3\x07\n\xb0\xf3\xb3\x07\x01\xd0\xf4\xb3\x07\x01\x12!\n\x08group_id\x18\x04 \x01(\tB\x0f\xf2\xf8\xb3\x07\n\xb0\xf3\xb3\x07\x01\xd0\xf4\xb3\x07\x01:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\x32\xdb\x04\n\x11PeeringGroupNodes\x12~\n\x06\x43reate\x12!.v1.PeeringGroupNodeCreateRequest\x1a\".v1.PeeringGroupNodeCreateResponse\"-\x82\xf9\xb3\x07\t\xa2\xf3\xb3\x07\x04post\x82\xf9\xb3\x07\x1a\xaa\xf3\xb3\x07\x15/v1/peeringGroupNodes\x12\x85\x01\n\x06\x44\x65lete\x12!.v1.PeeringGroupNodeDeleteRequest\x1a\".v1.PeeringGroupNodeDeleteResponse\"4\x82\xf9\xb3\x07\x0b\xa2\xf3\xb3\x07\x06\x64\x65lete\x82\xf9\xb3\x07\x1f\xaa\xf3\xb3\x07\x1a/v1/peeringGroupNodes/{id}\x12y\n\x03Get\x12\x1e.v1.PeeringGroupNodeGetRequest\x1a\x1f.v1.PeeringGroupNodeGetResponse\"1\x82\xf9\xb3\x07\x08\xa2\xf3\xb3\x07\x03get\x82\xf9\xb3\x07\x1f\xaa\xf3\xb3\x07\x1a/v1/peeringGroupNodes/{id}\x12w\n\x04List\x12\x1f.v1.PeeringGroupNodeListRequest\x1a .v1.PeeringGroupNodeListResponse\",\x82\xf9\xb3\x07\x08\xa2\xf3\xb3\x07\x03get\x82\xf9\xb3\x07\x1a\xaa\xf3\xb3\x07\x15/v1/peeringGroupNodes\x1aJ\xca\xf9\xb3\x07\x15\xc2\xf9\xb3\x07\x10PeeringGroupNode\xca\xf9\xb3\x07\x08\xd2\xf9\xb3\x07\x03gn-\xca\xf9\xb3\x07\x06\xca\xf9\xb3\x07\x01*\xca\xf9\xb3\x07\t\xca\xf9\xb3\x07\x04!cli\xca\xf9\xb3\x07\x05\xd8\xf9\xb3\x07\x01\x42m\n\x19\x63om.strongdm.api.plumbingB\x19PeeringGroupNodesPlumbingZ5github.com/strongdm/strongdm-sdk-go/v3/internal/v1;v1b\x06proto3')



_PEERINGGROUPNODECREATEREQUEST = DESCRIPTOR.message_types_by_name['PeeringGroupNodeCreateRequest']
_PEERINGGROUPNODECREATERESPONSE = DESCRIPTOR.message_types_by_name['PeeringGroupNodeCreateResponse']
_PEERINGGROUPNODEGETREQUEST = DESCRIPTOR.message_types_by_name['PeeringGroupNodeGetRequest']
_PEERINGGROUPNODEGETRESPONSE = DESCRIPTOR.message_types_by_name['PeeringGroupNodeGetResponse']
_PEERINGGROUPNODEDELETEREQUEST = DESCRIPTOR.message_types_by_name['PeeringGroupNodeDeleteRequest']
_PEERINGGROUPNODEDELETERESPONSE = DESCRIPTOR.message_types_by_name['PeeringGroupNodeDeleteResponse']
_PEERINGGROUPNODELISTREQUEST = DESCRIPTOR.message_types_by_name['PeeringGroupNodeListRequest']
_PEERINGGROUPNODELISTRESPONSE = DESCRIPTOR.message_types_by_name['PeeringGroupNodeListResponse']
_PEERINGGROUPNODE = DESCRIPTOR.message_types_by_name['PeeringGroupNode']
PeeringGroupNodeCreateRequest = _reflection.GeneratedProtocolMessageType('PeeringGroupNodeCreateRequest', (_message.Message,), {
  'DESCRIPTOR' : _PEERINGGROUPNODECREATEREQUEST,
  '__module__' : 'peering_group_nodes_pb2'
  # @@protoc_insertion_point(class_scope:v1.PeeringGroupNodeCreateRequest)
  })
_sym_db.RegisterMessage(PeeringGroupNodeCreateRequest)

PeeringGroupNodeCreateResponse = _reflection.GeneratedProtocolMessageType('PeeringGroupNodeCreateResponse', (_message.Message,), {
  'DESCRIPTOR' : _PEERINGGROUPNODECREATERESPONSE,
  '__module__' : 'peering_group_nodes_pb2'
  # @@protoc_insertion_point(class_scope:v1.PeeringGroupNodeCreateResponse)
  })
_sym_db.RegisterMessage(PeeringGroupNodeCreateResponse)

PeeringGroupNodeGetRequest = _reflection.GeneratedProtocolMessageType('PeeringGroupNodeGetRequest', (_message.Message,), {
  'DESCRIPTOR' : _PEERINGGROUPNODEGETREQUEST,
  '__module__' : 'peering_group_nodes_pb2'
  # @@protoc_insertion_point(class_scope:v1.PeeringGroupNodeGetRequest)
  })
_sym_db.RegisterMessage(PeeringGroupNodeGetRequest)

PeeringGroupNodeGetResponse = _reflection.GeneratedProtocolMessageType('PeeringGroupNodeGetResponse', (_message.Message,), {
  'DESCRIPTOR' : _PEERINGGROUPNODEGETRESPONSE,
  '__module__' : 'peering_group_nodes_pb2'
  # @@protoc_insertion_point(class_scope:v1.PeeringGroupNodeGetResponse)
  })
_sym_db.RegisterMessage(PeeringGroupNodeGetResponse)

PeeringGroupNodeDeleteRequest = _reflection.GeneratedProtocolMessageType('PeeringGroupNodeDeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _PEERINGGROUPNODEDELETEREQUEST,
  '__module__' : 'peering_group_nodes_pb2'
  # @@protoc_insertion_point(class_scope:v1.PeeringGroupNodeDeleteRequest)
  })
_sym_db.RegisterMessage(PeeringGroupNodeDeleteRequest)

PeeringGroupNodeDeleteResponse = _reflection.GeneratedProtocolMessageType('PeeringGroupNodeDeleteResponse', (_message.Message,), {
  'DESCRIPTOR' : _PEERINGGROUPNODEDELETERESPONSE,
  '__module__' : 'peering_group_nodes_pb2'
  # @@protoc_insertion_point(class_scope:v1.PeeringGroupNodeDeleteResponse)
  })
_sym_db.RegisterMessage(PeeringGroupNodeDeleteResponse)

PeeringGroupNodeListRequest = _reflection.GeneratedProtocolMessageType('PeeringGroupNodeListRequest', (_message.Message,), {
  'DESCRIPTOR' : _PEERINGGROUPNODELISTREQUEST,
  '__module__' : 'peering_group_nodes_pb2'
  # @@protoc_insertion_point(class_scope:v1.PeeringGroupNodeListRequest)
  })
_sym_db.RegisterMessage(PeeringGroupNodeListRequest)

PeeringGroupNodeListResponse = _reflection.GeneratedProtocolMessageType('PeeringGroupNodeListResponse', (_message.Message,), {
  'DESCRIPTOR' : _PEERINGGROUPNODELISTRESPONSE,
  '__module__' : 'peering_group_nodes_pb2'
  # @@protoc_insertion_point(class_scope:v1.PeeringGroupNodeListResponse)
  })
_sym_db.RegisterMessage(PeeringGroupNodeListResponse)

PeeringGroupNode = _reflection.GeneratedProtocolMessageType('PeeringGroupNode', (_message.Message,), {
  'DESCRIPTOR' : _PEERINGGROUPNODE,
  '__module__' : 'peering_group_nodes_pb2'
  # @@protoc_insertion_point(class_scope:v1.PeeringGroupNode)
  })
_sym_db.RegisterMessage(PeeringGroupNode)

_PEERINGGROUPNODES = DESCRIPTOR.services_by_name['PeeringGroupNodes']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031com.strongdm.api.plumbingB\031PeeringGroupNodesPlumbingZ5github.com/strongdm/strongdm-sdk-go/v3/internal/v1;v1'
  _PEERINGGROUPNODECREATEREQUEST.fields_by_name['peering_group_node']._options = None
  _PEERINGGROUPNODECREATEREQUEST.fields_by_name['peering_group_node']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _PEERINGGROUPNODECREATERESPONSE.fields_by_name['meta']._options = None
  _PEERINGGROUPNODECREATERESPONSE.fields_by_name['meta']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _PEERINGGROUPNODECREATERESPONSE.fields_by_name['peering_group_node']._options = None
  _PEERINGGROUPNODECREATERESPONSE.fields_by_name['peering_group_node']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _PEERINGGROUPNODECREATERESPONSE.fields_by_name['rate_limit']._options = None
  _PEERINGGROUPNODECREATERESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\022\262\364\263\007\r!json_gateway'
  _PEERINGGROUPNODECREATERESPONSE._options = None
  _PEERINGGROUPNODECREATERESPONSE._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _PEERINGGROUPNODEGETREQUEST.fields_by_name['id']._options = None
  _PEERINGGROUPNODEGETREQUEST.fields_by_name['id']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _PEERINGGROUPNODEGETRESPONSE.fields_by_name['meta']._options = None
  _PEERINGGROUPNODEGETRESPONSE.fields_by_name['meta']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _PEERINGGROUPNODEGETRESPONSE.fields_by_name['peering_group_node']._options = None
  _PEERINGGROUPNODEGETRESPONSE.fields_by_name['peering_group_node']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _PEERINGGROUPNODEGETRESPONSE.fields_by_name['rate_limit']._options = None
  _PEERINGGROUPNODEGETRESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\022\262\364\263\007\r!json_gateway'
  _PEERINGGROUPNODEGETRESPONSE._options = None
  _PEERINGGROUPNODEGETRESPONSE._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _PEERINGGROUPNODEDELETEREQUEST.fields_by_name['id']._options = None
  _PEERINGGROUPNODEDELETEREQUEST.fields_by_name['id']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _PEERINGGROUPNODEDELETERESPONSE.fields_by_name['meta']._options = None
  _PEERINGGROUPNODEDELETERESPONSE.fields_by_name['meta']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _PEERINGGROUPNODEDELETERESPONSE.fields_by_name['rate_limit']._options = None
  _PEERINGGROUPNODEDELETERESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\022\262\364\263\007\r!json_gateway'
  _PEERINGGROUPNODEDELETERESPONSE._options = None
  _PEERINGGROUPNODEDELETERESPONSE._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _PEERINGGROUPNODELISTREQUEST.fields_by_name['filter']._options = None
  _PEERINGGROUPNODELISTREQUEST.fields_by_name['filter']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _PEERINGGROUPNODELISTRESPONSE.fields_by_name['peering_group_nodes']._options = None
  _PEERINGGROUPNODELISTRESPONSE.fields_by_name['peering_group_nodes']._serialized_options = b'\362\370\263\007\005\270\363\263\007\001'
  _PEERINGGROUPNODELISTRESPONSE.fields_by_name['rate_limit']._options = None
  _PEERINGGROUPNODELISTRESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\022\262\364\263\007\r!json_gateway'
  _PEERINGGROUPNODE.fields_by_name['id']._options = None
  _PEERINGGROUPNODE.fields_by_name['id']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _PEERINGGROUPNODE.fields_by_name['node_id']._options = None
  _PEERINGGROUPNODE.fields_by_name['node_id']._serialized_options = b'\362\370\263\007\n\260\363\263\007\001\320\364\263\007\001'
  _PEERINGGROUPNODE.fields_by_name['group_id']._options = None
  _PEERINGGROUPNODE.fields_by_name['group_id']._serialized_options = b'\362\370\263\007\n\260\363\263\007\001\320\364\263\007\001'
  _PEERINGGROUPNODE._options = None
  _PEERINGGROUPNODE._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _PEERINGGROUPNODES._options = None
  _PEERINGGROUPNODES._serialized_options = b'\312\371\263\007\025\302\371\263\007\020PeeringGroupNode\312\371\263\007\010\322\371\263\007\003gn-\312\371\263\007\006\312\371\263\007\001*\312\371\263\007\t\312\371\263\007\004!cli\312\371\263\007\005\330\371\263\007\001'
  _PEERINGGROUPNODES.methods_by_name['Create']._options = None
  _PEERINGGROUPNODES.methods_by_name['Create']._serialized_options = b'\202\371\263\007\t\242\363\263\007\004post\202\371\263\007\032\252\363\263\007\025/v1/peeringGroupNodes'
  _PEERINGGROUPNODES.methods_by_name['Delete']._options = None
  _PEERINGGROUPNODES.methods_by_name['Delete']._serialized_options = b'\202\371\263\007\013\242\363\263\007\006delete\202\371\263\007\037\252\363\263\007\032/v1/peeringGroupNodes/{id}'
  _PEERINGGROUPNODES.methods_by_name['Get']._options = None
  _PEERINGGROUPNODES.methods_by_name['Get']._serialized_options = b'\202\371\263\007\010\242\363\263\007\003get\202\371\263\007\037\252\363\263\007\032/v1/peeringGroupNodes/{id}'
  _PEERINGGROUPNODES.methods_by_name['List']._options = None
  _PEERINGGROUPNODES.methods_by_name['List']._serialized_options = b'\202\371\263\007\010\242\363\263\007\003get\202\371\263\007\032\252\363\263\007\025/v1/peeringGroupNodes'
  _PEERINGGROUPNODECREATEREQUEST._serialized_start=61
  _PEERINGGROUPNODECREATEREQUEST._serialized_end=195
  _PEERINGGROUPNODECREATERESPONSE._serialized_start=198
  _PEERINGGROUPNODECREATERESPONSE._serialized_end=447
  _PEERINGGROUPNODEGETREQUEST._serialized_start=449
  _PEERINGGROUPNODEGETREQUEST._serialized_end=539
  _PEERINGGROUPNODEGETRESPONSE._serialized_start=542
  _PEERINGGROUPNODEGETRESPONSE._serialized_end=785
  _PEERINGGROUPNODEDELETEREQUEST._serialized_start=787
  _PEERINGGROUPNODEDELETEREQUEST._serialized_end=883
  _PEERINGGROUPNODEDELETERESPONSE._serialized_start=886
  _PEERINGGROUPNODEDELETERESPONSE._serialized_end=1073
  _PEERINGGROUPNODELISTREQUEST._serialized_start=1075
  _PEERINGGROUPNODELISTREQUEST._serialized_end=1171
  _PEERINGGROUPNODELISTRESPONSE._serialized_start=1174
  _PEERINGGROUPNODELISTRESPONSE._serialized_end=1396
  _PEERINGGROUPNODE._serialized_start=1398
  _PEERINGGROUPNODE._serialized_end=1521
  _PEERINGGROUPNODES._serialized_start=1524
  _PEERINGGROUPNODES._serialized_end=2127
# @@protoc_insertion_point(module_scope)
