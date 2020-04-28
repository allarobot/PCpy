import grpc
import interface_pb2
import interface_pb2_grpc
import functions
from concurrent import futures
import time

_PORT = '50051'
_ONE_DAY_IN_SECONDS = 60 * 60 * 24

# cd to current folder
# python -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. interface.proto

class CalculatorService(interface_pb2_grpc.CalculatorServicer):

    def SquareRoot(self, requrest, context):

        response = interface_pb2.Number()

        response.value = functions.sq_root(requrest.value)
        return response

def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  interface_pb2_grpc.add_CalculatorServicer_to_server(
      CalculatorService(), server)
  server.add_insecure_port('[::]:{}'.format(_PORT))
  server.start()
  try:
      while True:
          time.sleep(_ONE_DAY_IN_SECONDS)
  except KeyboardInterrupt:
      server.stop(0)


if __name__ == "__main__":
    serve()
