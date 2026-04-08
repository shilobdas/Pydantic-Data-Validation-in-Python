from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict,Optional,Annotated

# 1. Define the data structure
class Patient(BaseModel):
    name: Annotated[str,Field(max_length=50,title='name of the patient',description='give the name of the patiend in less then 50 chars ',example=['Nitish','Amit'])]
    email:EmailStr
    linkedin_url:AnyUrl
    age: int=Field(gt=0,lt=120)
    weight:Annotated[float,Field(gt=0,strict=True)]
    married:Optional[bool]=None
    allergies:Optional[List[str]]=Field(max_length=5) 
    contact_details:Dict[str,str]

# 2. Define the function to handle the data 
def insert_patient_data(patient: Patient):
    # Use lowercase 'patient' to access the instance data

    print(patient.name)
    print(patient.email)
    print(patient.linkedin_url)
    print(patient.age)
    print(patient.allergies)
    print('inserted')

# 3. Create the data and call the function
patient_info = {'name': 'nitish','email':'abc@gmail.com','linkedin_url':'http://linkedin.com/','age':111,'weight':'94','married':True,'allergies':['polln','dust'], 'contact_details': {'phone':'1112345555555555'}}
patient1 = Patient(**patient_info)

insert_patient_data(patient1) 
print(patient1)
