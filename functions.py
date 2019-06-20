import sys

def student_info(*args,**kwargs):
    print(args)
    print(kwargs)


courses = ['Math', 'CompSci']
info = {'name': 'Mateusz', 'lastname': 'Oberda' , 'age': '29'}

student_info(*courses, **info)

print(sys.path)