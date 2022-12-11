# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tapi.proto\x12\x06\x61pi.v1\"\xa2\x01\n\x07\x44\x61taset\x12\"\n\x04type\x18\x01 \x01(\x0e\x32\x14.api.v1.EmulatorType\x12-\n\x07options\x18\x02 \x03(\x0b\x32\x1c.api.v1.Dataset.OptionsEntry\x12\x14\n\x0c\x64\x61taset_path\x18\x03 \x01(\t\x1a.\n\x0cOptionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"u\n\x0eRunCodeRequest\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\x12\x18\n\x03sdk\x18\x02 \x01(\x0e\x32\x0b.api.v1.Sdk\x12\x18\n\x10pipeline_options\x18\x03 \x01(\t\x12!\n\x08\x64\x61tasets\x18\x04 \x03(\x0b\x32\x0f.api.v1.Dataset\"(\n\x0fRunCodeResponse\x12\x15\n\rpipeline_uuid\x18\x01 \x01(\t\"+\n\x12\x43heckStatusRequest\x12\x15\n\rpipeline_uuid\x18\x01 \x01(\t\"5\n\x13\x43heckStatusResponse\x12\x1e\n\x06status\x18\x01 \x01(\x0e\x32\x0e.api.v1.Status\"3\n\x1aGetValidationOutputRequest\x12\x15\n\rpipeline_uuid\x18\x01 \x01(\t\"-\n\x1bGetValidationOutputResponse\x12\x0e\n\x06output\x18\x01 \x01(\t\"4\n\x1bGetPreparationOutputRequest\x12\x15\n\rpipeline_uuid\x18\x01 \x01(\t\".\n\x1cGetPreparationOutputResponse\x12\x0e\n\x06output\x18\x01 \x01(\t\"0\n\x17GetCompileOutputRequest\x12\x15\n\rpipeline_uuid\x18\x01 \x01(\t\"*\n\x18GetCompileOutputResponse\x12\x0e\n\x06output\x18\x01 \x01(\t\",\n\x13GetRunOutputRequest\x12\x15\n\rpipeline_uuid\x18\x01 \x01(\t\"&\n\x14GetRunOutputResponse\x12\x0e\n\x06output\x18\x01 \x01(\t\"+\n\x12GetRunErrorRequest\x12\x15\n\rpipeline_uuid\x18\x01 \x01(\t\"%\n\x13GetRunErrorResponse\x12\x0e\n\x06output\x18\x01 \x01(\t\"\'\n\x0eGetLogsRequest\x12\x15\n\rpipeline_uuid\x18\x01 \x01(\t\"!\n\x0fGetLogsResponse\x12\x0e\n\x06output\x18\x01 \x01(\t\"(\n\x0fGetGraphRequest\x12\x15\n\rpipeline_uuid\x18\x01 \x01(\t\"!\n\x10GetGraphResponse\x12\r\n\x05graph\x18\x01 \x01(\t\"&\n\rCancelRequest\x12\x15\n\rpipeline_uuid\x18\x01 \x01(\t\"\x10\n\x0e\x43\x61ncelResponse\"\xd4\x02\n\x11PrecompiledObject\x12\x12\n\ncloud_path\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12+\n\x04type\x18\x04 \x01(\x0e\x32\x1d.api.v1.PrecompiledObjectType\x12\x18\n\x10pipeline_options\x18\x05 \x01(\t\x12\x0c\n\x04link\x18\x06 \x01(\t\x12\x11\n\tmultifile\x18\x07 \x01(\x08\x12\x14\n\x0c\x63ontext_line\x18\x08 \x01(\x05\x12\x17\n\x0f\x64\x65\x66\x61ult_example\x18\t \x01(\x08\x12\x18\n\x03sdk\x18\n \x01(\x0e\x32\x0b.api.v1.Sdk\x12&\n\ncomplexity\x18\x0b \x01(\x0e\x32\x12.api.v1.Complexity\x12\x0c\n\x04tags\x18\x0c \x03(\t\x12!\n\x08\x64\x61tasets\x18\r \x03(\x0b\x32\x0f.api.v1.Dataset\"\xb2\x01\n\nCategories\x12\x18\n\x03sdk\x18\x01 \x01(\x0e\x32\x0b.api.v1.Sdk\x12/\n\ncategories\x18\x02 \x03(\x0b\x32\x1b.api.v1.Categories.Category\x1aY\n\x08\x43\x61tegory\x12\x15\n\rcategory_name\x18\x01 \x01(\t\x12\x36\n\x13precompiled_objects\x18\x02 \x03(\x0b\x32\x19.api.v1.PrecompiledObject\"J\n\x1cGetPrecompiledObjectsRequest\x12\x18\n\x03sdk\x18\x01 \x01(\x0e\x32\x0b.api.v1.Sdk\x12\x10\n\x08\x63\x61tegory\x18\x02 \x01(\t\"1\n\x1bGetPrecompiledObjectRequest\x12\x12\n\ncloud_path\x18\x01 \x01(\t\"5\n\x1fGetPrecompiledObjectCodeRequest\x12\x12\n\ncloud_path\x18\x01 \x01(\t\"7\n!GetPrecompiledObjectOutputRequest\x12\x12\n\ncloud_path\x18\x01 \x01(\t\"5\n\x1fGetPrecompiledObjectLogsRequest\x12\x12\n\ncloud_path\x18\x01 \x01(\t\"6\n GetPrecompiledObjectGraphRequest\x12\x12\n\ncloud_path\x18\x01 \x01(\t\">\n\"GetDefaultPrecompiledObjectRequest\x12\x18\n\x03sdk\x18\x01 \x01(\x0e\x32\x0b.api.v1.Sdk\"K\n\x1dGetPrecompiledObjectsResponse\x12*\n\x0esdk_categories\x18\x01 \x03(\x0b\x32\x12.api.v1.Categories\"U\n\x1cGetPrecompiledObjectResponse\x12\x35\n\x12precompiled_object\x18\x01 \x01(\x0b\x32\x19.api.v1.PrecompiledObject\"0\n GetPrecompiledObjectCodeResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\"4\n\"GetPrecompiledObjectOutputResponse\x12\x0e\n\x06output\x18\x01 \x01(\t\"2\n GetPrecompiledObjectLogsResponse\x12\x0e\n\x06output\x18\x01 \x01(\t\"2\n!GetPrecompiledObjectGraphResponse\x12\r\n\x05graph\x18\x01 \x01(\t\"\\\n#GetDefaultPrecompiledObjectResponse\x12\x35\n\x12precompiled_object\x18\x01 \x01(\x0b\x32\x19.api.v1.PrecompiledObject\"=\n\x0bSnippetFile\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\x12\x0f\n\x07is_main\x18\x03 \x01(\x08\"\x94\x01\n\x12SaveSnippetRequest\x12\"\n\x05\x66iles\x18\x01 \x03(\x0b\x32\x13.api.v1.SnippetFile\x12\x18\n\x03sdk\x18\x02 \x01(\x0e\x32\x0b.api.v1.Sdk\x12\x18\n\x10pipeline_options\x18\x03 \x01(\t\x12&\n\ncomplexity\x18\x04 \x01(\x0e\x32\x12.api.v1.Complexity\"!\n\x13SaveSnippetResponse\x12\n\n\x02id\x18\x01 \x01(\t\"\x1f\n\x11GetSnippetRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\x94\x01\n\x12GetSnippetResponse\x12\"\n\x05\x66iles\x18\x01 \x03(\x0b\x32\x13.api.v1.SnippetFile\x12\x18\n\x03sdk\x18\x02 \x01(\x0e\x32\x0b.api.v1.Sdk\x12\x18\n\x10pipeline_options\x18\x03 \x01(\t\x12&\n\ncomplexity\x18\x04 \x01(\x0e\x32\x12.api.v1.Complexity*R\n\x03Sdk\x12\x13\n\x0fSDK_UNSPECIFIED\x10\x00\x12\x0c\n\x08SDK_JAVA\x10\x01\x12\n\n\x06SDK_GO\x10\x02\x12\x0e\n\nSDK_PYTHON\x10\x03\x12\x0c\n\x08SDK_SCIO\x10\x04*\xb8\x02\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x15\n\x11STATUS_VALIDATING\x10\x01\x12\x1b\n\x17STATUS_VALIDATION_ERROR\x10\x02\x12\x14\n\x10STATUS_PREPARING\x10\x03\x12\x1c\n\x18STATUS_PREPARATION_ERROR\x10\x04\x12\x14\n\x10STATUS_COMPILING\x10\x05\x12\x18\n\x14STATUS_COMPILE_ERROR\x10\x06\x12\x14\n\x10STATUS_EXECUTING\x10\x07\x12\x13\n\x0fSTATUS_FINISHED\x10\x08\x12\x14\n\x10STATUS_RUN_ERROR\x10\t\x12\x10\n\x0cSTATUS_ERROR\x10\n\x12\x16\n\x12STATUS_RUN_TIMEOUT\x10\x0b\x12\x13\n\x0fSTATUS_CANCELED\x10\x0c*\xae\x01\n\x15PrecompiledObjectType\x12\'\n#PRECOMPILED_OBJECT_TYPE_UNSPECIFIED\x10\x00\x12#\n\x1fPRECOMPILED_OBJECT_TYPE_EXAMPLE\x10\x01\x12 \n\x1cPRECOMPILED_OBJECT_TYPE_KATA\x10\x02\x12%\n!PRECOMPILED_OBJECT_TYPE_UNIT_TEST\x10\x03*n\n\nComplexity\x12\x1a\n\x16\x43OMPLEXITY_UNSPECIFIED\x10\x00\x12\x14\n\x10\x43OMPLEXITY_BASIC\x10\x01\x12\x15\n\x11\x43OMPLEXITY_MEDIUM\x10\x02\x12\x17\n\x13\x43OMPLEXITY_ADVANCED\x10\x03*F\n\x0c\x45mulatorType\x12\x1d\n\x19\x45MULATOR_TYPE_UNSPECIFIED\x10\x00\x12\x17\n\x13\x45MULATOR_TYPE_KAFKA\x10\x01\x32\x8b\r\n\x11PlaygroundService\x12:\n\x07RunCode\x12\x16.api.v1.RunCodeRequest\x1a\x17.api.v1.RunCodeResponse\x12\x46\n\x0b\x43heckStatus\x12\x1a.api.v1.CheckStatusRequest\x1a\x1b.api.v1.CheckStatusResponse\x12I\n\x0cGetRunOutput\x12\x1b.api.v1.GetRunOutputRequest\x1a\x1c.api.v1.GetRunOutputResponse\x12:\n\x07GetLogs\x12\x16.api.v1.GetLogsRequest\x1a\x17.api.v1.GetLogsResponse\x12=\n\x08GetGraph\x12\x17.api.v1.GetGraphRequest\x1a\x18.api.v1.GetGraphResponse\x12\x46\n\x0bGetRunError\x12\x1a.api.v1.GetRunErrorRequest\x1a\x1b.api.v1.GetRunErrorResponse\x12^\n\x13GetValidationOutput\x12\".api.v1.GetValidationOutputRequest\x1a#.api.v1.GetValidationOutputResponse\x12\x61\n\x14GetPreparationOutput\x12#.api.v1.GetPreparationOutputRequest\x1a$.api.v1.GetPreparationOutputResponse\x12U\n\x10GetCompileOutput\x12\x1f.api.v1.GetCompileOutputRequest\x1a .api.v1.GetCompileOutputResponse\x12\x37\n\x06\x43\x61ncel\x12\x15.api.v1.CancelRequest\x1a\x16.api.v1.CancelResponse\x12\x64\n\x15GetPrecompiledObjects\x12$.api.v1.GetPrecompiledObjectsRequest\x1a%.api.v1.GetPrecompiledObjectsResponse\x12\x61\n\x14GetPrecompiledObject\x12#.api.v1.GetPrecompiledObjectRequest\x1a$.api.v1.GetPrecompiledObjectResponse\x12m\n\x18GetPrecompiledObjectCode\x12\'.api.v1.GetPrecompiledObjectCodeRequest\x1a(.api.v1.GetPrecompiledObjectCodeResponse\x12s\n\x1aGetPrecompiledObjectOutput\x12).api.v1.GetPrecompiledObjectOutputRequest\x1a*.api.v1.GetPrecompiledObjectOutputResponse\x12m\n\x18GetPrecompiledObjectLogs\x12\'.api.v1.GetPrecompiledObjectLogsRequest\x1a(.api.v1.GetPrecompiledObjectLogsResponse\x12p\n\x19GetPrecompiledObjectGraph\x12(.api.v1.GetPrecompiledObjectGraphRequest\x1a).api.v1.GetPrecompiledObjectGraphResponse\x12v\n\x1bGetDefaultPrecompiledObject\x12*.api.v1.GetDefaultPrecompiledObjectRequest\x1a+.api.v1.GetDefaultPrecompiledObjectResponse\x12\x46\n\x0bSaveSnippet\x12\x1a.api.v1.SaveSnippetRequest\x1a\x1b.api.v1.SaveSnippetResponse\x12\x43\n\nGetSnippet\x12\x19.api.v1.GetSnippetRequest\x1a\x1a.api.v1.GetSnippetResponseB8Z6beam.apache.org/playground/backend/internal;playgroundb\x06proto3')

