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
# source: activities.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x61\x63tivities.proto\x12\x02v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\roptions.proto\x1a\nspec.proto\"|\n\x12\x41\x63tivityGetRequest\x12$\n\x04meta\x18\x01 \x01(\x0b\x32\x16.v1.GetRequestMetadata\x12\x16\n\x02id\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:(\xfa\xf8\xb3\x07\x06\xd2\xf3\xb3\x07\x01*\xfa\xf8\xb3\x07\x18\xd2\xf3\xb3\x07\x13!terraform-provider\"\x81\x02\n\x13\x41\x63tivityGetResponse\x12\x31\n\x04meta\x18\x01 \x01(\x0b\x32\x17.v1.GetResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12*\n\x08\x61\x63tivity\x18\x02 \x01(\x0b\x32\x0c.v1.ActivityB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12W\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB,\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway:2\xfa\xf8\xb3\x07\x06\xd2\xf3\xb3\x07\x01*\xfa\xf8\xb3\x07\x18\xd2\xf3\xb3\x07\x13!terraform-provider\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"\x82\x01\n\x13\x41\x63tivityListRequest\x12%\n\x04meta\x18\x01 \x01(\x0b\x32\x17.v1.ListRequestMetadata\x12\x1a\n\x06\x66ilter\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:(\xfa\xf8\xb3\x07\x06\xd2\xf3\xb3\x07\x01*\xfa\xf8\xb3\x07\x18\xd2\xf3\xb3\x07\x13!terraform-provider\"\xef\x01\n\x14\x41\x63tivityListResponse\x12&\n\x04meta\x18\x01 \x01(\x0b\x32\x18.v1.ListResponseMetadata\x12,\n\nactivities\x18\x02 \x03(\x0b\x32\x0c.v1.ActivityB\n\xf2\xf8\xb3\x07\x05\xb8\xf3\xb3\x07\x01\x12W\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB,\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway:(\xfa\xf8\xb3\x07\x06\xd2\xf3\xb3\x07\x01*\xfa\xf8\xb3\x07\x18\xd2\xf3\xb3\x07\x13!terraform-provider\"\x88\x03\n\x08\x41\x63tivity\x12\x16\n\x02id\x18\x01 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x18\n\x04verb\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x1f\n\x0b\x64\x65scription\x18\x03 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12<\n\x0c\x63ompleted_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x30\n\x08\x65ntities\x18\x05 \x03(\x0b\x32\x12.v1.ActivityEntityB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x37\n\nip_address\x18\x06 \x01(\tB#\xf2\xf8\xb3\x07\x1e\xb0\xf3\xb3\x07\x01\xca\xf3\xb3\x07\x14\xc2\xf4\xb3\x07\x0f\n\x02go\x12\tIPAddress\x12,\n\x05\x61\x63tor\x18\x07 \x01(\x0b\x32\x11.v1.ActivityActorB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x1e\n\nuser_agent\x18\x08 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:2\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\xfa\xf8\xb3\x07\x06\xd2\xf3\xb3\x07\x01*\xfa\xf8\xb3\x07\x18\xd2\xf3\xb3\x07\x13!terraform-provider\"\xcc\x01\n\x0e\x41\x63tivityEntity\x12\x16\n\x02id\x18\x01 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x18\n\x04type\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x18\n\x04name\x18\x03 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x19\n\x05\x65mail\x18\x04 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x1f\n\x0b\x65xternal_id\x18\x05 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:2\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\xfa\xf8\xb3\x07\x06\xd2\xf3\xb3\x07\x01*\xfa\xf8\xb3\x07\x18\xd2\xf3\xb3\x07\x13!terraform-provider\"\xdf\x01\n\rActivityActor\x12\x16\n\x02id\x18\x01 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x19\n\x05\x65mail\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x1e\n\nfirst_name\x18\x03 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x1d\n\tlast_name\x18\x04 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12(\n\x14\x61\x63tivity_external_id\x18\x05 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:2\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\xfa\xf8\xb3\x07\x06\xd2\xf3\xb3\x07\x01*\xfa\xf8\xb3\x07\x18\xd2\xf3\xb3\x07\x13!terraform-provider2\xa5\x02\n\nActivities\x12\x62\n\x03Get\x12\x16.v1.ActivityGetRequest\x1a\x17.v1.ActivityGetResponse\"*\x82\xf9\xb3\x07\x08\xa2\xf3\xb3\x07\x03get\x82\xf9\xb3\x07\x18\xaa\xf3\xb3\x07\x13/v1/activities/{id}\x12`\n\x04List\x12\x17.v1.ActivityListRequest\x1a\x18.v1.ActivityListResponse\"%\x82\xf9\xb3\x07\x08\xa2\xf3\xb3\x07\x03get\x82\xf9\xb3\x07\x13\xaa\xf3\xb3\x07\x0e/v1/activities\x1aQ\xca\xf9\xb3\x07\r\xc2\xf9\xb3\x07\x08\x41\x63tivity\xca\xf9\xb3\x07\x08\xd2\xf9\xb3\x07\x03\x61t-\xca\xf9\xb3\x07\x05\xd8\xf9\xb3\x07\x01\xca\xf9\xb3\x07\x06\xca\xf9\xb3\x07\x01*\xca\xf9\xb3\x07\x18\xca\xf9\xb3\x07\x13!terraform-providerB\x8e\x01\n\x19\x63om.strongdm.api.plumbingB\x12\x41\x63tivitiesPlumbingZ5github.com/strongdm/strongdm-sdk-go/v3/internal/v1;v1\xc2\x92\xb4\x07\x06\xa2\x8c\xb4\x07\x01*\xc2\x92\xb4\x07\x18\xa2\x8c\xb4\x07\x13!terraform-providerb\x06proto3')



