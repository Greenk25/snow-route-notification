import csv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# please Replace these with your own values.

SENDGRID_API_KEY = "Your_Api_Key"
FROM_EMAIL = "Your_email"

listed_addresses = [
    "main",
    "broadway",
    "sherbrook"
]

def load_database():
    users = []
    with open("Residents.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Trim spaces and lowercase address
            row["address"] = row["address"].strip().lower()
            users.append(row)
    return users

def find_matching_emails():
    users = load_database()
    matching_emails = []

    for user in users:
        for listed in listed_addresses:
            if listed in user["address"]:   # substring match
                matching_emails.append(user["email"])
                break

    return matching_emails

def send_emails(emails):
    sg = SendGridAPIClient(SENDGRID_API_KEY)

    for email in emails:
        message = Mail(
            from_email=FROM_EMAIL,
            to_emails=email,
            subject="Address Match Notification",
            plain_text_content="""Hello,
            our address is affected by the Snow Route Ban —" 
            please do not park on snow routes from Nov 5, 2026""" )
        try:
            sg.send(message)
        except Exception as e:
            print("SENDGRID ERROR:", e)

@app.post("/trigger-action")
def trigger_action():
    matching_emails = find_matching_emails()

    if not matching_emails:
        return {"status": "No matching addresses found — emails NOT sent"}

    send_emails(matching_emails)

    return {
        "status": "Emails sent",
        "count": len(matching_emails),
        "emails": matching_emails
    }