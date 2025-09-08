from fastapi import FastAPI
import pandas as pd

app = FastAPI()

# Load CSV once at startup
df = pd.read_csv("VendorC_data.csv")
data = df.to_dict(orient="records")

@app.get("/")
def root():
    return {"message": "API is live and serving CSV data."}

@app.get("/data")
def get_all_data():
    return data

@app.get("/data/{row_id}")
def get_row(row_id: int):
    if 0 <= row_id < len(data):
        return data[row_id]
    return {"error": "Row not found"}
