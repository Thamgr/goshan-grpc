import random
import asyncio


class GoshanBrain:
    """Синглтон класс для принятия решений"""
    
    _instance = None
    _lock = asyncio.Lock()
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    async def process(self):
        """Возвращает рандомно 0 или 1"""
        return random.randint(0, 1)

