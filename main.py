import time
import logging
from watchdog.observers import Observer
from file_handler import MoveHandler
from config import source_dir
from database import init_db
from pathlib import Path
import os

def main(source_dir): #watchdog
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    init_db()
    path = source_dir
    event_handler = MoveHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    # Добавить удаление папки для отслеживания, если она пуста

if __name__ == "__main__":
    default_source_dir = os.path.expanduser('~') + r'\Downloads\saved_files' #изменить, чтобы имя пользователя python определял сам
    user_question = input(f"Использовать директорию для отслеживания по умолчанию?({default_source_dir})\n(y/n)")
    if user_question == "y":
        source_dir = Path(default_source_dir)
    elif user_question == "n":
        source_dir = Path(input("Введите свой путь директории")) #добавить пример директории, проблемы с unicodeescape

    if not source_dir.exists(): #проверка существует ли эта директория
        source_dir.mkdir(parents=True, exist_ok=True)

    main(source_dir)