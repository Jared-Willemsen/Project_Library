import os
import smtplib
from dotenv import load_dotenv


def send_email(to_email_address: str, subject: str, body: str):
    """
    send_email sends an email to the email address specified in the
    argument.
    """

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(os.getenv("GMAIL_EMAIL"), os.getenv("GMAIL_APP_PASSWORD"))
        server.sendmail(os.getenv("GMAIL_EMAIL"), to_email_address,
                        "Subject: {}\n\n{}".format(subject, body))


# Set email parameters
client_full_name = "Keith Maxwell"
book_title = "The Catcher in the Rye"
late_fee = "0.50 euro"
contact_email = "alexandria.library@gmail.com"
library_manager = "Samia el Abodi"
library_name = "Alexandria Library"

# Create email body
email_body = f"""
Dear {client_full_name},


We would like to inform you that the book titled "{book_title}" that you borrowed from our library is currently overdue.

We kindly ask that you return the book as soon as possible to avoid any additional fees. Please note that you will be \
charged a late fee of {late_fee} for each day that the book is not returned.

If you have already returned the book, please disregard this notice. If you have any questions or concerns, please \
feel free to contact us at {contact_email}.

Thank you for your cooperation.


Best regards,

{library_manager}
{library_name}
"""


# Send email
load_dotenv()
send_email('704342@student.inholland.nl', f'Reminder: Overdue Book from {library_name}', email_body)
