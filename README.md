# Predictive-Maintenance-project

## Overview
This project aims to develop a predictive maintenance model using machine learning techniques. The goal is to predict equipment failures before they occur, thereby reducing downtime and maintenance costs.

## Project Structure
Predictive-Maintenance-project/ ├── src/ │ └── MachineFailurePrediction/ │ ├── init.py │ ├── data/ │ │ └── init.py │ ├── notebooks/ │ │ └── init.py │ ├── scripts/ │ │ ├── init.py │ │ ├── preprocess.py │ │ └── train.py │ ├── models/ │ │ └── init.py │ ├── utils/ │ │ ├── init.py │ │ └── common.py │ ├── config/ │ │ ├── init.py │ │ └── configuration.py │ ├── pipeline/ │ │ └── init.py │ ├── entity/ │ │ └── init.py │ └── constants/ │ └── init.py ├── config/ │ └── config.yaml ├── params.yaml ├── app.py ├── main.py ├── Dockerfile ├── requirements.txt ├── setup.py ├── research/ │ └── trials.ipynb ├── tests/ │ └── test_pipeline.py └── logs/ └── logging.txt


## Installation
1. **Clone the repository**:
    ```sh
    git clone https://github.com/midhunroy995/Predictive-Maintenance-project.git
    cd Predictive-Maintenance-project
    ```

2. **Create and activate a virtual environment**:
    ```sh
    python -m venv venv
    # Activate the virtual environment
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
1. **Preprocess the data**:
    The `preprocess.py` script handles data loading and preprocessing.
    ```python
    from src.MachineFailurePrediction.scripts.preprocess import load_data, preprocess_data

    data = load_data('data/machine_failure_data.csv')
    processed_data = preprocess_data(data)
    ```

2. **Train the model**:
    The `train.py` script trains the XGBoost model.
    ```python
    from src.MachineFailurePrediction.scripts.train import train_model

    model = train_model(processed_data)
    ```

3. **Run the project**:
    You can run the entire project using the `main.py` script.
    ```sh
    python main.py
    ```

## Configuration
The project configuration is managed using YAML files:
- **config/config.yaml**: Contains model parameters and configurations.
- **params.yaml**: Contains data file paths and other parameters.

## Docker
To run the project in a Docker container:
1. **Build the Docker image**:
    ```sh
    docker build -t predictive-maintenance .
    ```

2. **Run the Docker container**:
    ```sh
    docker run -p 80:80 predictive-maintenance
    ```

## Testing
Unit tests are included in the `tests` directory. To run the tests:
```sh
pytest tests/

##Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

##License
This project is licensed under the MIT License. See the LICENSE file for details.

##Contact
For any questions or inquiries, please contact midhunroy7510@gmail.com.


This README file provides a clear and comprehensive overview of your project, including installation instructions, usage, configuration, Docker setup, testing, contributing guidelines, and contact information. Let me know if you need any further adjustments or additional sections!
