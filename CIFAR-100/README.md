# CIFAR-100 ResNet-50 Replay Buffer Fine-Tuning (Kaggle Dataset, Virginia Tech ARC HPC)

**Purpose**  
This notebook trains and fine-tunes a ResNet-50 model on the CIFAR-100 dataset using a replay-buffer strategy and exponential learning-rate decay.  
The trained model is evaluated on 5 000 random test samples, visualizing 50 representative predictions and a normalized confusion matrix.

**System Environment**  
- Compute Cluster: Virginia Tech ARC HPC (DGX-005 node)  
- GPU: NVIDIA A100 (80 GB HBM2e)  
- CUDA Toolkit: 12.9  
- cuDNN: 9.14  
- TensorFlow: 2.20.0  
- Python: 3.12.8  
- Installed Packages: See `requirements.txt` (generated via `pip freeze`)  
- Execution Context: Slurm-based GPU job within the `ml-env` conda environment  

**Model and Training Details**  
- Dataset: [Kaggle CIFAR-100 (Python version)](https://www.kaggle.com/datasets/alincijov/cifar-100)  
- Architecture: ResNet-50 pretrained on ImageNet  
- Replay Buffer: 5 000-sample cyclic memory for balanced fine-tuning across 100 classes  
- Learning Rate: Exponential-decay schedule during fine-tuning  
- Output Format: `.keras` (TensorFlow 2.x SavedModel format)  
- Evaluation:  
  - 5 000 random test samples  
  - 50 prediction visualizations (true vs. predicted)  
  - Normalized confusion matrix  

**Dataset Path**  
`/home/rameyjm7/.cache/kagglehub/datasets/alincijov/cifar-100/versions/1`
