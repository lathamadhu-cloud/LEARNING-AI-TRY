
# Use an official Python runtime as a base image
FROM python:3.9-slim

# set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# define the command to start the application using Gunicorn with 4 worker processes
# Module name is 'superkart_api' (from superkart_api.py), and the Flask app variable is 'superkart_model'
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:7860", "superkart_api:superkart_model"]
