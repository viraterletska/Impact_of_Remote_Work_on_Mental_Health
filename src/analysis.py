from pathlib import Path
import pandas as pd


def get_data_file_path():
    # Get the current script directory
    script_dir = Path(__file__).resolve().parent

    # Construct the relative path to the CSV file
    csv_file_path = script_dir.parent / 'data' / 'Impact_of_Remote_Work_on_Mental_Health.csv'

    return csv_file_path


csv_filepath = get_data_file_path()
df = pd.read_csv(csv_filepath)
