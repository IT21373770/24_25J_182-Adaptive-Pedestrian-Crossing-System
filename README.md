# 24_25J_182 - Adaptive-Pedestrian-Crossing-System
The Smart Step: Adaptive Pedestrian Crossing System is an innovative solution designed to address the challenges of pedestrian safety and traffic management at intersections. By leveraging cutting-edge technologies like machine learning and IoT, this system dynamically adjusts traffic signals based on real-time data. It prioritizes the needs of vulnerable groups, such as the elderly and disabled, while also accommodating emergency vehicles and adapting to varying environmental conditions, including adverse weather.

## Why Smart Step is Needed
Traditional traffic management systems are static and incapable of adapting to real-time pedestrian and traffic flow. This rigidity poses significant challenges:

  * Vulnerable pedestrians face increased safety risks due to insufficient crossing times.
  * Emergency vehicles experience delays, compromising their ability to respond promptly.
  *  Adverse weather conditions exacerbate the risk of accidents at pedestrian crossings.

## System Architecture
![Untitled](https://github.com/user-attachments/assets/6ffc84cb-5257-40b9-8788-3014ff2cd60c)

Main system components:
  1) Pedestrian count and vehicle presence analysis module.
  2) Vulnerable pedestrian detection module.
  3) Emergency vehicle detection module.
  4) Weather-adaptive timing module.

## Navigating this repository
* vulnerable_pedestrian_detection
    * ![SmartCrossNet.ipynb](https://github.com/IT21373770/24_25J_182-Adaptive-Pedestrian-Crossing-System/blob/main/pedestrian-detection-model/models/SmartCrossNet.ipynb) - This colab notebook contains the complete pipeline for the pedestrian detection model.
    * Pedestrian_classes.yaml - YAML configuration file listing the pedestrian classes used in the model.
    * trainin_vs_validation_loss_graph.png - Graph showing training and validation loss over epochs, helping analyze convergence and detect                                                overfitting or underfitting
    * precision_recall_map_graph.png - Precision-recall curve with mAP score. Provides insights into model performance for detecting each                                                  pedestrian class and overall.
* pedestrian_and_vehicle_presence_analysis
* emergency_vehicle_detection
* weather_adaptive_timing

## Inspecting training results
### Vulnerable pedestrian detection module
The training process automatically saves results in `./runs/detect/train` directory. Which includes:
  * Model weights: `best.pt` and `last.pt`.
  * Metric plots: Including mAP50, mAP50-95, class loss, F1 score, and others.
  * Batch visualizations: Quick visualization of some training and validation batches.
  * Summary file: `results.csv` summarizing the training results.

For example, the vulnerable pedestrian detection model trained with a YOLOv8 configuration for 50 epochs produces detailed outputs, including:
  1) Training and validation Loss Graph
  2) Sample Batch Visualization
     
     ![training_vs_validation_loss_graph](https://github.com/user-attachments/assets/29d57a61-1884-4ac1-aa7b-0965ad9fa2d4)
     ![Screenshot 2024-12-03 212302](https://github.com/user-attachments/assets/e667aafc-99b8-4b6a-a9cb-c50373462ade)

### Pedestrian count module
Training Results: Results are saved in runs/detect/train2.
Evaluation Metrics:
  * Precision: 85.40%
  * Recall: 71.13%
  * mAP@50: 74.81%
  * mAP@50-95: 55.51%

Training Details:
  * Model: YOLO8
  * Number of Epochs: 100

Performance Summary:
  * The model achieved high precision, indicating a low false positive rate.
  * The mAP@50 and mAP@50-95 scores suggest good overall detection accuracy across different IoU     thresholds.

 ![Training Validation loss graph pedestrian count model](https://github.com/IT21373770/24_25J_182-Adaptive-Pedestrian-Crossing-System/blob/main/Pedestrian_Count_Model/results/Training%20Validation%20loss%20graph%20pedestrian%20count%20model.png)
 ![Sample output from model](https://github.com/IT21373770/24_25J_182-Adaptive-Pedestrian-Crossing-System/blob/main/Pedestrian_Count_Model/results/Output%20From%20Model%20After%20Trainig.png)

 ### Vehicle density module
 Training Results: Results are saved in runs/detect/train2.
 Evaluation Metrics:
   * Precision: 80.30%
   * Recall: 74.88%
   * mAP@50: 76.44%
   * mAP@50-95: 58.99%
 
 Training Details:
   * Model: YOLO8
   * Number of Epochs: 50
 
 Performance Summary:
   * The model achieved a precision of 80.30%, indicating a good ability to avoid false    
     positives.
   * Recall of 74.88% suggests that the model successfully detects most relevant objects.
   * The mAP@50 and mAP@50-95 scores demonstrate a strong overall detection performance across 
     different IoU thresholds.

 ![Sample output from model](https://github.com/IT21373770/24_25J_182-Adaptive-Pedestrian-Crossing-System/blob/main/Vehicle_Density_Model/results/sample_output_of_vehicle_dencity_model_2.png)
