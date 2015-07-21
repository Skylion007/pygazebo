# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: geometry.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import boxgeom_pb2
import cylindergeom_pb2
import spheregeom_pb2
import planegeom_pb2
import imagegeom_pb2
import heightmapgeom_pb2
import meshgeom_pb2
import vector3d_pb2
import polylinegeom_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='geometry.proto',
  package='gazebo.msgs',
  serialized_pb='\n\x0egeometry.proto\x12\x0bgazebo.msgs\x1a\rboxgeom.proto\x1a\x12\x63ylindergeom.proto\x1a\x10spheregeom.proto\x1a\x0fplanegeom.proto\x1a\x0fimagegeom.proto\x1a\x13heightmapgeom.proto\x1a\x0emeshgeom.proto\x1a\x0evector3d.proto\x1a\x12polylinegeom.proto\"\xb5\x04\n\x08Geometry\x12(\n\x04type\x18\x01 \x01(\x0e\x32\x1a.gazebo.msgs.Geometry.Type\x12!\n\x03\x62ox\x18\x02 \x01(\x0b\x32\x14.gazebo.msgs.BoxGeom\x12+\n\x08\x63ylinder\x18\x03 \x01(\x0b\x32\x19.gazebo.msgs.CylinderGeom\x12%\n\x05plane\x18\x04 \x01(\x0b\x32\x16.gazebo.msgs.PlaneGeom\x12\'\n\x06sphere\x18\x05 \x01(\x0b\x32\x17.gazebo.msgs.SphereGeom\x12%\n\x05image\x18\x06 \x01(\x0b\x32\x16.gazebo.msgs.ImageGeom\x12-\n\theightmap\x18\x07 \x01(\x0b\x32\x1a.gazebo.msgs.HeightmapGeom\x12#\n\x04mesh\x18\x08 \x01(\x0b\x32\x15.gazebo.msgs.MeshGeom\x12%\n\x06points\x18\t \x03(\x0b\x32\x15.gazebo.msgs.Vector3d\x12\'\n\x08polyline\x18\n \x01(\x0b\x32\x15.gazebo.msgs.Polyline\"\x93\x01\n\x04Type\x12\x07\n\x03\x42OX\x10\x01\x12\x0c\n\x08\x43YLINDER\x10\x02\x12\n\n\x06SPHERE\x10\x03\x12\t\n\x05PLANE\x10\x04\x12\t\n\x05IMAGE\x10\x05\x12\r\n\tHEIGHTMAP\x10\x06\x12\x08\n\x04MESH\x10\x07\x12\x10\n\x0cTRIANGLE_FAN\x10\x08\x12\x0e\n\nLINE_STRIP\x10\t\x12\x0c\n\x08POLYLINE\x10\n\x12\t\n\x05\x45MPTY\x10\x0b')



_GEOMETRY_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='gazebo.msgs.Geometry.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BOX', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CYLINDER', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SPHERE', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLANE', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IMAGE', index=4, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HEIGHTMAP', index=5, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MESH', index=6, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRIANGLE_FAN', index=7, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LINE_STRIP', index=8, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POLYLINE', index=9, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMPTY', index=10, number=11,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=610,
  serialized_end=757,
)


_GEOMETRY = _descriptor.Descriptor(
  name='Geometry',
  full_name='gazebo.msgs.Geometry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='gazebo.msgs.Geometry.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='box', full_name='gazebo.msgs.Geometry.box', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cylinder', full_name='gazebo.msgs.Geometry.cylinder', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='plane', full_name='gazebo.msgs.Geometry.plane', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sphere', full_name='gazebo.msgs.Geometry.sphere', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='image', full_name='gazebo.msgs.Geometry.image', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='heightmap', full_name='gazebo.msgs.Geometry.heightmap', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mesh', full_name='gazebo.msgs.Geometry.mesh', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='points', full_name='gazebo.msgs.Geometry.points', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='polyline', full_name='gazebo.msgs.Geometry.polyline', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GEOMETRY_TYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=192,
  serialized_end=757,
)

_GEOMETRY.fields_by_name['type'].enum_type = _GEOMETRY_TYPE
_GEOMETRY.fields_by_name['box'].message_type = boxgeom_pb2._BOXGEOM
_GEOMETRY.fields_by_name['cylinder'].message_type = cylindergeom_pb2._CYLINDERGEOM
_GEOMETRY.fields_by_name['plane'].message_type = planegeom_pb2._PLANEGEOM
_GEOMETRY.fields_by_name['sphere'].message_type = spheregeom_pb2._SPHEREGEOM
_GEOMETRY.fields_by_name['image'].message_type = imagegeom_pb2._IMAGEGEOM
_GEOMETRY.fields_by_name['heightmap'].message_type = heightmapgeom_pb2._HEIGHTMAPGEOM
_GEOMETRY.fields_by_name['mesh'].message_type = meshgeom_pb2._MESHGEOM
_GEOMETRY.fields_by_name['points'].message_type = vector3d_pb2._VECTOR3D
_GEOMETRY.fields_by_name['polyline'].message_type = polylinegeom_pb2._POLYLINE
_GEOMETRY_TYPE.containing_type = _GEOMETRY;
DESCRIPTOR.message_types_by_name['Geometry'] = _GEOMETRY

class Geometry(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GEOMETRY

  # @@protoc_insertion_point(class_scope:gazebo.msgs.Geometry)


# @@protoc_insertion_point(module_scope)
