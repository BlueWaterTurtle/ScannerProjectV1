import os
import time
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pyzbar.pyzbar import decode
from PIL import Image
import PyMuPDF # fitz, I've swapped these around. I had Fitz as the import, I'll probably need to find where "fitz" is called below and modify that.
import io
import configparser
import logging

# Configure logging
logging.basicConfig(filename='file_monitor.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Read configuration
config = configparser.ConfigParser()
config.read('config.ini')

SOURCE_DIR = config['directories']['source_dir']
DESTINATION_DIR = config['directories']['destination_dir']
FINISHED_DIR = config['directories']['finished_dir']

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        time.sleep(5)  # Delay to allow the scanner to finish
        print(f"New file created: {event.src_path}")
        logging.info(f"New file created: {event.src_path}")
        os.makedirs(DESTINATION_DIR, exist_ok=True)
        os.makedirs(FINISHED_DIR, exist_ok=True)

        # Extract barcode data from the file
        barcode_data = self.extract_barcode(event.src_path)
        if barcode_data:
            file_extension = os.path.splitext(event.src_path)[1]
            new_name = f"{barcode_data}{file_extension}"
            destination_path = os.path.join(DESTINATION_DIR, new_name)
            logging.info(f"New file created: {event.src_path}")
            
            if os.path.exists(destination_path):
                base_name = os.path.splitext(new_name)[0]
                timestamp = time.strftime("%Y%m%d%H%M%S")
                new_name = f"{base_name}_{timestamp}{file_extension}"
                destination_path = os.path.join(DESTINATION_DIR, new_name)

            shutil.copy(event.src_path, destination_path)
            print(f"File copied and renamed to: {destination_path}")
            logging.info(f"File copied and renamed to: {destination_path}")

            if file_extension.lower() == '.png':
                pdf_path = self.convert_png_to_pdf(destination_path)
                if pdf_path:
                    print(f"PNG converted to PDF: {pdf_path}")
                    logging.info(f"PNG converted to PDF: {pdf_path}")
                    self.move_to_finished(pdf_path, FINISHED_DIR)
            elif file_extension.lower() == '.pdf':
                self.move_to_finished(destination_path, FINISHED_DIR)
        else:
            print("No barcode detected in the file.")
            logging.warning("No barcode detected in the file.")

    def extract_barcode(self, file_path):
        try:
            file_extension = os.path.splitext(file_path)[1].lower()
            if file_extension == '.pdf':
                return self.extract_barcode_from_pdf(file_path)
            else:
                return self.extract_barcode_from_image(file_path)
        except Exception as e:
            print(f"Error extracting barcode: {e}")
            return None

    def extract_barcode_from_image(self, file_path):
        try:
            img = Image.open(file_path)
            decoded_objects = decode(img)
            if decoded_objects:
                return decoded_objects[0].data.decode('utf-8')
            else:
                return None
        except Exception as e:
            print(f"Error extracting barcode from image: {e}")
            return None
        finally:
            img.close()

    def extract_barcode_from_pdf(self, file_path):
        try:
            doc = fitz.open(file_path)
            for page_num in range(len(doc)):
                page = doc.load_page(page_num)
                pix = page.get_pixmap()
                img = Image.open(io.BytesIO(pix.tobytes()))
                decoded_objects = decode(img)
                if decoded_objects:
                    return decoded_objects[0].data.decode('utf-8')
            return None
        except Exception as e:
            print(f"Error extracting barcode from PDF: {e}")
            return None
        finally:
            doc.close()

    def convert_png_to_pdf(self, png_path):
        try:
            img = Image.open(png_path)
            pdf_path = os.path.splitext(png_path)[0] + '.pdf'
            img.save(pdf_path, 'PDF', resolution=100.0)
            return pdf_path
        except Exception as e:
            print(f"Error converting PNG to PDF: {e}")
            return None

    def move_to_finished(self, file_path, finished_dir):
        try:
            shutil.move(file_path, finished_dir)
            print(f"File moved to: {os.path.join(finished_dir, os.path.basename(file_path))}")
        except Exception as e:
            print(f"Error moving file to finished directory: {e}")

def main():
    os.makedirs(SOURCE_DIR, exist_ok=True)
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, SOURCE_DIR, recursive=True)
    observer.start()
    print("Observer started. Monitoring directory for changes...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Keyboard interrupt received. Stopping observer...")
        observer.stop()
    observer.join()
    print("Observer stopped.")

if __name__ == "__main__":
    main()
    input("Press Enter to exit...")
