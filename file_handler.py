import os
import shutil
import time
from watchdog.events import FileSystemEventHandler
from config import DEFAULT_DEST_DIRS
from database import log_movement

class MoveHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        self.move_file(event.src_path)
    
    def move_file(self, src_path):
        filename = os.path.basename(src_path)
        ext = os.path.splitext(filename)[1].lower()
        dest_dir = DEFAULT_DEST_DIRS.get(ext)
        if dest_dir:
            time.sleep(1)
            dest_path = os.path.join(dest_dir, filename)
            shutil.move(src_path, dest_path)
            log_movement(filename, src_path, dest_path)
            print(f'Moved {filename} to {dest_path}')
        else:
            print(f'No destination specified for {ext} files')

if __name__ == "__main__":
    event_handler = MoveHandler()
    event_handler.on_created("example_file.txt")