_SDK = DESCRIPTOR.enum_types_by_name['Sdk']
Sdk = enum_type_wrapper.EnumTypeWrapper(_SDK)
_STATUS = DESCRIPTOR.enum_types_by_name['Status']
Status = enum_type_wrapper.EnumTypeWrapper(_STATUS)
_PRECOMPILEDOBJECTTYPE = DESCRIPTOR.enum_types_by_name['PrecompiledObjectType']
PrecompiledObjectType = enum_type_wrapper.EnumTypeWrapper(_PRECOMPILEDOBJECTTYPE)
_COMPLEXITY = DESCRIPTOR.enum_types_by_name['Complexity']
Complexity = enum_type_wrapper.EnumTypeWrapper(_COMPLEXITY)
_EMULATORTYPE = DESCRIPTOR.enum_types_by_name['EmulatorType']
EmulatorType = enum_type_wrapper.EnumTypeWrapper(_EMULATORTYPE)
SDK_UNSPECIFIED = 0
SDK_JAVA = 1
SDK_GO = 2
SDK_PYTHON = 3
SDK_SCIO = 4
STATUS_UNSPECIFIED = 0
STATUS_VALIDATING = 1
STATUS_VALIDATION_ERROR = 2
STATUS_PREPARING = 3
STATUS_PREPARATION_ERROR = 4
STATUS_COMPILING = 5
STATUS_COMPILE_ERROR = 6
STATUS_EXECUTING = 7
STATUS_FINISHED = 8
STATUS_RUN_ERROR = 9
STATUS_ERROR = 10
STATUS_RUN_TIMEOUT = 11
STATUS_CANCELED = 12
PRECOMPILED_OBJECT_TYPE_UNSPECIFIED = 0
PRECOMPILED_OBJECT_TYPE_EXAMPLE = 1
PRECOMPILED_OBJECT_TYPE_KATA = 2
PRECOMPILED_OBJECT_TYPE_UNIT_TEST = 3
COMPLEXITY_UNSPECIFIED = 0
COMPLEXITY_BASIC = 1
COMPLEXITY_MEDIUM = 2
COMPLEXITY_ADVANCED = 3
EMULATOR_TYPE_UNSPECIFIED = 0
EMULATOR_TYPE_KAFKA = 1


