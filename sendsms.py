import streamlit as st
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

def send_sms(account_sid, auth_token, sender_phone_number, receiver_phone_number):
    # Message to be Sent
    message = 'Hey Where Are You? 🤨...TUDU is missing you 😕 come fast and complete your goals'

    try:
        # Initialize Twilio Client
        client = Client(account_sid, auth_token)

        # Send SMS
        client.messages.create(
            body=message,
            from_=sender_phone_number,
            to=receiver_phone_number
        )

        st.success("SMS sent successfully!")
    except TwilioRestException as e:
        st.error(f"Failed to send SMS: {e}")
    except Exception as e:
        st.error(f"Error occurred: {e}")

def main():
    st.title("Twilio SMS Sender")

    # Load Twilio credentials from Streamlit secrets
    try:
        account_sid = st.secrets["twilio"]["account_sid"]
        auth_token = st.secrets["twilio"]["auth_token"]
        sender_phone_number = st.secrets["twilio"]["sender_phone_number"]
        receiver_phone_number = st.secrets["twilio"]["receiver_phone_number"]
    except KeyError:
        st.error("Twilio credentials not found in Streamlit secrets. Please check your configuration.")
        return

    # Button to send SMS
    if st.button("Send SMS"):
        send_sms(account_sid, auth_token, sender_phone_number, receiver_phone_number)

if __name__ == "__main__":
    main()
