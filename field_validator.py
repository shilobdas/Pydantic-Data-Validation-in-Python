from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator
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
    
    
    @field_validator('email')
    @classmethod
    
    def email_validator(cls,value):
       valid_domains =['hdfc.com','icici.com','savethechildren.org']
       domain_name=value.split('@')[-1]
       if domain_name not in valid_domains:
          raise ValueError('not a valid domain')
     
       return value
    @field_validator('name')
    @classmethod
    def transform_name(cls,value):
        return value.upper()
    
    @field_validator('allergies')
    @classmethod
    def uppercase_allergies(cls, value):return [item.upper() for item in value]
    @field_validator('age',mode='after')
    @classmethod
    def validate_age(cls,value):
      if 0<value<100:
       return value 
      else:
       raise ValueError ('age should be in between 0 to 100')
    

# 2. Define the function to update the data 
def update_patient_data(patient: Patient):
    # Use lowercase 'patient' to access the instance data

    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.allergies)
    print('updated')

# 3. Create the data and call the function
patient_info = {'name': 'nitish','email':'abc@savethechildren.org','age':1,'weight':'94','married':True,'allergies':['polln','dust'], 'contact_details': {'location':'dhaka','phone':'1112345555555555'}}
patient1 = Patient(**patient_info)

update_patient_data(patient1)

