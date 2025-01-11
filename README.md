# Smart Wildlife Security: Fog-Powered Video Compression for Cloud Efficiency

## Video Demonstration

Watch the demonstration of this project below:

<iframe width="560" height="315" src="https://www.youtube.com/embed/HP0E5seDTeQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

## Project Description

This project, **Smart Wildlife Security: Fog-Powered Video Compression for Cloud Efficiency**, aims to address the issue of wildlife incursions in rural areas by integrating cutting-edge technologies such as **fog computing** and **intelligent video compression**. The key features of the system include:

- **24/7 Surveillance**: Continuous video recording with selective transmission of relevant segments to the cloud.
- **Fog Computing**: Processes data closer to the source, minimizing latency and enhancing responsiveness.
- **Intelligent Compression**: Applies algorithms for smart frame extraction, reducing bandwidth usage and conserving resources.
- **Detailed Reporting**: Generates real-time PDF reports for monitoring wildlife activities and improving security measures.
- **Sustainability**: Promotes resource efficiency, aligning with environmentally friendly practices.

By optimizing data management and leveraging advanced technologies, this system aims to enhance human-wildlife coexistence and ensure rural safety.

---

## System Architecture

![System Architecture](https://github.com/user-attachments/assets/8952c02d-913f-4a19-a2e7-b0ca3aa7bba8)

The above diagram provides a high-level view of how fog computing and intelligent video compression are integrated into the system. Key components include:

1. **Video Capture Module**: Captures and processes video frames using an intelligent frame extraction algorithm.
2. **Data Transmission Module**: Transmits only compressed, relevant video segments to the cloud to conserve resources.
3. **Reporting and Monitoring**: Generates detailed reports for real-time analysis and post-event reviews.

---

## System Design of Smart Wildlife Security

The system design employs an advanced algorithm for video capture, frame extraction, and video compression. The key steps involved are:

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
