import joblib
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "model" / "pipeline.joblib"

pipeline = joblib.load(MODEL_PATH)


def predict(data):

    df = pd.DataFrame([data])

    prediction = pipeline.predict(df)

    return int(prediction[0])