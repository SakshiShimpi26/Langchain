# In pydantic we get type validation
# If type of value does not match a error is thrown in Pydantic.
# In TypedDict type mismatched was considered and no error was thrown but in pydantic error is thrown.

# ============================== CODE-1 =================================================
# from pydantic import BaseModel, EmailStr, Field
# from typing import Optional

# class Student(BaseModel):
#     name: str 

# new_student = {'name':'Sakshi'}
# # new_student = {'name':22} # If here we pass name as a int value a error will be thrown

# student = Student(**new_student)

# student_dict = dict(student)

# print(student_dict['name'])
# print(type(student_dict))


# ============================== CODE-2 =================================================
from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):

    name: str = 'Sakshu'
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10, default=5, description='A decimal value representing the cgpa of the student')


new_student = {'age':'22', 'email':'sakshi@gmail.com'}

student = Student(**new_student)

student_dict = dict(student)

print(student_dict['age'])