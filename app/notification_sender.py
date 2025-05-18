def send_notification(message: dict):
    notif_type = message.get("type")
    recipient = message.get("recipient")
    content = message.get("content")

    if notif_type == "email":
        send_email(recipient, content)
    elif notif_type == "sms":
        send_sms(recipient, content)
    elif notif_type == "inapp":
        store_in_app_notification(recipient, content)
    else:
        print(f"Unknown notification type: {notif_type}")

def send_email(to, body):
    print(f"Sending EMAIL to {to}: {body}")
    # Integrate actual SMTP or SendGrid/Mailgun here

def send_sms(to, body):
    print(f"Sending SMS to {to}: {body}")
    # Integrate Twilio or mock here

def store_in_app_notification(user_id, body):
    print(f"Storing IN-APP notification for user {user_id}: {body}")
    # Store in DB table `in_app_notifications`
