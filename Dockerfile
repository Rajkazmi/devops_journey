FROM python:3.10-slim

WORKDIR /app

COPY automation.py .

CMD ["python", "automation.py"]
