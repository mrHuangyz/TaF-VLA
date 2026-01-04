# TaF-VLA: Tactile-Force Alignment in Vision-Language-Action Models for Force-aware Manipulation

<img src="teaser.png" width="800">

---

## Highlight

- **Tactile-Force Data Acquisition Device**  
  We develop a low-cost, automated device and pipeline for collecting aligned tactile-force data at scale.

- **Tactile-Force Alignment**  
  We introduce the TaF-Adapter, a module that maps sequential tactile observations into a force-aligned latent space using a contrastive learning framework. By constructing a vector-quantized shared latent space that aligns temporal visuotactile data with 6-axis force/torque signals and matrix pressure maps, our approach learns representations that are robust to force noise and cross-sensor variation, while capturing rich, history-dependent contact dynamics.

- **TaF-VLA Policy**  
  We propose TaF-VLA, a VLA framework capable of incorporating tactile information. Experiments show that explicit force alignment enables force-aware manipulation behaviors that are difficult for vision-only or naive tactile-vision baselines.

---

## Hardware Design

### Mechanical Structure and Assembly

<table>
  <tr>
    <td>
      <img src="video/hardware.png" width="380">
    </td>
    <td>
      <img src="video/assembly.png" width="380">
    </td>
  </tr>
</table>

**Description**  
We design a compact and low-cost device (TaF-Device) that enables rapid acquisition of large-scale tactile-force aligned data pairs.

---

### Hardware Demonstration

<img src="video/TaF-device.gif" width="800">

**Description**  
The video shows the TaF-Device operating during data collection, illustrating synchronized tactile and force signal acquisition.

---

## Force-aware Manipulation Dataset

<img src="video/dataset.gif" width="800">

**Description**  
We introduce a force-aware manipulation dataset covering diverse objects and interaction scenarios, with synchronized vision, tactile, and force observations.

---

## Experiment Results

### 1. TaF-VLA Highlight

<table>
  <tr>
    <td>
      <img src="video/jelly.gif" width="380">
    </td>
    <td>
      <img src="video/weight.gif" width="380">
    </td>
  </tr>
</table>

**Description**  
TaF-VLA demonstrates robust manipulation performance across objects with significantly different physical properties, including deformable and rigid objects.

---

### 2. Comparison with Baselines

<img src="video/weight_compares.gif" width="800">

**Tweezer Weight Pick**  
Comparison of different methods on weighted object grasping tasks.

<br>

<img src="video/jelly_compares.gif" width="800">

**Jelly Slicing**  
TaF-VLA maintains stable contact and force control when manipulating soft objects.

<br>

<img src="video/tube_compares.gif" width="800">

**Tube Insertion**  
Our method achieves higher success rates and smoother force profiles than baseline approaches.

---

### 3. Plug-and-Play Capability

<img src="video/plug_and_play.gif" width="800">

**Description**  
The proposed TaF-Adapter supports plug-and-play integration with different policy backbones, including Diffusion Policy and ACT, without architecture-specific tuning.

---

### 4. Comparison with Force Prediction

<img src="video/force_predict.gif" width="800">

**Description**  
Instead of explicitly predicting forces, TaF-Adapter aligns multimodal representations in a shared semantic latent space, leading to superior robustness and cross-sensor generalization.

---

### 5. Ablation Study

<table>
  <tr>
    <td>
      <img src="video/ablation1.gif" width="380">
    </td>
    <td>
      <img src="video/ablation2.gif" width="380">
    </td>
  </tr>
</table>

**Description**  
Ablation results confirm that each component of the TaF-Adapter is critical for achieving robust force-aware manipulation performance.
