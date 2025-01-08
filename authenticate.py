import requests
from flask import make_response, abort, request

from config import accountInformation
from models import User
from config import db

def login():
    auth_url = 'https://web.socem.plymouth.ac.uk/COMP2001/auth/api/users'
    details = request.get_json()
    emailAddress = details.get("emailAddress")
    password = details.get("password")

    credentials = {
        'email': emailAddress,
        'password': password
    }

    response = requests.post(auth_url, json=credentials)

    if response.status_code == 200:
        try:
            json_response = response.json()
            accountInformation.login(emailAddress)

            # Get the user ID from the users table in the database
            user = db.session.query(User).filter(User.emailAddress == emailAddress).one_or_none()
            # If the user does not exist, create a new user
            if user is None:
                return "User does not exist", 404
            else:
                accountInformation.set_user_id(user.userID)

                # Get the user's role from the response
                role = user.role
                if (role == "admin"):
                    accountInformation.set_admin(True)

            return json_response, 200
        except requests.JSONDecodeError:
            print("Response is not JSON")
            return "Authentication failed", 401
    else:
        return f"Authentication failed | {response.text}", response.status_code
    
def logout():
    if (accountInformation.logout()):
        return "Logged out", 200
    else:
        return "Failed to logout", 400