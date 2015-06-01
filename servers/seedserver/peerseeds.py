# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: peerseeds.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='peerseeds.proto',
  package='',
  serialized_pb=_b('\n\x0fpeerseeds.proto\"M\n\x0cPeerSeedData\x12\x12\n\nip_address\x18\x01 \x02(\t\x12\x0c\n\x04port\x18\x02 \x02(\r\x12\x1b\n\x08services\x18\x03 \x03(\x0e\x32\t.Services\"H\n\tPeerSeeds\x12\x1b\n\x04seed\x18\x01 \x03(\x0b\x32\r.PeerSeedData\x12\x11\n\ttimestamp\x18\x02 \x02(\x04\x12\x0b\n\x03net\x18\x03 \x02(\t**\n\x08Services\x12\r\n\tNODE_LITE\x10\x01\x12\x0f\n\x0bNODE_SERVER\x10\x02')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_SERVICES = _descriptor.EnumDescriptor(
  name='Services',
  full_name='Services',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NODE_LITE', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NODE_SERVER', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=172,
  serialized_end=214,
)
_sym_db.RegisterEnumDescriptor(_SERVICES)

Services = enum_type_wrapper.EnumTypeWrapper(_SERVICES)
NODE_LITE = 1
NODE_SERVER = 2



_PEERSEEDDATA = _descriptor.Descriptor(
  name='PeerSeedData',
  full_name='PeerSeedData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ip_address', full_name='PeerSeedData.ip_address', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='port', full_name='PeerSeedData.port', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='services', full_name='PeerSeedData.services', index=2,
      number=3, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=19,
  serialized_end=96,
)


_PEERSEEDS = _descriptor.Descriptor(
  name='PeerSeeds',
  full_name='PeerSeeds',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='seed', full_name='PeerSeeds.seed', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='PeerSeeds.timestamp', index=1,
      number=2, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='net', full_name='PeerSeeds.net', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=98,
  serialized_end=170,
)

_PEERSEEDDATA.fields_by_name['services'].enum_type = _SERVICES
_PEERSEEDS.fields_by_name['seed'].message_type = _PEERSEEDDATA
DESCRIPTOR.message_types_by_name['PeerSeedData'] = _PEERSEEDDATA
DESCRIPTOR.message_types_by_name['PeerSeeds'] = _PEERSEEDS
DESCRIPTOR.enum_types_by_name['Services'] = _SERVICES

PeerSeedData = _reflection.GeneratedProtocolMessageType('PeerSeedData', (_message.Message,), dict(
  DESCRIPTOR = _PEERSEEDDATA,
  __module__ = 'peerseeds_pb2'
  # @@protoc_insertion_point(class_scope:PeerSeedData)
  ))
_sym_db.RegisterMessage(PeerSeedData)

PeerSeeds = _reflection.GeneratedProtocolMessageType('PeerSeeds', (_message.Message,), dict(
  DESCRIPTOR = _PEERSEEDS,
  __module__ = 'peerseeds_pb2'
  # @@protoc_insertion_point(class_scope:PeerSeeds)
  ))
_sym_db.RegisterMessage(PeerSeeds)


# @@protoc_insertion_point(module_scope)
