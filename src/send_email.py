import os
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


def read_html_template():
    try:
        with open('resources/templates/overdue_notification.html') as file:
            email_template = file.read()
    except IOError:
        print('The message template file was not found')
        return
    return email_template


def generate_email_body(client_full_name, book_title):
    # Replace placeholders with dynamic values
    email_body = EMAIL_TEMPLATE \
        .replace("[Client's Full Name]", client_full_name) \
        .replace("[Book Title]", book_title) \
        .replace("[Late Fee]", LATE_FEE) \
        .replace("[Contact Email]", LIBRARY_EMAIL) \
        .replace("[Library Manager]", LIBRARY_MANAGER) \
        .replace("[Library Name]", LIBRARY_NAME)

    return email_body


def send_email(receiver: str, email_body: str):
    sender = os.getenv("GMAIL_EMAIL")
    password = os.getenv("GMAIL_APP_PASSWORD")

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    try:
        server.login(sender, password)
        msg = MIMEText(email_body, 'html')
        msg['From'] = formataddr(('Alexandria Library', f'{sender}'))
        msg['To'] = receiver
        msg['Subject'] = 'Overdue Book Reminder '
        server.sendmail(sender, receiver, msg.as_string())
        print(f'The message was sent successfully!')
    except Exception as e:
        print(f'Error: {e}: Check your login or password, please!')
    finally:
        server.quit()


def send_all_notifications():
    # TODO: reuse database connection from main controller
    from src.models.database import Database
    database = Database()
    dataframe = database.execute_query("""
    SELECT c.name, c.surname, b.title, c.email FROM borrowings a
    INNER JOIN books b ON a.book_id = b.book_id
    INNER JOIN clients c ON a.client_id = c.client_id
    WHERE ((a.to_date < CURDATE() and a.extension = 0) 
        OR (a.to_date < DATE_ADD(CURDATE(), INTERVAL 7 DAY) AND a.extension = 1))
        AND returned = 0
        AND reminder_sent = 0;
    """)

    email_counter = 0
    for i, data in enumerate(dataframe):
        name, surname, title, email = data
        email_body = generate_email_body(f'{name} {surname}', f'{title}')
        send_email(email, email_body)
        email_counter += 1

    return f'Total emails sent: {email_counter}'


# Set library parameters
LATE_FEE = "€2"
LIBRARY_EMAIL = "alexandria.library@gmail.com"
LIBRARY_MANAGER = "Samia el Abodi"
LIBRARY_NAME = "Alexandria Library"
EMAIL_TEMPLATE = read_html_template()

if __name__ == '__main__':
    send_all_notifications()