_DATASET = DESCRIPTOR.message_types_by_name['Dataset']
_DATASET_OPTIONSENTRY = _DATASET.nested_types_by_name['OptionsEntry']
_RUNCODEREQUEST = DESCRIPTOR.message_types_by_name['RunCodeRequest']
_RUNCODERESPONSE = DESCRIPTOR.message_types_by_name['RunCodeResponse']
_CHECKSTATUSREQUEST = DESCRIPTOR.message_types_by_name['CheckStatusRequest']
_CHECKSTATUSRESPONSE = DESCRIPTOR.message_types_by_name['CheckStatusResponse']
_GETVALIDATIONOUTPUTREQUEST = DESCRIPTOR.message_types_by_name['GetValidationOutputRequest']
_GETVALIDATIONOUTPUTRESPONSE = DESCRIPTOR.message_types_by_name['GetValidationOutputResponse']
_GETPREPARATIONOUTPUTREQUEST = DESCRIPTOR.message_types_by_name['GetPreparationOutputRequest']
_GETPREPARATIONOUTPUTRESPONSE = DESCRIPTOR.message_types_by_name['GetPreparationOutputResponse']
_GETCOMPILEOUTPUTREQUEST = DESCRIPTOR.message_types_by_name['GetCompileOutputRequest']
_GETCOMPILEOUTPUTRESPONSE = DESCRIPTOR.message_types_by_name['GetCompileOutputResponse']
_GETRUNOUTPUTREQUEST = DESCRIPTOR.message_types_by_name['GetRunOutputRequest']
_GETRUNOUTPUTRESPONSE = DESCRIPTOR.message_types_by_name['GetRunOutputResponse']
_GETRUNERRORREQUEST = DESCRIPTOR.message_types_by_name['GetRunErrorRequest']
_GETRUNERRORRESPONSE = DESCRIPTOR.message_types_by_name['GetRunErrorResponse']
_GETLOGSREQUEST = DESCRIPTOR.message_types_by_name['GetLogsRequest']
_GETLOGSRESPONSE = DESCRIPTOR.message_types_by_name['GetLogsResponse']
_GETGRAPHREQUEST = DESCRIPTOR.message_types_by_name['GetGraphRequest']
_GETGRAPHRESPONSE = DESCRIPTOR.message_types_by_name['GetGraphResponse']
_CANCELREQUEST = DESCRIPTOR.message_types_by_name['CancelRequest']
_CANCELRESPONSE = DESCRIPTOR.message_types_by_name['CancelResponse']
_PRECOMPILEDOBJECT = DESCRIPTOR.message_types_by_name['PrecompiledObject']
_CATEGORIES = DESCRIPTOR.message_types_by_name['Categories']
_CATEGORIES_CATEGORY = _CATEGORIES.nested_types_by_name['Category']
_GETPRECOMPILEDOBJECTSREQUEST = DESCRIPTOR.message_types_by_name['GetPrecompiledObjectsRequest']
_GETPRECOMPILEDOBJECTREQUEST = DESCRIPTOR.message_types_by_name['GetPrecompiledObjectRequest']
_GETPRECOMPILEDOBJECTCODEREQUEST = DESCRIPTOR.message_types_by_name['GetPrecompiledObjectCodeRequest']
_GETPRECOMPILEDOBJECTOUTPUTREQUEST = DESCRIPTOR.message_types_by_name['GetPrecompiledObjectOutputRequest']
_GETPRECOMPILEDOBJECTLOGSREQUEST = DESCRIPTOR.message_types_by_name['GetPrecompiledObjectLogsRequest']
_GETPRECOMPILEDOBJECTGRAPHREQUEST = DESCRIPTOR.message_types_by_name['GetPrecompiledObjectGraphRequest']
_GETDEFAULTPRECOMPILEDOBJECTREQUEST = DESCRIPTOR.message_types_by_name['GetDefaultPrecompiledObjectRequest']
_GETPRECOMPILEDOBJECTSRESPONSE = DESCRIPTOR.message_types_by_name['GetPrecompiledObjectsResponse']
_GETPRECOMPILEDOBJECTRESPONSE = DESCRIPTOR.message_types_by_name['GetPrecompiledObjectResponse']
_GETPRECOMPILEDOBJECTCODERESPONSE = DESCRIPTOR.message_types_by_name['GetPrecompiledObjectCodeResponse']
_GETPRECOMPILEDOBJECTOUTPUTRESPONSE = DESCRIPTOR.message_types_by_name['GetPrecompiledObjectOutputResponse']
_GETPRECOMPILEDOBJECTLOGSRESPONSE = DESCRIPTOR.message_types_by_name['GetPrecompiledObjectLogsResponse']
_GETPRECOMPILEDOBJECTGRAPHRESPONSE = DESCRIPTOR.message_types_by_name['GetPrecompiledObjectGraphResponse']
_GETDEFAULTPRECOMPILEDOBJECTRESPONSE = DESCRIPTOR.message_types_by_name['GetDefaultPrecompiledObjectResponse']
_SNIPPETFILE = DESCRIPTOR.message_types_by_name['SnippetFile']
_SAVESNIPPETREQUEST = DESCRIPTOR.message_types_by_name['SaveSnippetRequest']
_SAVESNIPPETRESPONSE = DESCRIPTOR.message_types_by_name['SaveSnippetResponse']
_GETSNIPPETREQUEST = DESCRIPTOR.message_types_by_name['GetSnippetRequest']
_GETSNIPPETRESPONSE = DESCRIPTOR.message_types_by_name['GetSnippetResponse']
Dataset = _reflection.GeneratedProtocolMessageType('Dataset', (_message.Message,), {

  'OptionsEntry' : _reflection.GeneratedProtocolMessageType('OptionsEntry', (_message.Message,), {
    'DESCRIPTOR' : _DATASET_OPTIONSENTRY,
    '__module__' : 'api_pb2'
    # @@protoc_insertion_point(class_scope:api.v1.Dataset.OptionsEntry)
    })
  ,
  'DESCRIPTOR' : _DATASET,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.v1.Dataset)
  })
