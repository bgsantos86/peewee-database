from peewee import *

db = SqliteDatabase('student.db')

class Student(Model):
    username = CharField(max_length=255, unique=True)
    points = IntegerField(default=0)

    class Meta:
        database = db

students = [
    {'username': 'Bruno',
     'points': 14734},
     {'username': 'Alzi',
     'points': 4534},
     {'username': 'Ana',
     'points': 6455},
     {'username': 'Dida',
     'points': 5345},
     {'username': 'Snoopy',
     'points': 14674}
]

def add_students():
    try: 
        for student in students:
            Student.create(username=student['username'], 
                        points=student['points'])
    except IntegrityError:
        student_record = Student.get(username=student['username'])
        student_record.points = student['points']
        student_record.save()

def top_student():
    student = Student.select().order_by(Student.points.desc()).get()
    return student

if __name__ == '__main__':
    db.connect()
    db.create_tables([Student], safe=True)
    add_students()
    print(f'Our top student right now is: {top_student().username}.')