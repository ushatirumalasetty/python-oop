import json
class Student:
    def __init__(self,name,standard,state):
        self.name=name
        self.standard=standard
        self.state=state



student_details_1=student("usha","secondary","Andhra Pradesh",)
student_details_2=student("rayvalesh","primary","Tamilnadu")

print(json.dumps(student_details_1.__dict__,indent=4,sort_keys=True))
print(student_details_2.__dict__)
