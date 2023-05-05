import grpc
from concurrent import futures
import time
import anonymize_pb2_grpc as pb2_grpc
import anonymize_pb2 as pb2
from deepface import DeepFace
from PIL import Image
import io
import logging

logger = logging.getLogger(__name__)
img_aux_path = "./aux.jpg"


class AnonymizationService(pb2_grpc.AnonymizerServicer):
    def __init__(self, *args, **kwargs):
        pass

    def Anonymize(self, request, context):
        logger.info("Request received")

        logger.debug("Request: %s", str(request))

        image_bytes = request.image

        image = Image.open(io.BytesIO(image_bytes))

        image.save(img_aux_path)

        embeddings = DeepFace.represent(img_aux_path)

        logger.info("Embeddings returned")

        result = pb2.AnonymizeRS()

        result.embeddings = embeddings[0]["embeddings"]

        logger.debug("Result: %s", str(result))

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
