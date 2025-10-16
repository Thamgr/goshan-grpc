# Goshan gRPC Server

Минимальный асинхронный gRPC сервер на базе `grpclib` с синглтоном GoshanBrain для принятия решений.

## Установка

Создайте виртуальное окружение и установите зависимости:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Генерация Python кода из proto файла

Для `grpclib` используется специальный плагин генерации:

```bash
source venv/bin/activate
python -m grpc_tools.protoc -I. --python_out=. --grpclib_python_out=. gamebot.proto
```

Или используя прямой путь:

```bash
./venv/bin/python -m grpc_tools.protoc -I. --python_out=. --grpclib_python_out=. gamebot.proto
```

Это сгенерирует два файла:
- `gamebot_pb2.py` - классы для proto сообщений
- `gamebot_grpc.py` - классы для gRPC сервиса (для grpclib)

*Примечание: Перед генерацией убедитесь, что установлен пакет `grpcio-tools`.*

## Запуск сервера

Быстрый запуск:

```bash
./run_server.sh
```

Или вручную:

```bash
source venv/bin/activate
python server.py
```

Или:

```bash
./venv/bin/python server.py
```

Сервер запустится на порту `50051`.

## Тестирование

В отдельном терминале запустите клиент:

Быстрый запуск:

```bash
./run_client.sh
```

Или вручную:

```bash
source venv/bin/activate
python client.py
```

Или:

```bash
./venv/bin/python client.py
```

## Архитектура

### Основные файлы:
- **gamebot.proto** - определение gRPC сервиса
- **goshan_brain.py** - асинхронный синглтон класс GoshanBrain с методом process(), возвращающим рандомно 0 или 1
- **server.py** - асинхронный gRPC сервер на базе `grpclib`, который на каждый запрос обращается к GoshanBrain
- **client.py** - пример асинхронного клиента для тестирования

### Сгенерированные файлы:
- **gamebot_pb2.py** - сгенерированные Python классы для proto сообщений
- **gamebot_grpc.py** - сгенерированные Python классы для gRPC сервиса (grpclib)

### Вспомогательные файлы:
- **run_server.sh** - скрипт для быстрого запуска сервера
- **run_client.sh** - скрипт для быстрого запуска клиента
- **requirements.txt** - список зависимостей Python

