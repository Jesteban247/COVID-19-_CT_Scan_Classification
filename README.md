# 🦠 COVID-19 CT Scan Classification 🧬

This repository provides the necessary tools to classify CT scans using a deep learning model designed to identify COVID-19 cases. The project is intended for researchers, developers, and anyone interested in AI applications in healthcare.

## 🗂️ Table of Contents

- [🔍 Project Overview](#-project-overview)
- [🚀 Getting Started](#-getting-started)
  - [⚙️ Prerequisites](#️-prerequisites)
  - [📦 Installation](#-installation)
  - [🏃‍♂️ Running the Model](#-running-the-model)
- [🌐 Web Application](#-web-application)
- [📊 MLflow and DagsHub Integration](#-mlflow-and-dagshub-integration)
- [🔮 Future Work](#-future-work)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)
- [🙏 Acknowledgments](#-acknowledgments)

## 🔍 Project Overview

The objective of this project is to develop a machine learning model capable of classifying CT scans into three categories: COVID-19, CAP, and non-COVID. TensorFlow and Keras are used for model development, with MLflow integrated for experiment tracking and performance analysis.

## 🚀 Getting Started

### ⚙️ Prerequisites

Before starting, ensure that Python 3.8 or higher is installed. Required Python packages are listed in the `requirements.txt` file.

### 📦 Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Jesteban247/COVID-19-_CT_Scan_Classification.git
   cd COVID-19-_CT_Scan_Classification
   ```

2. **Install the required packages**:

   ```bash
   pip install -r requirements.txt
   ```

### 🏃‍♂️ Running the Model

To train and evaluate the model, refer to the Jupyter notebooks (`.ipynb` files) provided in the repository. These notebooks include detailed instructions for data preprocessing, model training, and performance evaluation. Open and execute the notebooks in environments like Jupyter Lab or Google Colab.

### 🌐 Running the Web Application

1. **Install all dependencies** by following the instructions in the `requirements.txt` file.
2. **Run the application** using the command:

   ```bash
   python main.py
   ```

3. **Access the application** through a web browser to start making predictions.

## 🌐 Web Application

The web application offers an easy-to-use interface for uploading CT scans and obtaining predictions. It includes a scrollable gallery to display images and prediction results.

**[🎥 Video Demonstration Coming Soon]**

## 📊 MLflow and DagsHub Integration

This project integrates with MLflow and DagsHub to track and log experiment data. Metrics such as accuracy, loss, precision, recall, and F1-score are recorded for comprehensive performance analysis.

**[⚙️ Instructions for MLflow and DagsHub Setup Coming Soon]**

## 🔮 Future Work

- 📈 Expand the dataset to improve model generalization.
- 🛠️ Further fine-tune the model for enhanced accuracy.
- 🔄 Implement live data prediction capabilities.

## 🤝 Contributing

Contributions are welcome. Interested individuals can fork the repository and submit a pull request for review.

## 📜 License

This project is licensed under the MIT License. For more information, refer to the [LICENSE](LICENSE) file.

## 🙏 Acknowledgments

Acknowledgment is given to the contributors and the open-source community for their support and resources, which have been invaluable to the project's development.