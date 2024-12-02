# 24_25J_182 - Adaptive-Pedestrian-Crossing-System
The Smart Step: Adaptive Pedestrian Crossing System is an innovative solution designed to address the challenges of pedestrian safety and traffic management at intersections. By leveraging cutting-edge technologies like machine learning and IoT, this system dynamically adjusts traffic signals based on real-time data. It prioritizes the needs of vulnerable groups, such as the elderly and disabled, while also accommodating emergency vehicles and adapting to varying environmental conditions, including adverse weather.

## Why Smart Step is Needed
Traditional traffic management systems are static and incapable of adapting to real-time pedestrian and traffic flow. This rigidity poses significant challenges:

  1) Vulnerable pedestrians face increased safety risks due to insufficient crossing times.
  2) Emergency vehicles experience delays, compromising their ability to respond promptly.
  3) Adverse weather conditions exacerbate the risk of accidents at pedestrian crossings.

## System Architecture
![Untitled](https://github.com/user-attachments/assets/6ffc84cb-5257-40b9-8788-3014ff2cd60c)

Main system components:
  1) Pedestrian count and vehicle presence analysis module.
  2) Vulnerable pedestrian detection module.
  3) Emergency vehicle detection module.
  4) Weather-adaptive timing module.

## Navigating this repository
* vulnerable_pedestrian_detection
    * SmartCrossNet.ipynb - This colab notebook contains the complete pipeline for the pedestrian detection model.
    * Pedestrian_classes.yaml - YAML configuration file listing the pedestrian classes used in the model.
    * trainin_vs_validation_loss_graph.png - Graph showing training and validation loss over epochs, helping analyze convergence and detect       
                                             overfitting or underfitting
    * precision_recall_map_graph.png - Precision-recall curve with mAP score. Provides insights into model performance for detecting each                                                  pedestrian class and overall.
* pedestrian_and_vehicle_presence_analysis
* emergency_vehicle_detection
* weather_adaptive_timing


