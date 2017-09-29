Docker Test for creating a dev server for an existing project.
(I am going to test it with ticha project)

Here are the steps to setup a dev server:
1. Install Docker to your computer/laptop
2. Create a working directory for projectname-Docker
3. Inside the directory, create a txt file named Dockerfile
   with the following contents:
  For Flask:

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
  CMD ["python", "app.py"] # change the name of "app.py" accordingly

  For Django:
  
  FROM python:3
  ENV PYTHONUNBUFFERED 1
  RUN mkdir /code
  WORKDIR /code
  ADD requirements.txt /code/
  RUN pip install -r requirements.txt
  ADD . /code/

  *Note: For Django, besides using Dockerfile, we also need to create a docker-compose.yml
  with the following contents:

version: '3'

services:
  db:
    image: postgres
  web:
    build: .
    command: python3 manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/code
    ports:
      - "8000:8000"
    depends_on:
      - db

4. Make sure that the Dockerfile, the app.py, and the requirement.txt in
   the same directory
5. Run the command 
      docker build -t "projectname"
6. Run the app 
      docker run -p 4000:80 "projectname"
   You should see a notice that the app is running at http://localhost:4000.
7. To share your image, you should tag the image so Docker can find it by running
   this command:
      docker tag image username/repository:tag
      # replace username with your username, repository with your repository, and tag name.
8. If you want to publish the image, you should push the tagged image to the repository
   by running this command:
      docker push username/repository:tag
   Once completed, your image is publicly visible.
9. To pull the image, just run this command:
      docker run -p 4000:80 username/repository:tag
   because Docker will automatically pull the image from the Docker repository.
