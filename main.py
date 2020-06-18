import os, os.path
#import face_recognition
# from shututil import copyfile

#Create an encoding of my facial features than can be compared to other faces
# picture_of_me = face_recognition.load_image_file("~/faceRecognition/Photos/818D4927-0124-420D-B049-7CEA487EA777.jpg")
# my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

# Get total of files in a folder
DIR = "/home/fhery/faceRecognition/Photos"
# cant_files = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
# # print (cant_files)
#
# # Iterate through all the 10,0000 pictures
# for i in range(1, cant_files):
#     file_name = str(i).zfill(5) + ".jpg"
#     print(file_name)


# Lista de archivos con extencion
onlyfiles = next(os.walk(DIR))[2]
for  nombres in onlyfiles:
    print(nombres)
    Obteniendo las extensiones
    extension = nombres.split(".")
    print(extension[1])
print(onlyfiles)