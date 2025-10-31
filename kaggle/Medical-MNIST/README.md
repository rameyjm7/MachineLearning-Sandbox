# Medical MNIST Model Simplification and Visualization

This project explores how convolutional neural network (CNN) complexity impacts performance on the **Medical MNIST** dataset.  
The work began with a **ResNet50** backbone pre-trained on ImageNet, which achieved excellent accuracy but was computationally inefficient for small grayscale medical images.  
The objective was to **progressively simplify the model** while maintaining comparable performance, leading to several lightweight CNN designs.

---

## Overview

### Baseline: ResNet50
- Pre-trained on ImageNet and fine-tuned on Medical MNIST.  
- Achieved near-perfect validation accuracy (~99–100%).  
- Contained millions of parameters—unnecessary for 64×64 imagery.  

### Simplification Phase
- Replaced ResNet50 with a custom **Basic CNN**, achieving similar accuracy with orders of magnitude fewer parameters.  
- Further reductions explored filter count, layer depth, and pooling strategies to find the **minimum viable architecture**.

---

## Comparative Study

Three lightweight CNN variants were implemented and trained under identical conditions:

| Model | Description |
|-------|--------------|
| **TinyCNN** | Two convolutional layers followed by a 64-unit dense layer. |
| **Reduced-Filter CNN** | Fewer filters (8) and a smaller dense layer (32 units). |
| **Global-Average-Pooling CNN** | Replaced flattening with global average pooling for better generalization and fewer parameters. |

---

## Visualization and Analysis

- **Validation Accuracy & Loss:** Plotted across epochs to compare convergence speed and stability.  
- **Confusion Matrices:** Evaluated per-class prediction performance.  
- **Activation Layer Maps:** Visualized how deeper layers extract higher-level anatomical features, confirming consistent feature hierarchies across models.  
- **Feature Propagation Diagrams:** Illustrated how inputs transform through convolutional stages, highlighting spatial and semantic abstraction.

---

## Results

- All simplified CNNs achieved **>99% validation accuracy**, demonstrating that **deep architectures like ResNet50 are unnecessary** for this dataset.  
- The **Global-Average-Pooling CNN** provided the best balance of accuracy, efficiency, and generalization.  
- Activation visualizations confirmed that even small CNNs learn edge, texture, and structure detectors comparable to those in much deeper networks.

---

## Files

- `compare_cnn.ipynb` — Main experiment notebook.  
- `.keras` model files — Trained models for TinyCNN, Reduced-Filter CNN, and Global-Average-Pooling CNN.  
- Output visualizations:
  - Validation accuracy curves  
  - Confusion matrices  
  - Activation and feature propagation plots  

---

## Conclusion

For small, structured medical imaging datasets, **deep architectures provide diminishing returns**.  
Compact CNNs can achieve equivalent accuracy with dramatically fewer parameters, faster training, and improved interpretability.  
By visualizing activation layers and feature propagation, this study confirms that **network simplicity does not preclude rich feature learning**—it enhances transparency and efficiency.
