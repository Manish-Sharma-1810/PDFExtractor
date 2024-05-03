# Stage 1: Build Flask application
FROM python:3.12-slim AS builder

WORKDIR /app

# Copy only requirements to cache them in Docker layer
COPY requirements.txt .

# Install dependencies
RUN pip3 install --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt

# Copy the application code
COPY app/ .

# Stage 2: Create a lightweight production image
FROM python:3.12-slim

LABEL maintainer="manishkumar.sharma0103@gmail.com"

WORKDIR /app

# Copy installed dependencies from the builder stage
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin/gunicorn /usr/local/bin/gunicorn

# Copy the application code from the builder stage
COPY --from=builder /app /app

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Expose the port your app runs on
EXPOSE 5000

# Run the Flask application with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app", "--workers=5", "--timeout=60"]
