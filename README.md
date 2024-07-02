# Vehicle Tire Condition Detection

This repository contains the code for detecting vehicle tire conditions using a deep learning model. The model classifies tire images into two categories: "perfect" and "defective" using transfer learning with MobileNet_v2.

## Project Overview

The primary objective of this project is to enhance vehicle safety by providing a reliable method for identifying tire defects. Tire-related crashes are a significant concern, and timely detection of defects can prevent accidents and ensure road safety.
[Click here to try this project in huggaingface space](https://arsalanzabeeb-vehicle-tires-health-checkup.hf.space)

## Key Features

- **Binary Classification**: Classifies tire images into "perfect" and "defective".
- **Transfer Learning**: Utilizes MobileNet_v2 for efficient and accurate predictions.
- **Real-Time Detection**: Provides quick and reliable classification results.
- **Web Interface**: Includes a Gradio web interface for easy image upload and prediction.

## Dataset

The dataset consists of images of vehicle tires categorized into "perfect" and "defective". The data is split into training, validation, and test sets. The dataset was obtained from [Roboflow](https://roboflow.com/).

## Model Architecture

The model is built using MobileNet_v2 as the base model, with additional custom layers for the binary classification task.

## Installation

To run this project, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/Arsalanzabeeb786/vehicle-tire-condition-detection.git
    cd vehicle-tire-condition-detection
    ```

