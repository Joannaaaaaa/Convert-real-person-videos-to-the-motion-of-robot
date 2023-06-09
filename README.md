# Synthesizing Dynamic Movements for Non-Experts
NYCU 2023 AI Final Project

## Introduction
Developing an AI model to convert human motion to skeleton and generate an image of another human performing the same motion.

## related work
keypint detection: [Mask R-CNN](https://arxiv.org/pdf/1703.06870.pdf)

image to image: [Image-to-Image Translation with Conditional Adversarial Networks](https://arxiv.org/abs/1611.07004)

## Dataset
COCO2017  
https://cocodataset.org/#download

# Keypoint Detection
install require package  

run train.py: 
```
python train.py
```
VideotoImage.py: get the dataset of Image2Image (B)
```
python VideotoImage.py
```

run predict_visualize.py: get the dataset of Image2Image (A)
(need to create file named: plot_img and plot_result) 
```
python predict_visualize.py
```

- plot_result
- data  
  - plot_img  
  - COCO2017  
    - train2017  
    - val2017  
    - annotations  

## result:  
<img src="https://github.com/Joannaaaaaa/Synthesizing-Dynamic-Movements-for-Non-Experts/assets/98182630/ecebcef6-460c-4908-bdd4-00eb17720ca0" width="500">
<img src="https://github.com/Joannaaaaaa/Synthesizing-Dynamic-Movements-for-Non-Experts/assets/98182630/96283f18-9a88-471d-8c97-34e64bb42f2d" width="500" heigh="300">

# Image to Image
install required package

run train.py:

```
python train.py --dataset facades --cuda
```

run different epoch:
```
python train.py --dataset facades --epoch_count {# of epoch} --cuda
```

run test.py:
```
python test.py --dataset facades --cuda
```

results are stored in "result" folder

## result
<img src="https://github.com/navis0721/image/blob/main/688_a.jpg" width="400"> <img src="https://github.com/navis0721/image/blob/main/688_b.jpg" width="400">
<img src="https://github.com/navis0721/image/blob/main/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202023-06-09%20191055.png" width="300">

