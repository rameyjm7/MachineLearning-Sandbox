# CIFAR-10 ResNet-50 Replay Buffer Fine-Tuning (Kaggle Dataset, A100 HPC)

**Purpose:**  
This notebook trains and fine-tunes a ResNet-50 model on the CIFAR-10 dataset using a replay buffer strategy combined with an exponential learning rate decay schedule.  
The trained model is evaluated on 5,000 randomly selected test images, with visualizations of 50 representative predictions and a normalized confusion matrix summarizing class-level performance.

**Experimental Configuration:**
- **Compute Environment:** Virginia Tech ARC HPC (A100 GPU node)
- **GPU:** NVIDIA A100 (80 GB HBM2e)
- **Framework:** TensorFlow 2.15 + CUDA 12.x
- **Python Version:** 3.10
- **Runtime:** Slurm batch environment with GPU acceleration enabled

**Model and Training Details:**
- **Dataset:** [Kaggle CIFAR-10 (Python version)](https://www.kaggle.com/datasets/pankrzysiu/cifar10-python)  
- **Architecture:** ResNet-50 pretrained on ImageNet  
- **Replay Buffer:** 3,000-sample cyclic memory used during fine-tuning for balanced incremental learning  
- **Learning Rate:** Exponential decay schedule during fine-tuning  
- **Output Format:** `.keras` (TensorFlow 2.x SavedModel format)  
- **Evaluation:**  
  - 5,000 random test samples  
  - 50 prediction visualizations (true vs. predicted labels)  
  - Normalized confusion matrix  

**Dataset Path:**  
`/home/rameyjm7/.cache/kagglehub/datasets/pankrzysiu/cifar10-python/versions/1/cifar-10-batches-py`
