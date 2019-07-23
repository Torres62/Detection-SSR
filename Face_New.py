from imageai.Detection import ObjectDetection
import os

def paths():
    execution_path = os.getcwd()
    dir = r'/home/torres/Documents/FOTOS'
    dir_len = len(os.listdir(dir))
    path = os.scandir(dir)
    image_index = 1

    for image in path:
        file_name = image.name
        detection(file_name, dir, execution_path)
        print(f'Imagem: {image_index} de {dir_len}')
        image_index += 1


def detection(image, dir, execution_path):

    image_path = os.path.join(dir, image)

    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
    detector.loadModel()
    custom = detector.CustomObjects(person=True, car=True, motorcycle=True)
    detections = detector.detectCustomObjectsFromImage(custom_objects=custom , input_image=image_path, output_image_path=os.path.join(execution_path , image), minimum_percentage_probability=40)

    if detections != []:
        file = open(r'/home/torres/Documents/teste.txt', "a")
        file.write(image + "\n")
        file.close()

    file_remove = os.path.join(execution_path, image)
    os.remove(file_remove)
