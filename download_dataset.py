import kagglehub

path = kagglehub.dataset_download(
    "aryan208/financial-transactions-dataset-for-fraud-detection"
)

print("Path to dataset files:", path)
