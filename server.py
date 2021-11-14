import grpc
from ingest_pb2 import Event, PublishReply, BulkStatus
import ingest_pb2_grpc
from concurrent import futures

class IngestService(ingest_pb2_grpc.IngestServicer):
    def Publish(self, request, context):
        print(request)
        reply = PublishReply(
            success = True,
            message = "The ID {} is read successfully".format(request.event.id),
            id = request.event.id
        )

        return reply


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ingest_pb2_grpc.add_IngestServicer_to_server(
        IngestService(), server
    )
    server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()