#program for monitoring a folder and renaming any new files that enter the directory
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"New file created: {event.src_path}")

def main():
    path = 'C:\\Users\Public\\Documents\\Waves' #I have a testing directory setup in my laptop
    os.makedirs(path, exist_ok=True)  # Create the directory if it doesn't exist
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()






