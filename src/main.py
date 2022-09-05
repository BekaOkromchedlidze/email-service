import os
from smtplib import SMTPServerDisconnected

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from starlette import status

from src import send_mail


class EmailRequest(BaseModel):
    """Email request model"""

    receiver_email: str
    message: str


app = FastAPI()


@app.on_event("startup")
async def startup_event():
    """Load environment variables from .env file during application startup."""
    load_dotenv(".env")
    if os.getenv("SMTP_SERVER") is None:
        raise Exception("SMTP server not defined in environment variables")
    if os.getenv("PORT") is None:
        raise Exception("SMTP server PORT not defined in environment variables")
    if os.getenv("SENDER_EMAIL") is None:
        raise Exception(
            "SENDER_EMAIL for SMTP server not defined in environment variables"
        )
    if os.getenv("PASSWORD") is None:
        raise Exception("PASSWORD for SMTP server not defined in environment variables")


@app.post("/email")
async def send_email(email_req: EmailRequest):
    """Given receiver_email and message within EmailRequest, send email to receiver"""
    email = send_mail.Email(
        smtp_server=os.getenv("SMTP_SERVER"),
        port=os.getenv("PORT"),
        sender_email=os.getenv("SENDER_EMAIL"),
        password=os.getenv("PASSWORD"),
    )
    try:
        email.send_email(email_req.receiver_email, email_req.message)
    except SMTPServerDisconnected as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to connect to SMTP server. Please ensure SMTP_SERVER, PORT, SENDER_EMAIL and PASSWORD are "
            "added as environment variables. ",
        )
