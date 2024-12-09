# Program for monitoring a folder and renaming any new files that enter the directory
import os
import time
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pyzbar.pyzbar import decode
from PIL import Image

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"New file created: {event.src_path}")
        destination_dir = 'C:\\Users\\Public\\Documents\\ProcessedWaves'  # Define the destination directory
        os.makedirs(destination_dir, exist_ok=True)  # Create the directory if it doesn't exist

        # Extract barcode data from the image
        barcode_data = self.extract_barcode(event.src_path)
        if barcode_data:
            # Define the new name and path
            file_extension = os.path.splitext(event.src_path)[1]
            new_name = f"{barcode_data}{file_extension}"
            destination_path = os.path.join(destination_dir, new_name)

            # Copy and rename the file to the destination directory
            shutil.copy(event.src_path, destination_path)
            print(f"File copied and renamed to: {destination_path}")
        else:
            print("No barcode detected in the file.")

    def extract_barcode(self, file_path):
        # Open the image file
        try:
            img = Image.open(file_path)
            decoded_objects = decode(img)
            if decoded_objects:
                # Return the first decoded barcode data (assuming one barcode per image)
                return decoded_objects[0].data.decode('utf-8')
            else:
                return None
        except Exception as e:
            print(f"Error extracting barcode: {e}")
            return None

def main():
    path = 'C:\\Users\\Public\\Documents\\Waves'  # I have a testing directory setup in my laptop
    os.makedirs(path, exist_ok=True)  # Create the directory if it doesn't exist
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    print("Observer started. Monitoring directory for changes...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Keyboard interrupt received. Stopping observer...")
        observer.stop()
   # observer.join()
   # print("Observer stopped.")

if __name__ == "__main__":
    main()
    input("press Enter to Exit...")
