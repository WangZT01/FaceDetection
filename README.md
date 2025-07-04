# FaceDetection

A Python-based face detection and recognition system using PCA (Principal Component Analysis, "Eigenfaces") and OpenCV. The project provides tools for collecting face data, preprocessing images, training a face recognition model, and running recognition via command line or a simple GUI.

## Features

- **Face Data Collection**: Capture face images from webcam and organize them by user.
- **Preprocessing**: Detect and crop faces from images, convert to grayscale, and resize for model input.
- **Face Recognition**: Implements PCA (Eigenfaces) for face recognition on the ORL dataset or your own collected data.
- **GUI**: Simple Tkinter-based interface for face detection and recognition.
- **Batch Processing**: Tools for renaming and organizing datasets.

## Project Structure & File Functions

- `main.py`: Main entry point. Provides a GUI for face detection and recognition, and includes functions for database creation and PCA training.
- `faceDetection.py`: Functions for face data collection from webcam and face detection in images. Can be used to collect new face data and preprocess images.
- `ImageProcessing.py`: Image preprocessing utilities, including renaming, resizing, and face cropping for datasets.
- `PCA_algorithm.py`: Implements the PCA algorithm for face recognition and evaluates accuracy on the ORL dataset.
- `method.py`: Utility for batch renaming images in dataset folders to a standard format.
- `haarcascade_frontalface_alt2.xml`: Pre-trained Haar Cascade for face detection.
- `FaceData/ORL/`: Example dataset (ORL face database) organized by subject.
- `FaceData/photos/`: Directory for storing and processing user face photos.
- `testData/`: (Purpose inferred as test images, can be clarified as needed.)

## Requirements

- Python 3.x
- OpenCV (`opencv-python`)
- NumPy
- Pillow
- Matplotlib (for plotting accuracy in PCA_algorithm.py)

Install dependencies with:

- opencv-python
- numpy
- pillow
- matplotlib

## Introduction to PCA and Its Application in Face Recognition

Principal Component Analysis (PCA) is a statistical technique used for dimensionality reduction while preserving as much variance as possible in the data. In the context of face recognition, PCA is used to extract the most significant features (called "eigenfaces") from a set of face images. Each face image is represented as a high-dimensional vector, and PCA projects these vectors onto a lower-dimensional subspace defined by the principal components.

The process involves:
1. Collecting a set of face images and converting them into grayscale vectors.
2. Computing the mean face and subtracting it from each image vector.
3. Calculating the covariance matrix and its eigenvectors (eigenfaces).
4. Projecting both training and test images onto the eigenface subspace.
5. Recognizing a face by comparing its projection to those of known faces, typically using a distance metric (e.g., Euclidean distance).

By using PCA, the system can efficiently recognize faces even with variations in lighting, expression, or minor occlusions, as it focuses on the most informative features of the face images.

---

For questions or contributions, please open an issue or contact the maintainer. 