import face_recognition
from shutil import move
import os, os.path

# Get total of files in a folder
# DIR = "/home/fhery/faceRecognition/Photos/"
DIR = "/home/fhery/Pictures/tbojfu/Photos/"
# cant_files = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
# # print (cant_files)

# Create an encoding of my facial features than can be compared to other faces
picture_of_me = face_recognition.load_image_file(DIR+"IMG_4973.jpg")
my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

#
# Lista de archivos con extencion
onlyfiles = next(os.walk(DIR))[2]
mis_extenciones = []
for foto in onlyfiles:
    # Obteniendo las extensiones
    extension = foto.split(".")[1]
    # Obteniendo extensiones unicas de lista para ver cuales son lis tipos de archivos
    # mis_extenciones.append(extension)
    # mis_exts = set(mis_extenciones)
    # Creando grupos de extensiones
    if extension == "png" or extension == "jpg":
        # print(foto)
        # Load this picture
        new_picture = face_recognition.load_image_file(DIR+foto)
        # Iterate through every face detected in the new picture
        for face_encoding in face_recognition.face_encodings(new_picture):
            # Run the algorithm of face comparison for the detected face, with 0.5 tolerance
            results = face_recognition.compare_faces([my_face_encoding], face_encoding, 0.5)
            # Save the image to a separate folder if there is a match
            if results[0] == True:
                move(DIR+foto, "/home/fhery/Pictures/tbojfu/Madox/"+foto)
            else:
                print("No hay coincidencias")
