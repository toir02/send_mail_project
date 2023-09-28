# Сервис рассылок

### Используемые технологии
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white) ![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white) ![HTML](https://img.shields.io/badge/html-%23E34F26.svg?style=for-the-badge&logo=html&logoColor=white) ![CSS](https://img.shields.io/badge/css-%231572B6.svg?style=for-the-badge&logo=css&logoColor=white) ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E) ![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)
____

### Для чего нужен этот проект?
Сервис рассылок - это веб-приложение для управления рассылками. Проект создан для отправки рассылок на электронную почту клиентов, управления рассылками и сбора статистики.

____

### Сущности системы
#### Клиент сервиса
* Email клиента
* Имя клиента
* Комментарий к клиенту

#### Настройки рассылки
* Время начала рассылки
* Время окончания рассылки
* Период рассылки
* Статус рассылки

#### Сообщение рассылки
* Заголовок сообщения
* Текст сообщения

#### Логи рассылки
* Дата и время последней попытки отправки рассылки
* Статус рассылки
* Ответ почтового сервера

#### Пользователь
* Email
* Пароль

____

### Как использовать данный проект?
* Склонировать репозиторий в IDE
  
  В терминале ввести команду:
  ```
  git clone https://github.com/toir02/send_mail_project
* Установить вирутальное окружение

  В терминале ввести команду:
  ```
  python3 -m venv venv
  ```
* Активировать виртуальное окружение

  В терминале ввести команду:
  ```
  source venv/bin/activate
  ```
* Установить зависимости

  В терминале ввести команду:
  ```
  pip install -r requirements.txt
  ```
* Создать файл ``.env``. Его необходимо заполнить данными из файла ``.env.sample``
* Создать базу данных, одноименную с названием базы данных в заполненном вами файле ``.env``
* Создать и применить миграции

  В терминале ввести следующие команды:
  ```
  python3 manage.py makemigrations
  ```
  ```
  python3 manage.py migrate
  ```
* Создать суперпользователя с данными, которые находятся модуле ``csu.py``

  В терминале ввести команду:
  ```
  python3 manage.py csu
  ```
* Запустить сервер локально

  В терминале ввести команду:
  ```
  python3 manage.py runserver
  ```
____

#### Контакты
Если у вас возникли вопросы или проблемы при использовании проекта, свяжитесь со мной.

tg: @toir02
