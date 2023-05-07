# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster

# Set the working directory to /app
WORKDIR /TelegramBot

# Copy the requirements file into the container at /app
COPY requirements.txt /TelegramBot

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y ffmpeg

# Copy the current directory contents into the container at /app
COPY . /TelegramBot

# Define environment variable
ENV TELEGRAM_BOT_TOKEN=<"6275176649:AAEBuWf6GlYeVWGoOdBrKSJHQvPTY2BYFhw">

# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
CMD ["python", "app.py"]
