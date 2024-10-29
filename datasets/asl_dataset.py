import os
from kaggle.api.kaggle_api_extended import KaggleApi

# Initialize the Kaggle API
api = KaggleApi()
api.authenticate()

# Set the dataset name and path
dataset_name = "prathumarikeri/american-sign-language-09az"
path = os.path.join(os.getcwd(), dataset_name)

# Download the dataset
api.dataset_download_files(dataset_name, path=path, unzip=True)

print("Path to dataset files:", path)