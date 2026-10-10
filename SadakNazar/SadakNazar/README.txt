# 🚧 SadakNazar – AI-Based Pothole Detection & Priority System

**SadakNazar** is a deep learning project that detects potholes in road images, estimates their severity, and ranks them by maintenance priority.

## 🎯 Problem & Solution

Traditional pothole detection identifies road damage but does not always explain which pothole should be repaired first.

SadakNazar aims to solve this by:
- Detecting potholes in road images.
- Estimating severity using a simple scoring method.
- Generating a priority list for road maintenance.
- Evaluating performance under normal, dark, and shadow conditions.

## ⚙️ How It Works

1. Input road images.
2. Preprocess images and run the trained model.
3. Generate pothole predictions and bounding boxes.
4. Estimate severity and rank detected potholes.
5. Evaluate results using Precision, Recall, and F1-score.

## 🤖 Models

The project compares **Model A and Model B** to identify which performs better on the same evaluation data.

Deep learning is used to learn pothole patterns from images. Other approaches, such as traditional image processing and object detection models, could also be evaluated in future experiments.

*The exact model architectures and final performance must be documented from the training notebook.*

## 📊 Dataset & Experiments

The current notebook reports this severity distribution:

| Severity | Count |
|---|---:|
| High | 524 |
| Medium | 334 |
| Low | 148 |
| **Total** | **1,006** |

The counts represent the reported severity distribution, not necessarily unique images.

The project evaluates:
- Training, validation, and test performance.
- Model A vs Model B.
- Normal vs dark vs shadow conditions.
- Baseline vs data augmentation.
- Three random seeds using **mean ± standard deviation**.

Actual split counts, F1-scores, augmentation improvements, and graphs should be added after running the experiments.

## 📏 Evaluation & Limitations

Precision, Recall, and F1-score measure detection performance. Predictions are matched with ground-truth bounding boxes using IoU.

- Box-derived masks are approximate; evaluation is performed at the bounding-box level, not pixel-level segmentation.
- F1-score may be lower in dark, wet-road, and shadow conditions.
- Augmentation may improve robustness, but any improvement and remaining performance gap must be measured.
- The severity score is a project-defined heuristic, not an official standard. A civil engineer should validate it before real-world use.

## 🛠️ Skills & Technologies

- Python, NumPy, Pandas
- Deep Learning and Computer Vision
- Image Processing and Data Augmentation
- Precision, Recall, F1-score and IoU
- Data Visualization and Model Evaluation
- Git and GitHub

## 🚀 Applications

- Road inspection and pothole mapping.
- Maintenance planning and prioritization.
- Preliminary road-condition reporting.
- Research into AI-based road monitoring.

## 🔮 Future Scope

- Improve detection in low light, rain, and shadows.
- Test more models and larger datasets.
- Validate severity scores with civil engineering experts.
- Add GPS-based pothole mapping and real-world testing.

## 👨‍💻 Author

**Vaibhav Tayde**

[GitHub Repository](https://github.com/vaibhavtaydeivt29-alt/SadakNazar-Pothole-Detection-Priority-System)

*Note: SadakNazar is a research prototype and does not replace professional road inspection.*
