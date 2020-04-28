import grpc

# cd to current folder
# python -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. interface.proto

import interface_pb2
import interface_pb2_grpc


_HOST = 'localhost'
_PORT = '50051'

def run():

    # open a gRPC channel
    channel = grpc.insecure_channel("{}:{}".format(_HOST,_PORT))

    # create a stub
    stub = interface_pb2_grpc.CalculatorStub(channel)

    # create
    response = stub.SquareRoot(interface_pb2.Number(value= 11))

    print(response.value)

if __name__ == "__main__":
    run()