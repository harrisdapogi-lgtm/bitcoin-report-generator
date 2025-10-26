import pandas as pd
import numpy as np
from datetime import datetime

# --- Configuration ---
OUTPUT_FILE = "daily_report.csv"
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
NUM_SAMPLES = 100

def generate_report():
    """
    Simulates generating a daily report with actual and predicted values,
    and saves the results to a CSV file.
    """
    try:
        # 1. Generate Mock Data
        # We simulate 100 observations where the 'Predicted' value is close to the 'Actual' value
        np.random.seed(int(datetime.now().timestamp() * 1000) % (2**32)) # Seed for semi-random results

        actual_values = np.random.normal(loc=50, scale=10, size=NUM_SAMPLES)
        # Prediction is slightly offset from the actual value
        predicted_noise = np.random.normal(loc=1, scale=0.5, size=NUM_SAMPLES)
        predicted_values = actual_values * 1.05 + predicted_noise - 5

        # 2. Create DataFrame
        data = {
            'Date': [datetime.now().strftime(DATE_FORMAT)] * NUM_SAMPLES,
            'Observation_ID': [f'Obs-{i:03d}' for i in range(1, NUM_SAMPLES + 1)],
            'Actual_Value': actual_values.round(2),
            'Predicted_Value': predicted_values.round(2),
            'Error': (actual_values - predicted_values).round(2)
        }
        df = pd.DataFrame(data)

        # 3. Save to CSV
        df.to_csv(OUTPUT_FILE, index=False)

        print(f"Successfully generated and saved report to {OUTPUT_FILE}")
        print(f"Current Date: {datetime.now().strftime(DATE_FORMAT)}")
        print(f"Generated {NUM_SAMPLES} observations.")

    except Exception as e:
        print(f"An error occurred during report generation: {e}")
        # Exit with a non-zero status code to fail the GitHub Action
        exit(1)

if __name__ == "__main__":
    generate_report()
