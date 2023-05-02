import grpc
from concurrent import futures
import time
import anonymize_pb2_grpc as pb2_grpc
import anonymize_pb2 as pb2

# from deepface import DeepFace
from PIL import Image
import io


class AnonymizationService(pb2_grpc.AnonymizerServicer):
    def __init__(self, *args, **kwargs):
        pass

    def Anonymize(self, request, context):
        print("Request received:", request)

        image_bytes = request.image

        image = Image.open(io.BytesIO(image_bytes))

        # embedded_image = DeepFace.represent(image)

        # print(embedded_image)

        result = pb2.AnonymizeRS()

        result.anonymizedImage = image_bytes

        print("Resultado ANONYMIZE_RS", result)

        return result


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_AnonymizerServicer_to_server(AnonymizationService(), server)
    server.add_insecure_port("[::]:5098")
    server.start()
    print("Server Started - Awaiting requests...")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
