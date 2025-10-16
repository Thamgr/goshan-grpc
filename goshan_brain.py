import random
from threading import Lock


class GoshanBrain:
    """Синглтон класс для принятия решений"""
    
    _instance = None
    _lock = Lock()
    
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance
    
    def process(self):
        """Возвращает рандомно 0 или 1"""
        return random.randint(0, 1)

