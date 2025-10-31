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

<img width="846" height="547" alt="image" src="https://github.com/user-attachments/assets/d92f8eb9-c71b-426e-9d7f-566651b36c6e" />

<img width="663" height="618" alt="image" src="https://github.com/user-attachments/assets/218c27e0-7b3e-4cdf-a3f4-d770288563a4" />

<img width="1136" height="359" alt="image" src="https://github.com/user-attachments/assets/8f2c5098-687c-4784-8c75-22345605347f" />

<img width="1128" height="522" alt="image" src="https://github.com/user-attachments/assets/77fbfbc9-b662-4786-931f-ebd55f6d69df" />

Input Image

<img width="328" height="350" alt="image" src="https://github.com/user-attachments/assets/108a39e0-f88c-42b6-a5c1-5e9ea76b7631" />

Example Propagation

<img width="1151" height="1190" alt="image" src="https://github.com/user-attachments/assets/c93399ad-9b6e-415b-afcb-7dd0e02039ff" />



---

## Results

- All simplified CNNs achieved **>99% validation accuracy**, demonstrating that **deep architectures like ResNet50 are unnecessary** for this dataset.  
- The **Global-Average-Pooling CNN** provided the best balance of accuracy, efficiency, and generalization.  
- Activation visualizations confirmed that even small CNNs learn edge, texture, and structure detectors comparable to those in much deeper networks.

---

## Files

- `medical_mnist_comparison_cnn.ipynb` — Main experiment notebook.  
- Output visualizations:
  - Validation accuracy curves  
  - Confusion matrices  
  - Activation and feature propagation plots  

---

## Conclusion

For small, structured medical imaging datasets, **deep architectures provide diminishing returns**.  
Compact CNNs can achieve equivalent accuracy with dramatically fewer parameters, faster training, and improved interpretability.  
By visualizing activation layers and feature propagation, this study confirms that **network simplicity does not preclude rich feature learning**—it enhances transparency and efficiency.
