# О проекте

[py-savemp3youtube-cmdbot](https://github.com/kaefik/py-savemp3youtube-cmdbot) - телеграмм бот получает ссылку на видео ютуба и возвращает звуковую дорожку видео.

# Реализованные возможности:

- получение ссылки на видео ютуба -> на выходе пользователю возвращается звуковая дорожка видео (файлы в формате mp3)
- mp3 файл делятся на несколько каждый длительностью 60 минут
- администратор бота только один пользователь
- администратор может выполнять следующие действия: добавить пользователя по id, удалить пользователя из доступа к данному боту, информация о тех пользователях кто имеет доступ
- каждый пользователь может удалить все mp3 файлы которые хранятся на сервере где работает бот

# Настройка проекта для запуска

## Установка зависимостей

```bash
pip3 install telethon
pip3 install requests
```

или запустите файл install_libs.sh

## Установить программы для работы

- [mp3splt](https://mp3splt.sourceforge.net/mp3splt_page/home.php) - для разбивания аудофайлов различных форматов без декодинга.

Для установки на убунту:

```bash
apt install -y mp3splt 
apt-get install -y ffmpeg
```

- в папке plugins_bot/yotube2mp3 находится *yt-dlp_linux* - скачивает и конвертирует ютуб видео в mp3, 
для установки новой версии можете скачать [здесь](https://github.com/yt-dlp/yt-dlp/releases)


## Конфигурационные файлы проекта:

* **cfg/config_tlg.py** - за основу можно взять файл config_tlg_example.py

  ```
    # здесь указывается переменные для запуска телеграмм бота
    TLG_APP_NAME = "tlgbotappexample"  # APP NAME get from https://my.telegram.org
    TLG_APP_API_ID = 1258887  # APP API ID get from https://my.telegram.org
    TLG_APP_API_HASH = "sdsadsadasd45522665f"  # APP API HASH get from https://my.telegram.org
    I_BOT_TOKEN = "0000000000:sfdfdsfsdf5s5541sd2f1sd5"  # TOKEN Bot from BotFather
    TLG_ADMIN_ID_CLIENT = [1258889]  # admin clients for admin telegram bot
    # proxy for Telegram
    TLG_PROXY_SERVER = None  # address MTProxy Telegram
    TLG_PROXY_PORT = None  # port  MTProxy Telegram
    TLG_PROXY_KEY = None  # secret key  MTProxy Telegram
    # for save settings user
    # CSV - сохранение данных настроек для доступа к боту используя БД в формате CSV
    # SQLITE - сохранение данных настроек для доступа к боту используя БД в формате sqlite3
    TYPE_DB = "SQLITE"
  ```

Параметром **TYPE_DB** можно выбрать сохранять настройки с помощью sqlite3 или в файле csv (бывает полезно когда по
каким-то причинам на устройстве нет встроенной библиотеки slite3)

# Запуск бота как сервис

сохраним файл start-youtube-audio.service в папку /etc/systemd/system

```bash
[Unit]
Description=Youtube video to audio
After=network.target

[Service]
ExecStart=/bin/bash /home/scripts/py-savemp3youtube-cmdbot/start-youtube2mp3.sh

[Install]
WantedBy=default.target
```

Запуск сервиса

```bash
systemctl enable start-youtube-audio.service
systemctl start start-youtube-audio.service
```

# Запуск сервиса как docker контейнер

* создание образа контейнера

```buildoutcfg
docker build -t tlgyoutube2mp3bot .  
```

* запуск образа для тестирования

```bash
docker run --rm --it   -v "/home/oilnur/youtube2mp3/config_tlg.py:/home/app/cfg/config_tlg.py" -v "/home/oilnur/youtube2mp3/mp3:/home/app/mp3" tlgyoutube2mp3bot
```

* запуск образа в бою

```bash
docker run --restart=always -v "/home/oilnur/youtube2mp3/config_tlg.py:/home/app/cfg/config_tlg.py" -v "/home/oilnur/youtube2mp3/mp3:/home/app/mp3" tlgyoutube2mp3bot
```


