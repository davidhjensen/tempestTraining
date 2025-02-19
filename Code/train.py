from ultralytics import YOLO
from roboflow import Roboflow

#----LOCAL MODEL / DATA----#
# make sure to add absolute paths here

# load local model
MODEL_PATH = '/home/a12b345/path/to/TempestTraining/Models/yolov8m.pt' # absolute path to .pt model
model = YOLO(MODEL_PATH)
# OR load cloud model:
# model = YOLO("yolov8m.pt")

# load local data
DATASET = '/home/a12b345/path/to/TempestTraining/Data/dataset/data.yaml' # absolute path to data.yaml
# local path to save run to
SAVE_TO = '/home/a12b345/path/to/TempestTraining/Results/TrainingRunName'

if __name__ == "__main__":
    results = model.train(data=DATASET,
                          epochs=100,
                          imgsz=640,
                          patience=10,
                          cache=False,
                          seed=17,
                          device=[0,1,2,3], #train on four GPUs
                          project=SAVE_TO,
                          )