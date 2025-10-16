# Goshan gRPC Server

Минимальный gRPC сервер с синглтоном GoshanBrain для принятия решений.

## Установка

Создайте виртуальное окружение и установите зависимости:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Генерация Python кода из proto файла

```bash
source venv/bin/activate
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. gamebot.proto
```

Или используя прямой путь:

```bash
./venv/bin/python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. gamebot.proto
```

*Примечание: Файлы `gamebot_pb2.py` и `gamebot_pb2_grpc.py` уже сгенерированы.*

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
- **goshan_brain.py** - синглтон класс GoshanBrain с методом process(), возвращающим рандомно 0 или 1
- **server.py** - gRPC сервер, который на каждый запрос обращается к GoshanBrain
- **client.py** - пример клиента для тестирования

### Сгенерированные файлы:
- **gamebot_pb2.py** - сгенерированные Python классы для proto сообщений
- **gamebot_pb2_grpc.py** - сгенерированные Python классы для gRPC сервиса

### Вспомогательные файлы:
- **run_server.sh** - скрипт для быстрого запуска сервера
- **run_client.sh** - скрипт для быстрого запуска клиента
- **requirements.txt** - список зависимостей Python

