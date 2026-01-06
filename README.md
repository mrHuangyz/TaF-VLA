<div align="center">

# TaF-VLA: Tactile-Force Alignment in Vision-Language-Action Models <br> for Force-aware Manipulation

<br>

<img src="teaser.png" width="800">

</div>

---

## 🌟 Highlights

**TaF-VLA** enables robots to "feel" what they touch by aligning tactile and force data within a Vision-Language-Action framework.

- **🤖 Tactile-Force Data Acquisition Device**  
  We develop a low-cost, automated device and pipeline for collecting aligned tactile-force data at scale.

- **🧠 Tactile-Force Alignment (TaF-Adapter)**  
  We introduce the **TaF-Adapter**, a module that maps sequential tactile observations into a force-aligned latent space via contrastive learning. By constructing a vector-quantized shared latent space, our approach aligns temporal visuotactile data with 6-axis force/torque signals. This results in representations robust to force noise and cross-sensor variation while capturing rich, history-dependent contact dynamics.

- **🦾 TaF-VLA Policy**  
  We propose **TaF-VLA**, a framework capable of incorporating tactile information into VLA models. Experiments show that explicit force alignment enables force-aware manipulation behaviors difficult for vision-only or naive tactile-vision baselines.

---

## 🛠️ Hardware Design

### Mechanical Structure & Assembly

<div align="center">

| Mechanical Structure | Assembly Process |
| :---: | :---: |
| <img src="video/hardware.png" width="380"> | <img src="video/assembly.png" width="380"> |

**Description:**  
We design a compact, low-cost device (**TaF-Device**) enabling rapid acquisition of large-scale tactile-force aligned data pairs.

<br>

### Hardware Demonstration

<img src="video/TaF-device.gif" width="800">

**Description:**  
The TaF-Device in operation during data collection, showcasing synchronized tactile and force signal acquisition.

</div>

---

## 📂 Force-aware Manipulation Dataset

<div align="center">
  <img src="video/dataset.gif" width="800">
</div>

We introduce a comprehensive **force-aware manipulation dataset** covering diverse objects and interaction scenarios, featuring synchronized vision, tactile, and force observations.

---

## 📊 Experiment Results

### 1. Robust Manipulation (TaF-VLA Highlight)

<div align="center">

| Jelly Slicing (Deformable) | Weight Lifting (Rigid) |
| :---: | :---: |
| <img src="video/jelly.gif" width="380"> | <img src="video/weight.gif" width="380"> |

</div>

**Result:** TaF-VLA demonstrates robust manipulation performance across objects with significantly different physical properties.

<br>

### 2. Comparison with Baselines

<div align="center">

#### Tweezer Weight Pick
<img src="video/weight_compares.gif" width="800">
<em>Comparison of different methods on weighted object grasping tasks.</em>

<br>

#### Jelly Slicing
<img src="video/jelly_compares.gif" width="800">
<em>TaF-VLA maintains stable contact and force control when manipulating soft objects.</em>

<br>

#### Tube Insertion
<img src="video/tube_compares.gif" width="800">
<em>Our method achieves higher success rates and smoother force profiles than baseline approaches.</em>

</div>

<br>

### 3. Plug-and-Play Capability

<div align="center">
  <img src="video/plug_and_play.gif" width="800">
</div>

**Insight:** The proposed **TaF-Adapter** supports plug-and-play integration with various policy backbones (e.g., Diffusion Policy, ACT) without architecture-specific tuning.

<br>

### 4. Alignment vs. Prediction

<div align="center">
  <img src="video/force_predict.gif" width="800">
</div>

**Insight:** Instead of explicitly predicting forces, TaF-Adapter aligns multimodal representations in a shared semantic latent space, leading to superior robustness and cross-sensor generalization.

<br>

### 5. Ablation Study

<div align="center">

| Component Analysis A | Component Analysis B |
| :---: | :---: |
| <img src="video/ablation1.gif" width="380"> | <img src="video/ablation2.gif" width="380"> |

</div>

**Conclusion:** Ablation results confirm that each component of the TaF-Adapter is critical for achieving robust force-aware manipulation.
