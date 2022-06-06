from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def homepage(request):
    #return HttpResponse("Hello - this is the firt req/reponse flow!")
    return render(request, 'home.html', {}) #redirect to a template


def updatedata(request):
    ## soem processing
 
    batches = [{'batch':'EEC TE Batch2', 'course':'webapp101'}, 
               {'batch':'EEC TE Batch3', 'course':'iot'},
               {'batch':'EEC TE Batch4', 'course':'devops'},
               {'batch':'EEC TE Batch5', 'course':'Web App  101'},
               {'batch':'EEC TE Batch6', 'course':'Embedded'}]

    return render(request, 'update.html', {'context':batches})



def register(request):
    rows = getDBData()
    print ('#### DEBUG ####')
    print(rows)

    return render(request, 'register.html', {'context':rows})

    
def acknowledge(request):
    if request.method == 'POST':
        id = request.POST.get('courseid')
        batch = request.POST.get('batch')
        course = request.POST.get('coursename')


    print('######### DEBUG ########')
    print(id)
    print(batch)
    print(course)

    dbUpdate(id, batch, course)

    statement = "Acknowledgement - Welcome to the course"

    return render(request, 'acknowledge.html', {'context':statement})


def dbUpdate(id, batch, course):
    id_val = int(id)
    with connection.cursor() as cursor: # RAW SQL QUERY
        cursor.execute("INSERT INTO courses VALUES (%s, %s, %s)", [id_val, batch, course])


def getDBData():
    with connection.cursor() as cursor:
        cursor.execute('select * from courses')
        rows = cursor.fetchall()
    return rows







# def registration(request):
#     #names = ['Abhijeet Deogirikar', 'Pratibimb Parijat']
#     #courses = ['WebApp101', 'DevOps', 'Internet of Things', 'IT101', 'Embedded101']

#     #batches = {'batch1':'webapp101', 'batch2':'webapp101', 'batch3':'devops', 'batch4':'IoT 101'}
#     batches = [{'batch':'EEC TE Batch2', 'course':'webapp101'}, 
#                {'batch':'EEC TE Batch3', 'course':'iot'},
#                {'batch':'EEC TE Batch4', 'course':'devops'}]


    return render(request, 'register.html', {'context':batches}) 



































# def registerform(request):
#     return render(request, 'registerform.html', {}) 

# def submitform(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         course = request.POST.get('course')

#     statement = 'Dear ' + name + ', Welcome  to the ' + course + ' from CopperCloud'

#     print(name)
#     print(course)
#     print(statement)

#     return render(request, 'acknowledge.html', {'context':statement}) #redirect to a template
