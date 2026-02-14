FROM python:3.10-slim

WORKDIR /app

COPY src/requirements.txt .
RUN pip install -r requirements.txt

COPY src/model_training.py .

CMD ["python", "model_training.py"]