# Week 1           : App Containerization
# Cloud Boot-Camper: Utra Man (Tony)
#
# Configurations for Backend
#
#

FROM python:3.10-slim-buster

# Inside Container
# Make a new folder inside container
WORKDIR /backend-flask

# Outside container --> inside container
# This contains the libraries we want install to run the app
COPY requirements.txt requirements.txt

# Insiside container
# Install the Python libraries used for the app
RUN pip3 install -r requirements.txt

# Outside container --> inside container
# . (period) means copy everything in the current directory
# The first period . = everything in the directory /back-flask (outside the container)
# The second period .. = /back-flask (inside the container)
COPY . .

# Set Environment Variables (En Vars)
# Inside container and will remain set when the container is running in
ENV FLASK_ENV=development

EXPOSE ${PORT}

# python3 -m flask run --host=0.0.0.0 --port=4567
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=4567"]
