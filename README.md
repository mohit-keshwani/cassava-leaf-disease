# Cassava Leaf Disease Prediction

## About
A flask based web application for cassava leaf disease prediction developed using Deep Learning algorithms and deployed on AWS cloud using Docker and Nginx server. 
CNN algorithms and Transfer Learning architectures like VGG-16, MobileNetV2, DenseNet169, ResNet etc were experimented to detect cassava leaf disease. Python 3.7 and TensorFlow 2.4.1 was used for this project.
All the other requirements can be found at [requirements.txt](https://github.com/mohit-keshwani/cassava-leaf-disease/blob/main/Docker/flaskapp-docker/requirements.txt).

<br>
<b>You can find the webapp live at:</b> https://ec2-3-22-97-212.us-east-2.compute.amazonaws.com/ <br>

## Dataset and Kaggle Notebook Link
Dataset was obtained from kaggle.<br>
[Dataset](https://www.kaggle.com/c/cassava-leaf-disease-classification/overview)<br>
[Training Notebook](https://www.kaggle.com/mohitkeshwanii/cassava-ensemble-vgg16-mobilenetv2-densenet169/)<br>
[Inference Notebook](https://www.kaggle.com/mohitkeshwanii/inference-ensemble-vgg16-densenet169/)<br>

## Models With Their Accuracy of Prediction
CNN Model | Accuracy | Loss
--- | --- | ---
VGG-16 | 84% | 0.44
MobileNetV2 | 77% | 0.63
DenseNet169 | 73% | 0.70

<br> <b> Baseline Ensemble Technique was used to attain high recall rate and high accuracy. <br>
Ensemble | Accuracy
--- | ---
VGG-16 + DenseNet169 | 86%

## Steps to run the dockorized web application on local host
**Step-1** Clone the entire [Repository]().<br>
**Step-2** Download the docker desktop from the official website of Dockers.<br>
**Step-3** Create your docker account at https://hub.docker.com/. <br>
**Step-4** Make sure that you have cloned the [Repository]() and open the command prompt in [Docker](https://github.com/mohit-keshwani/cassava-leaf-disease/tree/main/Docker) directory.<br>
**Step-5** Run these following commands in the command prompt:<br>
```python
 docker-compose up --build
```
That's it you can see your website running at localhost.
