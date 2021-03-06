# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: c2s.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='c2s.proto',
  package='tud.seemuh.nfcgate.network.c2s',
  syntax='proto2',
  serialized_pb=_b('\n\tc2s.proto\x12\x1etud.seemuh.nfcgate.network.c2s\"\x8a\x06\n\x07Session\x12\x45\n\x06opcode\x18\x01 \x02(\x0e\x32\x35.tud.seemuh.nfcgate.network.c2s.Session.SessionOpcode\x12\x16\n\x0esession_secret\x18\x02 \x01(\t\x12X\n\x07\x65rrcode\x18\x03 \x02(\x0e\x32\x38.tud.seemuh.nfcgate.network.c2s.Session.SessionErrorCode:\rERROR_NOERROR\"\x91\x02\n\rSessionOpcode\x12\x12\n\x0eSESSION_CREATE\x10\x00\x12\x1a\n\x16SESSION_CREATE_SUCCESS\x10\x01\x12\x17\n\x13SESSION_CREATE_FAIL\x10\x02\x12\x10\n\x0cSESSION_JOIN\x10\x03\x12\x18\n\x14SESSION_JOIN_SUCCESS\x10\x04\x12\x15\n\x11SESSION_JOIN_FAIL\x10\x05\x12\x11\n\rSESSION_LEAVE\x10\x06\x12\x19\n\x15SESSION_LEAVE_SUCCESS\x10\x07\x12\x16\n\x12SESSION_LEAVE_FAIL\x10\x08\x12\x17\n\x13SESSION_PEER_JOINED\x10\t\x12\x15\n\x11SESSION_PEER_LEFT\x10\n\"\xb1\x02\n\x10SessionErrorCode\x12\x11\n\rERROR_NOERROR\x10\x00\x12\x17\n\x13\x45RROR_CREATE_UNKOWN\x10\x01\x12$\n ERROR_CREATE_ALREADY_HAS_SESSION\x10\x02\x12\x16\n\x12\x45RROR_JOIN_UNKNOWN\x10\x03\x12\x1d\n\x19\x45RROR_JOIN_UNKNOWN_SECRET\x10\x04\x12\x1b\n\x17\x45RROR_JOIN_SESSION_FULL\x10\x05\x12\"\n\x1e\x45RROR_JOIN_ALREADY_HAS_SESSION\x10\x06\x12\x17\n\x13\x45RROR_LEAVE_UNKNOWN\x10\x07\x12\x1e\n\x1a\x45RROR_LEAVE_UNKNOWN_SECRET\x10\x08\x12\x1a\n\x16\x45RROR_LEAVE_NOT_JOINED\x10\t\"\xd4\x01\n\x04\x44\x61ta\x12R\n\x07\x65rrcode\x18\x01 \x02(\x0e\x32\x32.tud.seemuh.nfcgate.network.c2s.Data.DataErrorCode:\rERROR_NOERROR\x12\x0c\n\x04\x62lob\x18\x02 \x01(\x0c\"j\n\rDataErrorCode\x12\x11\n\rERROR_NOERROR\x10\x00\x12\x11\n\rERROR_UNKNOWN\x10\x01\x12\x14\n\x10\x45RROR_NO_SESSION\x10\x02\x12\x1d\n\x19\x45RROR_TRANSMISSION_FAILED\x10\x03')
)



_SESSION_SESSIONOPCODE = _descriptor.EnumDescriptor(
  name='SessionOpcode',
  full_name='tud.seemuh.nfcgate.network.c2s.Session.SessionOpcode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SESSION_CREATE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SESSION_CREATE_SUCCESS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SESSION_CREATE_FAIL', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SESSION_JOIN', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SESSION_JOIN_SUCCESS', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SESSION_JOIN_FAIL', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SESSION_LEAVE', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SESSION_LEAVE_SUCCESS', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SESSION_LEAVE_FAIL', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SESSION_PEER_JOINED', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SESSION_PEER_LEFT', index=10, number=10,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=243,
  serialized_end=516,
)
_sym_db.RegisterEnumDescriptor(_SESSION_SESSIONOPCODE)

