# Anonymization Service GRPC
A python anonymization server that connects with comparison service, another repository from this github profile.

## Running local
Install and configure python on local machine, documentation: https://www.python.org/downloads/

Install and configure GRPC tools for python, the documentation can be found in https://grpc.io/docs/languages/python/quickstart/

To install dependencies run
```shell
pip install pillow deepface numpy grpcio grpcio-tools
```

To generate the GRPC files correctly use the command
```shell
python3 -m grpc_tools.protoc --proto_path=protos --python_out=. --pyi_out=. --grpc_python_out=. protos/*.proto
```

To run the project, being in the root folder of it, run
```shell
python3 anonymization.py
```
