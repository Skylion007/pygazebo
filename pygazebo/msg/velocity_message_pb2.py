# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: velocity_message.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import vector3d_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='velocity_message.proto',
  package='model_velocity.msgs',
  serialized_pb='\n\x16velocity_message.proto\x12\x13model_velocity.msgs\x1a\x0evector3d.proto\"D\n\nModelVel_V\x12\x36\n\x07linkage\x18\x01 \x03(\x0b\x32%.model_velocity.msgs.ModelVelResponse\"u\n\x10ModelVelResponse\x12\x0c\n\x04name\x18\x01 \x02(\t\x12)\n\nangularVel\x18\x02 \x01(\x0b\x32\x15.gazebo.msgs.Vector3d\x12(\n\tlinearVel\x18\x03 \x01(\x0b\x32\x15.gazebo.msgs.Vector3d')




_MODELVEL_V = _descriptor.Descriptor(
  name='ModelVel_V',
  full_name='model_velocity.msgs.ModelVel_V',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='linkage', full_name='model_velocity.msgs.ModelVel_V.linkage', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=63,
  serialized_end=131,
)


_MODELVELRESPONSE = _descriptor.Descriptor(
  name='ModelVelResponse',
  full_name='model_velocity.msgs.ModelVelResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='model_velocity.msgs.ModelVelResponse.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='angularVel', full_name='model_velocity.msgs.ModelVelResponse.angularVel', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='linearVel', full_name='model_velocity.msgs.ModelVelResponse.linearVel', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=133,
  serialized_end=250,
)

_MODELVEL_V.fields_by_name['linkage'].message_type = _MODELVELRESPONSE
_MODELVELRESPONSE.fields_by_name['angularVel'].message_type = vector3d_pb2._VECTOR3D
_MODELVELRESPONSE.fields_by_name['linearVel'].message_type = vector3d_pb2._VECTOR3D
DESCRIPTOR.message_types_by_name['ModelVel_V'] = _MODELVEL_V
DESCRIPTOR.message_types_by_name['ModelVelResponse'] = _MODELVELRESPONSE

class ModelVel_V(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MODELVEL_V

  # @@protoc_insertion_point(class_scope:model_velocity.msgs.ModelVel_V)

class ModelVelResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MODELVELRESPONSE

  # @@protoc_insertion_point(class_scope:model_velocity.msgs.ModelVelResponse)


# @@protoc_insertion_point(module_scope)