_sym_db.RegisterMessage(Dataset)
_sym_db.RegisterMessage(Dataset.OptionsEntry)

RunCodeRequest = _reflection.GeneratedProtocolMessageType('RunCodeRequest', (_message.Message,), {
  'DESCRIPTOR' : _RUNCODEREQUEST,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.v1.RunCodeRequest)
  })
_sym_db.RegisterMessage(RunCodeRequest)

RunCodeResponse = _reflection.GeneratedProtocolMessageType('RunCodeResponse', (_message.Message,), {
  'DESCRIPTOR' : _RUNCODERESPONSE,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.v1.RunCodeResponse)
  })
_sym_db.RegisterMessage(RunCodeResponse)

CheckStatusRequest = _reflection.GeneratedProtocolMessageType('CheckStatusRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHECKSTATUSREQUEST,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.v1.CheckStatusRequest)
  })
_sym_db.RegisterMessage(CheckStatusRequest)

CheckStatusResponse = _reflection.GeneratedProtocolMessageType('CheckStatusResponse', (_message.Message,), {
  'DESCRIPTOR' : _CHECKSTATUSRESPONSE,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.v1.CheckStatusResponse)
  })
_sym_db.RegisterMessage(CheckStatusResponse)

GetValidationOutputRequest = _reflection.GeneratedProtocolMessageType('GetValidationOutputRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETVALIDATIONOUTPUTREQUEST,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.v1.GetValidationOutputRequest)
  })
