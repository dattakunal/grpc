# grpc #
### This code is an example of GRPC client and server ###

* Below is the installation command for GRPC.
    * pip install grpcio-tools
* First the proto file is created. The protofile contains the structure of request and response.
* Then the grpc files are created based on below command:
    * python -m grpc_tools.protoc -I ./protobuf --python_out=. --grpc_python_out=. .\protobuf\ingest.proto
* After the the client and server python code is created.

