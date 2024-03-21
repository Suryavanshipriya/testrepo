# Use an official Python runtime as the base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Flask
RUN pip install Flask

# Expose the Flask port
EXPOSE 5000

# Command to run the Flask application
CMD ["python", "app.py"]