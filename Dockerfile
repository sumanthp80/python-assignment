# Use a Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the code files to the working directory
COPY requirements.txt .
COPY orders.py .

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Use non-root user for better container security
RUN useradd orders-user
USER orders-user

# Set the entrypoint command
CMD ["python", "orders.py"]