# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pose.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import vector3d_pb2
import quaternion_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pose.proto',
  package='gazebo.msgs',
  serialized_pb='\n\npose.proto\x12\x0bgazebo.msgs\x1a\x0evector3d.proto\x1a\x10quaternion.proto\"w\n\x04Pose\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\r\x12\'\n\x08position\x18\x03 \x02(\x0b\x32\x15.gazebo.msgs.Vector3d\x12,\n\x0borientation\x18\x04 \x02(\x0b\x32\x17.gazebo.msgs.Quaternion')




_POSE = _descriptor.Descriptor(
  name='Pose',
  full_name='gazebo.msgs.Pose',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='gazebo.msgs.Pose.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='gazebo.msgs.Pose.id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='position', full_name='gazebo.msgs.Pose.position', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='orientation', full_name='gazebo.msgs.Pose.orientation', index=3,
      number=4, type=11, cpp_type=10, label=2,
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
  serialized_start=61,
  serialized_end=180,
)

_POSE.fields_by_name['position'].message_type = vector3d_pb2._VECTOR3D
_POSE.fields_by_name['orientation'].message_type = quaternion_pb2._QUATERNION
DESCRIPTOR.message_types_by_name['Pose'] = _POSE

class Pose(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _POSE

  # @@protoc_insertion_point(class_scope:gazebo.msgs.Pose)


# @@protoc_insertion_point(module_scope)
