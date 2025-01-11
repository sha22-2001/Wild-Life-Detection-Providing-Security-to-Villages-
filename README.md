# Smart Wildlife Security: Fog-Powered Video Compression for Cloud Efficiency

## Video Demonstration

Watch the demonstration of this project on YouTube:  
[![Video Demonstration](https://img.youtube.com/vi/HP0E5seDTeQ/0.jpg)](https://www.youtube.com/watch?v=HP0E5seDTeQ)

Click the image above or [here](https://www.youtube.com/watch?v=HP0E5seDTeQ) to watch the video.

---

## Project Description

This project, **Smart Wildlife Security: Fog-Powered Video Compression for Cloud Efficiency**, addresses the issue of wildlife incursions in rural areas by integrating cutting-edge technologies such as **fog computing** and **intelligent video compression**. 

### Key Features:
- **24/7 Surveillance**: Continuous video recording with selective transmission of relevant segments to the cloud.
- **Fog Computing**: Processes data closer to the source, minimizing latency and enhancing responsiveness.
- **Intelligent Compression**: Applies algorithms for smart frame extraction, reducing bandwidth usage and conserving resources.
- **Detailed Reporting**: Generates real-time PDF reports for monitoring wildlife activities and improving security measures.
- **Sustainability**: Promotes resource efficiency, aligning with environmentally friendly practices.

By optimizing data management and leveraging advanced technologies, this system enhances human-wildlife coexistence and ensures rural safety.

---

## System Architecture

![System Architecture](https://github.com/user-attachments/assets/7cb0a4c9-7fef-4766-9651-12b06c64cb53)

The above diagram provides a high-level view of how fog computing and intelligent video compression are integrated into the system. 

### Key Components:
1. **Video Capture Module**: Captures and processes video frames using an intelligent frame extraction algorithm.
2. **Data Transmission Module**: Transmits only compressed, relevant video segments to the cloud to conserve resources.
3. **Reporting and Monitoring**: Generates detailed reports for real-time analysis and post-event reviews.

---

## System Design of Smart Wildlife Security

The system design employs an advanced algorithm for video capture, frame extraction, and video compression. 

### Key Workflow Steps:
1. **Video Capture**: Captures video and converts it into frames.
2. **Object Detection**: Identifies objects in each frame and tracks detected objects.
3. **Video Generation**: Processes and merges frames to generate a consolidated, trimmed video.
4. **Encryption and Transmission**: Encrypts and securely transmits video data to the cloud for further processing.
5. **Decryption and Reporting**: Decrypts data on the server and generates comprehensive reports.

---

## Time Complexity Analysis

### Time Complexity Comparison: Object Detection vs. Sliding Window Technique

![Time Complexity Graph](https://github.com/user-attachments/assets/37fda879-ede2-417e-a2c4-5298db825eea)

- **YOLOv8**: Offers superior time efficiency by processing data holistically, making it the preferred model for real-time wildlife detection. Its streamlined architecture ensures rapid detection without compromising accuracy.
- **Sliding Window**: Processes each window separately, resulting in slower detection times compared to YOLOv8.

---

## Conclusion

This project integrates **fog computing**, **intelligent video compression**, and advanced algorithms to provide an efficient, sustainable solution for rural wildlife security. With features like optimized data management, real-time monitoring, and detailed reporting, the system ensures safety for rural communities while conserving resources and promoting harmonious coexistence with wildlife.

---

## Cloning the Repository

To clone and set up this project, follow the steps below:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/smart-wildlife-security.git
