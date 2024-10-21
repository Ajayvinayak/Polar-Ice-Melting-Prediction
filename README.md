# Polar Ice Melting Prediction

## Project Overview

This project focuses on predicting the **onset of polar ice melt and freeze patterns** using a **hybrid machine learning model**. By combining **SARIMA (Seasonal AutoRegressive Integrated Moving Average)**, **LSTM (Long Short-Term Memory)**, and **Random Forest** models, the project aims to deliver accurate forecasts of ice melting and freezing events for Arctic regions. 

By analyzing historical data from **1979 to 2022**, the project predicts these patterns for the next 30 years, providing actionable insights for **policymakers** and **climate scientists** to address rising sea levels and the impacts on Arctic ecosystems.

## Motivation and Impact

The melting of polar ice has profound implications for global sea levels, ecosystems, and human communities, especially those near coastlines. This project seeks to address key questions such as:
- **When will the polar ice start melting earlier in the year?**
- **How will freezing patterns shift over the coming decades?**
- **Which regions are most vulnerable to climate change-induced melting?**

The project is intended to support climate mitigation policies, environmental protection efforts, and adaptation strategies for communities and wildlife impacted by these environmental changes.

## Key Features

### Hybrid Model Approach
1. **SARIMA**: A powerful time-series forecasting model that captures seasonal trends, such as the yearly ice melt and freeze cycles. This model helps establish baseline patterns in the data.
2. **LSTM (Long Short-Term Memory Networks)**: A deep learning architecture designed to model long-term dependencies in sequential data. It captures complex, nonlinear relationships in the ice melt and freeze patterns, providing more accurate predictions over extended time frames.
3. **Random Forest**: A robust ensemble method used to handle complex and noisy data. Random Forest regression is used to enhance the prediction accuracy, especially when dealing with non-linearities and higher-order interactions between features.

### 95% Confidence Interval
All predictions are provided with a **95% confidence interval**, giving a range of uncertainty around the forecasts. This feature allows for more informed decision-making by providing a realistic range of outcomes instead of a single point estimate.

## Data

The dataset used for this project is derived from **NASA's Earth Science data**, covering the period **1979 to 2022**. It includes historical data on the **melting and freezing patterns** of the Arctic's polar ice, focusing on various Arctic regions, each of which is critical in the global climate system.
https://earth.gsfc.nasa.gov/cryo/data/arctic-sea-ice-melt 


### Key Regions

The following Arctic regions are included in the dataset:

- **Sea of Okhotsk**
- **Bering Sea**
- **Hudson Bay**
- **Baffin Bay**
- **Greenland Sea**
- **Barents Sea**
- **Kara Sea**
- **Laptev Sea**
- **East Siberian Sea**
- **Chukchi Sea**
- **Beaufort Sea**
- **Canadian Archipelago**
- **Central Arctic**

The dataset provides yearly values for:
- **Early Melt Onset**: The time when the first significant melt starts.
- **Melt Onset**: The period when melting becomes continuous.
- **Early Freeze Onset**: The first period when freezing begins.
- **Freeze Onset**: The time when freezing stabilizes across the region.

## Methodology

### 1. SARIMA (Seasonal AutoRegressive Integrated Moving Average)
- **Purpose**: Capture seasonal patterns in ice melt and freezing data.
- **Usage**: Used for time-series forecasting where historical data shows consistent seasonal trends.
- **Strengths**: Good for long-term trend identification and initial forecasting based on historical data.

### 2. LSTM (Long Short-Term Memory Networks)
- **Purpose**: Model complex dependencies in sequential ice melt and freeze data, especially useful for data with delayed effects or long-term memory.
- **Usage**: Applied to handle non-linear patterns and detect relationships in the time series that traditional statistical models may miss.
- **Strengths**: Excellent for learning long-term temporal dependencies.

### 3. Random Forest
- **Purpose**: Build an ensemble model to improve accuracy by averaging multiple decision trees.
- **Usage**: Used to handle the interaction between multiple variables in predicting melting and freezing patterns.
- **Strengths**: Works well with noisy data and provides better generalization when patterns are non-linear.

### Model Evaluation
- The hybrid model is evaluated using several metrics, including **RMSE (Root Mean Square Error)**, **MAE (Mean Absolute Error)**, and confidence intervals for robustness.
- The **RMSE of the SARIMA model** for initial predictions is approximately **11.93**.

## Predictions

The model forecasts the **next 30 years** of polar ice melt and freeze patterns for each region, providing specific predictions on:
- **Early Melt Onset**: The expected first melt occurrence for each year.
- **Melt Onset**: The start of continuous melting each year.
- **Early Freeze Onset**: When freezing is expected to begin each year.
- **Freeze Onset**: When freezing stabilizes for the region.

These predictions are essential for understanding the future of Arctic ice and preparing for the global impacts of ice loss, including:
- **Rising sea levels** that threaten coastal cities.
- **Disrupted ecosystems** that depend on seasonal ice cover for survival.
- **Economic effects** on industries like shipping, fishing, and tourism.

## Installation and Usage

### Requirements
To run the prediction models, you'll need the following Python libraries:
- `numpy`
- `pandas`
- `matplotlib`
- `scikit-learn`
- `tensorflow`
- `statsmodels`
- `geopandas`

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/your-repository/polar-ice-melt-prediction.git
    cd polar-ice-melt-prediction
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Download the dataset from the **NASA Earth Science** portal, and ensure the file paths are correctly set in the configuration.

### Running the Model
1. Preprocess the data and extract features:
    ```bash
    python preprocess_data.py
    ```

2. Train the hybrid model:
    ```bash
    python train_model.py
    ```

3. Generate predictions for the next 30 years:
    ```bash
    python predict.py
    ```

4. The results, including the predicted melt and freeze onset dates for all regions, will be saved in the output folder.

## Results and Analysis

The results of the predictions include:
- **Early Melt Onset Predictions**: A forecast of when melting will begin for each region.
- **Melt Onset Predictions**: Predictions for when continuous melting will occur.
- **Early Freeze Onset Predictions**: When the freezing period is expected to begin.
- **Freeze Onset Predictions**: The point at which freezing stabilizes across each region.

### Visualizations
You can visualize the results using the following command:
```bash
python plot_results.py



