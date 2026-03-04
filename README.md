# Network Intrusion Detection using Machine Learning

## Project Overview

This project focuses on detecting malicious network traffic using machine learning.  
The goal is to train a model that can analyze network flow statistics and determine whether the traffic is **normal (benign)** or part of an **attack**.

Cyber attacks such as DoS, brute force attacks, and port scans are common in modern networks. Intrusion Detection Systems (IDS) help identify these threats early. In this project, I built a machine learning pipeline that learns patterns from network traffic data and predicts the type of traffic.

---

## Dataset

Dataset used in this project:  
https://www.kaggle.com/datasets/solarmainframe/ids-intrusion-csv

The dataset contains **network traffic flow data**, where each row represents a network connection with different statistical features.

Some examples of features in the dataset include:

- Flow Duration  
- Total Forward Packets  
- Total Backward Packets  
- Flow Bytes/s  
- Flow Packets/s  
- Destination Port  
- Protocol  

The target column is **Label**, which represents the type of traffic.

Examples of labels:

- BENIGN  
- DoS  
- DDoS  
- Bot  
- PortScan  
- Brute Force  

The goal of the model is to learn from these features and classify the traffic correctly.

---

## What I Did in This Project

This project follows a typical machine learning workflow.

### 1. Data Understanding

First, I explored the dataset to understand:

- Number of features  
- Feature types  
- Distribution of attack types  
- Missing or unusual values  

This helped in deciding how the data should be cleaned and prepared.

---

### 2. Data Cleaning

The dataset contained some issues that needed to be handled before training the model.

#### Handling Missing Values

Some features had missing values.  
These values were replaced using the **median of the column**.

Median was chosen because it is more stable than the mean when the data contains extreme values.

---

#### Handling Infinite Values

Certain features like **Flow Bytes/s** or **Flow Packets/s** sometimes contained infinite values due to division operations.

Since machine learning models cannot handle infinite values, these were replaced during preprocessing.

---

### 3. Feature Engineering

The dataset contains a **Timestamp column**, which is not directly useful in its raw format.

To make it more useful for the model, time-based information was extracted such as:

- Hour of the day

This can help the model detect patterns related to **when certain attacks occur**.

---

### 4. Train-Test Split

The dataset was split into:

- **80% training data**
- **20% testing data**

Stratified splitting was used based on the **Label column** so that both the training and testing datasets maintain a similar distribution of attack types.

This helps ensure a fair evaluation of the model.

---

### 5. One-Hot Encoding (Target Variable)

The **Label column contains categorical values** such as:

BENIGN  
DoS  
DDoS  
Bot  

Machine learning models require numerical input, so the target variable was converted using **One-Hot Encoding**.

Example:

Original label:

```
BENIGN
```

After encoding:

```
BENIGN = [1,0,0,0,0,...]
```

This method avoids introducing any false ranking between categories and allows the model to treat each class independently.

---

### 6. Model Training

After preprocessing the dataset, machine learning model DecisionTreeClassifier was trained using the processed data.  
The model learn patterns from the network traffic features and try to predict the correct traffic label.

---

### 7. Model Evaluation

The trained model was evaluated using the train not test dataset.

Common evaluation metrics include:

- Accuracy  
- Precision  
- Recall  
- F1 Score  

These metrics help measure how well the model can detect malicious network traffic.

---

## Technologies Used

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Matplotlib  
- Seaborn  
- Google Colab  

---

## Project Structure

```
network-intrusion-detection
│
├── notebooks
│   └── intrusion_detection.ipynb
│
├── Images
│   └── intrusion_detection.ipynb
│
├── README.md
└── requirements.txt
```

---

## Future Improvements

Some possible improvements for this project include:

- Trying more advanced machine learning models like RandomForest 
- Handling class imbalance more carefully  
- Hyperparameter tuning  
- Building a real-time intrusion detection system  

---

## Author

**Bhavan Parkash**

If you found this project interesting or have suggestions for improvements, feel free to connect or reach out.

I’m always open to discussions about **machine learning, data science, and software development.**
