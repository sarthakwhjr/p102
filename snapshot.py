
from os import access
import cv2
import dropbox
import time
import random
StartTime=time.time()
def snapshot():
        name=random.randint(0,10)
        videocaptureobject=cv2.VideoCapture(0)
        result=True
        while(result):
                ret,frame=videocaptureobject.read()
                image="image"+str(name)+".png"
                cv2.imwrite(image,frame)
                result=False
        
        print("Snapshot Taken")   
        videocaptureobject.release()
        cv2.destroyAllWindows() 
        return image

def uploadfiles(image):
                 accesstoken="kM06Xp1WUY0AAAAAAAAAAfGwqJv3BYdwgz6OWAvPsueuj5yC2VUcvnreJzuZwUQZ"
                 file=image
                 file_from=file
                 file_to="/imagefolder/"+(image)
                 dbx = dropbox.Dropbox(accesstoken)
                 with open(file_from, 'rb') as f:
                  dbx.files_upload(f.read(), file_to,mode=dropbox.files.Writemode.overwrite)       
def main():
    while(True):
        if ((time.time() - StartTime) >= 5):
            name = snapshot()
            uploadfiles(name)

main()
