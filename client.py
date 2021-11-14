from ingest_pb2 import PublishRequest, Event
from ingest_pb2_grpc import IngestStub
import grpc

ev = Event(
    id= '12345',
    event_payload = '''
   "name":"Kunal",
   "last_name": "Datta"
   '''
)

request = PublishRequest(
    event=ev
)

channel = grpc.insecure_channel("localhost:50051")
client = IngestStub(channel)
status = client.Publish(request)
print(status)