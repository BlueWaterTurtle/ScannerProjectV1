#program for monitoring a folder and renaming any new files that enter the directory
import time
from watchdog.observers import observer
from watchdog.events import filesystemeventhandler

class myhandler(fileSystemEventHandler):
    def on_created(self, event):
        print(f"new file created: {event.src_path}")

def main():
    path = 'C:\\Users\Public\\Documents\\Waves' #I have a testing directory setup in my laptop
    os.makedirs(path, exist_ok=True)  # Create the directory if it doesn't exist
    event_handler = myhandler()
    observer = Observers()
    observer.schedule(event_handler, path, recursive=true)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()






