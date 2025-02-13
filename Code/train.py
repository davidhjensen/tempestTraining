from ultralytics import YOLO
from roboflow import Roboflow

#----LOCAL MODEL / DATA----#
# make sure to add absolute paths here
# load local model
MODEL_PATH = '/home/r71b151/bmw/i-ETC-2025/Models/yolov8m.pt' # absolute path to .pt model
model = YOLO(MODEL_PATH)
# load local data
dataset = '/home/r71b151/bmw/i-ETC-2025/Data/i-ETC-2025:-Combined-Detection/data.yaml' # absolute path to data.yaml
# local path to save run to
save_to = '/home/r71b151/bmw/i-ETC-2025/Results/Combined'

if __name__ == "__main__":
    results = model.train(data=dataset,
                          epochs=100,
                          imgsz=640,
                          patience=10,
                          cache=False,
                          seed=17,
                          device=[0,1], #train on two GPUs
                          project=save_to,
                          )