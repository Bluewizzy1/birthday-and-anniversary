import smtplib
from email.mime.text import MIMEText
from twilio.rest import Client
import datetime


friends = {
    "Blue": {
        "birthday": "28-04-2020",
        "anniversary": "29-04-2018",
        "email": "jbluewizzy@gmail.com",
        "phone": "07065202012"
    },
    "Wizzy": {
        "birthday": "28-04-2017",
        "anniversary": "01-05-2013",
        "email": "jbluewizzy@gmail.com",
        "phone": "07065202012"
    },
     "Zinny": {
        "email": "zinnyvee12@gmail.com",
        "birthday": "22-11-1994", 
        "anniversary":"09-08-2016", 
        "phone": "0813636994"
    },
    "Riirii": {
        "email": "goodnews123@gmail.com", 
        "birthday": "02-03-1989", 
        "anniversary":"12-02-2021", 
        "phone": "0813636994"
    },
    "MCJ": {
        "email": "chetaplanet@gmail.com", 
        "birthday": "10-05-1993", 
        "anniversary":"10-06-2017", 
        "phone": "0813636994"
    },
    "Miimii": {
        "email": "chukwunenyejohnmiracle@gmail.com", 
        "birthday": "22-10-1990", 
        "anniversary":"04-04-2018", 
        "phone": "0813636994"
    },
    "AdeT": {
        "email": "adeleket18@gmail.com", 
        "birthday": "28-04-1990", 
        "anniversary":"30-04-2020", 
        "phone": "08108012195"
    },
}

today = datetime.date.today()
print(today.month, today.day)
def is_special_day(*args, **kwargs):    
    print(today)
    bdate = datetime.datetime.strptime(*args, "%Y-%m-%d").date()
    return (bdate.month, bdate.day) == (today.month, today.day)

def send_email(to, subject, body):
    # Create a message object
    message = MIMEText(body)
    message["Subject"] = subject
    message["From"] = "jbluewizzy@gmail.com"
    message["To"] = to

    # Send the message
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.ehlo()
        # server.starttls()
        server.login("jbluewizzy@gmail.com", "kezmjaenfcmfwyth")
        server.sendmail("jbluewizzy@gmail.com", to, message.as_string())
        print("sent successfully")

def send_sms(to, body):
    # Your Twilio account SID and auth token
    account_sid = "AC183129835ca22e405b4d34e89ac260eb"
    auth_token = "da37cd57265e7dcc889c4212fd74c95e"
    client = Client(account_sid, auth_token)

    # Create a message
    message = client.messages.create(
        to=to,
        from_="07065202012",
        body=body
    )

    # Print the message SID
    print(message.sid)


for name, data in friends.items():
    btdate = datetime.datetime.strptime(data["birthday"], "%d-%m-%Y").date()
    btanniv = datetime.datetime.strptime(data["anniversary"], "%d-%m-%Y").date()
    # print(btdate.month, btdate.day)
    if btdate.month == today.month and btdate.day == today.day:
        print("HAPPY")
    
        # Send a birthday email
        subject = f"Happy Birthday, {name}!"
        body = f"Dear {name},\n\nWishing you a very happy birthday!\n\nBest regards,\nBluewizzy"
        send_email(data["email"], subject, body)
        # Send a birthday SMS
        body = f"Happy Birthday, {name}! Have a great day!"
        send_sms(data["phone"], body)

    if is_special_day(btanniv):
        # Send an anniversary email
        subject = f"Happy Anniversary, {name}!"
        body = f"Dear {name},\n\nWishing you a very happy anniversary!\n\nBest regards,\nBluewizzy"
        send_email(data["email"], subject, body)
        # Send an anniversary SMS
        body = f"Happy Anniversary, {name}! Best wishes to you and your partner."
        send_sms(data["phone"], body)
