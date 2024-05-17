import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email import encoders
from os.path import basename

FROM_EMAIL = "your_email_here"
FROM_EMAIL_PASSWORD = "your_password_here"


def send_email(recipient_email, subject, message, files):
    for f in files or []:
        with open(f, "rb") as fil:
            part = MIMEApplication(
                fil.read(),
                Name=basename(f)
            )
        # After the file is closed
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
        msg.attach(part)

    msg = MIMEMultipart()
    msg['From'] = 'me@pankajbhattarai.com.np'
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    try:
        with smtplib.SMTP('smtp.zoho.com', 587) as server:
            server.starttls()
            server.login(FROM_EMAIL, FROM_EMAIL_PASSWORD)
            server.sendmail(FROM_EMAIL, recipient_email, msg.as_string())
        print("Email sent successfully.")
    except Exception as e:
        print(f"Error: {e}")



