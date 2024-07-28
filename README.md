# An auto file organizer?

https://github.com/user-attachments/assets/b6cd7914-0789-49bd-a097-400e76057c3d

_Moves every file in one or more folders to their respective organized extension folder._

# Guide

  _1. Firstly, clone this repository using **git clone [[repository link]](https://github.com/sunbaee/FileOrganizer.git)**<br>_
  _2. Type inside the project folder in the terminal `pip install python-dotenv`_

## Add a **.env file** inside the project folder containing these variables:
 - USER_NAME
 - IMG_PATH
 - VID_PATH
 - AUD_PATH
 - GIF_PATH
 - PDF_PATH
 - EXE_PATH

### Each _PATH_ variable should contain a string with the file path to the folder you want to organize with each file extension.
_Example: VID_PATH = "C:\Users\\(your user here)\Videos"_

_**> USER_NAME should contain your user on the pc.**_ <br>
_The **user variable** is used to access the download and desktop folders in your pc, which are the default folders that'll be organized._

Once the .env file is finished, everything should work fine _-unless you use an OS other than windows. If yes, follow the insctructions in the section below-_. 
To run the program, type inside the project folder in the terminal `py main.pyw`.

### Extra configuration:
If you want, you can add more folders to organize or change the folders you want to organize: just go to **line 49** and add or change Strings in the **organizedFolder** list with the paths you want to organize, following the other String models _(rf"Your path here")_.<br><br>
_You can create a shortcut of the script in a folder set to an environment variable so the script becomes accessible from anywhere. Here's a link explaining how to do it:
[[here]](https://superuser.com/questions/1354503/how-do-i-make-my-batch-code-a-command-i-can-access-anywhere)_

# For non-windows users:
The default script is set to work in the _windows OS_. To change it, go to **main.pyw** and change the **organizedFolders** list, at **line 49**, according to your OS file system path.
