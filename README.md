# docker-training
Материальчики для тренинга по докеру
## нужно:
docker,   
docker-compose,  
python,  
git,  
любая из этих команд выдает страничку помощи  
дополнительно для питона стоит pip (устанавливается через apt-get install python-pip). 
должен быть веб-браузер запускаемый на данной машине - links например 
(идеально выполнять на линукс машине - команды прописывались под линукс). 

## sample1

находясь в каталоге sample1 
1) запускаем приложение: python app.py  
   заходим браузером http:\\\localhost:5000\ - убеждаемся что приложение работает  
   останавливаем приложение. 
2) строим образ докер: docker build -t my_docker_flask:latest .  
   запускаем контейнер: docker run -d  my_docker_flask:latest. 
   Задача - добиться того, чтобы по адресу http:\\\XXX.XXX.XXX.XXX:5000\ был доступен hello world. 
3) После выполнения задачи 1 - останавливаем контейнер командой docker stop. 
   Запускаем приложение python app.py. 
   Пробуем запустить контейнер: docker start - убеждаемся что из-за занятого 5000 порта контйенер не стартует. Бывает срывается автодеплой и запуск докер-compose из-за того что порт занят старым контейнером
   
   
## sample2

- здесь app.py - пополнился вычитыванием db_host из переменной окружения и попыткой получить коннект на данную бд
1) Запустим контейнер с postgresql -  
   docker run --name psql -p 5432:5432 -e POSTGRES_PASSWORD=postgres -d --rm postgres  
   находясь в каталоге sample2 выполним:  
   python app.py. 
   видно, что приложение  получило коннект на базу и вычитало версию бд. 
   Остановим приложение. 
2) Соберем и запустим контейнер, предполагая что контейнер сможет получить по дефолту localhost и получить коннект на ранее запущенную базу  
   docker build -t my_docker_flask:latest .  
   docker rm -f training  
   docker run -p 5000:5000 --name training  my_docker_flask:latest  
   Мы видим что коннект на БД получить не удалось, т.к. для контейнера 'localhost' - это то, что находится внутри контейнера.  
3) Остановим контейнера и попробуем запустить их через docker-compose:
   docker stop psql  
   docker stop training  
   docker-compose build  
   docker-compose up  
   Видим, что приложение обращается за коннектом к бд раньше, чем база начинает отвечать на запросы  
4) Задача  
    - использовать в docker-compose директиву depends_on  
    - применить скрипт гарантирующий запуск приложения только после подъема сервиса находящегося в другом контейнере  
    (https://github.com/ufoscout/docker-compose-wait)


