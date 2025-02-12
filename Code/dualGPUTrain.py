from ultralytics import YOLO
from roboflow import Roboflow

# Uncomment as necessary:

#----LOCAL MODEL / DATA----#
'''
# make sure to add absolute paths here
# load local model
MODEL_PATH = '' # absolute path to .pt model
model = YOLO(MODEL_PATH)
# load local data
dataset = '' # absolute path to data.yaml
'''

#----CLOUD MODEL ----#
'''
# load cloud model
model = YOLO('yolov8m.pt')
# load cloud data (following three lines from snippet provided when exporting dataset online)
rf = Roboflow(api_key="NCHwa6UFXqHLKog4K44T") #update API key as necessary
project = rf.workspace("robocats-mcupa").project("robosub-2024")
version = project.version(1)

dataset = version.download("yolov8").location + "\\data.yaml"
'''

if __name__ == "__main__":
    results = model.train(data=dataset,
                          epochs=100,
                          imgsz=640,
                          patience=10,
                          cache=False,
                          seed=17,
                          device=[0,1] #train on two GPUs
                          )
