# **Лабораторна робота №4**
---
## Послідовність виконання лабораторної роботи:
#### 1. Для ознайомляння з `Docker` звернувся до документації.
#### 2. Для перевірки чи докер встановлений і працює правильно на віртуальній машині запустітив перевірку версії командою `sudo docker -v > my_work.log`, виведення допомоги командою `sudo docker --help >> my_work.log` та тестовий імедж командою `sudo docker run docker/whalesay cowsay Docker is fun >> my_work.log`. Вивід цих команд перенаправляв у файл `my_work.log` та закомітив його до репозиторію.
#### 3. `Docker` працює з Імеджами та Контейнерами. Імедж це свого роду операційна система з попередньо інстальованим ПЗ. Контейнер це запущений Імедж. Ідея роботи `Docker` дещо схожа на віртуальні машини. Спочатку створив імедж з якого буде запускатись контейнер.
#### 4. Для знайомства з `Docker` створив імедж із `Django` сайтом зробленим у попередній роботі.
1. ##### Оскільки мій проект на `Python` то і базовий імедж також потрібно вибрати відповідний. Використовую команду `docker pull python:3.8-slim` щоб завантажити базовий імедж з репозиторію. Переглядаю створеного вміст імеджа командою `docker inspect python:3.8-slim`
    ##### Перевіряю чи добре встановився даний імедж командою:
    
    ```text
    mishakin@mishakin-VirtualBox:~/Git/_ik31_Mishakin_labs_TPIS/lab4$ sudo docker images
    [sudo] password for mishakin: 
    REPOSITORY            TAG          IMAGE ID       CREATED          SIZE
    servaretur/lab4       monitoring   9053777b088d   21 minutes ago   373MB
    servaretur/lab4       django       31a526a6e9f7   43 minutes ago   373MB
    python                3.8-slim     214d62795dbb   2 weeks ago      122MB
    hello-world           latest       feb5d9fea6a5   7 weeks ago      13.3kB


    ```
2. ##### Створив файл з іменем `Dockerfile` та скопіював туди вміс такого ж файлу з репозиторію викладача.
    ###### Вміст файлу `Dockerfile`:
    ```text
    FROM python:3.8-slim
    
    LABEL author="Bohdan"
    LABEL version=1.0
    
    # оновлюємо систему
    RUN apt-get update && apt-get upgrade -y
    
    # Встановлюємо потрібні пакети
    RUN apt-get install git -y && pip install pipenv
    
    # Створюємо робочу папку
    WORKDIR /lab
    
    # Завантажуємо файли з Git
    RUN git clone https://github.com/BobasB/devops_course.git
    
    # Створюємо остаточну робочу папку з Веб-сайтом та копіюємо туди файли
    WORKDIR /app
    RUN cp -r /lab/devops_course/lab3/* .
    
    # Інсталюємо всі залежності
    RUN pipenv install
    
    # Відкриваємо порт 8000 на зовні
    EXPOSE 8000
    
    # Це команда яка виконається при створенні контейнера
    ENTRYPOINT ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
    ```
3. ##### Ознайомився із коментарями та зрозумів структуру написання `Dockerfile`.
4. ##### Змінений`Dockerfile` файл:
    ```text
   FROM python:3.8-slim
   LABEL author="Bohdan"
   LABEL version=1.0
   
   # оновлюємо систему
   RUN apt-get update && apt-get upgrade -y
   
   # Встановлюємо потрібні пакети
   RUN apt-get install git -y && pip install pipenv && pip install django
   
   # Створюємо робочу папку
   WORKDIR /lab
   
   # Завантажуємо файли з Git
   RUN git clone https://github.com/MishakinMax/_ik31_Mishakin_labs_TPIS.git
   
   # Створюємо остаточну робочу папку з Веб-сайтом та копіюємо туди файли
   WORKDIR /app
   RUN cp -r /lab/_ik31_Mishakin_labs_TPIS/lab3/* .
   
   # Інсталюємо всі залежності
   RUN pipenv install
   
   # Відкриваємо порт 8000 на зовні
   EXPOSE 8000
   
   # Це команда яка виконається при створенні контейнера
   ENTRYPOINT ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
    ```
