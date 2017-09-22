Docker Test for creating a dev server for an existing project.
(I am going to test it with ticha project)

Here are the steps to setup a dev server:
1. Install Docker to your computer/laptop
2. Create a working directory for projectname-Docker
3. Inside the directory, create a txt file named Dockerfile
   with the following contents:

  # Use an official Python runtime as a parent image
  FROM python:2.7-slim

  # Set the working directory to /app
  WORKDIR /app

  # Copy the current directory contents into the container at /app
  ADD . /app

  # Install any needed packages specified in requirements.txt
  RUN pip install -r requirements.txt

  # Make port 80 available to the world outside this container
  EXPOSE 80

  # Define environment variable
  ENV NAME World

  # Run app.py when the container launches
  CMD ["python", "app.py"]

4.
