# Kaggle Deep Learning Experiments

This repository contains a collection of deep learning experiments built around popular Kaggle datasets.  
Each subdirectory represents an independent study exploring model architecture, transfer learning, and visualization techniques.  
The goal of this workspace is to benchmark model performance while demonstrating interpretable and reproducible workflows in TensorFlow/Keras.

---

## Structure Overview

| Folder | Description |
|---------|--------------|
| **CIFAR-10** | Experiments on 10-class natural image classification using convolutional and residual networks. Includes data augmentation, replay buffer testing, and knowledge distillation studies. |
| **CIFAR-100** | Multi-class variant (100 categories) expanding the CIFAR-10 setup. Used for hierarchical classification and fine-grained visual analysis. |
| **Medical-MNIST** | Model simplification study starting from a pre-trained ResNet50 and progressively pruning down to lightweight CNNs with comparable accuracy. Focus on efficiency and activation visualization. |

---

## Key Themes

- **Transfer Learning:** Evaluating pre-trained ImageNet backbones (ResNet, VGG) on smaller custom datasets.  
- **Model Simplification:** Systematic reduction of network depth and parameter count without significant accuracy loss.  
- **Replay & Distillation:** Experiments with incremental learning and soft-target transfer across models.  
- **Visualization:** Feature maps, activation propagation, and confusion matrices for model interpretability.  
- **Performance Benchmarking:** Consistent training scripts, metrics tracking, and validation curves across all datasets.

---

## Framework and Tools

- **TensorFlow / Keras** for model design, training, and visualization  
- **Matplotlib / Seaborn** for performance plots and activation heatmaps  
- **NumPy / Pandas / Scikit-learn** for preprocessing and evaluation  
- **KaggleHub** for automated dataset download and version tracking  

---

## Example Highlights

### Medical-MNIST  
Demonstrated that deep architectures like ResNet50 provide minimal benefit for 64×64 grayscale medical imagery.  
Compact CNNs achieved >99% validation accuracy while offering faster training and improved interpretability through feature visualization.

### CIFAR-10  
Compared traditional CNNs and pre-trained residual networks under identical augmentation and replay conditions.  
Explored knowledge distillation for model compression.

### CIFAR-100  
Extended the CIFAR-10 experiments to a fine-grained dataset, assessing scalability and class separation performance.

---

## Repository Goals

- Provide **clear, modular examples** for academic or applied ML research.  
- Encourage **interpretable model design** through visual diagnostics.  
- Maintain **reproducible experiments** with consistent dataset handling and model checkpoints.

---

## Author

**Jacob M. Ramey**  
Graduate Researcher — Virginia Tech  
Focus Areas: Computer Vision, Deep Learning, Embedded AI Systems  

---

## License

This project is released under the **MIT License** unless otherwise specified in sub-directories.

