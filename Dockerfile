# Use the official Python image from the Docker Hub
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install the dependencies
RUN pip install -r requirements.txt

# Make port 10000 available to the world outside this container
EXPOSE 10000

# Run the server
CMD ["python", "social_network_server.py"]