_ACTIVITYGETREQUEST = DESCRIPTOR.message_types_by_name['ActivityGetRequest']
_ACTIVITYGETRESPONSE = DESCRIPTOR.message_types_by_name['ActivityGetResponse']
_ACTIVITYLISTREQUEST = DESCRIPTOR.message_types_by_name['ActivityListRequest']
_ACTIVITYLISTRESPONSE = DESCRIPTOR.message_types_by_name['ActivityListResponse']
_ACTIVITY = DESCRIPTOR.message_types_by_name['Activity']
_ACTIVITYENTITY = DESCRIPTOR.message_types_by_name['ActivityEntity']
_ACTIVITYACTOR = DESCRIPTOR.message_types_by_name['ActivityActor']
ActivityGetRequest = _reflection.GeneratedProtocolMessageType('ActivityGetRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACTIVITYGETREQUEST,
  '__module__' : 'activities_pb2'
  # @@protoc_insertion_point(class_scope:v1.ActivityGetRequest)
  })
_sym_db.RegisterMessage(ActivityGetRequest)

ActivityGetResponse = _reflection.GeneratedProtocolMessageType('ActivityGetResponse', (_message.Message,), {
  'DESCRIPTOR' : _ACTIVITYGETRESPONSE,
  '__module__' : 'activities_pb2'
  # @@protoc_insertion_point(class_scope:v1.ActivityGetResponse)
  })
_sym_db.RegisterMessage(ActivityGetResponse)

ActivityListRequest = _reflection.GeneratedProtocolMessageType('ActivityListRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACTIVITYLISTREQUEST,
  '__module__' : 'activities_pb2'
  # @@protoc_insertion_point(class_scope:v1.ActivityListRequest)
  })
_sym_db.RegisterMessage(ActivityListRequest)

ActivityListResponse = _reflection.GeneratedProtocolMessageType('ActivityListResponse', (_message.Message,), {
  'DESCRIPTOR' : _ACTIVITYLISTRESPONSE,
  '__module__' : 'activities_pb2'
  # @@protoc_insertion_point(class_scope:v1.ActivityListResponse)
  })
_sym_db.RegisterMessage(ActivityListResponse)

Activity = _reflection.GeneratedProtocolMessageType('Activity', (_message.Message,), {
  'DESCRIPTOR' : _ACTIVITY,
  '__module__' : 'activities_pb2'
  # @@protoc_insertion_point(class_scope:v1.Activity)
  })
_sym_db.RegisterMessage(Activity)

