# -*- coding: utf-8 -*-
Name = input('name:')
Age = input('age:')
Job = input('job:')
Hobbies = input('hobbies:')

info = '''
------------ info of Name -----------
name: %s 
age: %s
job: %s
hobbies: %s
-------------------------------------
''' % (Name, Age, Job, Hobbies)
print(info)