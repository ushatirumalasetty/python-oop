import json
class Student:

    counter=0
    year="2020"

    def __init__(self,name,standard,state):
        self.name=name
        self.standard=standard
        self.state=state
        Student.counter+=1

if __name__ == "__main__" :
    student_details_1=Student("usha","secondary","Andhra Pradesh",)
    student_details_2=Student("rayvalesh","primary","Tamilnadu")
    print(json.dumps(student_details_1.__dict__,indent=4,sort_keys=True))
    print(student_details_2.__dict__)
    print(Student.counter)
    print(student_details_2.counter)


class nature:
    attitude="very good"

    @classmethod
    def about(cls):
        print("This is about " + cls.attitude + "!")


class boy(nature):
    attitude = "bad"

class girl(nature):
    attitude = "good"

p = nature()
p.about()
d = girl()
d.about()
c = boy()
c.about()


class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname

    def fullname(self):
        print(self.firstname,self.lastname)
    
    def get_first_name(self):
        return self.firstname

class child(person):
    def __init__(self,fname,lname,mood,climate):
        self.mood=mood
        self.climate=climate
        person.__init__(self,fname,lname)

    def status(self):
        print(self.mood,self.climate)

k=child("usha","tirumalasetty","happy","sunny")
k.status()