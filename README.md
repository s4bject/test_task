# Пример серверного приложения на Flask

Это простое серверное приложение на Flask для управления пользователями.

## Конфигурация

Для настройки приложения необходимо изменить ключи в файле `config.py` на свои данные доступа к базе данных PostgreSQL:

```python
class Config:
    SECRET_KEY = 'ldgjsdlfksdgkljhsdfjgkhjsdfjgcm,vbnshguirjsgsxlkj'
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost/database_name'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```
# Запуск приложения
Для запуска приложения выполните следующие шаги:

Установите необходимые зависимости из файла requirements.txt:

```bash

pip install -r requirements.txt
```
Убедитесь, что ваша PostgreSQL база данных запущена и доступна.
Запустите сервер приложения:
```bash
python server.py
```
После запуска вы сможете открыть приложение в вашем браузере по адресу http://localhost:5000.
