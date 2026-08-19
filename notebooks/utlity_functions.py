import pandas as pd


def loadData(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:   
        print(f"Error: The file at {file_path} was not found.")
        return None