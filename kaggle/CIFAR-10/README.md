# CIFAR-10 ResNet-50 Replay Buffer Fine-Tuning (Kaggle Dataset, Virginia Tech ARC HPC)

**Purpose**  
This notebook trains and fine-tunes a ResNet-50 model on the CIFAR-10 dataset using a replay-buffer strategy and exponential learning-rate decay.  
The final model is evaluated on 5 000 randomly selected test samples, visualizing 50 representative predictions and a normalized confusion matrix.

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
- Dataset: [Kaggle CIFAR-10 (Python version)](https://www.kaggle.com/datasets/pankrzysiu/cifar10-python)  
- Architecture: ResNet-50 pretrained on ImageNet  
- Replay Buffer: 3 000-sample cyclic memory for balanced fine-tuning  
- Learning Rate: Exponential-decay schedule during fine-tuning  
- Output Format: `.keras` (TensorFlow 2.x SavedModel format)  
- Evaluation:  
  - 5 000 random test samples  
  - 50 prediction visualizations (true vs. predicted)  
  - Normalized confusion matrix  

**Dataset Path**  
`/home/rameyjm7/.cache/kagglehub/datasets/pankrzysiu/cifar10-python/versions/1/cifar-10-batches-py`
