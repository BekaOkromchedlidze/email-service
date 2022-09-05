# Official Python base image
FROM python:3.9

# Set the current working directory to /app
WORKDIR /app

# Copy the file with the requirements to the /app directory.
COPY ./requirements.txt requirements.txt

# Install the package dependencies in the requirements file.
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the project directory inside the /app directory.
WORKDIR /app/email-service
COPY ./src ./src

# Set the command to run the uvicorn server.
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]