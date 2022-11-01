import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir="C:/Users/91950/Desktop/P102/F1"
to_dir="C:/Users/91950/Desktop/P102/F2"
listF1=os.listdir(from_dir)
#print(listF1)


class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"Hey{event.src_path}! has created")
        time.sleep(1)
    def on_deleted(self, event):
        print(f"Hey{event.src_path}! has deleted")
        time.sleep(1)
    def on_modified(self, event):
        print(f"Hey{event.src_path}! has modified")
        time.sleep(1)
    def on_moved(self, event):
        print(f"Hey{event.src_path}! has moved")
        time.sleep(1)    

# Initialize Event Handler Class
event_handler = FileMovementHandler()


# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("program stopped")
    observer.stop()