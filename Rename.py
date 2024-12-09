#program for monitoring a folder and renaming any new files that enter the directory

import os
import time
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"New file created: {event.src_path}")
        destination_dir = 'C:\\Users\\Public\\Documents\\ProcessedWaves'                  # Define the destination directory
        os.makedirs(destination_dir, exist_ok=True)                                       # Create the directory if it doesn't exist

                                                                                         
        file_name, file_extension = os.path.splitext(os.path.basename(event.src_path))    # Extracting file name and extension

         # Define the new name and path
        new_name = f"{file_name}_renamed{file_extension}"
        destination_path = os.path.join(destination_dir, new_name)


        
        shutil.copy(event.src_path, destination_dir)                                      # Copy the file to the destination directory
        print(f"File copied and renamed to: {destination_path}")

def main():
    path = 'C:\\Users\Public\\Documents\\Waves'                                           #I have a testing directory setup in my laptop
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






