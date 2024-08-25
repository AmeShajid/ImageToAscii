#first pipinstall pywhatkit
import pywhatkit 
import os

#here is the image file path
#we made it a string incase there are numbers
imagefilepath = str(input("Enter the path of the image to convert: "))

#here change the ending of the image to txt
savefilepath = str(input("Change the file name to txt: "))

#this is what converts it to the art
#there needs to be error handling in case you put a file that doesn't exist
try:
    pywhatkit.image_to_ascii_art(imagefilepath, savefilepath)
    #this is to get the absolute path of the saved file
    full_save_path = os.path.abspath(savefilepath)
    print("Conversion Complete!")
    print(F"This file is saved at: {full_save_path}")
except:
    print("Error")


