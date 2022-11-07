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
# source: nodes.proto
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
from . import tags_pb2 as tags__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bnodes.proto\x12\x02v1\x1a\roptions.proto\x1a\nspec.proto\x1a\ntags.proto\"`\n\x11NodeCreateRequest\x12\'\n\x04meta\x18\x01 \x01(\x0b\x32\x19.v1.CreateRequestMetadata\x12\"\n\x04node\x18\x02 \x01(\x0b\x32\x08.v1.NodeB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xf3\x01\n\x12NodeCreateResponse\x12\x34\n\x04meta\x18\x01 \x01(\x0b\x32\x1a.v1.CreateResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\"\n\x04node\x18\x02 \x01(\x0b\x32\x08.v1.NodeB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x1e\n\x05token\x18\x03 \x01(\tB\x0f\xf2\xf8\xb3\x07\n\xb0\xf3\xb3\x07\x01\xf0\xf3\xb3\x07\x01\x12W\n\nrate_limit\x18\x04 \x01(\x0b\x32\x15.v1.RateLimitMetadataB,\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"N\n\x0eNodeGetRequest\x12$\n\x04meta\x18\x01 \x01(\x0b\x32\x16.v1.GetRequestMetadata\x12\x16\n\x02id\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xcd\x01\n\x0fNodeGetResponse\x12\x31\n\x04meta\x18\x01 \x01(\x0b\x32\x17.v1.GetResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\"\n\x04node\x18\x02 \x01(\x0b\x32\x08.v1.NodeB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12W\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB,\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"l\n\x11NodeUpdateRequest\x12\'\n\x04meta\x18\x01 \x01(\x0b\x32\x19.v1.UpdateRequestMetadata\x12\n\n\x02id\x18\x02 \x01(\t\x12\"\n\x04node\x18\x03 \x01(\x0b\x32\x08.v1.NodeB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xd3\x01\n\x12NodeUpdateResponse\x12\x34\n\x04meta\x18\x01 \x01(\x0b\x32\x1a.v1.UpdateResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\"\n\x04node\x18\x02 \x01(\x0b\x32\x08.v1.NodeB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12W\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB,\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"T\n\x11NodeDeleteRequest\x12\'\n\x04meta\x18\x01 \x01(\x0b\x32\x19.v1.DeleteRequestMetadata\x12\x16\n\x02id\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xaf\x01\n\x12NodeDeleteResponse\x12\x34\n\x04meta\x18\x01 \x01(\x0b\x32\x1a.v1.DeleteResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12W\n\nrate_limit\x18\x02 \x01(\x0b\x32\x15.v1.RateLimitMetadataB,\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"T\n\x0fNodeListRequest\x12%\n\x04meta\x18\x01 \x01(\x0b\x32\x17.v1.ListRequestMetadata\x12\x1a\n\x06\x66ilter\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xb8\x01\n\x10NodeListResponse\x12&\n\x04meta\x18\x01 \x01(\x0b\x32\x18.v1.ListResponseMetadata\x12#\n\x05nodes\x18\x02 \x03(\x0b\x32\x08.v1.NodeB\n\xf2\xf8\xb3\x07\x05\xb8\xf3\xb3\x07\x01\x12W\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB,\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway\"\xc5\x01\n\x04Node\x12\x1a\n\x05relay\x18\x01 \x01(\x0b\x32\t.v1.RelayH\x00\x12\x1e\n\x07gateway\x18\x02 \x01(\x0b\x32\x0b.v1.GatewayH\x00:[\xfa\xf8\xb3\x07L\xc2\xf3\xb3\x07G\xa2\xf3\xb3\x07\x1dtf_examples/node_resource.txt\xaa\xf3\xb3\x07 tf_examples/node_data_source.txt\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\x42$\n\x04node\x12\x1c\xaa\xf8\xb3\x07\t\xaa\xf8\xb3\x07\x04tags\xaa\xf8\xb3\x07\t\xaa\xf8\xb3\x07\x04name\"\xd0\x01\n\x05Relay\x12\x16\n\x02id\x18\x01 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x1d\n\x04name\x18\x02 \x01(\tB\x0f\xf2\xf8\xb3\x07\n\xb0\xf3\xb3\x07\x01\xd0\xf4\xb3\x07\x01\x12<\n\x05state\x18\x03 \x01(\tB-\xf2\xf8\xb3\x07(\xb0\xf3\xb3\x07\x01\x98\xf4\xb3\x07\x01\xb2\xf4\xb3\x07\x01*\xb2\xf4\xb3\x07\x13!terraform-provider\x12\"\n\x04tags\x18\x04 \x01(\x0b\x32\x08.v1.TagsB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\"\n\x0egateway_filter\x18\x05 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"\xac\x02\n\x07Gateway\x12\x16\n\x02id\x18\x01 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x1d\n\x04name\x18\x02 \x01(\tB\x0f\xf2\xf8\xb3\x07\n\xb0\xf3\xb3\x07\x01\xd0\xf4\xb3\x07\x01\x12<\n\x05state\x18\x03 \x01(\tB-\xf2\xf8\xb3\x07(\xb0\xf3\xb3\x07\x01\x98\xf4\xb3\x07\x01\xb2\xf4\xb3\x07\x01*\xb2\xf4\xb3\x07\x13!terraform-provider\x12,\n\x0elisten_address\x18\x04 \x01(\tB\x14\xf2\xf8\xb3\x07\x0f\xb0\xf3\xb3\x07\x01\xc0\xf3\xb3\x07\x01\xe0\xf3\xb3\x07\x01\x12*\n\x0c\x62ind_address\x18\x05 \x01(\tB\x14\xf2\xf8\xb3\x07\x0f\xb0\xf3\xb3\x07\x01\xe0\xf3\xb3\x07\x01\xd0\xf4\xb3\x07\x01\x12\"\n\x04tags\x18\x06 \x01(\x0b\x32\x08.v1.TagsB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\"\n\x0egateway_filter\x18\x07 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\x32\xee\x03\n\x05Nodes\x12Z\n\x06\x43reate\x12\x15.v1.NodeCreateRequest\x1a\x16.v1.NodeCreateResponse\"!\x82\xf9\xb3\x07\t\xa2\xf3\xb3\x07\x04post\x82\xf9\xb3\x07\x0e\xaa\xf3\xb3\x07\t/v1/nodes\x12U\n\x03Get\x12\x12.v1.NodeGetRequest\x1a\x13.v1.NodeGetResponse\"%\x82\xf9\xb3\x07\x08\xa2\xf3\xb3\x07\x03get\x82\xf9\xb3\x07\x13\xaa\xf3\xb3\x07\x0e/v1/nodes/{id}\x12^\n\x06Update\x12\x15.v1.NodeUpdateRequest\x1a\x16.v1.NodeUpdateResponse\"%\x82\xf9\xb3\x07\x08\xa2\xf3\xb3\x07\x03put\x82\xf9\xb3\x07\x13\xaa\xf3\xb3\x07\x0e/v1/nodes/{id}\x12\x61\n\x06\x44\x65lete\x12\x15.v1.NodeDeleteRequest\x1a\x16.v1.NodeDeleteResponse\"(\x82\xf9\xb3\x07\x0b\xa2\xf3\xb3\x07\x06\x64\x65lete\x82\xf9\xb3\x07\x13\xaa\xf3\xb3\x07\x0e/v1/nodes/{id}\x12S\n\x04List\x12\x13.v1.NodeListRequest\x1a\x14.v1.NodeListResponse\" \x82\xf9\xb3\x07\x08\xa2\xf3\xb3\x07\x03get\x82\xf9\xb3\x07\x0e\xaa\xf3\xb3\x07\t/v1/nodes\x1a\x1a\xca\xf9\xb3\x07\t\xc2\xf9\xb3\x07\x04Node\xca\xf9\xb3\x07\x07\xd2\xf9\xb3\x07\x02n-Ba\n\x19\x63om.strongdm.api.plumbingB\rNodesPlumbingZ5github.com/strongdm/strongdm-sdk-go/v3/internal/v1;v1b\x06proto3')



_NODECREATEREQUEST = DESCRIPTOR.message_types_by_name['NodeCreateRequest']
_NODECREATERESPONSE = DESCRIPTOR.message_types_by_name['NodeCreateResponse']
_NODEGETREQUEST = DESCRIPTOR.message_types_by_name['NodeGetRequest']
_NODEGETRESPONSE = DESCRIPTOR.message_types_by_name['NodeGetResponse']
_NODEUPDATEREQUEST = DESCRIPTOR.message_types_by_name['NodeUpdateRequest']
_NODEUPDATERESPONSE = DESCRIPTOR.message_types_by_name['NodeUpdateResponse']
_NODEDELETEREQUEST = DESCRIPTOR.message_types_by_name['NodeDeleteRequest']
_NODEDELETERESPONSE = DESCRIPTOR.message_types_by_name['NodeDeleteResponse']
_NODELISTREQUEST = DESCRIPTOR.message_types_by_name['NodeListRequest']
_NODELISTRESPONSE = DESCRIPTOR.message_types_by_name['NodeListResponse']
_NODE = DESCRIPTOR.message_types_by_name['Node']
_RELAY = DESCRIPTOR.message_types_by_name['Relay']
_GATEWAY = DESCRIPTOR.message_types_by_name['Gateway']
NodeCreateRequest = _reflection.GeneratedProtocolMessageType('NodeCreateRequest', (_message.Message,), {
  'DESCRIPTOR' : _NODECREATEREQUEST,
  '__module__' : 'nodes_pb2'
  # @@protoc_insertion_point(class_scope:v1.NodeCreateRequest)
  })
_sym_db.RegisterMessage(NodeCreateRequest)

NodeCreateResponse = _reflection.GeneratedProtocolMessageType('NodeCreateResponse', (_message.Message,), {
  'DESCRIPTOR' : _NODECREATERESPONSE,
  '__module__' : 'nodes_pb2'
  # @@protoc_insertion_point(class_scope:v1.NodeCreateResponse)
  })
_sym_db.RegisterMessage(NodeCreateResponse)

NodeGetRequest = _reflection.GeneratedProtocolMessageType('NodeGetRequest', (_message.Message,), {
  'DESCRIPTOR' : _NODEGETREQUEST,
  '__module__' : 'nodes_pb2'
  # @@protoc_insertion_point(class_scope:v1.NodeGetRequest)
  })
_sym_db.RegisterMessage(NodeGetRequest)

NodeGetResponse = _reflection.GeneratedProtocolMessageType('NodeGetResponse', (_message.Message,), {
  'DESCRIPTOR' : _NODEGETRESPONSE,
  '__module__' : 'nodes_pb2'
  # @@protoc_insertion_point(class_scope:v1.NodeGetResponse)
  })
_sym_db.RegisterMessage(NodeGetResponse)

NodeUpdateRequest = _reflection.GeneratedProtocolMessageType('NodeUpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _NODEUPDATEREQUEST,
  '__module__' : 'nodes_pb2'
  # @@protoc_insertion_point(class_scope:v1.NodeUpdateRequest)
  })
