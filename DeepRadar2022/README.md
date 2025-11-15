# DeepRadar2022 – CNN + Bidirectional LSTM Classifier

**Author:** [Jacob Ramey](https://www.kaggle.com/jacobramey)  
**Repository:** [MachineLearning-Sandbox](https://github.com/rameyjm7/MachineLearning-Sandbox/tree/main/DeepRadar2022)

---

## Overview

This project implements a high-accuracy modulation classifier for the **DeepRadar2022** dataset using a **hybrid CNN + Bidirectional LSTM** architecture.  
The model operates directly on **I/Q radar signals** and includes **SNR as an explicit feature channel**, improving performance under varying noise conditions.

> Achieved **94.4 % accuracy** on SNR ≥ –6 dB data and **84.3 % accuracy overall** across all SNR levels.

---

## Dataset

**DeepRadar2022** contains **782 000 synthetic radar waveforms** across **23 modulation types** with SNRs ranging from **–12 dB → +20 dB**.  
Each sample is a `1024 × 2` matrix representing **I (in-phase)** and **Q (quadrature)** components.

| Split | Samples | Description |
|:------|:--------:|:------------|
| Train | 469 200 | 23 classes × 13 SNR values × 1200 signals |
| Val   | 156 400 | 23 classes × 13 SNR values × 400 signals |
| Test  | 156 400 | 23 classes × 13 SNR values × 400 signals |

Each `lbl_*.mat` file encodes six parameters per signal:  
`[ Class, SNR, Length, Carrier Freq, Bandwidth/Symbol Rate, Frequency Excursion ]`

---

## Model Architecture

The final model combines convolutional and recurrent layers for both local and long-range temporal feature extraction:

```
Input (1024 × 3) → Conv1D(64,5) → BN → MaxPool(2)
                 → Conv1D(128,3) → BN → MaxPool(2)
                 → BiLSTM(128, return_sequences)
                 → Dropout(0.3)
                 → BiLSTM(64)
                 → Dense(128, ReLU)
                 → Dropout(0.3)
                 → Dense(23, Softmax)
```

**Input channels:**  
- I component  
- Q component  
- Normalized SNR (as a third channel)

**Training details**
- Optimizer: Adam (lr = 5 × 10⁻⁴, clipnorm = 1.0)  
- Loss: Categorical Crossentropy  
- Batch Size: 128  
- Epochs: 35 with early stopping & LR reduction  
- Mixed precision enabled (`float16` inference)  

---

## Results

### Overall (All SNRs)
| Metric | Value |
|:-------|------:|
| Accuracy | **84.3 %** |
| Macro F1 | **0.843** |
| Weighted F1 | **0.843** |
| Samples | 156 400 |

![](https://github.com/user-attachments/assets/f722c96c-ab0e-46d4-bacf-fab95bf70912)

---

### High-SNR Only (≥ –6 dB)
| Metric | Value |
|:-------|------:|
| Accuracy | **94.4 %** |
| Macro F1 | **0.943** |
| Weighted F1 | **0.943** |
| Samples | 128 800 |

![](https://github.com/user-attachments/assets/d11b2b07-8aca-42b6-8043-dc909b192821)

---

### Confusion Matrix (All SNRs)
![](https://github.com/user-attachments/assets/3904c0f1-7557-416f-8bd8-76f4975de84b)

Each cell corresponds to classification counts for the 23 radar modulations:

| # | Modulation | # | Modulation |
|--:|:---------------------|--:|:--------------------|
| 1 | Linear FM (LFM)      | 13 | P2 Code |
| 2 | 2 FSK                | 14 | P3 Code |
| 3 | 4 FSK                | 15 | P4 Code |
| 4 | 8 FSK                | 16 | Px Code |
| 5 | Costas Code          | 17 | Zadoff-Chu |
| 6 | 2 PSK                | 18 | T1 Code |
| 7 | 4 PSK                | 19 | T2 Code |
| 8 | 8 PSK                | 20 | T3 Code |
| 9 | Barker Code          | 21 | T4 Code |
|10 | Huffman Code         | 22 | Non-Modulated (NM) |
|11 | Frank Code           | 23 | Complex Gaussian Noise |
|12 | P1 Code              |    | |

---

### Accuracy vs SNR

![](https://github.com/user-attachments/assets/d11b2b07-8aca-42b6-8043-dc909b192821)

Accuracy remains above 90 % for SNR ≥ –6 dB and gradually degrades at lower SNR values, confirming noise robustness from SNR-aware training.

---

## Key Findings

- Including **SNR as an explicit feature channel** improves stability under noise.  
- CNN layers capture instantaneous spectral/phase characteristics.  
- Bidirectional LSTMs model temporal structure and code sequences.  
- Training only on high-SNR samples generalizes well to full SNR range.

---

## Future Work

- Add **spectrogram branch** for joint time–frequency learning.  
- Augment with random phase/timing jitter for better low-SNR generalization.  
- Perform curriculum fine-tuning on < –6 dB subset for incremental robustness.

---

## Model Artifact

Final model saved in modern `.keras` format:

```
deepradar2022_cnn_bilstm_final.keras
```

It includes both architecture and optimizer state for continued fine-tuning.

---

## Citation

If using this implementation, please cite:

> Ramey, J. M. (2025). *DeepRadar2022 – CNN + Bidirectional LSTM Modulation Classifier*.  
> GitHub Repository: https://github.com/rameyjm7/MachineLearning-Sandbox/tree/main/DeepRadar2022

---
