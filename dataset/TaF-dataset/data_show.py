import argparse
import pickle
import sys
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import cv2

def load_data(file_path):
    path = Path(file_path)
    if not path.exists():
        print(f"Error: File {file_path} not found.")
        sys.exit(1)
        
    try:
        with open(path, 'rb') as f:
            data = pickle.load(f)
        return data
    except Exception as e:
        print(f"Error loading pickle: {e}")
        sys.exit(1)

def visualize_tactile_data(data, file_name="Data"):
    
    pressure_matrix = data.get("pressure_matrix", np.zeros((12, 12)))
    tactile_img = data.get("tactile_image", None)
    force_torque = data.get("force_torque", [])

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    fig.suptitle(f"Tactile Data Viewer: {file_name}", fontsize=14)

    ax_heatmap = axes[0]
    im = ax_heatmap.imshow(pressure_matrix, cmap=cm.inferno, vmin=0, vmax=1023)
    ax_heatmap.set_title("Pressure Matrix (12x12)")
    fig.colorbar(im, ax=ax_heatmap, fraction=0.046, pad=0.04)

    ax_img = axes[1]
    if tactile_img is not None:
        if len(tactile_img.shape) == 3:
            tactile_img_rgb = cv2.cvtColor(tactile_img, cv2.COLOR_BGR2RGB)
        else:
            tactile_img_rgb = tactile_img
            
        ax_img.imshow(tactile_img_rgb)
        ax_img.set_title("Tactile Image")
        ax_img.axis('off')
    else:
        ax_img.text(0.5, 0.5, "No Image Data", ha='center')


    force_text = "Force/Torque: N/A"
    if len(force_torque) > 0:
        force_str = ", ".join([f"{x:.3f}" for x in force_torque])
        force_text = f"6D Force: [{force_str}]"
    
    fig.text(0.5, 0.05, force_text, ha='center', fontsize=12, 
             bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray'))

    print(force_text)
    
    plt.tight_layout(rect=[0, 0.08, 1, 0.95])
    plt.show()

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Visualize Tactile Data from PKL")
    parser.add_argument("file", nargs="?", default="000155.pkl", help="Path to the .pkl file")
    args = parser.parse_args()
    
    data_content = load_data(args.file)
    visualize_tactile_data(data_content, file_name=args.file)