_sym_db.RegisterMessage(GetValidationOutputRequest)

GetValidationOutputResponse = _reflection.GeneratedProtocolMessageType('GetValidationOutputResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETVALIDATIONOUTPUTRESPONSE,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.v1.GetValidationOutputResponse)
  })
_sym_db.RegisterMessage(GetValidationOutputResponse)

GetPreparationOutputRequest = _reflection.GeneratedProtocolMessageType('GetPreparationOutputRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPREPARATIONOUTPUTREQUEST,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.v1.GetPreparationOutputRequest)
  })
_sym_db.RegisterMessage(GetPreparationOutputRequest)

GetPreparationOutputResponse = _reflection.GeneratedProtocolMessageType('GetPreparationOutputResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETPREPARATIONOUTPUTRESPONSE,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.v1.GetPreparationOutputResponse)
  })
_sym_db.RegisterMessage(GetPreparationOutputResponse)

GetCompileOutputRequest = _reflection.GeneratedProtocolMessageType('GetCompileOutputRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCOMPILEOUTPUTREQUEST,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.v1.GetCompileOutputRequest)
  })
_sym_db.RegisterMessage(GetCompileOutputRequest)

GetCompileOutputResponse = _reflection.GeneratedProtocolMessageType('GetCompileOutputResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETCOMPILEOUTPUTRESPONSE,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.v1.GetCompileOutputResponse)
  })
_sym_db.RegisterMessage(GetCompileOutputResponse)

GetRunOutputRequest = _reflection.GeneratedProtocolMessageType('GetRunOutputRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETRUNOUTPUTREQUEST,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.v1.GetRunOutputRequest)
  })
_sym_db.RegisterMessage(GetRunOutputRequest)

GetRunOutputResponse = _reflection.GeneratedProtocolMessageType('GetRunOutputResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETRUNOUTPUTRESPONSE,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.v1.GetRunOutputResponse)
  })
_sym_db.RegisterMessage(GetRunOutputResponse)

GetRunErrorRequest = _reflection.GeneratedProtocolMessageType('GetRunErrorRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETRUNERRORREQUEST,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.v1.GetRunErrorRequest)
  })
_sym_db.RegisterMessage(GetRunErrorRequest)

GetRunErrorResponse = _reflection.GeneratedProtocolMessageType('GetRunErrorResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETRUNERRORRESPONSE,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.v1.GetRunErrorResponse)
  })
_sym_db.RegisterMessage(GetRunErrorResponse)

GetLogsRequest = _reflection.GeneratedProtocolMessageType('GetLogsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETLOGSREQUEST,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.v1.GetLogsRequest)
  })
_sym_db.RegisterMessage(GetLogsRequest)

