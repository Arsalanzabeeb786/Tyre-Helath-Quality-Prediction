# Vehicle Tires Health Condition Detector 

This repository contains the code for detecting vehicle tire conditions using a deep learning model. The model classifies tire images into two categories: "perfect" and "defective" using transfer learning with MobileNet_v2.

## Project Overview

The primary objective of this project is to learn and utilize weights and Biases's different logs and artifacts in keras and tensorflow . Also to enhance vehicle safety by providing a reliable method for identifying tire defects. Tire-related crashes are a significant concern, and timely detection of defects can prevent accidents and ensure road safety.
[Click here to try this project in huggingface space](https://arsalanzabeeb-vehicle-tires-health-checkup.hf.space)



## Key Features

- **Binary Classification**: Classifies tire images into "perfect" and "defective".
- **Transfer Learning**: Utilizes MobileNet_v2 for efficient and accurate predictions.
- **Real-Time Detection**: Provides quick and reliable classification results.
- **Web Interface**: Includes a Gradio web interface for easy image upload and prediction.

## Dataset

The dataset consists of images of vehicle tires categorized into "perfect" and "defective". The data is split into training, validation, and test sets. 
The dataset was obtained from [Roboflow](https://universe.roboflow.com/dhruti/tyre-quality-zoog0)

Provided by a Roboflow user
License: CC BY 4.0


## Model Architecture

The model is built using MobileNet_v2 as the base model, with additional custom layers for the binary classification task.

## Experiments Tracking with Weights and Biases

This project utilizes [Weights and Biases](https://wandb.ai/) to track experiments, log metrics, and visualize model performance.

### Setup Weights and Biases

1. Create an account on [Weights and Biases](https://wandb.ai/).
2. Install the `wandb` library:
    ```bash
    pip install wandb
    ```
3. Login to your Weights and Biases account:
    ```bash
    wandb login
    ```
4. Initialize Weights and Biases in your training script:
    ```python
    import wandb
    wandb.init(project="Project name", entity="your_wandb_entity")

    # Example of logging metrics
    wandb.log({"accuracy": accuracy, "loss": loss})
    ```

## Installation

To run this project, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/Arsalanzabeeb786/vehicle-tire-condition-detection.git
    
    ```
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```



[Report of weight and biases can be seen here](https://wandb.ai/teamarsalan/Vehicle-Tyres-Health-Condition-Classification/reports/Vehicle-Tire-Condition-Detection-using-MobileNet_v2--Vmlldzo4NTc1NTk2?accessToken=qwmq85lbg62a2a20qhato5s7awc945m3turtghco1edmaca6smr100s0oy4ezjpt)

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. 
