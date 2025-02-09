# Copyright (c) 2022 - 2024 EDM115
import os


class Config:
    APP_ID = int(os.environ.get("APP_ID", "26775695"))
    API_HASH = os.environ.get("API_HASH", "b15bb60859bef151762fc5d9eb206c67")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7684599268:AAFf97fALKymo_Xi1hb3t0kiFP8Wmis1k8I")
    LOGS_CHANNEL = (
        int(os.environ.get("LOGS_CHANNEL", "-1002482663527"))
        if os.environ.get("LOGS_CHANNEL").strip("-").isdigit()
        else os.environ.get("LOGS_CHANNEL", "-1002482663527")
    )
    MONGODB_URL = os.environ.get("MONGODB_URL", "mongodb+srv://pangphu9:0pSRO3UHIoH5ouAx@cluster0.ipqp2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    MONGODB_DBNAME = os.environ.get("MONGODB_DBNAME", "Unzipper_Bot")
    BOT_OWNER = int(os.environ.get("BOT_OWNER", "1200411908"))
    DOWNLOAD_LOCATION = f"{os.path.dirname(__file__)}/Downloaded"
    THUMB_LOCATION = f"{os.path.dirname(__file__)}/Thumbnails"
    TG_MAX_SIZE = 2097152000
    MAX_MESSAGE_LENGTH = 4096
    # Default chunk size (0.005 MB → 1024*6) Increase if you need faster downloads
    CHUNK_SIZE = 1024 * 1024 * 10  # 10 MB
    BOT_THUMB = f"{os.path.dirname(__file__)}/bot_thumb.jpg"
    MAX_CONCURRENT_TASKS = 75
    MAX_TASK_DURATION_EXTRACT = 120 * 60  # 2 hours (in seconds)
    MAX_TASK_DURATION_MERGE = 240 * 60  # 4 hours (in seconds)
