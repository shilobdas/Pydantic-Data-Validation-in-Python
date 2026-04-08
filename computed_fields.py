from pydantic import BaseModel,EmailStr,computed_field
from typing import List,Dict,Optional,Annotated

# 1. Define the data structure
class Patient(BaseModel):
    name:str
    email:EmailStr
    age: int
    weight:float #kg
    height:float #mtr
    married:bool
    allergies:List[str]
    contact_details:Dict[str,str]
    
    @computed_field
    @property
    def bmi(self)->float: 
        bmi =round(self.weight/(self.height**2),2)
    
    
# 2. Define the function to update the data 
def update_patient_data(patient: Patient):
    # Use lowercase 'patient' to access the instance data

    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.allergies)
    print('BMI',patient.bmi)
    print('updated')

# 3. Create the data and call the function
patient_info = {'name': 'nitish','email':'abc@savethechildren.org','age':65,'weight':'94','height':1.80,'married':True,'allergies':['polln','dust'], 'contact_details': {'phone':'1112345555555555','emergency':'001212312123'}}
patient1 = Patient(**patient_info)

update_patient_data(patient1)
print(patient1)

