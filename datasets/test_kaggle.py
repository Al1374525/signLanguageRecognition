import os
import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi

# Initialize the Kaggle API
api = KaggleApi()
api.authenticate()
api.model_list_cli()

# Print a success message if authentication is successful
print("Kaggle API setup successful!")