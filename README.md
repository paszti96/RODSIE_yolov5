# [Robust Object Detection in Simulated Industrial Environment (2021)](https://github.com/paszti96/RODSIE_yolov5/blob/main/Robust%20Object%20Detection%20in%20SImulated%20Environment.pdf)

## Mission Statement 👨‍🎓
This research project was my Master's Thesis @ Budapest University of Technology and Economics. 👨🏻‍🎓
The project was awarded with scholarship by the [Artificial Intelligence National Laboratory (MILAB) of Hungary](https://mi.nemzetilabor.hu/) 

The main focus of deep learning research is the development of self-supervised learning methods, where the agent completes different detection tasks by understanding his environment, and not by relying on labeled training examples. A typical usage of self-supervised learning methods is to substitute obscured details from images or
to estimate the impact of actions taken by robots. The main goal of the following thesis is to create an algorithm that is able to recognize different objects and their
relevant visual properties in a simulated environment and to estimate the effect of different actions on them. In this thesis, I will not only present such a robust object
detection algorithm, but also create a simulated industrial environment capable of generating the data needed for training quickly and easily.

## Setting 👨🏻‍💻
The environment consists of two main part: 
### Tartarus 🌍
A simulated industrial environment that can be used to generate images and metadata for the deep learning algorithm. The simulation should also be modifiable and capable of generating randomized scenarios sufficient to create diverse train dataset. 
The simulated environment is made with [Unity Engine](https://unity.com/) and it can be found here: [Tartarus](https://github.com/paszti96/Tartarus).

![Tartarus](https://github.com/paszti96/RODSIE_yolov5/blob/main/images/conv_post.PNG "Environment")

### RODSIE algorithm 🤖📷
This repository contains the Object Detection Algorithm which contains combinations of a [YOLO v5](https://github.com/ultralytics/yolov5) object detector and a [U-Net](https://en.wikipedia.org/wiki/U-Net)-based segmentation layer.

The most efficient solution was to expand the neural network used by YOLO with an auxiliary segmentation output. As I discussed before, the single-shot object detector has a highly efficient feature detector layer with the application of CSPNet and PANet.

For the semantic segmentation, I added three successive blocks of the following
layers:
1. Upsample layer
2. Shortcut
3. 2x2 convolution with Batch Normalization and Leaky ReLU activation function
4. CSP Bottleneck layer that used to obtain a representation of the input with reduced dimensionality.

## Algorithm 💡
The algorithm has two different output:
1. Predicted bounding box coordinates and class labels from the YOLO-based object detector.
2. Predicted segmentation mask, which shows the covered regions of the objects. The final output of the cover detection process is a combined image of these two images, where the found objects with bounding boxes and class labels are shown with white cloud-like regions, where covered parts are predicted by the deep neural network.

For the object detection I use RGBD image from the environment and the ground thruth, and the segmentation is predicted based on a mask that contains the overlapping area of the bounding boxes.

![Input](https://github.com/paszti96/RODSIE_yolov5/blob/main/images/input.png "Input image")

#### The output of the prediction:

![Output](https://github.com/paszti96/RODSIE_yolov5/blob/main/images/output.png "Prediction otput")

### Performance 📈
The algorithm tested with different combinations and its performance is shown in the following images:

![MAP](https://github.com/paszti96/RODSIE_yolov5/blob/main/images/map.png)
![Segmentation loss](https://github.com/paszti96/RODSIE_yolov5/blob/main/images/segmentation%20loss.png)

### For more details, please check my [Thesis](https://github.com/paszti96/RODSIE_yolov5/blob/main/Robust%20Object%20Detection%20in%20SImulated%20Environment.pdf) ❤️ 🧡 
