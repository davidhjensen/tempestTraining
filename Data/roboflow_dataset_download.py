from ultralytics import YOLO
from roboflow import Roboflow

API_KEY = "<API_KEY>"
WORKSPACE = "workspace"
PROJECT = "project"

# load cloud data (following three lines from snippet provided when exporting dataset online)
rf = Roboflow(api_key=API_KEY) # update API key as necessary
project = rf.workspace(WORKSPACE).project(PROJECT)
version = project.version(1)

dataset = version.download("yolov8").location + "\\data.yaml
print("Dataset dowloaded to the following directory:\n%s"%dataset)