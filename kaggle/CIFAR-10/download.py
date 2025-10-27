import kagglehub

# Download latest version
path = kagglehub.dataset_download("pankrzysiu/cifar10-python")

print("Path to dataset files:", path)