"""Module for smtp authentication and mail commands"""
import smtplib
import ssl


class Email:
    """This class is used to connect to email SMTP server and send email."""

    smtp_server: str
    port: int
    sender_email: str
    password: str

    def __init__(self, smtp_server, port, sender_email, password):
        self.smtp_server = smtp_server
        self.port = port
        self.sender_email = sender_email
        self.password = password

    def send_email(self, receiver_email: str, message: str):
        """This method is used to send an email."""

        # Create a secure SSL context
        context = ssl.create_default_context()
        # Login & Send mail
        with smtplib.SMTP_SSL(self.smtp_server, self.port, context=context) as server:
            server.login(self.sender_email, self.password)
            server.sendmail(self.sender_email, receiver_email, message)
