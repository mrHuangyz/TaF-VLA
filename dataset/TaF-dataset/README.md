# TaF Dataset

**Note:** Due to storage limits, only a small subset of the dataset is uploaded here for review.

## File Format
Files are named chronologically. Each file contains a single frame of data stored as a dictionary:

* **`tactile_image`**: Vision-based tactile image.
* **`force_torque`**: 6D Force/Torque sensor data.
* **`pressure_matrix`**: 12x12 pressure distribution map.

## Usage
To visualize a data sample, use the provided script:

```bash
python data_show.py 000167.pkl