# email-service

Email-Service is a REST API service developed with Python FastAPI framework. It can be used to create a connection to an SMTP server and send an email. It can be used as a communication centre for sending email notifications. The API is passed the receivers email and text to include within email.




## Installation

If deploying locally, checkout project and update .env file in the root directory with the specified SMTP connection details. The service can be started by running the following command from the root directory.

```bash
  pip install --upgrade -r requirements.txt | uvicorn src.main:app --host 0.0.0.0 --port 80
```
Alternatively, you may deploy using Docker. Download the docker-compose.yaml file from this project and update the environment variables within with the respective SMTP connection details. 
```bash
      - SMTP_SERVER=[your SMTP server address]
      - PORT=[SMTP port]
      - SENDER_EMAIL=[Email address where the email will be sent from]
      - PASSWORD=[Email password]
      
    ports:
      - [SMTP port]:[SMTP port]
      - 80:80
```

Once the above is updated, you may start the service by running the following command:

```bash
  docker compose -f PATH_TO_DOCKER_COMPOSE_FILE up
```
## Usage

You may access the API documentation by going to 
```bash
  localhost:80/docs
```
