from dotenv import load_dotenv;
import shutil, os;

load_dotenv()

# tuples and variables containing file extensions
imgExtensions = ( ".jpg", ".png", ".jpeg", ".svg", 
                  ".webp", ".jfif", ".pjpeg", ".pjp" )

vidExtensions = ( ".mp4", ".m4p", "m4v", 
                  ".svi", ".mkv", ".avi" )

audExtensions = (".mp3", ".wav", ".m4a",".webm")

gifExtension = ".gif"
pdfExtension = ".pdf"
exeExtension = ".exe"

allExtensions = [ imgExtensions, vidExtensions, 
                  audExtensions, gifExtension, 
                  pdfExtension, exeExtension ]

# get organizing folders from .env file
imgPath = os.getenv('IMG_PATH')
vidPath = os.getenv('VID_PATH')
audPath = os.getenv('AUD_PATH')
gifPath = os.getenv('GIF_PATH')
pdfPath = os.getenv('PDF_PATH')
exePath = os.getenv('EXE_PATH')

allPaths = [imgPath, vidPath, audPath, gifPath, pdfPath, exePath]

user = os.getenv('USER_NAME')

def OrganizeFolder(filePath:str):
    if not os.path.exists(filePath): return "Invalid path."

    # looks for every file in the folder filePath
    for fileName in os.listdir(filePath):
            for i, ext in enumerate(allExtensions):
                # if the file ends with an available extension
                if fileName.endswith(ext, len(fileName) - len(ext) - 1):
                    # move it to the corresponding folder
                    shutil.move(os.path.join(filePath, fileName), allPaths[i])
    return "Folders organized."
                    

# folders to be organized
organizedFolders = [rf"C:\Users\{user}\Downloads", rf"C:\Users\{user}\Desktop"]

for folder in organizedFolders:
    OrganizeFolder(folder)