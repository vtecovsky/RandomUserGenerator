# RandomUserGenerator
RandomUserGenerator - это веб-сервис, позволяющий получить N случайно сгенерированных несуществующих пользователей. 

## Содержание

1. [Установка](#установка)
2. [Запуск](#запуск)
3. [Примеры использования API](#примеры-использования)

## Установка

Чтобы установить проект, его нужно склонировать себе на компьютер, прописав в терминале команду ниже.
```bash
git clone https://github.com/vtecovsky/RandomUserGenerator
```

## Запуск

Для запуска проекта с использованием Docker Compose, находясь в директории проекта, необходимо прописать в терминале следующую команду: 

```bash
docker-compose up -d
```

Проект будет запущен и доступен по адресу 127.0.0.1:8000.

## Примеры использования

GET /api/v1/users/ - возвращает N случайно сгенерированных несуществующих пользователей

    Например, http://127.0.0.1:8000/api/v1/users/?n=500

Вы можете протестировать API по адресу 127.0.0.1:8000/docs
