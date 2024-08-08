from src.MachineFailurePrediction.scripts.preprocess import load_data, preprocess_data
from src.MachineFailurePrediction.scripts.train import train_model
from src.MachineFailurePrediction.utils.common import setup_logging

def main():
    setup_logging()
    data = load_data(r"C:\Users\midhu\OneDrive\Documents\My Tableau Repository\OneDrive\Desktop\Predictive-Maintenance-project\src\MachineFailurePrediction\data\predictive_maintenance.csv")
    processed_data = preprocess_data(data)
    model = train_model(processed_data)

if __name__ == "__main__":
    main()