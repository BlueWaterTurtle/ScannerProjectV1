#program for monitoring a folder and renaming any new files that enter the directory
import time
from watchdog.observers import observer
from watchdog.events import filesystemeventhandler

class myhandler(filesystemeventhandler):
    def on_created(self, event):
        print(f"new file created: {ecent.src_path}")

def main():
    path = 'C:\Users\Public\Documents\Waves' #I have a testing directory setup in my laptop
    event_handler = myhandler()
    observer = observer()
    observer.scheduler(event_handler, path, recursive=true)
    observer.start()

    try:
        while true:
            time.sleep(1)
    except keyboardinterupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()






