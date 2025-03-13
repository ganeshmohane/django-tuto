from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import MySQLdb
import json

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





# # login 
# @csrf_exempt
# def login(request):