_SESSION_SESSIONERRORCODE = _descriptor.EnumDescriptor(
  name='SessionErrorCode',
  full_name='tud.seemuh.nfcgate.network.c2s.Session.SessionErrorCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ERROR_NOERROR', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_CREATE_UNKOWN', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_CREATE_ALREADY_HAS_SESSION', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_JOIN_UNKNOWN', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_JOIN_UNKNOWN_SECRET', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_JOIN_SESSION_FULL', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_JOIN_ALREADY_HAS_SESSION', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_LEAVE_UNKNOWN', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_LEAVE_UNKNOWN_SECRET', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_LEAVE_NOT_JOINED', index=9, number=9,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=519,
  serialized_end=824,
)
_sym_db.RegisterEnumDescriptor(_SESSION_SESSIONERRORCODE)

_DATA_DATAERRORCODE = _descriptor.EnumDescriptor(
  name='DataErrorCode',
  full_name='tud.seemuh.nfcgate.network.c2s.Data.DataErrorCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ERROR_NOERROR', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_UNKNOWN', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_NO_SESSION', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_TRANSMISSION_FAILED', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=933,
  serialized_end=1039,
)
_sym_db.RegisterEnumDescriptor(_DATA_DATAERRORCODE)


_SESSION = _descriptor.Descriptor(
  name='Session',
  full_name='tud.seemuh.nfcgate.network.c2s.Session',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='opcode', full_name='tud.seemuh.nfcgate.network.c2s.Session.opcode', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='session_secret', full_name='tud.seemuh.nfcgate.network.c2s.Session.session_secret', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='errcode', full_name='tud.seemuh.nfcgate.network.c2s.Session.errcode', index=2,
      number=3, type=14, cpp_type=8, label=2,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SESSION_SESSIONOPCODE,
    _SESSION_SESSIONERRORCODE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=46,
  serialized_end=824,
)


_DATA = _descriptor.Descriptor(
  name='Data',
  full_name='tud.seemuh.nfcgate.network.c2s.Data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='errcode', full_name='tud.seemuh.nfcgate.network.c2s.Data.errcode', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='blob', full_name='tud.seemuh.nfcgate.network.c2s.Data.blob', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DATA_DATAERRORCODE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=827,
  serialized_end=1039,
)

_SESSION.fields_by_name['opcode'].enum_type = _SESSION_SESSIONOPCODE
_SESSION.fields_by_name['errcode'].enum_type = _SESSION_SESSIONERRORCODE
_SESSION_SESSIONOPCODE.containing_type = _SESSION
_SESSION_SESSIONERRORCODE.containing_type = _SESSION
_DATA.fields_by_name['errcode'].enum_type = _DATA_DATAERRORCODE
_DATA_DATAERRORCODE.containing_type = _DATA
DESCRIPTOR.message_types_by_name['Session'] = _SESSION
DESCRIPTOR.message_types_by_name['Data'] = _DATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Session = _reflection.GeneratedProtocolMessageType('Session', (_message.Message,), dict(
  DESCRIPTOR = _SESSION,
  __module__ = 'c2s_pb2'
  # @@protoc_insertion_point(class_scope:tud.seemuh.nfcgate.network.c2s.Session)
  ))
_sym_db.RegisterMessage(Session)

Data = _reflection.GeneratedProtocolMessageType('Data', (_message.Message,), dict(
  DESCRIPTOR = _DATA,
  __module__ = 'c2s_pb2'
  # @@protoc_insertion_point(class_scope:tud.seemuh.nfcgate.network.c2s.Data)
  ))
_sym_db.RegisterMessage(Data)


# @@protoc_insertion_point(module_scope)
