import pandas as pd # type: ignore

def load_data(file_path):
    return pd.read_csv(file_path)

def preprocess_data(df):
    # Convert temperatures from Kelvin to Celsius
    df['Air temperature [C]'] = df['Air temperature [K]'] - 273.15
    df['Process temperature [C]'] = df['Process temperature [K]'] - 273.15
    
    # Drop the original temperature columns in Kelvin
    df.drop(['Air temperature [K]', 'Process temperature [K]'], axis=1, inplace=True)
    
    # Encode categorical variables
    df['Type'] = df['Type'].astype('category').cat.codes
    df['Failure Type'] = df['Failure Type'].astype('category').cat.codes
    
    # Handle missing values if any (example: fill with mean)
    df.fillna(df.mean(), inplace=True)
    
    return df
