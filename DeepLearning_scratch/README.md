
This repository contains a collection of Jupyter notebooks developed during a Deep Learning course and ongoing research. The notebooks cover a wide range of architectures, datasets, and experimental approaches, from foundational RNNs to advanced open set incremental learning.

## Contents under DeepLearning_scratch

- **RNN / LSTM Experiments**
  - `lstm_rnn_original.ipynb` – baseline RNN/LSTM implementation.
  - `LSTM_RNN_128_from_scratch.ipynb` (and versions 2, 3) – custom LSTM/RNN models built from scratch.
  - `RML2018a_LSTM_RNN.ipynb` – LSTM applied to the RML2018a dataset.

- **Generative Models**
  - `GAN_LSTM.ipynb`, `GAN_LSTM_2.ipynb` – hybrid GANs with recurrent components.
  - `gan_cifar10.ipynb` – GAN trained on the CIFAR-10 dataset.
  - `VAE_LSTM_RNN.ipynb` – variational autoencoder with recurrent layers.

- **Open Set Incremental Learning (OSIL)**
  - `open_set_incremental_learning_MNIST.ipynb`
  - `open_set_incremental_learning_RML2016a.ipynb`
  - `open_set_incremental_learning_cifar10.ipynb`
  - `open_set_incremental_learning_cifar100.ipynb`
  - `open_set_incremental_learning_oxford_pets.ipynb`
  - `open_set_incremental_learning_sports_videos.ipynb`
  - `open_set_incremental_learning_tiny_imagenet.ipynb`

  These notebooks explore strategies for **open set recognition and incremental learning**, where models start with a subset of classes and adapt over time as new classes are discovered.  
  - The `open_set_incremental_learning_cifar100.ipynb` notebook focuses on **CIFAR-100**, demonstrating how incremental updates handle the larger class space and evaluating performance across class additions.

- **Other Notebooks**
  - `RML2018a_ResNet_OSIL.ipynb` – ResNet-based OSIL experiments on RF modulation data.
  - `Final_Testing.ipynb` – final evaluations and experiments.
  - `recover_model.ipynb` – model checkpoint recovery and continuation.

## Requirements

- Python 3.x
- TensorFlow / PyTorch
- NumPy, Matplotlib, scikit-learn
- Jupyter Notebook



## Open Set Incremental Learning (OSIL) and Open World Learning

### Open Set Incremental Learning (OSIL)
Traditional supervised learning assumes a closed set of classes known during training. **OSIL** relaxes this assumption by allowing models to:
1. **Recognize unknowns** – detect when an input does not belong to any of the classes seen so far.
2. **Adapt incrementally** – integrate new classes into the model while retaining knowledge of old ones.

Our OSIL experiments span multiple domains:
- **Image datasets** (MNIST, CIFAR-10, CIFAR-100, Tiny-ImageNet, Oxford Pets, Sports Videos).
- **Wireless signal datasets** (RML2016a, RML2018a).  

The workflow includes:
- Training on a subset of classes.
- Identifying unseen inputs using entropy thresholds, distance metrics, or confidence-based rejection.
- Expanding the classifier to include new labels.
- Using a **replay buffer** or knowledge distillation to reduce catastrophic forgetting.

For example, in `open_set_incremental_learning_cifar100.ipynb`, the model starts with a small subset of CIFAR-100 classes and progressively integrates additional classes, testing scalability under a large class space.

---

### Open World Learning
While OSIL focuses on extending models in controlled increments, **Open World Learning** takes a step further. It envisions systems that operate in **dynamic, real-world environments**, where:
- Novel classes appear **continuously and unpredictably**.
- The model must **autonomously detect, label, and learn** from these classes.
- Adaptation must occur with minimal supervision, ideally in **real time**.

In our experiments, Open World Learning means building pipelines where:
- Unknown signals/images are flagged automatically.
- Novel categories are assigned new labels.
- The model retrains itself (with buffering and fine-tuning) without requiring a full restart.

The long-term goal is to create **lifelong learning systems** that remain robust and flexible in the face of change — whether classifying modulation types in wireless communications or adapting to unseen object categories in computer vision tasks.
