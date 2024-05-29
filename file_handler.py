import os
import shutil
import time
from watchdog.events import FileSystemEventHandler
from config import DEFAULT_DEST_DIRS
from database import log_movement

class MoveHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory: #Проверка папка или файл
            return
        self.move_file(event.src_path)
    
    def move_file(self, src_path):
        filename = os.path.basename(src_path) #Функция вытаскивает имя файлы из пути
        ext = os.path.splitext(filename)[1].lower() #вытаскиваем расширение файла
        dest_dir = DEFAULT_DEST_DIRS.get(ext)
        if dest_dir:
            time.sleep(1) #нужна, иначе файл занят другим... протестить меньшую паузу
            dest_path = os.path.join(dest_dir, filename) #Полный путь файла в целевой директории
            shutil.move(src_path, dest_path) #Само перемещение файла
            log_movement(filename, src_path, dest_path) #Запись в бд
            print(f'Moved {filename} to {dest_path}') 
        else:
            print(f'No destination specified for {ext} files')

if __name__ == "__main__": #А это что я тут написал??
    event_handler = MoveHandler()
    event_handler.on_created("example_file.txt")