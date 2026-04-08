from pydantic import BaseModel,EmailStr,model_validator
from typing import List,Dict,Optional,Annotated

# 1. Define the data structure
class Patient(BaseModel):
    name:str
    email:EmailStr
    age: int
    weight:float 
    married:bool
    allergies:List[str]
    contact_details:Dict[str,str]
   
    @model_validator(mode='after')
    def validate_emargency_contract(cls,model):
        if model.age>60 and 'emergency' not in model.contact_details:
                raise ValueError('Patients older then 60 must have an emergency contact')
        return model
    
    
    
    
    
    

# 2. Define the function to update the data 
def update_patient_data(patient: Patient):
    # Use lowercase 'patient' to access the instance data

    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.allergies)
    print('updated')

# 3. Create the data and call the function
patient_info = {'name': 'nitish','email':'abc@savethechildren.org','age':65,'weight':'94','married':True,'allergies':['polln','dust'], 'contact_details': {'phone':'1112345555555555','emergency':'001212312123'}}
patient1 = Patient(**patient_info)

update_patient_data(patient1)

