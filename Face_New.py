from imageai.Detection import ObjectDetection
import os

def paths():
        execution_path = os.getcwd()
        src = r'C:\Users\Jupiter\Desktop\TESTE'
        path = os.listdir(src)

        for image in path:
                detection(image, src, execution_path)


def detection(image, src, execution_path):
        image_path = os.path.join(src, image)

        detections = []
        detector = ObjectDetection()
        detector.setModelTypeAsRetinaNet()
        detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
        detector.loadModel()
        custom = detector.CustomObjects(person=True, car=True, motorcycle=True)
        detections = detector.detectCustomObjectsFromImage(custom_objects= custom, input_image=image_path, output_image_path=os.path.join(execution_path , image), minimum_percentage_probability=40)
        
        file_remove = os.path.join(execution_path, image)
        os.remove(file_remove)

        if detections != []:
                txtPath = os.path.join(execution_path, "teste.txt")
                txtFile = open(txtPath, "a")
                txtFile.write(image + "\n")
                txtFile.close()