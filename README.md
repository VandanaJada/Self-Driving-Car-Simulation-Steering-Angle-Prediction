# Self-Driving Car Simulation: Steering Angle Prediction

This project demonstrates an end-to-end pipeline for building an autonomous driving model. Using the Udacity Self-Driving Car Simulator, we developed a Convolutional Neural Network (CNN) to predict steering angles from simulated driving data, enabling the car to drive autonomously.

---

## Project Overview

- **Objective**: Train a deep learning model to predict steering angles based on input images from the car's front-facing camera.
- **Simulator**: [Udacity Self-Driving Car Simulator](https://github.com/udacity/self-driving-car-sim)
- **Key Features**:
  - Data preprocessing and augmentation for robust training.
  - CNN-based architecture for real-time steering angle prediction.
  - Smooth and autonomous driving in simulation.

---

## Tools & Frameworks

- **Programming Language**: Python
- **Libraries**: TensorFlow/Keras, NumPy, Pandas, OpenCV, Matplotlib
- **Simulator**: Udacity Self-Driving Car Simulator

---

## Dataset

- The dataset was generated using the simulator in training mode.
- It consists of:
  - Front-facing camera images.
  - Steering angle values (as labels).

### Data Preprocessing
1. Cropped unnecessary parts of the images (sky and hood of the car).
2. Normalized pixel values.
3. Augmented data with techniques like:
   - Random brightness adjustment.
   - Horizontal flipping to simulate opposite turns.
   - Adding random shadows for varying lighting conditions.

---

## Model Architecture

The CNN architecture is inspired by NVIDIA's end-to-end self-driving car model:

- **Input Layer**: 66x200x3 RGB image.
- **Convolutional Layers**: Extract spatial features.
- **Fully Connected Layers**: Predict steering angle.
- **Activation**: ReLU for non-linearity.
- **Output**: Single scalar for steering angle.

---

## How to Run

### 1. Clone the Repository
git clone https://github.com/VandanaJada/Self-Driving-Car-Simulation-Steering-Angle-Prediction.git
cd Self-Driving-Car-Simulation
### 2. Install Dependencies
pip install -r requirements.txt
### 3. Prepare Data
Use the Udacity simulator to collect driving data or use the sample data provided in the data/ folder.
### 4. Train the Model
Run the training notebook or script:

python model/model.py
### 5. Test in Simulator
Load the trained model in the simulator and run it in autonomous mode.


