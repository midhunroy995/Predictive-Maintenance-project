import unittest
from src.MachineFailurePrediction.scripts.preprocess import preprocess_data
import pandas as pd # type: ignore

class TestPipeline(unittest.TestCase):
    def test_preprocess_data(self):
        data = {
            'Air temperature [K]': [300, 310],
            'Process temperature [K]': [320, 330],
            'Rotational speed [rpm]': [1500, 1600],
            'Torque [Nm]': [50, 55],
            'Tool wear [min]': [10, 20],
            'Target': [0, 1],
            'Failure Type': ['None', 'Heat']
        }
        df = pd.DataFrame(data)
        processed_df = preprocess_data(df)
        self.assertTrue('Air temperature [C]' in processed_df.columns)
        self.assertTrue('Process temperature [C]' in processed_df.columns)

if __name__ == '__main__':
    unittest.main()
