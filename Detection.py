from imageai.Detection import ObjectDetection
import os

def controller():
    execution_path = os.getcwd()

    detector = ObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath( os.path.join(execution_path , "yolo.h5"))
    detector.loadModel()
    custom_objects = detector.CustomObjects(car=True, motorcycle=True, person=True)

    src = r'C:\Users\Rafael\Desktop\FotosFrontais\Entregavel_13'
    dst = r'S:\Prefeituras\Taubate_2018\Videos_e_fotos\FotosFrontais\Entregavel_13'
    path = os.listdir(src)
    contador = 1
    path_len = len(path) + 1
    print(dst)

    for eachImage in path:
        img = os.path.join(src, eachImage)
        model(dst, img, custom_objects, detector, eachImage)
        print(f'Imagem: {contador} de {path_len} processada')
        contador += 1

def model(dst, img, custom_objects, detector, eachImage):

    if (eachImage.endswith(".jpg") or  eachImage.endswith(".png")):
        detected_image_array, detections = detector.detectCustomObjectsFromImage(custom_objects=custom_objects, input_image=img, output_type="array" , minimum_percentage_probability=60)

        if detections != []:
            txtPath = os.path.join(dst, "Entregavel13.txt")
            txtFile = open(txtPath, "a")
            txtFile.write(eachImage + "\n")
            txtFile.close()

def view():
    controller()

if __name__ == "__main__":
    view()