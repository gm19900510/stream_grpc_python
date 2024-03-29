# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: filetransfer.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='filetransfer.proto',
  package='filetransfer',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x12\x66iletransfer.proto\x12\x0c\x66iletransfer\"\x1b\n\x0bRequestData\x12\x0c\n\x04text\x18\x01 \x01(\t\"E\n\x0cResponseData\x12\x10\n\x08\x64\x65viceId\x18\x01 \x01(\t\x12\x11\n\trequestId\x18\x02 \x01(\t\x12\x10\n\x08\x66ileData\x18\x03 \x01(\x0c\x32g\n\x13\x46ileTransferService\x12P\n\x13ServerSideStreamFun\x12\x19.filetransfer.RequestData\x1a\x1a.filetransfer.ResponseData\"\x00\x30\x01\x62\x06proto3')
)




_REQUESTDATA = _descriptor.Descriptor(
  name='RequestData',
  full_name='filetransfer.RequestData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='filetransfer.RequestData.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=36,
  serialized_end=63,
)


_RESPONSEDATA = _descriptor.Descriptor(
  name='ResponseData',
  full_name='filetransfer.ResponseData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='deviceId', full_name='filetransfer.ResponseData.deviceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='requestId', full_name='filetransfer.ResponseData.requestId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fileData', full_name='filetransfer.ResponseData.fileData', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=65,
  serialized_end=134,
)

DESCRIPTOR.message_types_by_name['RequestData'] = _REQUESTDATA
DESCRIPTOR.message_types_by_name['ResponseData'] = _RESPONSEDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RequestData = _reflection.GeneratedProtocolMessageType('RequestData', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTDATA,
  __module__ = 'filetransfer_pb2'
  # @@protoc_insertion_point(class_scope:filetransfer.RequestData)
  ))
_sym_db.RegisterMessage(RequestData)

ResponseData = _reflection.GeneratedProtocolMessageType('ResponseData', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSEDATA,
  __module__ = 'filetransfer_pb2'
  # @@protoc_insertion_point(class_scope:filetransfer.ResponseData)
  ))
_sym_db.RegisterMessage(ResponseData)



_FILETRANSFERSERVICE = _descriptor.ServiceDescriptor(
  name='FileTransferService',
  full_name='filetransfer.FileTransferService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=136,
  serialized_end=239,
  methods=[
  _descriptor.MethodDescriptor(
    name='ServerSideStreamFun',
    full_name='filetransfer.FileTransferService.ServerSideStreamFun',
    index=0,
    containing_service=None,
    input_type=_REQUESTDATA,
    output_type=_RESPONSEDATA,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_FILETRANSFERSERVICE)

DESCRIPTOR.services_by_name['FileTransferService'] = _FILETRANSFERSERVICE

# @@protoc_insertion_point(module_scope)
