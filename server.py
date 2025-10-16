import asyncio
from grpclib.server import Server
from grpclib.utils import graceful_exit
import gamebot_pb2
import gamebot_grpc
from goshan_brain import GoshanBrain


class GameBotService(gamebot_grpc.GameBotBase):
    """Реализация gRPC сервиса GameBot"""
    
    def __init__(self):
        self.brain = GoshanBrain()
    
    async def SendAction(self, stream):
        """Обрабатывает запрос Action и возвращает ActionResponse"""
        # Получаем запрос
        request = await stream.recv_message()
        
        # Получаем решение от GoshanBrain
        decision = await self.brain.process()
        
        # Формируем ответ
        response = gamebot_pb2.ActionResponse(
            status=str(decision)
        )
        
        print(f"Получен запрос: x={request.x}, y={request.y}, duration={request.duration}")
        print(f"Решение GoshanBrain: {decision}")
        
        # Отправляем ответ
        await stream.send_message(response)


async def serve():
    """Запуск gRPC сервера"""
    server = Server([GameBotService()])
    
    port = 50051
    
    # graceful_exit добавляет обработку сигналов для корректной остановки
    with graceful_exit([server]):
        await server.start("0.0.0.0", port)
        print(f"gRPC сервер запущен на порту {port}")
        await server.wait_closed()


if __name__ == "__main__":
    asyncio.run(serve())