GetLogsResponse = _reflection.GeneratedProtocolMessageType('GetLogsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETLOGSRESPONSE,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.v1.GetLogsResponse)
  })
_sym_db.RegisterMessage(GetLogsResponse)

GetGraphRequest = _reflection.GeneratedProtocolMessageType('GetGraphRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETGRAPHREQUEST,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.v1.GetGraphRequest)
  })
_sym_db.RegisterMessage(GetGraphRequest)

GetGraphResponse = _reflection.GeneratedProtocolMessageType('GetGraphResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETGRAPHRESPONSE,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.v1.GetGraphResponse)
  })
_sym_db.RegisterMessage(GetGraphResponse)

CancelRequest = _reflection.GeneratedProtocolMessageType('CancelRequest', (_message.Message,), {
  'DESCRIPTOR' : _CANCELREQUEST,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.v1.CancelRequest)
  })
_sym_db.RegisterMessage(CancelRequest)

CancelResponse = _reflection.GeneratedProtocolMessageType('CancelResponse', (_message.Message,), {
  'DESCRIPTOR' : _CANCELRESPONSE,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.v1.CancelResponse)
  })
_sym_db.RegisterMessage(CancelResponse)

PrecompiledObject = _reflection.GeneratedProtocolMessageType('PrecompiledObject', (_message.Message,), {
  'DESCRIPTOR' : _PRECOMPILEDOBJECT,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.v1.PrecompiledObject)
  })
_sym_db.RegisterMessage(PrecompiledObject)

Categories = _reflection.GeneratedProtocolMessageType('Categories', (_message.Message,), {

  'Category' : _reflection.GeneratedProtocolMessageType('Category', (_message.Message,), {
    'DESCRIPTOR' : _CATEGORIES_CATEGORY,
    '__module__' : 'api_pb2'
    # @@protoc_insertion_point(class_scope:api.v1.Categories.Category)
    })
  ,
  'DESCRIPTOR' : _CATEGORIES,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.v1.Categories)
  })
_sym_db.RegisterMessage(Categories)
_sym_db.RegisterMessage(Categories.Category)

GetPrecompiledObjectsRequest = _reflection.GeneratedProtocolMessageType('GetPrecompiledObjectsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPRECOMPILEDOBJECTSREQUEST,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.v1.GetPrecompiledObjectsRequest)
  })
_sym_db.RegisterMessage(GetPrecompiledObjectsRequest)

GetPrecompiledObjectRequest = _reflection.GeneratedProtocolMessageType('GetPrecompiledObjectRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPRECOMPILEDOBJECTREQUEST,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.v1.GetPrecompiledObjectRequest)
  })
_sym_db.RegisterMessage(GetPrecompiledObjectRequest)

GetPrecompiledObjectCodeRequest = _reflection.GeneratedProtocolMessageType('GetPrecompiledObjectCodeRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPRECOMPILEDOBJECTCODEREQUEST,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.v1.GetPrecompiledObjectCodeRequest)
  })
_sym_db.RegisterMessage(GetPrecompiledObjectCodeRequest)

GetPrecompiledObjectOutputRequest = _reflection.GeneratedProtocolMessageType('GetPrecompiledObjectOutputRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPRECOMPILEDOBJECTOUTPUTREQUEST,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.v1.GetPrecompiledObjectOutputRequest)
  })
_sym_db.RegisterMessage(GetPrecompiledObjectOutputRequest)

GetPrecompiledObjectLogsRequest = _reflection.GeneratedProtocolMessageType('GetPrecompiledObjectLogsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPRECOMPILEDOBJECTLOGSREQUEST,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.v1.GetPrecompiledObjectLogsRequest)
  })
_sym_db.RegisterMessage(GetPrecompiledObjectLogsRequest)

GetPrecompiledObjectGraphRequest = _reflection.GeneratedProtocolMessageType('GetPrecompiledObjectGraphRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPRECOMPILEDOBJECTGRAPHREQUEST,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.v1.GetPrecompiledObjectGraphRequest)
  })
_sym_db.RegisterMessage(GetPrecompiledObjectGraphRequest)

GetDefaultPrecompiledObjectRequest = _reflection.GeneratedProtocolMessageType('GetDefaultPrecompiledObjectRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETDEFAULTPRECOMPILEDOBJECTREQUEST,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.v1.GetDefaultPrecompiledObjectRequest)
  })
_sym_db.RegisterMessage(GetDefaultPrecompiledObjectRequest)

GetPrecompiledObjectsResponse = _reflection.GeneratedProtocolMessageType('GetPrecompiledObjectsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETPRECOMPILEDOBJECTSRESPONSE,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.v1.GetPrecompiledObjectsResponse)
  })
_sym_db.RegisterMessage(GetPrecompiledObjectsResponse)

GetPrecompiledObjectResponse = _reflection.GeneratedProtocolMessageType('GetPrecompiledObjectResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETPRECOMPILEDOBJECTRESPONSE,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.v1.GetPrecompiledObjectResponse)
  })
_sym_db.RegisterMessage(GetPrecompiledObjectResponse)

