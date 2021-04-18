import firebase_admin
from firebase_admin import credentials, messaging

cred = credentials.Certificate(".serviceAccountKey.json")
firebase_admin.initialize_app(cred)

registration_token = "e_89OFTOJblj3EUc4JoUEQ:APA91bFuHqy_cg8m2E-rzi4xtSJKw6WOGMVke6MVKfDRlAa5cJAgEJKk4ER3LudCEeMCFPW6doFMqF654A9xOgXLhR4LQxbZqeYDwAGobUGDtSpGk4hND29GiVN_T2DHdURww-puNbFk"
# See documentation on defining a message payload.
message = messaging.Message(
    notification=messaging.Notification(
        title="안녕하세요 타이틀 입니다",
        body="안녕하세요 메세지 입니다",
    ),
    token=registration_token,
)

# Send a message to the device corresponding to the provided
# registration token.
response = messaging.send(message)
# Response is a message ID string.
print("Successfully sent message:", response)
