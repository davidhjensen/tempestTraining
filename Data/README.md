# Data Info
Templates for image classification and object detection are provided below, as well as a quick guide on downloading datasets from Roboflow.
## Roboflow Dataset Download
To download a dataset from Roboflow...
1. On Roboflow, create a new dataset version
2. Select `Download Dataset`, choose a format, and select `Show download code`
3. Copy the provided code snippet, which has necessary values to download the dataset
4. Open `roboflow_dataset_download.py` and update the `API_KEY`, `WORKSPACE`, `PROJECT`, and `VERSION` variables at the top of the file
5. Run the script, which should download the dataset into this directory

## Templates
### Image Classification
The following folder structure is used for a single-label image classification dataset:
 ```
template_classification_dataset
├───test
│   ├───class1
│   └───class2
├───train
│   ├───class1
│   └───class2
└───valid
    ├───class1
    └───class2
```
Inside of each of the folders are the images beloning to the corrisponding class.

### Object detection
The following folder  structure is used for an object detection dataset:
```
template_detection_dataset
    ├───test
    │   ├───images
    │   └───labels
    ├───train
    │   ├───images
    │   └───labels
    └───valid
        ├───images
        └───labels
```
Inside of pair of folders (`images`/`labels`) are image/annotation pairs with the same name but different extensions (`image0.jpg`/`image0.txt`). Inside of the top level folder (`template_detection_dataset`), there also must be a `data.yaml` file with the following contents, where `<class1>` and `<class2>` should be replaced with the classes corrisponding to your dataset:
```
train: ../train/images
val: ../valid/images
test: ../test/images

nc: <number of classes>
names: ['<class1>', '<class2>']
```