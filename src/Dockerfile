FROM python:3.12-slim

WORKDIR /app

# Layer 1: Copy and install Python dependencies first
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Layer 2: Copy the rest of the application code
COPY . .

# Layer 3: Require a build argument and set the environment variable
ARG APP_ENV
ENV APP_ENV=${APP_ENV}

# Configure the application port
EXPOSE 5000

# Start the Flask application
CMD ["python", "app.py"]
