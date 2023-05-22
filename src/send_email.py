import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv


def generate_email_body(client_full_name, book_title, late_fee, email_contact, library_manager, library_name):
    try:
        with open('resources/templates/overdue_notification.html') as file:
            email_template = file.read()
    except IOError:
        print('The message template file was not found')
        return

    # Replace placeholders with dynamic values
    email_body = email_template\
        .replace("[Client's Full Name]", client_full_name) \
        .replace("[Book Title]", book_title) \
        .replace("[Late Fee]", late_fee) \
        .replace("[Contact Email]", email_contact) \
        .replace("[Library Manager]", library_manager) \
        .replace("[Library Name]", library_name)

    return email_body


def send_email(receiver: str, email_body: str):
    sender = os.getenv("GMAIL_EMAIL")
    password = os.getenv("GMAIL_APP_PASSWORD")

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    try:
        server.login(sender, password)
        msg = MIMEText(email_body, 'html')
        msg['From'] = sender
        msg['To'] = receiver
        msg['Subject'] = 'Overdue Book Reminder '
        server.sendmail(sender, receiver, msg.as_string())
        print(f'The message was sent successfully!')
    except Exception as e:
        print(f'Error: {e}: Check your login or password, please!')
    finally:
        server.quit()


def main():
    # Example dynamic values
    client_full_name = "Keith Maxwell"
    book_title = "The Catcher in the Rye"
    late_fee = "€2"
    email_contact = "alexandria.library@gmail.com"
    library_manager = "Samia el Abodi"
    library_name = "Alexandria Library"
    email_body = generate_email_body(client_full_name, book_title, late_fee, email_contact, library_manager,
                                     library_name)
    if not email_body:
        return

    load_dotenv()
    receiver = '704342@student.inholland.nl'
    send_email(receiver, email_body)


main()
