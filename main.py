import joblib
import pickle

with open('model_scaling.pkl', 'rb') as file_1:
    model_scaling = joblib.load(file_1)