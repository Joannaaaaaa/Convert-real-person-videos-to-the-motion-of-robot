# Synthesizing Dynamic Movements for Non-Experts
NYCU 2023 AI Final Project

# Introduction
Developing an AI model to convert human motion to skeleton and generate an image of another human performing the same motion.

## related work
keypint detection: [Mask R-CNN](https://arxiv.org/pdf/1703.06870.pdf)

image to image: [Image-to-Image Translation with Conditional Adversarial Networks](https://arxiv.org/abs/1611.07004)

# Dataset
COCO2017  
https://cocodataset.org/#download

# Keypoint Detection
install require package  

run train.py: 
```
python train.py
```
VideotoImage.py
```
python VideotoImage.py
```

run predict_visualize.py (need to create file named: plot_img and plot_result)   
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


