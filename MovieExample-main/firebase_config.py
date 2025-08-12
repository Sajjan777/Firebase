import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyA987xu8PyecAYdZzRKOLO3ytDdYzBwpSo",
    "authDomain": "first-46e58.firebaseapp.com",
    "databaseURL": "https://movie-ab85f-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "first-46e58",
    "storageBucket": "first-46e58.firebasestorage.app",
    "messagingSenderId": "464854734052",
    "appId": "1:464854734052:web:f50241c603f93043fd08f1",
    "measurementId": "G-BJJX8WKERH"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()