GetPrecompiledObjectCodeResponse = _reflection.GeneratedProtocolMessageType('GetPrecompiledObjectCodeResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETPRECOMPILEDOBJECTCODERESPONSE,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.v1.GetPrecompiledObjectCodeResponse)
  })
_sym_db.RegisterMessage(GetPrecompiledObjectCodeResponse)

GetPrecompiledObjectOutputResponse = _reflection.GeneratedProtocolMessageType('GetPrecompiledObjectOutputResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETPRECOMPILEDOBJECTOUTPUTRESPONSE,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.v1.GetPrecompiledObjectOutputResponse)
  })
_sym_db.RegisterMessage(GetPrecompiledObjectOutputResponse)

GetPrecompiledObjectLogsResponse = _reflection.GeneratedProtocolMessageType('GetPrecompiledObjectLogsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETPRECOMPILEDOBJECTLOGSRESPONSE,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.v1.GetPrecompiledObjectLogsResponse)
  })
_sym_db.RegisterMessage(GetPrecompiledObjectLogsResponse)

GetPrecompiledObjectGraphResponse = _reflection.GeneratedProtocolMessageType('GetPrecompiledObjectGraphResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETPRECOMPILEDOBJECTGRAPHRESPONSE,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.v1.GetPrecompiledObjectGraphResponse)
  })
_sym_db.RegisterMessage(GetPrecompiledObjectGraphResponse)

GetDefaultPrecompiledObjectResponse = _reflection.GeneratedProtocolMessageType('GetDefaultPrecompiledObjectResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETDEFAULTPRECOMPILEDOBJECTRESPONSE,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.v1.GetDefaultPrecompiledObjectResponse)
  })
_sym_db.RegisterMessage(GetDefaultPrecompiledObjectResponse)

SnippetFile = _reflection.GeneratedProtocolMessageType('SnippetFile', (_message.Message,), {
  'DESCRIPTOR' : _SNIPPETFILE,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.v1.SnippetFile)
  })
_sym_db.RegisterMessage(SnippetFile)

SaveSnippetRequest = _reflection.GeneratedProtocolMessageType('SaveSnippetRequest', (_message.Message,), {
  'DESCRIPTOR' : _SAVESNIPPETREQUEST,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.v1.SaveSnippetRequest)
  })
_sym_db.RegisterMessage(SaveSnippetRequest)

SaveSnippetResponse = _reflection.GeneratedProtocolMessageType('SaveSnippetResponse', (_message.Message,), {
  'DESCRIPTOR' : _SAVESNIPPETRESPONSE,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.v1.SaveSnippetResponse)
  })
_sym_db.RegisterMessage(SaveSnippetResponse)

GetSnippetRequest = _reflection.GeneratedProtocolMessageType('GetSnippetRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSNIPPETREQUEST,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.v1.GetSnippetRequest)
  })
_sym_db.RegisterMessage(GetSnippetRequest)

GetSnippetResponse = _reflection.GeneratedProtocolMessageType('GetSnippetResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETSNIPPETRESPONSE,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.v1.GetSnippetResponse)
  })
_sym_db.RegisterMessage(GetSnippetResponse)

