# Digital Image Processing Projects

This repository contains several projects related to Digital Image Processing, each focusing on different techniques and algorithms. Below is a summary of each project.

## 1. Connected Component Analysis and Skeletonization
- **Description**: This project implements algorithms for connected component analysis and skeletonization of images.
- **Key Features**:
  - Load an image and count 8-connected objects.
  - Convert the image to binary and recount connected components.
  - Skeletonize the objects and count skeletonized pixels.
  - Count objects using 4-connectivity.
- **Code Snippet**:
  ```python
  num_labels_8, labels_8, stats_8, centroids_8 = cv2.connectedComponentsWithStats(binary_image, connectivity=8)
  ```

## 2. Connected Component Labeling and Object Segmentation
- **Description**: This project focuses on labeling connected components in an image without using built-in functions.
- **Key Features**:
  - Implement a connected component labeling algorithm.
  - Display equivalency tables and total number of objects found.
- **Code Snippet**:
  ```python
  labels[i, j] = current_label
  ```

## 3. Image Processing Resampling
- **Description**: This project explores various image resampling techniques, including downsampling and interpolation.
- **Key Features**:
  - Create a grayscale image with alternating black and white columns.
  - Implement custom downsampling algorithms.
  - Compare bilinear interpolation with custom implementations.
- **Code Snippet**:
  ```python
  downsampled_img = cv2.resize(img, (200, 200))
  ```

## 4. Noise Addition and Filtering Techniques
- **Description**: This project adds different types of noise to images and applies various filtering techniques.
- **Key Features**:
  - Add salt and pepper noise, uniform noise, and Gaussian noise.
  - Filter noisy images using different kernel sizes.
  - Apply order statistic filters and geometric mean filtering.
- **Code Snippet**:
  ```python
  noisy_image = add_salt_and_pepper_noise(image, noise_percentage=0.05)
  ```

## 5. Optimized Neighborhood Averaging
- **Description**: This project implements optimized neighborhood averaging techniques to improve computation time.
- **Key Features**:
  - Create an 11x11 image with sequential pixel values.
  - Implement traditional and optimized averaging methods.
  - Count operations for both methods.
- **Code Snippet**:
  ```python
  output_row, operations = traditional_averaging(image, mask_size=5)
  ```

This README provides an overview of the projects included in this repository. Each project demonstrates different aspects of digital image processing, showcasing various techniques and algorithms.
