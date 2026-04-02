from app import app, db
from models import Major, User, Student
from werkzeug.security import generate_password_hash
from datetime import datetime as dt

with app.app_context():
    db.drop_all()
    db.create_all()

    # Initial loading of majors
    majors = ['Accounting', 'Finance', 'Information Systems', 'International Business', 'Management', \
              'Operations Management & Business Analytics', 'Supply Chain Management']
    for each_major in majors:
        print(each_major)
        a_major = Major(major=each_major)
        db.session.add(a_major)
        db.session.commit()

    # Initial loading of users
    users = [
        {'username': 'echarron', 'email': 'echarron@terpmail.umd.edu', 'first_name':'Emily', 'last_name':'Charron',
            'password': generate_password_hash('echarron', method='pbkdf2:sha256'), 'role':'STUDENT'},
        {'username': 'admin', 'email': 'admin@gmail.com', 'first_name': 'Emily', 'last_name': 'Charron',
         'password': generate_password_hash('admin', method='pbkdf2:sha256'), 'role': 'ADMIN'},
        {'username': 'manager', 'email': 'manager@gmail.com', 'first_name': 'Emily', 'last_name': 'Charron',
         'password': generate_password_hash('manager', method='pbkdf2:sha256'), 'role': 'MANAGER'},
    ]

    for each_user in users:
        print(f'{each_user["username"]} inserted into user')
        a_user = User(username=each_user["username"], email=each_user["email"], first_name=each_user["first_name"],
                    last_name=each_user["last_name"], password=each_user["password"], role=each_user["role"])
        db.session.add(a_user)
        db.session.commit()

    # Initial loading of students first_name, last_name, major_id, birth_date, is_honors
    students = [
        {'student_id': '1', 'first_name': 'Robert', 'last_name':'Smith', 'email': 'robert.smith@gmail.com', 'major_id':3,
            'birth_date': dt(2007, 6, 1), 'is_honors':1},
        {'student_id': '2', 'first_name': 'Leo', 'last_name': 'Van Munching', 'email': 'leo.vanmunching@gmail.com', 'major_id':6,
         'birth_date': dt(2008, 3, 24), 'is_honors': 0},
        {'student_id':'3', 'first_name':'Emily','last_name':'Charron', 'email':'echarron@terpmail.umd.edu','major_id':3,
            'birth_date': dt(2005, 5, 18), 'is_honors': 0}
    ]

    for each_student in students:
        print(f'{each_student["first_name"]} {each_student["last_name"]} inserted into Student')
        a_student = Student(first_name=each_student["first_name"], last_name=each_student["last_name"],
                            email=each_student["email"], major_id=each_student["major_id"], birth_date=each_student["birth_date"],
                            is_honors=each_student["is_honors"])
        db.session.add(a_student)
        db.session.commit()


