# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pkg/protocol/core/template-space/template_space.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bk_bscp.grpc_lib.core.base import base_pb2 as pkg_dot_protocol_dot_core_dot_base_dot_base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5pkg/protocol/core/template-space/template_space.proto\x12\x04pbts\x1a!pkg/protocol/core/base/base.proto\"\x99\x01\n\rTemplateSpace\x12\n\n\x02id\x18\x01 \x01(\r\x12%\n\x04spec\x18\x02 \x01(\x0b\x32\x17.pbts.TemplateSpaceSpec\x12\x31\n\nattachment\x18\x03 \x01(\x0b\x32\x1d.pbts.TemplateSpaceAttachment\x12\"\n\x08revision\x18\x04 \x01(\x0b\x32\x10.pbbase.Revision\"/\n\x11TemplateSpaceSpec\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04memo\x18\x02 \x01(\t\")\n\x17TemplateSpaceAttachment\x12\x0e\n\x06\x62iz_id\x18\x01 \x01(\rB_Z]github.com/TencentBlueKing/bk-bcs/bcs-services/bcs-bscp/pkg/protocol/core/template-space;pbtsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pkg.protocol.core.template_space.template_space_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z]github.com/TencentBlueKing/bk-bcs/bcs-services/bcs-bscp/pkg/protocol/core/template-space;pbts'
  _globals['_TEMPLATESPACE']._serialized_start=99
  _globals['_TEMPLATESPACE']._serialized_end=252
  _globals['_TEMPLATESPACESPEC']._serialized_start=254
  _globals['_TEMPLATESPACESPEC']._serialized_end=301
  _globals['_TEMPLATESPACEATTACHMENT']._serialized_start=303
  _globals['_TEMPLATESPACEATTACHMENT']._serialized_end=344
# @@protoc_insertion_point(module_scope)