_sym_db.RegisterMessage(NodeUpdateRequest)

NodeUpdateResponse = _reflection.GeneratedProtocolMessageType('NodeUpdateResponse', (_message.Message,), {
  'DESCRIPTOR' : _NODEUPDATERESPONSE,
  '__module__' : 'nodes_pb2'
  # @@protoc_insertion_point(class_scope:v1.NodeUpdateResponse)
  })
_sym_db.RegisterMessage(NodeUpdateResponse)

NodeDeleteRequest = _reflection.GeneratedProtocolMessageType('NodeDeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _NODEDELETEREQUEST,
  '__module__' : 'nodes_pb2'
  # @@protoc_insertion_point(class_scope:v1.NodeDeleteRequest)
  })
_sym_db.RegisterMessage(NodeDeleteRequest)

NodeDeleteResponse = _reflection.GeneratedProtocolMessageType('NodeDeleteResponse', (_message.Message,), {
  'DESCRIPTOR' : _NODEDELETERESPONSE,
  '__module__' : 'nodes_pb2'
  # @@protoc_insertion_point(class_scope:v1.NodeDeleteResponse)
  })
_sym_db.RegisterMessage(NodeDeleteResponse)

NodeListRequest = _reflection.GeneratedProtocolMessageType('NodeListRequest', (_message.Message,), {
  'DESCRIPTOR' : _NODELISTREQUEST,
  '__module__' : 'nodes_pb2'
  # @@protoc_insertion_point(class_scope:v1.NodeListRequest)
  })