ActivityEntity = _reflection.GeneratedProtocolMessageType('ActivityEntity', (_message.Message,), {
  'DESCRIPTOR' : _ACTIVITYENTITY,
  '__module__' : 'activities_pb2'
  # @@protoc_insertion_point(class_scope:v1.ActivityEntity)
  })
_sym_db.RegisterMessage(ActivityEntity)

ActivityActor = _reflection.GeneratedProtocolMessageType('ActivityActor', (_message.Message,), {
  'DESCRIPTOR' : _ACTIVITYACTOR,
  '__module__' : 'activities_pb2'
  # @@protoc_insertion_point(class_scope:v1.ActivityActor)
  })
_sym_db.RegisterMessage(ActivityActor)

_ACTIVITIES = DESCRIPTOR.services_by_name['Activities']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031com.strongdm.api.plumbingB\022ActivitiesPlumbingZ5github.com/strongdm/strongdm-sdk-go/v3/internal/v1;v1\302\222\264\007\006\242\214\264\007\001*\302\222\264\007\030\242\214\264\007\023!terraform-provider'
  _ACTIVITYGETREQUEST.fields_by_name['id']._options = None
  _ACTIVITYGETREQUEST.fields_by_name['id']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACTIVITYGETREQUEST._options = None
  _ACTIVITYGETREQUEST._serialized_options = b'\372\370\263\007\006\322\363\263\007\001*\372\370\263\007\030\322\363\263\007\023!terraform-provider'
  _ACTIVITYGETRESPONSE.fields_by_name['meta']._options = None
  _ACTIVITYGETRESPONSE.fields_by_name['meta']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACTIVITYGETRESPONSE.fields_by_name['activity']._options = None
  _ACTIVITYGETRESPONSE.fields_by_name['activity']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACTIVITYGETRESPONSE.fields_by_name['rate_limit']._options = None
  _ACTIVITYGETRESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\022\262\364\263\007\r!json_gateway'
  _ACTIVITYGETRESPONSE._options = None
  _ACTIVITYGETRESPONSE._serialized_options = b'\372\370\263\007\006\322\363\263\007\001*\372\370\263\007\030\322\363\263\007\023!terraform-provider\372\370\263\007\005\250\363\263\007\001'
  _ACTIVITYLISTREQUEST.fields_by_name['filter']._options = None
  _ACTIVITYLISTREQUEST.fields_by_name['filter']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACTIVITYLISTREQUEST._options = None
  _ACTIVITYLISTREQUEST._serialized_options = b'\372\370\263\007\006\322\363\263\007\001*\372\370\263\007\030\322\363\263\007\023!terraform-provider'
  _ACTIVITYLISTRESPONSE.fields_by_name['activities']._options = None
  _ACTIVITYLISTRESPONSE.fields_by_name['activities']._serialized_options = b'\362\370\263\007\005\270\363\263\007\001'
  _ACTIVITYLISTRESPONSE.fields_by_name['rate_limit']._options = None
  _ACTIVITYLISTRESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\022\262\364\263\007\r!json_gateway'
  _ACTIVITYLISTRESPONSE._options = None
  _ACTIVITYLISTRESPONSE._serialized_options = b'\372\370\263\007\006\322\363\263\007\001*\372\370\263\007\030\322\363\263\007\023!terraform-provider'
  _ACTIVITY.fields_by_name['id']._options = None
  _ACTIVITY.fields_by_name['id']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACTIVITY.fields_by_name['verb']._options = None
  _ACTIVITY.fields_by_name['verb']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACTIVITY.fields_by_name['description']._options = None
  _ACTIVITY.fields_by_name['description']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACTIVITY.fields_by_name['completed_at']._options = None
  _ACTIVITY.fields_by_name['completed_at']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACTIVITY.fields_by_name['entities']._options = None
  _ACTIVITY.fields_by_name['entities']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACTIVITY.fields_by_name['ip_address']._options = None
  _ACTIVITY.fields_by_name['ip_address']._serialized_options = b'\362\370\263\007\036\260\363\263\007\001\312\363\263\007\024\302\364\263\007\017\n\002go\022\tIPAddress'
  _ACTIVITY.fields_by_name['actor']._options = None
  _ACTIVITY.fields_by_name['actor']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACTIVITY.fields_by_name['user_agent']._options = None
  _ACTIVITY.fields_by_name['user_agent']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACTIVITY._options = None
  _ACTIVITY._serialized_options = b'\372\370\263\007\005\250\363\263\007\001\372\370\263\007\006\322\363\263\007\001*\372\370\263\007\030\322\363\263\007\023!terraform-provider'
  _ACTIVITYENTITY.fields_by_name['id']._options = None
  _ACTIVITYENTITY.fields_by_name['id']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACTIVITYENTITY.fields_by_name['type']._options = None
  _ACTIVITYENTITY.fields_by_name['type']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACTIVITYENTITY.fields_by_name['name']._options = None
  _ACTIVITYENTITY.fields_by_name['name']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACTIVITYENTITY.fields_by_name['email']._options = None
  _ACTIVITYENTITY.fields_by_name['email']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACTIVITYENTITY.fields_by_name['external_id']._options = None
  _ACTIVITYENTITY.fields_by_name['external_id']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACTIVITYENTITY._options = None
  _ACTIVITYENTITY._serialized_options = b'\372\370\263\007\005\250\363\263\007\001\372\370\263\007\006\322\363\263\007\001*\372\370\263\007\030\322\363\263\007\023!terraform-provider'
  _ACTIVITYACTOR.fields_by_name['id']._options = None
  _ACTIVITYACTOR.fields_by_name['id']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACTIVITYACTOR.fields_by_name['email']._options = None
  _ACTIVITYACTOR.fields_by_name['email']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACTIVITYACTOR.fields_by_name['first_name']._options = None
  _ACTIVITYACTOR.fields_by_name['first_name']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACTIVITYACTOR.fields_by_name['last_name']._options = None
  _ACTIVITYACTOR.fields_by_name['last_name']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACTIVITYACTOR.fields_by_name['activity_external_id']._options = None
  _ACTIVITYACTOR.fields_by_name['activity_external_id']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _ACTIVITYACTOR._options = None
  _ACTIVITYACTOR._serialized_options = b'\372\370\263\007\005\250\363\263\007\001\372\370\263\007\006\322\363\263\007\001*\372\370\263\007\030\322\363\263\007\023!terraform-provider'
  _ACTIVITIES._options = None
  _ACTIVITIES._serialized_options = b'\312\371\263\007\r\302\371\263\007\010Activity\312\371\263\007\010\322\371\263\007\003at-\312\371\263\007\005\330\371\263\007\001\312\371\263\007\006\312\371\263\007\001*\312\371\263\007\030\312\371\263\007\023!terraform-provider'
  _ACTIVITIES.methods_by_name['Get']._options = None
  _ACTIVITIES.methods_by_name['Get']._serialized_options = b'\202\371\263\007\010\242\363\263\007\003get\202\371\263\007\030\252\363\263\007\023/v1/activities/{id}'
  _ACTIVITIES.methods_by_name['List']._options = None
  _ACTIVITIES.methods_by_name['List']._serialized_options = b'\202\371\263\007\010\242\363\263\007\003get\202\371\263\007\023\252\363\263\007\016/v1/activities'
  _ACTIVITYGETREQUEST._serialized_start=84
  _ACTIVITYGETREQUEST._serialized_end=208
  _ACTIVITYGETRESPONSE._serialized_start=211
  _ACTIVITYGETRESPONSE._serialized_end=468
  _ACTIVITYLISTREQUEST._serialized_start=471
  _ACTIVITYLISTREQUEST._serialized_end=601
  _ACTIVITYLISTRESPONSE._serialized_start=604
  _ACTIVITYLISTRESPONSE._serialized_end=843
  _ACTIVITY._serialized_start=846
  _ACTIVITY._serialized_end=1238
  _ACTIVITYENTITY._serialized_start=1241
  _ACTIVITYENTITY._serialized_end=1445
  _ACTIVITYACTOR._serialized_start=1448
  _ACTIVITYACTOR._serialized_end=1671
  _ACTIVITIES._serialized_start=1674
  _ACTIVITIES._serialized_end=1967
# @@protoc_insertion_point(module_scope)