#### 5. Створив власний репозиторій на [Docker Hub](https://cloud.docker.com/repository/registry-1.docker.io/pavlovulchak/lab4). Для цього залогінився у власний аккаунт на `Docker Hub` після чого перейшов у вкладку Repositories і далі натиснув кнопку `Create new repository`.
#### 6. Виконав білд (build) Docker імеджа та завантажтажив його до репозиторію. Для цього я повинен вказати правильну назву репозиторію та TAG. Оскільки мій репозиторій `servaretur/lab4` то команда буде виглядати `sudo docker build -t servaretur/lab4:django .`, де `django` - це тег.
Команда для завантаження на власний репозеторій `docker push servaretur/lab4`.
Посилання на мій [`Docker Hub`](https://github.com/MishakinMax/_ik31_Mishakin_labs_TPIS/tree/master/lab4) репозиторій та посилання на [`імедж`](https://hub.docker.com/repository/docker/servaretur/lab4).
#### 7. Для запуску веб-сайту виконав команду `sudo docker run -it --name=django --rm -p 8000:8000 servaretur/lab4`:
```text
mishakin@mishakin-VirtualBox:~/Git/_ik31_Mishakin_labs_TPIS/lab4$ sudo docker run -it --name=django --rm -p 8000:8000 lab45:django
[sudo] password for mishakin: 
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
November 14, 2021 - 14:52:05
Django version 3.2.9, using settings 'my_site.settings'
Starting development server at http://0.0.0.0:8000/
Quit the server with CONTROL-C.

```
#### 8. Оскільки веб-сайт готовий і працює, потрібно створит ще один контейнер із програмою моніторингу нашого веб-сайту (Моє Завдання на роботу):
1. ##### Створив ще один Dockerfile з назвою `Dockerfile.site` в якому помістив програму моніторингу.
    Вміст файлу `Dockerfile.site`:
```text
    FROM python:3.8-slim

LABEL author="Bohdan"
LABEL version=1.0

# оновлюємо систему
RUN apt-get update && apt-get upgrade -y

# Встановлюємо потрібні пакети
RUN apt-get install git -y && pip install pipenv && pip install django

# Створюємо робочу папку
WORKDIR /lab

# Завантажуємо файли з Git
RUN git clone https://github.com/MishakinMax/_ik31_Mishakin_labs_TPIS.git

# Створюємо остаточну робочу папку з Веб-сайтом та копіюємо туди файли
WORKDIR /app
RUN cp -r /lab/_ik31_Mishakin_labs_TPIS/lab3/* .

# Інсталюємо всі залежності
RUN pipenv install

# Відкриваємо порт 8000 на зовні
EXPOSE 8000

# Це команда яка виконається при створенні контейнера
ENTRYPOINT ["pipenv", "run", "python", "monitoring.py", "0.0.0.0:8000"]
```
2. ##### Виконав білд даного імеджа та дав йому тег `monitoring` командами:
    ```text
    sudo docker build -f Dockerfile.site -t servaretur/lab4:monitoring .
    docker push servaretur/lab4:monitoring
    ```
3. ##### Запустив два контейнери одночасно (у різних вкладках) та переконався що програма моніторингу успішно доступається до сторінок мого веб-сайту.
    ##### Використовуючи команди:
    Запуск серевера:
    ```text
    mishakin@mishakin-VirtualBox:~/Git/_ik31_Mishakin_labs_TPIS/lab4$ docker run -it --name=django --rm -p 8000:8000 servaretur/lab4:django
    Watching for file changes with StatReloader
    Performing system checks...
    
    System check identified no issues (0 silenced).
    
    You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
    Run 'python manage.py migrate' to apply them.
    November 13, 2021 - 21:44:04
    Django version 3.2.9, using settings 'my_site.settings'
    Starting development server at http://0.0.0.0:8000/
    Quit the server with CONTROL-C.
    Invalid HTTP_HOST header: '0.0.0.0:8000'. You may need to add '0.0.0.0' to ALLOWED_HOSTS.
    Bad Request: /
    [13/Nov/2021 21:44:30] "GET / HTTP/1.1" 400 60228
    Invalid HTTP_HOST header: '0.0.0.0:8000'. You may need to add '0.0.0.0' to ALLOWED_HOSTS.
    Bad Request: /favicon.ico
    [13/Nov/2021 21:44:30] "GET /favicon.ico HTTP/1.1" 400 60290
    [13/Nov/2021 21:48:42] "GET /health HTTP/1.1" 301 0
    [13/Nov/2021 21:48:42] "GET /health/ HTTP/1.1" 200 340
    [13/Nov/2021 21:49:42] "GET /health HTTP/1.1" 301 0
    [13/Nov/2021 21:49:42] "GET /health/ HTTP/1.1" 200 340
    23:53:19 pavlovulchak ~/TPIS/Pavlo_Vulchak_IK_31/Lab4 (master) $ 
    ```
    Запуск моніторингу:
    ```text
    mishakin@mishakin-VirtualBox:~/Git/_ik31_Mishakin_labs_TPIS/lab4$ sudo docker run -it --name=monitoring --rm --net=host -v $(pwd)/server.log:/app/server.log servaretur/lab4:monitoring
    ```
    (перед запуском моніторингу спочатку створив файл server.log)
    Вміст файла `Server.log`:
```text
INFO 2021-11-14 14:20:25,071 root : Сервер доступний. Час на сервері: 14.11.21 14:20
INFO 2021-11-14 14:20:25,072 root : Запитувана сторінка: : localhost:8000/health/
INFO 2021-11-14 14:20:25,072 root : Відповідь сервера місти наступні поля:
INFO 2021-11-14 14:20:25,072 root : Ключ: date, Значення: 14.11.21 14:20
INFO 2021-11-14 14:20:25,072 root : Ключ: current_page, Значення: localhost:8000/health/
INFO 2021-11-14 14:20:25,072 root : Ключ: server_info, Значення: OSName: Linux; NodeName: ac93d9c1a00d; Release:5.11.0-40-generic; Version:#44~20.04.2-Ubuntu SMP Tue Oct 26 18:07:44 UTC 2021; Indentificator:x86_64
INFO 2021-11-14 14:20:25,072 root : Ключ: client_info, Значення: Browser: python-requests/2.26.0  IP: 172.17.0.1 
INFO 2021-11-14 14:21:25,128 root : Сервер доступний. Час на сервері: 14.11.21 14:21
INFO 2021-11-14 14:21:25,128 root : Запитувана сторінка: : localhost:8000/health/
INFO 2021-11-14 14:21:25,128 root : Відповідь сервера місти наступні поля:
INFO 2021-11-14 14:21:25,128 root : Ключ: date, Значення: 14.11.21 14:21
INFO 2021-11-14 14:21:25,128 root : Ключ: current_page, Значення: localhost:8000/health/
INFO 2021-11-14 14:21:25,128 root : Ключ: server_info, Значення: OSName: Linux; NodeName: ac93d9c1a00d; Release:5.11.0-40-generic; Version:#44~20.04.2-Ubuntu SMP Tue Oct 26 18:07:44 UTC 2021; Indentificator:x86_64
INFO 2021-11-14 14:21:25,128 root : Ключ: client_info, Значення: Browser: python-requests/2.26.0  IP: 172.17.0.1 

```
4. ##### Закомітив `Dockerfile.site` та результати роботи програми моніторингу запущеної з `Docker` контейнера.
