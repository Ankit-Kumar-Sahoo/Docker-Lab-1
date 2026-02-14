# Docker-Lab-1

# Docker Lab 1: ML Model Training Container

## Overview
Containerized a machine learning training script using Docker. The script trains a Random Forest classifier on the Iris dataset and saves the model.

---

## Project Structure

```
DOCKER LAB 1/
├── src/
│   ├── model_training.py     # ML training script
│   └── requirements.txt      # Python dependencies
├── Dockerfile                # Docker image definition
├── ml-training.tar          # Exported Docker image
└── README.md                # This file
```

---

## What I Did

### 1. Created ML Training Script
- Trained Random Forest classifier on Iris dataset
- Evaluated model accuracy
- Saved trained model to `iris_model.pkl`

### 2. Created Dockerfile
```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY src/requirements.txt .
RUN pip install -r requirements.txt
COPY src/model_training.py .
CMD ["python", "model_training.py"]
```

### 3. Built and Ran Docker Container
```bash
# Build image
docker build -t ml-training:v1.2 .

# Run container
docker run --name ml-training-container ml-training:v1.2

# Export image
docker save ml-training:v1.2 > ml-training.tar
```

---

## Key Learnings

- How to write a Dockerfile
- Building Docker images from Dockerfiles
- Running containers from images
- Exporting Docker images to TAR files
- Using WORKDIR to organize container filesystem
- Copying files from specific directories into containers
- **Image vs Container**: Everything before CMD executes during image build. CMD only runs when container starts

---

## Important Notes

- All setup commands (FROM, WORKDIR, COPY, RUN) execute during **image build**
- CMD command only executes when **container starts**

---

## Author
**Ankit Kumar Sahoo**  
Northeastern University  
February 2026