_PLAYGROUNDSERVICE = DESCRIPTOR.services_by_name['PlaygroundService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z6beam.apache.org/playground/backend/internal;playground'
  _DATASET_OPTIONSENTRY._options = None
  _DATASET_OPTIONSENTRY._serialized_options = b'8\001'
  _SDK._serialized_start=2961
  _SDK._serialized_end=3043
  _STATUS._serialized_start=3046
  _STATUS._serialized_end=3358
  _PRECOMPILEDOBJECTTYPE._serialized_start=3361
  _PRECOMPILEDOBJECTTYPE._serialized_end=3535
  _COMPLEXITY._serialized_start=3537
  _COMPLEXITY._serialized_end=3647
  _EMULATORTYPE._serialized_start=3649
  _EMULATORTYPE._serialized_end=3719
  _DATASET._serialized_start=22
  _DATASET._serialized_end=184
  _DATASET_OPTIONSENTRY._serialized_start=138
  _DATASET_OPTIONSENTRY._serialized_end=184
  _RUNCODEREQUEST._serialized_start=186
  _RUNCODEREQUEST._serialized_end=303
  _RUNCODERESPONSE._serialized_start=305
  _RUNCODERESPONSE._serialized_end=345
  _CHECKSTATUSREQUEST._serialized_start=347
  _CHECKSTATUSREQUEST._serialized_end=390
  _CHECKSTATUSRESPONSE._serialized_start=392
  _CHECKSTATUSRESPONSE._serialized_end=445
  _GETVALIDATIONOUTPUTREQUEST._serialized_start=447
  _GETVALIDATIONOUTPUTREQUEST._serialized_end=498
  _GETVALIDATIONOUTPUTRESPONSE._serialized_start=500
  _GETVALIDATIONOUTPUTRESPONSE._serialized_end=545
  _GETPREPARATIONOUTPUTREQUEST._serialized_start=547
  _GETPREPARATIONOUTPUTREQUEST._serialized_end=599
  _GETPREPARATIONOUTPUTRESPONSE._serialized_start=601
  _GETPREPARATIONOUTPUTRESPONSE._serialized_end=647
  _GETCOMPILEOUTPUTREQUEST._serialized_start=649
  _GETCOMPILEOUTPUTREQUEST._serialized_end=697
  _GETCOMPILEOUTPUTRESPONSE._serialized_start=699
  _GETCOMPILEOUTPUTRESPONSE._serialized_end=741
  _GETRUNOUTPUTREQUEST._serialized_start=743
  _GETRUNOUTPUTREQUEST._serialized_end=787
  _GETRUNOUTPUTRESPONSE._serialized_start=789
  _GETRUNOUTPUTRESPONSE._serialized_end=827
  _GETRUNERRORREQUEST._serialized_start=829
  _GETRUNERRORREQUEST._serialized_end=872
  _GETRUNERRORRESPONSE._serialized_start=874
  _GETRUNERRORRESPONSE._serialized_end=911
  _GETLOGSREQUEST._serialized_start=913
  _GETLOGSREQUEST._serialized_end=952
  _GETLOGSRESPONSE._serialized_start=954
  _GETLOGSRESPONSE._serialized_end=987
  _GETGRAPHREQUEST._serialized_start=989
  _GETGRAPHREQUEST._serialized_end=1029
  _GETGRAPHRESPONSE._serialized_start=1031
  _GETGRAPHRESPONSE._serialized_end=1064
  _CANCELREQUEST._serialized_start=1066
  _CANCELREQUEST._serialized_end=1104
  _CANCELRESPONSE._serialized_start=1106
  _CANCELRESPONSE._serialized_end=1122
  _PRECOMPILEDOBJECT._serialized_start=1125
  _PRECOMPILEDOBJECT._serialized_end=1465
  _CATEGORIES._serialized_start=1468
  _CATEGORIES._serialized_end=1646
  _CATEGORIES_CATEGORY._serialized_start=1557
  _CATEGORIES_CATEGORY._serialized_end=1646
  _GETPRECOMPILEDOBJECTSREQUEST._serialized_start=1648
  _GETPRECOMPILEDOBJECTSREQUEST._serialized_end=1722
  _GETPRECOMPILEDOBJECTREQUEST._serialized_start=1724
  _GETPRECOMPILEDOBJECTREQUEST._serialized_end=1773
  _GETPRECOMPILEDOBJECTCODEREQUEST._serialized_start=1775
  _GETPRECOMPILEDOBJECTCODEREQUEST._serialized_end=1828
  _GETPRECOMPILEDOBJECTOUTPUTREQUEST._serialized_start=1830
  _GETPRECOMPILEDOBJECTOUTPUTREQUEST._serialized_end=1885
  _GETPRECOMPILEDOBJECTLOGSREQUEST._serialized_start=1887
  _GETPRECOMPILEDOBJECTLOGSREQUEST._serialized_end=1940
  _GETPRECOMPILEDOBJECTGRAPHREQUEST._serialized_start=1942
  _GETPRECOMPILEDOBJECTGRAPHREQUEST._serialized_end=1996
  _GETDEFAULTPRECOMPILEDOBJECTREQUEST._serialized_start=1998
  _GETDEFAULTPRECOMPILEDOBJECTREQUEST._serialized_end=2060
  _GETPRECOMPILEDOBJECTSRESPONSE._serialized_start=2062
  _GETPRECOMPILEDOBJECTSRESPONSE._serialized_end=2137
  _GETPRECOMPILEDOBJECTRESPONSE._serialized_start=2139
  _GETPRECOMPILEDOBJECTRESPONSE._serialized_end=2224
  _GETPRECOMPILEDOBJECTCODERESPONSE._serialized_start=2226
  _GETPRECOMPILEDOBJECTCODERESPONSE._serialized_end=2274
  _GETPRECOMPILEDOBJECTOUTPUTRESPONSE._serialized_start=2276
  _GETPRECOMPILEDOBJECTOUTPUTRESPONSE._serialized_end=2328
  _GETPRECOMPILEDOBJECTLOGSRESPONSE._serialized_start=2330
  _GETPRECOMPILEDOBJECTLOGSRESPONSE._serialized_end=2380
  _GETPRECOMPILEDOBJECTGRAPHRESPONSE._serialized_start=2382
  _GETPRECOMPILEDOBJECTGRAPHRESPONSE._serialized_end=2432
  _GETDEFAULTPRECOMPILEDOBJECTRESPONSE._serialized_start=2434
  _GETDEFAULTPRECOMPILEDOBJECTRESPONSE._serialized_end=2526
  _SNIPPETFILE._serialized_start=2528
  _SNIPPETFILE._serialized_end=2589
  _SAVESNIPPETREQUEST._serialized_start=2592
  _SAVESNIPPETREQUEST._serialized_end=2740
  _SAVESNIPPETRESPONSE._serialized_start=2742
  _SAVESNIPPETRESPONSE._serialized_end=2775
  _GETSNIPPETREQUEST._serialized_start=2777
  _GETSNIPPETREQUEST._serialized_end=2808
  _GETSNIPPETRESPONSE._serialized_start=2811
  _GETSNIPPETRESPONSE._serialized_end=2959
  _PLAYGROUNDSERVICE._serialized_start=3722
  _PLAYGROUNDSERVICE._serialized_end=5397
# @@protoc_insertion_point(module_scope)