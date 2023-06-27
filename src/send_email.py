import os
import dotenv
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
# import schedule
# import time

from src.resources.config import TEMPLATES_DIR


def read_html_template(path_to_html_template: str):
    """Get email template from html file"""
    try:
        with open(path_to_html_template) as file:
            html_template = file.read()
    except IOError:
        print('The message template file was not found')
        return
    return html_template


def generate_email_body_overdue_notification(client_full_name, book_title):
    """Replace html template placeholders with dynamic values. For email of type Reset Password"""
    email_body = OVERDUE_TEMPLATE \
        .replace("[Client Full Name]", client_full_name) \
        .replace("[Book Title]", book_title) \
        .replace("[Late Fee]", LATE_FEE) \
        .replace("[Contact Email]", LIBRARY_EMAIL) \
        .replace("[Library Name]", LIBRARY_NAME)

    return email_body


def generate_email_body_confirm_password(client_full_name):
    """Replace html template placeholders with dynamic values. For email of type Reset Password Confirmation"""
    email_body = CONFIRM_TEMPLATE \
        .replace("[Client Full Name]", client_full_name) \
        .replace("[Library Name]", LIBRARY_NAME)

    return email_body


def generate_email_body_reset_password(client_full_name, reset_token):
    """Replace html template placeholders with dynamic values. For email of type Overdue Notifications"""
    email_body = RESET_TEMPLATE \
        .replace("[Client Full Name]", client_full_name) \
        .replace("[Reset token]", reset_token) \
        .replace("[Library Name]", LIBRARY_NAME)

    return email_body


def send_email(receiver: str, email_body: str, subject: str) -> bool:
    """Sends email using SMTP protocol. Returns True if successful, False otherwise."""
    dotenv.load_dotenv()
    sender = os.getenv("GMAIL_EMAIL")
    password = os.getenv("GMAIL_APP_PASSWORD")

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    try:
        server.login(sender, password)
        msg = MIMEText(email_body, 'html')
        msg['From'] = formataddr(('Alexandria Library', f'{sender}'))
        msg['To'] = receiver
        msg['Subject'] = subject
        server.sendmail(sender, receiver, msg.as_string())
        print(f'The message was sent successfully!')
        return True
    except Exception as e:
        print(f'Error: {e}: Check your login or password, please!')
    finally:
        server.quit()
    return False


def send_reset_password_request(database, receiver: str, reset_token: str):
    """Send email with token for reset password request"""
    query = 'SELECT CONCAT(name, " ", surname) AS full_name FROM EMPLOYEES WHERE email = %s'
    result = database.execute_query_fetchone(query, (receiver,))

    if not result:
        return

    client_name = result[0]
    email_body = generate_email_body_reset_password(client_name, reset_token)

    return send_email(receiver, email_body, 'Reset Password Request')


def send_reset_password_confirmation(database, receiver: str):
    """Send email that informs user of successfully resetting password """

    query = 'SELECT CONCAT(name, " ", surname) AS full_name FROM EMPLOYEES WHERE email = %s'
    result = database.execute_query_fetchone(query, (receiver,))

    if not result:
        return

    client_name = result[0]
    email_body = generate_email_body_confirm_password(client_name)

    return send_email(receiver, email_body, 'Your Alexandria password has been changed')


def send_all_notifications():
    """Notify all users who have overdue books"""
    # FIXME: reuse database connection
    from src.models.database import Database
    database = Database()
    dataframe = database.execute_query("""
    SELECT c.name, c.surname, b.title, c.email FROM borrowings a
    INNER JOIN books b ON a.book_id = b.book_id
    INNER JOIN clients c ON a.client_id = c.client_id
    WHERE ((a.to_date < CURDATE() and a.extension = 0) 
        OR (a.to_date < DATE_ADD(CURDATE(), INTERVAL 7 DAY) AND a.extension = 1))
    """)
    # AND returned = 0
    # AND reminder_sent = 0;

    email_counter = 0
    for i, data in enumerate(dataframe):
        name, surname, title, email = data
        email_body = generate_email_body_overdue_notification(f'{name} {surname}', f'{title}')
        send_email(email, email_body, 'Overdue Book Reminder')
        email_counter += 1

    return f'Total emails sent: {email_counter}'


# Set library parameters
LATE_FEE = "€2"
LIBRARY_EMAIL = "noreply@alexandria.library.com"
LIBRARY_NAME = "Alexandria Library"
OVERDUE_TEMPLATE = read_html_template(os.path.join(TEMPLATES_DIR, 'overdue_notification.html'))
RESET_TEMPLATE = read_html_template(os.path.join(TEMPLATES_DIR, 'reset_password_request.html'))
CONFIRM_TEMPLATE = read_html_template(os.path.join(TEMPLATES_DIR, 'reset_password_confirmation.html'))


# schedule.every().day.at("00:07").do(send_all_notifications)
#
# while True:
#     schedule.run_pending()
#     time.sleep(100)
#     print(1)
