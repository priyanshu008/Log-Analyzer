# Log-Analyzer

About This Project
This project is a machine learning-based system log classifier that predicts whether a given network traffic entry is Benign or an Infiltration attempt using system log data.

Description
The model reads and processes a dataset of system logs (systemlogs.csv) and uses features such as:
Destination Port
Protocol
Flow Duration
Total Backward Packets
ACK Flag Count
PSH Flag Count

These features are preprocessed and fed into two classification models:
Logistic Regression
Decision Tree Classifier

The dataset is split into training and testing sets, standardized using StandardScaler, and the models are evaluated for accuracy. A small prediction system is also included to allow interactive user input from the command line.

Key Components
Preprocessing: Handles missing values and label encoding.
Feature Selection: Focuses on relevant features for better performance.
Modeling: Trains and compares Logistic Regression and Decision Tree Classifier.
Interactive CLI: Allows user input to predict traffic class in real-time.

Sample Features for Prediction
[Dst Port, Protocol, Flow Duration, Tot Bwd Pkts, ACK Flag Cnt, PSH Flag Cnt]


Example:
[23, 6, 3, 1, 0, 1]

Output
The models predict whether the input corresponds to:
Benign
Infiltration

