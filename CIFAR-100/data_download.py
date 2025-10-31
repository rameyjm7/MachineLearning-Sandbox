import kagglehub

# Download latest version
path = kagglehub.dataset_download("alincijov/cifar-100")

print("Path to dataset files:", path)