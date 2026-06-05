from pathlib import Path
import pandas as pd

base_dir = Path(__file__).parent
csv_path = base_dir / "data.csv"

df = pd.read_csv(csv_path)