_sym_db.RegisterMessage(NodeListRequest)

NodeListResponse = _reflection.GeneratedProtocolMessageType('NodeListResponse', (_message.Message,), {
  'DESCRIPTOR' : _NODELISTRESPONSE,
  '__module__' : 'nodes_pb2'
  # @@protoc_insertion_point(class_scope:v1.NodeListResponse)
  })
_sym_db.RegisterMessage(NodeListResponse)

Node = _reflection.GeneratedProtocolMessageType('Node', (_message.Message,), {
  'DESCRIPTOR' : _NODE,
  '__module__' : 'nodes_pb2'
  # @@protoc_insertion_point(class_scope:v1.Node)
  })
_sym_db.RegisterMessage(Node)

Relay = _reflection.GeneratedProtocolMessageType('Relay', (_message.Message,), {
  'DESCRIPTOR' : _RELAY,
  '__module__' : 'nodes_pb2'
  # @@protoc_insertion_point(class_scope:v1.Relay)
  })
_sym_db.RegisterMessage(Relay)

Gateway = _reflection.GeneratedProtocolMessageType('Gateway', (_message.Message,), {
  'DESCRIPTOR' : _GATEWAY,
  '__module__' : 'nodes_pb2'
  # @@protoc_insertion_point(class_scope:v1.Gateway)
  })
