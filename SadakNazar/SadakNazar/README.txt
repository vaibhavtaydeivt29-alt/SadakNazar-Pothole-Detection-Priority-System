# SadakNazar: AI-Based Pothole Detection & Priority System

**An AI-powered road inspection system that detects potholes, estimates their severity, and generates a priority list for road maintenance.**

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![AI](https://img.shields.io/badge/AI-Computer%20Vision-purple)
![Deep Learning](https://img.shields.io/badge/Deep%20Learning-CNN-orange)
![Status](https://img.shields.io/badge/Project-Research%20Prototype-yellow)

## 1. Project Overview

SadakNazar is a computer vision and deep learning research project designed to identify potholes from road images and prioritize them according to their estimated severity.

Traditional pothole detection systems primarily focus on identifying potholes. However, road maintenance teams also need to determine **which potholes should be repaired first**.

SadakNazar addresses this problem by combining image-based pothole detection, bounding-box generation, severity classification, and priority ranking.

The system is intended as a research prototype to support road inspection and maintenance planning. It does not replace professional road-condition assessment or civil engineering judgment.

## 2. Problem Statement and Research Contribution

### Problem

- Manual road inspection requires time and human effort.
- Potholes differ in size, shape, and apparent severity.
- Detecting potholes alone does not provide a maintenance priority list.
- Performance may decrease under difficult conditions such as darkness, wet roads, and shadows.

### Proposed Solution

SadakNazar extends pothole detection into a severity-aware prioritization workflow.

1. Input a road image.
2. Preprocess the image for model inference.
3. Predict a pothole probability map.
4. Apply a threshold to identify candidate pothole regions.
5. Extract connected components and convert them into bounding boxes.
6. Estimate severity using the project's defined scoring rules.
7. Rank detected potholes to produce a maintenance priority list.

### Key Contributions

- Pothole detection using deep learning.
- Comparison of two candidate models, Model A and Model B.
- Severity-based ranking rather than detection alone.
- Evaluation under normal, dark, and shadow conditions.
- Investigation of data augmentation to improve robustness.
- Transparent reporting of limitations and remaining performance gaps.

## 3. System Architecture

```text
Road Images
     |
     v
Image Preprocessing
     |
     v
Deep Learning Model
(Model A / Model B)
     |
     v
Pothole Probability Map
     |
     v
Thresholding and Connected Components
     |
     v
Bounding-Box Generation
     |
     v
Severity Estimation
     |
     v
Priority Ranking
     |
     v
Maintenance Priority List
```

The prediction pipeline uses a probability threshold to obtain candidate regions. Small regions can be filtered using a minimum-area parameter. The resulting bounding boxes are used for object-level evaluation and visualization.

## 4. Dataset and Data Analysis

The dataset contains road images with pothole annotations. The notebook generates severity predictions and a tabular summary for the detected regions.

### Observed Severity Distribution

The current notebook reports the following counts:

| Severity | Count | Percentage |
|---|---:|---:|
| High | 524 | 52.09% |
| Medium | 334 | 33.20% |
| Low | 148 | 14.71% |
| **Total** | **1,006** | **100%** |

These values represent the reported severity distribution in the notebook output. They should not automatically be interpreted as the number of unique images or as the final test-set distribution.

### Dataset Analysis

The project should report the following analyses:

- Total number of images.
- Training, validation, and test split sizes.
- Number of annotated potholes.
- Severity distribution.
- Bounding-box width, height, and area distribution.
- Image-size histogram.
- Representative normal, dark, wet-road, and shadow images.

### Sample Images and Visualizations

Add representative images from the repository after confirming their actual paths.

```text
assets/
├── sample_normal.jpg
├── sample_dark.jpg
├── sample_shadow.jpg
├── sample_wet_road.jpg
├── size_histogram.png
└── severity_distribution.png
```

If these assets are stored in another directory, update the paths accordingly.

Example Markdown for embedding a sample:

```markdown
![Pothole detection example](assets/sample_normal.jpg)
```

The sample figures should show the original image, predicted bounding boxes, confidence or probability visualization, and severity labels where available.

## 5. Models Used

The notebook compares two candidate models, identified as **Model A** and **Model B**.

Both models are evaluated through the same general prediction interface. The inference pipeline obtains a probability map, thresholds it, extracts connected regions, and produces bounding boxes.

The exact architecture, layer configuration, parameter count, and training settings for each model should be documented from the model-definition cells in the notebook.

### Why use deep learning?

Deep learning can learn visual patterns from road images, including irregular pothole boundaries, texture changes, and surrounding road surfaces. It can be more flexible than a hand-crafted rule-based detector when sufficient representative training data is available.

### Why not use another model?

| Alternative | Reason for not selecting it as the primary model |
|---|---|
| Traditional image processing | Can be sensitive to lighting, road texture, and shadows. |
| Classical machine learning | Usually requires hand-crafted features and a separate feature-engineering pipeline. |
| Object detection models | Useful alternatives, but should be compared using the same dataset, compute budget, and evaluation protocol. |
| Transformer-based vision models | Worth exploring, but may require more data, compute, and tuning. |

These are design considerations, not proof that the selected models outperform all alternatives. Such conclusions require controlled experiments.

### Why compare Model A and Model B?

The comparison helps determine which candidate provides a better balance of detection quality, robustness under difficult lighting, inference speed, and computational requirements.

The preferred model should be selected using validation results, not by choosing whichever performs best on the test set.

## 6. Training, Validation, and Testing

The dataset should be divided into three independent subsets.

| Split | Purpose |
|---|---|
| Training | Learn model parameters from annotated images. |
| Validation | Tune hyperparameters, probability thresholds, and model selection. |
| Test | Measure final performance on previously unseen images. |

Record the actual split counts and percentages from the dataset preparation code before publishing the report.

### Experimental Protocol

1. Fix the dataset split and preprocessing pipeline.
2. Train Model A and Model B using the same experimental protocol wherever practical.
3. Tune detection thresholds using the validation set.
4. Evaluate the selected configurations on the test set.
5. Repeat training with three random seeds.
6. Report mean and standard deviation.
7. Keep the test set separate from threshold tuning and model selection.

For reproducibility, document the random seeds, image dimensions, optimizer, learning rate, batch size, epoch count, loss function, and augmentation settings from the actual training code.

## 7. Evaluation Metrics

The project uses object-level detection metrics.

- **Precision:** The proportion of predicted detections that match ground-truth boxes.
- **Recall:** The proportion of ground-truth boxes successfully detected.
- **F1-score:** The harmonic mean of precision and recall.

\[
F1 = \frac{2PR}{P+R}
\]

where \(P\) is precision and \(R\) is recall.

A predicted bounding box is matched to a ground-truth box using Intersection over Union (IoU). The current evaluation function uses an IoU matching threshold of 0.5 by default.

The matching implementation should be checked to ensure that each ground-truth box is matched at most once and that predictions are matched consistently.

### Mask Limitation

The available annotations are bounding boxes, not precise pixel-level pothole masks. Any mask generated from a bounding box is only an approximation of the pothole's actual shape.

Therefore, the primary evaluation should be reported at the **bounding-box/object level**. Pixel-level mask IoU should not be reported as a validated segmentation metric unless genuine pixel-level ground-truth masks are available.

## 8. Model Comparison: Normal vs Dark vs Shadow

Performance can vary depending on lighting and road conditions. Evaluate both models on the same defined test subsets.

| Test condition | Model A Precision | Model A Recall | Model A F1 | Model B Precision | Model B Recall | Model B F1 |
|---|---:|---:|---:|---:|---:|---:|
| Normal lighting | TBD | TBD | TBD | TBD | TBD | TBD |
| Dark / low-light | TBD | TBD | TBD | TBD | TBD | TBD |
| Shadow | TBD | TBD | TBD | TBD | TBD | TBD |
| Wet road, if available | TBD | TBD | TBD | TBD | TBD | TBD |

**Reporting rule:** Replace TBD with measured test-set results. Do not estimate or invent metric values.

For a fair comparison, define condition labels consistently, use disjoint evaluation subsets where possible, and report the number of images and ground-truth objects in each subset.

### Bar Graph

Generate a grouped bar chart comparing Model A and Model B F1-scores across the defined conditions. Include a legend, condition labels, and the number of test samples per condition.

The graph must be generated from the measured results table rather than illustrative or fabricated values.

## 9. Data Augmentation and Robustness

Data augmentation can help expose the model to variations in brightness, contrast, orientation, and image appearance. Its benefit must be measured experimentally.

Compare the baseline model with the augmented-training model using the same test set.

| Condition | Baseline F1 | Augmented F1 | Absolute change |
|---|---:|---:|---:|
| Normal lighting | TBD | TBD | TBD |
| Dark / low-light | TBD | TBD | TBD |
| Shadow | TBD | TBD | TBD |
| Wet road, if available | TBD | TBD | TBD |

Calculate the absolute change as:

\[
\Delta F1 = F1_{\text{augmented}} - F1_{\text{baseline}}
\]

If reporting a percentage improvement, specify whether it means a relative percentage change or a percentage-point change.

### Remaining Performance Gap

Even when augmentation improves low-light or shadow performance, the remaining gap must be reported honestly. If dark-road or shadow F1 remains lower than normal-light F1, this indicates that robustness has not been fully solved.

Potential next steps include collecting more challenging road images, checking annotation quality, using balanced sampling, and evaluating additional lighting-specific augmentation techniques.

Augmentation should be applied only to training data. Validation and test images should not be augmented in a way that leaks information into training or changes the intended evaluation distribution.

## 10. Three-Seed Evaluation: Mean ± Standard Deviation

A single training run may be affected by random initialization, data shuffling, and other sources of variation.

Run each experiment with three fixed random seeds, for example:

```python
SEEDS = [42, 123, 2026]
```

Use these as experimental seed values only after setting the corresponding Python, NumPy, and deep learning framework seeds in the training code.

Report the results in the following format:

| Model / condition | F1, seed 1 | F1, seed 2 | F1, seed 3 | Mean ± Std |
|---|---:|---:|---:|---:|
| Model A — Normal | TBD | TBD | TBD | TBD |
| Model A — Dark | TBD | TBD | TBD | TBD |
| Model A — Shadow | TBD | TBD | TBD | TBD |
| Model B — Normal | TBD | TBD | TBD | TBD |
| Model B — Dark | TBD | TBD | TBD | TBD |
| Model B — Shadow | TBD | TBD | TBD | TBD |

Calculate the mean and standard deviation from the three measured runs. State whether the reported standard deviation is the sample or population standard deviation, and use the same convention throughout.

If the models have not yet been trained and evaluated with three seeds, describe this as planned work rather than completed experimentation.

## 11. Severity Scoring and Priority Ranking

The purpose of the severity module is to convert detections into a practical maintenance priority list.

A simple research scoring function can combine normalized pothole area and model confidence:

\[
S = 100\left(w_a A_n + w_c C\right)
\]

where:

- \(S\) is the research severity score.
- \(A_n\) is normalized detected pothole area.
- \(C\) is the model confidence or probability-derived score.
- \(w_a\) and \(w_c\) are non-negative weights satisfying \(w_a+w_c=1\).

The normalization range, weights, and thresholds must be defined and documented in the actual implementation. If the current code uses different rules, document those rules instead of claiming this formula is already implemented.

The priority list can sort detections from highest to lowest score, subject to the project's defined severity thresholds.

**Important limitation:** This is a project-defined heuristic, not an official road-safety, pavement-condition, or civil engineering standard. Model confidence is not a direct measure of structural damage or accident risk.

Before real-world use, the scoring formula and priority categories must be validated by a qualified civil engineer against actual road inspections and an appropriate maintenance assessment procedure.

## 12. Applications

Potential applications include:

- Road inspection and pothole mapping.
- Maintenance planning and repair prioritization.
- Municipal road-condition monitoring.
- Supporting road surveys using vehicle-mounted cameras.
- Generating preliminary road-maintenance reports.
- Research into robust computer vision under challenging environmental conditions.

These are potential applications. Operational deployment requires field validation, location tracking, data quality checks, and human review.

## 13. Skills Demonstrated

This project demonstrates practical work in:

- Python programming.
- NumPy and Pandas for data processing and analysis.
- Deep learning and computer vision.
- Image preprocessing and probability-map analysis.
- Bounding-box geometry and IoU evaluation.
- Precision, recall, and F1-score analysis.
- Data augmentation and robustness evaluation.
- Experimental design and reproducibility.
- Visualization using plots and sample predictions.
- Git, GitHub, and research documentation.

Update this list to match the tools and techniques actually used in the project.

## 14. Technologies

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| NumPy | Numerical operations |
| Pandas | Result tables and analysis |
| Pillow / image-processing libraries | Image loading and preprocessing, where used |
| SciPy | Connected-component labeling and region extraction, where used |
| Matplotlib | Visualization and graphs, where used |
| Deep learning framework | Model training and inference; specify the actual framework |
| Git and GitHub | Version control and project hosting |

The exact versions and framework names should be taken from `requirements.txt` and the model-training notebook.

## 15. Installation and Usage

Clone the repository:

```bash
git clone https://github.com/vaibhavtaydeivt29-alt/SadakNazar-Pothole-Detection-Priority-System.git
cd SadakNazar-Pothole-Detection-Priority-System
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Install the project dependencies:

```bash
pip install -r requirements.txt
```

Open the project notebook in Jupyter or VS Code and execute the cells in the required order.

Before running the notebook, verify that the dataset paths, trained model files, image dimensions, and split configuration are correct.

The exact commands for training, testing, and generating report figures should be added after confirming the project's actual scripts and notebook workflow.

## 16. Limitations

- Performance may decrease in dark, wet-road, and shadow conditions.
- Bounding boxes provide approximate object localization and do not represent precise pothole boundaries.
- Box-derived masks cannot establish pixel-level segmentation accuracy.
- Severity scores are heuristic estimates and require expert validation.
- Test results depend on dataset coverage, annotation quality, and split design.
- Performance on unseen cities, cameras, seasons, and road surfaces may differ.
- Three random seeds provide a preliminary measure of variability, not a guarantee of generalization.
- The system should not be used as the sole basis for road-safety decisions.

## 17. Future Work

- Improve low-light, wet-road, and shadow robustness.
- Expand the dataset across different roads, locations, and weather conditions.
- Validate severity categories with civil engineering experts.
- Compare additional detection and segmentation architectures.
- Measure inference latency and computational requirements.
- Add geolocation and road-segment-level reporting.
- Evaluate on an independent, real-world field dataset.
- Publish complete experiment configurations and reproducible results.

## 18. Research Reporting and Reproducibility

For a research-quality release, include:

1. Dataset source, licensing, and annotation methodology.
2. Train/validation/test split counts and image-level separation.
3. Model architectures and parameter counts.
4. Training hyperparameters and augmentation configuration.
5. Model A versus Model B test results.
6. Normal, dark, and shadow subgroup results.
7. Baseline versus augmentation comparison.
8. Three-seed mean and standard deviation.
9. Sample prediction images and the size histogram.
10. Known limitations, failure cases, and validation requirements.

Only report results that can be reproduced from the notebook, saved model checkpoints, and documented dataset splits.

## 19. Conclusion

SadakNazar explores how deep learning can support pothole detection and severity-aware maintenance prioritization. Its main research focus is the transition from identifying potholes to organizing detected road defects into an actionable priority list.

A reliable assessment requires fair model comparisons, independent test evaluation, controlled augmentation experiments, repeated runs, and transparent reporting of failure cases. Before deployment, the detection pipeline and severity heuristic must be validated against real-world road inspections.

---

**Project:** SadakNazar — Pothole Detection & Priority System  
**Author:** Vaibhav Tayde  
**Repository:** [GitHub Project Repository](https://github.com/vaibhavtaydeivt29-alt/SadakNazar-Pothole-Detection-Priority-System)

**Research disclaimer:** This project is a research prototype. Its outputs are estimates for decision support and are not a substitute for professional road inspection or civil engineering assessment.
