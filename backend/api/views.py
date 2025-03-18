from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import MySQLdb
import json
import joblib
import numpy as np
import os

# fetch all students
@csrf_exempt
def get_all_students(request):
    db = MySQLdb.connect(user='root', passwd='', db='django_db', host='localhost')
    cursor = db.cursor()
    cursor.execute("select * from students")
    students = cursor.fetchall()
    return JsonResponse({"students":students})

# create student
@csrf_exempt
def create_student(request):
    data = json.loads(request.body)
    name = data.get('name')
    username = data.get('username')
    password = data.get('password')
    print(name, username, password)

    db = MySQLdb.connect(user='root',passwd='',db='django_db',host='localhost')
    cursor = db.cursor()
    cursor.execute("insert into students(name, username, password) values(%s,%s,%s)",(name, username, password))
    db.commit()
    db.close()
    return JsonResponse({"message":"Create Succesfullly"})

# login 
@csrf_exempt
def login(request):
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')
    print(username,password)
    db = MySQLdb.connect(user='root',passwd='',db='django_db',host='localhost')
    cursor = db.cursor()
    cursor.execute("select password from students where username = %s", (username,))
    db_passwd = cursor.fetchone()
    print(db_passwd)
    db.close()
    if password != db_passwd[0]:
        return JsonResponse({"message":"Password is incorrect"},status=401)

    return JsonResponse({"message":"Logged In Successfully"})



# model test
@csrf_exempt
def predict_placement(request):
    data = json.loads(request.body)
    print(data)
    cgpa = data.get('cgpa')	
    projects = data.get('projects')	
    certifications = data.get('certifications')
    soft_skills = data.get('soft_skills')	
    hackathons = data.get('hackathons')	
    interview_attempts = data.get('interview_attempts')

    model = joblib.load(os.path.join(os.path.dirname(__file__), "model.pkl"))

    features = np.array([[cgpa,projects, certifications, soft_skills, hackathons, interview_attempts]])
    prediction = model.predict(features)[0]
    print(prediction)
    if int(prediction) == 1:
        return JsonResponse({"message":"You will get placement"})
    else :
        return JsonResponse({"message":"low chances"})


