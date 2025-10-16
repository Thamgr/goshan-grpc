import grpc
from concurrent import futures
import gamebot_pb2
import gamebot_pb2_grpc
from goshan_brain import GoshanBrain


class GameBotServicer(gamebot_pb2_grpc.GameBotServicer):
    """Реализация gRPC сервиса GameBot"""
    
    def __init__(self):
        self.brain = GoshanBrain()
    
    def SendAction(self, request, context):
        """Обрабатывает запрос Action и возвращает ActionResponse"""
        # Получаем решение от GoshanBrain
        decision = self.brain.process()
        
        # Формируем ответ
        response = gamebot_pb2.ActionResponse(
            status=str(decision)
        )
        
        print(f"Получен запрос: x={request.x}, y={request.y}, duration={request.duration}")
        print(f"Решение GoshanBrain: {decision}")
        
        return response


def serve():
    """Запуск gRPC сервера"""
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    gamebot_pb2_grpc.add_GameBotServicer_to_server(GameBotServicer(), server)
    
    port = "50051"
    server.add_insecure_port(f"[::]:{port}")
    server.start()
    
    print(f"gRPC сервер запущен на порту {port}")
    
    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        print("\nОстановка сервера...")
        server.stop(0)


if __name__ == "__main__":
    serve()

