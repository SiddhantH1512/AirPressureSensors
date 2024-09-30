# APS Failure Prediction for Scania Trucks
## Project Overview
This project focuses on predicting component failures in the Air Pressure System (APS) of heavy Scania trucks. The APS generates pressurized air used in critical truck functions, including braking and gear shifting. The goal is to develop a model that can accurately predict failures related to the APS, minimizing the cost of maintenance while ensuring truck safety.

## Dataset
The dataset is sourced from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/APS+Failure+at+Scania+Trucks) and consists of a collection of anonymized operational data. It represents two classes:
- **Positive Class:** Trucks with failures related to a specific component of the APS.
- **Negative Class:** Trucks with failures unrelated to the APS.
The challenge lies in the imbalance of the dataset and the high cost associated with misclassification. Incorrectly predicting a failure leads to unnecessary checks (low cost), while missing a real failure can cause truck breakdowns (high cost).

### Dataset Breakdown:
Training Set: 60,000 samples (1,000 positive, 59,000 negative).
Test Set: 16,000 samples.
Features: 171 attributes per record, including numerical counters.
Feature Description:
Missing Values: Represented as na.

### Objective:
The core objective is to develop a machine learning model that:
1. **Accurately Predicts APS Failures:** Correctly classify trucks with APS-related failures (positive class) while minimizing misclassifications.
2. **Minimizes Operational Costs:** The model must optimize for cost efficiency based on the following cost structure:
   - **Cost_1:** The cost of an unnecessary inspection, set at 10 units.
   - **Cost_2:** The cost of missing a faulty truck, set at 500 units.
   - **Total Cost:** The overall goal is to minimize the total cost, where:

Total Cost = (𝐶𝑜𝑠𝑡1 × False Positives) + (𝐶𝑜𝑠𝑡2 × False Negatives)

## Methodology

The project follows a structured approach to develop and evaluate a cost-sensitive model:

1. **Data Preprocessing:**
   - Handling missing values (`na`).
   - Feature scaling and normalization.
   - Addressing class imbalance through resampling techniques (oversampling/undersampling).

2. **Exploratory Data Analysis (EDA):**
   - Understanding feature distributions and correlations.
   - Visualizing class imbalance and critical features.

3. **Modeling:**
   - Investigating multiple classification algorithms:
     - Random Forest
     - XGBoost
     - Support Vector Machines (SVM)
     - Gradient Boosting Machines
     - Logistic Regression
     - LightGBM
     - Decision Trees
   - Reducing dimensionality using PCA.
   - Fine-tuning hyperparameters using Hyperopt.

4. **Cost-Sensitive Learning:**
   - Adjusting decision thresholds to prioritize minimizing False Negatives, given their higher cost impact.

5. **Model Evaluation:**
   - Performance metrics such as:
     - Recall, F1-Score, ROC-AUC.
     - Custom cost metric based on Total Cost calculation.
   - Analyzing model performance based on both Recall and cost-efficiency.
