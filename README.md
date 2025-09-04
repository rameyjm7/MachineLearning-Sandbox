# MachineLearning-Sandbox

This repository contains a collection of Jupyter notebooks developed during a Deep Learning course and ongoing research. The notebooks cover a wide range of architectures, datasets, and experimental approaches, from foundational RNNs to advanced open set incremental learning.

## Contents

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
