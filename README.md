# MRF-based-Video-Anomaly-Detection

This project introduces an advanced video anomaly detection system, combining frame extraction, and image segmentation with Markov Random Fields (MRFs), and autoencoders. The primary objective is to develop a robust framework capable of automatically identifying unusual activities or patterns in surveillance videos, enhancing security and safety by distinguishing abnormal behavior without relying on predefined rules.

## Overview

The proposed methodology combines sophisticated techniques to achieve accurate and reliable video anomaly detection:

1. **Frame Extraction**: The process begins by loading training and testing data, comprising videos obtained from a certain open-source website. Frames are extracted from the videos using OpenCV, a powerful computer vision library, and saved as individual image files (PNG format).

2. **Image Segmentation with MRFs**: Traditionally, image segmentation relies on Histogram of Oriented Gradients (HOG) or Local Binary Patterns (LBP). This project implements an enhanced approach using Markov Random Fields (MRFs) to model complex spatial dependencies. MRFs enable the detection of anomalies by capturing contextual relationships between frames in surveillance videos.

3. **Autoencoders Integration**: Autoencoders, neural network models, are utilized to learn efficient representations of input data. The segmented frames are divided into temporal sequences using the sliding window technique. The autoencoder reconstructs the video sequence, and the reconstruction error is computed to identify anomalies.

## Methodology

1. **Frame Extraction**: Videos are processed to extract frames at regular intervals, which are then saved as individual image files.
   - Fig 2: Extracted frame split into segments.

2. **Image Segmentation with MRFs**: 
   - MRFs model spatial-temporal dependencies between frames, capturing contextual relationships.
   - Fig 3: Frame segmented using Markov Random Fields.

3. **Autoencoders Integration**:
   - Autoencoders learn efficient representations of segmented frames and reconstruct the video sequence.
   - The reconstruction error identifies anomalies in the video.

## Results and Analysis

The fusion of MRFs and autoencoders surpasses traditional methods in video anomaly detection, offering a sophisticated approach to security and safety in surveillance applications. The system effectively learns compact representations of normal patterns and accurately identifies anomalies, ensuring robust anomaly detection.

## Conclusion

By integrating advanced techniques such as MRFs and autoencoders, this project advances the accuracy and reliability of video anomaly detection. The innovative blend of spatial-temporal modeling with deep learning offers a comprehensive solution for detecting abnormal behavior in surveillance videos, enhancing security and safety in various applications.

For detailed implementation and analysis, please refer to the provided documentation.
