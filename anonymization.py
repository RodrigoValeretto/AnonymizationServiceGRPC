import grpc
from concurrent import futures
import time
import anonymize_pb2_grpc as pb2_grpc
import anonymize_pb2 as pb2
from deepface import DeepFace
from PIL import Image
import io
import os

os.environ["CUDA_VISIBLE_DEVICES"] = "0"

image_path = "/home/rodrigo/Área de Trabalho/Coding/GRPCClientPython/lfw/Aaron_Eckhart/Aaron_Eckhart_0001.jpg"


class AnonymizationService(pb2_grpc.AnonymizerServicer):
    def __init__(self, *args, **kwargs):
        pass

    def Anonymize(self, request, context):
        print("Request received:", request)

        image_bytes = request.image

        image = Image.open(io.BytesIO(image_bytes))

        embeddings = DeepFace.represent(image_path, model_name="Facenet")

        print("retornou embeddings")

        result = pb2.AnonymizeRS()

        result.anonymizedImage = bytes(embeddings)

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