_sym_db.RegisterMessage(Gateway)

_NODES = DESCRIPTOR.services_by_name['Nodes']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031com.strongdm.api.plumbingB\rNodesPlumbingZ5github.com/strongdm/strongdm-sdk-go/v3/internal/v1;v1'
  _NODECREATEREQUEST.fields_by_name['node']._options = None
  _NODECREATEREQUEST.fields_by_name['node']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _NODECREATERESPONSE.fields_by_name['meta']._options = None
  _NODECREATERESPONSE.fields_by_name['meta']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _NODECREATERESPONSE.fields_by_name['node']._options = None
  _NODECREATERESPONSE.fields_by_name['node']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _NODECREATERESPONSE.fields_by_name['token']._options = None
  _NODECREATERESPONSE.fields_by_name['token']._serialized_options = b'\362\370\263\007\n\260\363\263\007\001\360\363\263\007\001'
  _NODECREATERESPONSE.fields_by_name['rate_limit']._options = None
  _NODECREATERESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\022\262\364\263\007\r!json_gateway'
  _NODECREATERESPONSE._options = None
  _NODECREATERESPONSE._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _NODEGETREQUEST.fields_by_name['id']._options = None
  _NODEGETREQUEST.fields_by_name['id']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _NODEGETRESPONSE.fields_by_name['meta']._options = None
  _NODEGETRESPONSE.fields_by_name['meta']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _NODEGETRESPONSE.fields_by_name['node']._options = None
  _NODEGETRESPONSE.fields_by_name['node']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _NODEGETRESPONSE.fields_by_name['rate_limit']._options = None
  _NODEGETRESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\022\262\364\263\007\r!json_gateway'
  _NODEGETRESPONSE._options = None
  _NODEGETRESPONSE._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _NODEUPDATEREQUEST.fields_by_name['node']._options = None
  _NODEUPDATEREQUEST.fields_by_name['node']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _NODEUPDATERESPONSE.fields_by_name['meta']._options = None
  _NODEUPDATERESPONSE.fields_by_name['meta']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _NODEUPDATERESPONSE.fields_by_name['node']._options = None
  _NODEUPDATERESPONSE.fields_by_name['node']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _NODEUPDATERESPONSE.fields_by_name['rate_limit']._options = None
  _NODEUPDATERESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\022\262\364\263\007\r!json_gateway'
  _NODEUPDATERESPONSE._options = None
  _NODEUPDATERESPONSE._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _NODEDELETEREQUEST.fields_by_name['id']._options = None
  _NODEDELETEREQUEST.fields_by_name['id']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _NODEDELETERESPONSE.fields_by_name['meta']._options = None
  _NODEDELETERESPONSE.fields_by_name['meta']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _NODEDELETERESPONSE.fields_by_name['rate_limit']._options = None
  _NODEDELETERESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\022\262\364\263\007\r!json_gateway'
  _NODEDELETERESPONSE._options = None
  _NODEDELETERESPONSE._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _NODELISTREQUEST.fields_by_name['filter']._options = None
  _NODELISTREQUEST.fields_by_name['filter']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _NODELISTRESPONSE.fields_by_name['nodes']._options = None
  _NODELISTRESPONSE.fields_by_name['nodes']._serialized_options = b'\362\370\263\007\005\270\363\263\007\001'
  _NODELISTRESPONSE.fields_by_name['rate_limit']._options = None
  _NODELISTRESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\022\262\364\263\007\r!json_gateway'
  _NODE.oneofs_by_name['node']._options = None
  _NODE.oneofs_by_name['node']._serialized_options = b'\252\370\263\007\t\252\370\263\007\004tags\252\370\263\007\t\252\370\263\007\004name'
  _NODE._options = None
  _NODE._serialized_options = b'\372\370\263\007L\302\363\263\007G\242\363\263\007\035tf_examples/node_resource.txt\252\363\263\007 tf_examples/node_data_source.txt\372\370\263\007\005\250\363\263\007\001'
  _RELAY.fields_by_name['id']._options = None
  _RELAY.fields_by_name['id']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _RELAY.fields_by_name['name']._options = None
  _RELAY.fields_by_name['name']._serialized_options = b'\362\370\263\007\n\260\363\263\007\001\320\364\263\007\001'
  _RELAY.fields_by_name['state']._options = None
  _RELAY.fields_by_name['state']._serialized_options = b'\362\370\263\007(\260\363\263\007\001\230\364\263\007\001\262\364\263\007\001*\262\364\263\007\023!terraform-provider'
  _RELAY.fields_by_name['tags']._options = None
  _RELAY.fields_by_name['tags']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _RELAY.fields_by_name['gateway_filter']._options = None
  _RELAY.fields_by_name['gateway_filter']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _RELAY._options = None
  _RELAY._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _GATEWAY.fields_by_name['id']._options = None
  _GATEWAY.fields_by_name['id']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _GATEWAY.fields_by_name['name']._options = None
  _GATEWAY.fields_by_name['name']._serialized_options = b'\362\370\263\007\n\260\363\263\007\001\320\364\263\007\001'
  _GATEWAY.fields_by_name['state']._options = None
  _GATEWAY.fields_by_name['state']._serialized_options = b'\362\370\263\007(\260\363\263\007\001\230\364\263\007\001\262\364\263\007\001*\262\364\263\007\023!terraform-provider'
  _GATEWAY.fields_by_name['listen_address']._options = None
  _GATEWAY.fields_by_name['listen_address']._serialized_options = b'\362\370\263\007\017\260\363\263\007\001\300\363\263\007\001\340\363\263\007\001'
  _GATEWAY.fields_by_name['bind_address']._options = None
  _GATEWAY.fields_by_name['bind_address']._serialized_options = b'\362\370\263\007\017\260\363\263\007\001\340\363\263\007\001\320\364\263\007\001'
  _GATEWAY.fields_by_name['tags']._options = None
  _GATEWAY.fields_by_name['tags']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _GATEWAY.fields_by_name['gateway_filter']._options = None
  _GATEWAY.fields_by_name['gateway_filter']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _GATEWAY._options = None
  _GATEWAY._serialized_options = b'\372\370\263\007\005\250\363\263\007\001'
  _NODES._options = None
  _NODES._serialized_options = b'\312\371\263\007\t\302\371\263\007\004Node\312\371\263\007\007\322\371\263\007\002n-'
  _NODES.methods_by_name['Create']._options = None
  _NODES.methods_by_name['Create']._serialized_options = b'\202\371\263\007\t\242\363\263\007\004post\202\371\263\007\016\252\363\263\007\t/v1/nodes'
  _NODES.methods_by_name['Get']._options = None
  _NODES.methods_by_name['Get']._serialized_options = b'\202\371\263\007\010\242\363\263\007\003get\202\371\263\007\023\252\363\263\007\016/v1/nodes/{id}'
  _NODES.methods_by_name['Update']._options = None
  _NODES.methods_by_name['Update']._serialized_options = b'\202\371\263\007\010\242\363\263\007\003put\202\371\263\007\023\252\363\263\007\016/v1/nodes/{id}'
  _NODES.methods_by_name['Delete']._options = None
  _NODES.methods_by_name['Delete']._serialized_options = b'\202\371\263\007\013\242\363\263\007\006delete\202\371\263\007\023\252\363\263\007\016/v1/nodes/{id}'
  _NODES.methods_by_name['List']._options = None
  _NODES.methods_by_name['List']._serialized_options = b'\202\371\263\007\010\242\363\263\007\003get\202\371\263\007\016\252\363\263\007\t/v1/nodes'
  _NODECREATEREQUEST._serialized_start=58
  _NODECREATEREQUEST._serialized_end=154
  _NODECREATERESPONSE._serialized_start=157
  _NODECREATERESPONSE._serialized_end=400
  _NODEGETREQUEST._serialized_start=402
  _NODEGETREQUEST._serialized_end=480
  _NODEGETRESPONSE._serialized_start=483
  _NODEGETRESPONSE._serialized_end=688
  _NODEUPDATEREQUEST._serialized_start=690
  _NODEUPDATEREQUEST._serialized_end=798
  _NODEUPDATERESPONSE._serialized_start=801
  _NODEUPDATERESPONSE._serialized_end=1012
  _NODEDELETEREQUEST._serialized_start=1014
  _NODEDELETEREQUEST._serialized_end=1098
  _NODEDELETERESPONSE._serialized_start=1101
  _NODEDELETERESPONSE._serialized_end=1276
  _NODELISTREQUEST._serialized_start=1278
  _NODELISTREQUEST._serialized_end=1362
  _NODELISTRESPONSE._serialized_start=1365
  _NODELISTRESPONSE._serialized_end=1549
  _NODE._serialized_start=1552
  _NODE._serialized_end=1749
  _RELAY._serialized_start=1752
  _RELAY._serialized_end=1960
  _GATEWAY._serialized_start=1963
  _GATEWAY._serialized_end=2263
  _NODES._serialized_start=2266
  _NODES._serialized_end=2760
# @@protoc_insertion_point(module_scope)
