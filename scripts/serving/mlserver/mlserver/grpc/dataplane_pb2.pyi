# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Iterable as typing___Iterable,
    Mapping as typing___Mapping,
    MutableMapping as typing___MutableMapping,
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int


DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class ServerLiveRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    def __init__(self,
        ) -> None: ...
type___ServerLiveRequest = ServerLiveRequest

class ServerLiveResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    live: builtin___bool = ...

    def __init__(self,
        *,
        live : typing___Optional[builtin___bool] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"live",b"live"]) -> None: ...
type___ServerLiveResponse = ServerLiveResponse

class ServerReadyRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    def __init__(self,
        ) -> None: ...
type___ServerReadyRequest = ServerReadyRequest

class ServerReadyResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    ready: builtin___bool = ...

    def __init__(self,
        *,
        ready : typing___Optional[builtin___bool] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"ready",b"ready"]) -> None: ...
type___ServerReadyResponse = ServerReadyResponse

class ModelReadyRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    name: typing___Text = ...
    version: typing___Text = ...

    def __init__(self,
        *,
        name : typing___Optional[typing___Text] = None,
        version : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"name",b"name",u"version",b"version"]) -> None: ...
type___ModelReadyRequest = ModelReadyRequest

class ModelReadyResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    ready: builtin___bool = ...

    def __init__(self,
        *,
        ready : typing___Optional[builtin___bool] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"ready",b"ready"]) -> None: ...
type___ModelReadyResponse = ModelReadyResponse

class ServerMetadataRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    def __init__(self,
        ) -> None: ...
type___ServerMetadataRequest = ServerMetadataRequest

class ServerMetadataResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    name: typing___Text = ...
    version: typing___Text = ...
    extensions: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text] = ...

    def __init__(self,
        *,
        name : typing___Optional[typing___Text] = None,
        version : typing___Optional[typing___Text] = None,
        extensions : typing___Optional[typing___Iterable[typing___Text]] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"extensions",b"extensions",u"name",b"name",u"version",b"version"]) -> None: ...
type___ServerMetadataResponse = ServerMetadataResponse

class ModelMetadataRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    name: typing___Text = ...
    version: typing___Text = ...

    def __init__(self,
        *,
        name : typing___Optional[typing___Text] = None,
        version : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"name",b"name",u"version",b"version"]) -> None: ...
type___ModelMetadataRequest = ModelMetadataRequest

class ModelMetadataResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class TensorMetadata(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        name: typing___Text = ...
        datatype: typing___Text = ...
        shape: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___int] = ...

        def __init__(self,
            *,
            name : typing___Optional[typing___Text] = None,
            datatype : typing___Optional[typing___Text] = None,
            shape : typing___Optional[typing___Iterable[builtin___int]] = None,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"datatype",b"datatype",u"name",b"name",u"shape",b"shape"]) -> None: ...
    type___TensorMetadata = TensorMetadata

    name: typing___Text = ...
    versions: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text] = ...
    platform: typing___Text = ...

    @property
    def inputs(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___ModelMetadataResponse.TensorMetadata]: ...

    @property
    def outputs(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___ModelMetadataResponse.TensorMetadata]: ...

    def __init__(self,
        *,
        name : typing___Optional[typing___Text] = None,
        versions : typing___Optional[typing___Iterable[typing___Text]] = None,
        platform : typing___Optional[typing___Text] = None,
        inputs : typing___Optional[typing___Iterable[type___ModelMetadataResponse.TensorMetadata]] = None,
        outputs : typing___Optional[typing___Iterable[type___ModelMetadataResponse.TensorMetadata]] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"inputs",b"inputs",u"name",b"name",u"outputs",b"outputs",u"platform",b"platform",u"versions",b"versions"]) -> None: ...
type___ModelMetadataResponse = ModelMetadataResponse

class ModelInferRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class InferInputTensor(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        class ParametersEntry(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
            key: typing___Text = ...

            @property
            def value(self) -> type___InferParameter: ...

            def __init__(self,
                *,
                key : typing___Optional[typing___Text] = None,
                value : typing___Optional[type___InferParameter] = None,
                ) -> None: ...
            def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> builtin___bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...
        type___ParametersEntry = ParametersEntry

        name: typing___Text = ...
        datatype: typing___Text = ...
        shape: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___int] = ...

        @property
        def parameters(self) -> typing___MutableMapping[typing___Text, type___InferParameter]: ...

        @property
        def contents(self) -> type___InferTensorContents: ...

        def __init__(self,
            *,
            name : typing___Optional[typing___Text] = None,
            datatype : typing___Optional[typing___Text] = None,
            shape : typing___Optional[typing___Iterable[builtin___int]] = None,
            parameters : typing___Optional[typing___Mapping[typing___Text, type___InferParameter]] = None,
            contents : typing___Optional[type___InferTensorContents] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"contents",b"contents"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"contents",b"contents",u"datatype",b"datatype",u"name",b"name",u"parameters",b"parameters",u"shape",b"shape"]) -> None: ...
    type___InferInputTensor = InferInputTensor

    class InferRequestedOutputTensor(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        class ParametersEntry(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
            key: typing___Text = ...

            @property
            def value(self) -> type___InferParameter: ...

            def __init__(self,
                *,
                key : typing___Optional[typing___Text] = None,
                value : typing___Optional[type___InferParameter] = None,
                ) -> None: ...
            def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> builtin___bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...
        type___ParametersEntry = ParametersEntry

        name: typing___Text = ...

        @property
        def parameters(self) -> typing___MutableMapping[typing___Text, type___InferParameter]: ...

        def __init__(self,
            *,
            name : typing___Optional[typing___Text] = None,
            parameters : typing___Optional[typing___Mapping[typing___Text, type___InferParameter]] = None,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"name",b"name",u"parameters",b"parameters"]) -> None: ...
    type___InferRequestedOutputTensor = InferRequestedOutputTensor

    class ParametersEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key: typing___Text = ...

        @property
        def value(self) -> type___InferParameter: ...

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[type___InferParameter] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...
    type___ParametersEntry = ParametersEntry

    model_name: typing___Text = ...
    model_version: typing___Text = ...
    id: typing___Text = ...

    @property
    def parameters(self) -> typing___MutableMapping[typing___Text, type___InferParameter]: ...

    @property
    def inputs(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___ModelInferRequest.InferInputTensor]: ...

    @property
    def outputs(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___ModelInferRequest.InferRequestedOutputTensor]: ...

    def __init__(self,
        *,
        model_name : typing___Optional[typing___Text] = None,
        model_version : typing___Optional[typing___Text] = None,
        id : typing___Optional[typing___Text] = None,
        parameters : typing___Optional[typing___Mapping[typing___Text, type___InferParameter]] = None,
        inputs : typing___Optional[typing___Iterable[type___ModelInferRequest.InferInputTensor]] = None,
        outputs : typing___Optional[typing___Iterable[type___ModelInferRequest.InferRequestedOutputTensor]] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"id",b"id",u"inputs",b"inputs",u"model_name",b"model_name",u"model_version",b"model_version",u"outputs",b"outputs",u"parameters",b"parameters"]) -> None: ...
type___ModelInferRequest = ModelInferRequest

class ModelInferResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class InferOutputTensor(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        class ParametersEntry(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
            key: typing___Text = ...

            @property
            def value(self) -> type___InferParameter: ...

            def __init__(self,
                *,
                key : typing___Optional[typing___Text] = None,
                value : typing___Optional[type___InferParameter] = None,
                ) -> None: ...
            def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> builtin___bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...
        type___ParametersEntry = ParametersEntry

        name: typing___Text = ...
        datatype: typing___Text = ...
        shape: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___int] = ...

        @property
        def parameters(self) -> typing___MutableMapping[typing___Text, type___InferParameter]: ...

        @property
        def contents(self) -> type___InferTensorContents: ...

        def __init__(self,
            *,
            name : typing___Optional[typing___Text] = None,
            datatype : typing___Optional[typing___Text] = None,
            shape : typing___Optional[typing___Iterable[builtin___int]] = None,
            parameters : typing___Optional[typing___Mapping[typing___Text, type___InferParameter]] = None,
            contents : typing___Optional[type___InferTensorContents] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"contents",b"contents"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"contents",b"contents",u"datatype",b"datatype",u"name",b"name",u"parameters",b"parameters",u"shape",b"shape"]) -> None: ...
    type___InferOutputTensor = InferOutputTensor

    class ParametersEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key: typing___Text = ...

        @property
        def value(self) -> type___InferParameter: ...

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[type___InferParameter] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...
    type___ParametersEntry = ParametersEntry

    model_name: typing___Text = ...
    model_version: typing___Text = ...
    id: typing___Text = ...

    @property
    def parameters(self) -> typing___MutableMapping[typing___Text, type___InferParameter]: ...

    @property
    def outputs(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___ModelInferResponse.InferOutputTensor]: ...

    def __init__(self,
        *,
        model_name : typing___Optional[typing___Text] = None,
        model_version : typing___Optional[typing___Text] = None,
        id : typing___Optional[typing___Text] = None,
        parameters : typing___Optional[typing___Mapping[typing___Text, type___InferParameter]] = None,
        outputs : typing___Optional[typing___Iterable[type___ModelInferResponse.InferOutputTensor]] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"id",b"id",u"model_name",b"model_name",u"model_version",b"model_version",u"outputs",b"outputs",u"parameters",b"parameters"]) -> None: ...
type___ModelInferResponse = ModelInferResponse

class InferParameter(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    bool_param: builtin___bool = ...
    int64_param: builtin___int = ...
    string_param: typing___Text = ...

    def __init__(self,
        *,
        bool_param : typing___Optional[builtin___bool] = None,
        int64_param : typing___Optional[builtin___int] = None,
        string_param : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"bool_param",b"bool_param",u"int64_param",b"int64_param",u"parameter_choice",b"parameter_choice",u"string_param",b"string_param"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"bool_param",b"bool_param",u"int64_param",b"int64_param",u"parameter_choice",b"parameter_choice",u"string_param",b"string_param"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"parameter_choice",b"parameter_choice"]) -> typing_extensions___Literal["bool_param","int64_param","string_param"]: ...
type___InferParameter = InferParameter

class InferTensorContents(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    raw_contents: builtin___bytes = ...
    bool_contents: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___bool] = ...
    int_contents: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___int] = ...
    int64_contents: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___int] = ...
    uint_contents: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___int] = ...
    uint64_contents: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___int] = ...
    fp32_contents: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___float] = ...
    fp64_contents: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___float] = ...
    bytes_contents: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___bytes] = ...

    def __init__(self,
        *,
        raw_contents : typing___Optional[builtin___bytes] = None,
        bool_contents : typing___Optional[typing___Iterable[builtin___bool]] = None,
        int_contents : typing___Optional[typing___Iterable[builtin___int]] = None,
        int64_contents : typing___Optional[typing___Iterable[builtin___int]] = None,
        uint_contents : typing___Optional[typing___Iterable[builtin___int]] = None,
        uint64_contents : typing___Optional[typing___Iterable[builtin___int]] = None,
        fp32_contents : typing___Optional[typing___Iterable[builtin___float]] = None,
        fp64_contents : typing___Optional[typing___Iterable[builtin___float]] = None,
        bytes_contents : typing___Optional[typing___Iterable[builtin___bytes]] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"bool_contents",b"bool_contents",u"bytes_contents",b"bytes_contents",u"fp32_contents",b"fp32_contents",u"fp64_contents",b"fp64_contents",u"int64_contents",b"int64_contents",u"int_contents",b"int_contents",u"raw_contents",b"raw_contents",u"uint64_contents",b"uint64_contents",u"uint_contents",b"uint_contents"]) -> None: ...
type___InferTensorContents = InferTensorContents
