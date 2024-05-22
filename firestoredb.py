import firebase_admin
from firebase_admin import credentials, firestore

# Initialize the Firebase Admin SDK
cred = credentials.Certificate('homeweather-ca8b9-firebase-adminsdk-1m5lo-31af22121a.json')
firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()

# Data to be saved
data = {
    'users': {
        'user_1': {
            'first_name': 'John',
            'last_name': 'Doe',
            'age': 30
        },
        'user_2': {
            'first_name': 'Jane',
            'last_name': 'Smith',
            'age': 25
        }
    }
}

# Save data to Firestore
for user_id, user_data in data['users'].items():
    db.collection('users').document(user_id).set(user_data)

print("Data saved successfully!")
