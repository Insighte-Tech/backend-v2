# # from pydantic import BaseModel
# # from datetime import date, time ,datetime

# # from typing import Optional



# # class AppointmentBase(BaseModel):
# #     name: str
# #     phone_num: str
# #     email: str
# #     # counsellorId: int
# #     counsellorName: str
# #     address: str
# #     date: date
# #     time: time

# #     class Config:
# #         orm_mode = True

# # class AppointmentCreate(AppointmentBase):
# #     pass

# # class AppointmentResponse(AppointmentBase):
# #     id: int

# #     class Config:
# #         orm_mode = True


# # class ContactUsCreate(BaseModel):
# #     name: str
# #     email: str
# #     phone: str
# #     message: str

# # class ContactUs(ContactUsCreate):
# #     id: int
# #     class Config:
# #         orm_mode = True

# # class BookAppointmentCreate(BaseModel):
# #     name: str
# #     phone_num: str
# #     email: str
# #     service: str
# #     address: str

# # class BookAppointment(BookAppointmentCreate):
# #     id: int
# #     class Config:
# #         orm_mode = True


# # class BlogSchema(BaseModel):
# #     id: int
# #     name: str
# #     slug: Optional[str] = None
# #     collection_id: Optional[str] = None
# #     item_id: Optional[str] = None
# #     created_on: datetime
# #     updated_on: datetime
# #     published_on: datetime
# #     main_image: Optional[str] = None
# #     blog_post: str
# #     post_description: Optional[str] = None
# #     author_name: Optional[str] = None
# #     author_image: Optional[str] = None

# #     class Config:
# #         orm_mode = True



# from pydantic import BaseModel
# from typing import List, Optional
# from datetime import date, time

# # AppointmentBase – no changes needed
# class AppointmentBase(BaseModel):
#     name: str
#     phone_num: str
#     email: str
#     counsellorName: str
#     address: str
#     date: date
#     time: time

#     class Config:
#         orm_mode = True

# class AppointmentCreate(AppointmentBase):
#     pass

# class AppointmentResponse(AppointmentBase):
#     id: int

#     class Config:
#         orm_mode = True

# # Contact Us – already good
# class ContactUsCreate(BaseModel):
#     name: str
#     email: str
#     phone: str
#     message: str

# class ContactUs(ContactUsCreate):
#     id: int

#     class Config:
#         orm_mode = True

# # ✅ Updated BookAppointmentCreate to match booking logic
# class BookAppointmentCreate(BaseModel):
#     name: str
#     phone_num: str
#     email: str
#     address: Optional[str]
#     date: date
#     time: time
#     counsellorId: int
#     counsellorName: str

# # ✅ Updated BookAppointment (response model)
# class BookAppointment(BookAppointmentCreate):
#     id: int
#     calendar_event_id: Optional[str] = None

#     class Config:
#         orm_mode = True

# # ✅ Minor change: id should match CounsellorProfile.id from the DB
# class CounsellorProfileSchema(BaseModel):
#     id: int
#     name: str
#     qualifications: Optional[List[str]] = []
#     experience: Optional[str]
#     short_bio: Optional[str]
#     long_bio: Optional[str]
#     concerns_addressed: Optional[List[str]] = []
#     languages: Optional[List[str]] = []
#     hobbies: Optional[str]
#     linkedin: Optional[str]
#     image: Optional[str]

#     class Config:
#         orm_mode = True
        
        
        
        
# combined code

from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date, time, datetime

# --- Book Counselling Appointment ---
class AppointmentBase(BaseModel):
    name: str
    phone_num: str
    email: str
    counsellorName: str
    address: str
    date: date
    time: time 
    counsellor_id: int 

    # model_config = ConfigDict(from_attributes=True)
    class Config:
        orm_mode = True

class AppointmentCreate(AppointmentBase):
    pass

class AppointmentResponse(AppointmentBase):
    id: int


# # --- Contact Us ---
# class ContactUsCreate(BaseModel):
#     name: str
#     email: str
#     phone: str
#     message: str

# class ContactUs(BaseModel):
#     id: int
#     name: str
#     email: str
#     phone: str
#     message: str

#     # model_config = ConfigDict(from_attributes=True)
#     class Config:
#         orm_mode = True


# --- Book Appointment ---
class BookAppointmentCreate(BaseModel):
    name: str
    phone_num: str
    email: str
    address: Optional[str]
    service: str
    
class BookAppointment(BaseModel):
    id: int
    name: str
    phone_num: str
    email: str
    address: Optional[str]
    service: str
    date_of_contact_to_insighte: datetime 
    

    # model_config = ConfigDict(from_attributes=True)
    class Config:
        orm_mode = True
        


# --- Counsellor Profile ---
class CounsellorProfileSchema(BaseModel):
    id: int
    name: str
    qualifications: Optional[List[str]] = []
    experience: Optional[str] = None
    short_bio: Optional[str] = None
    long_bio: Optional[str] = None
    concerns_addressed: Optional[List[str]] = []
    languages: Optional[List[str]] = []
    hobbies: Optional[str] = None
    linkedin: Optional[str] = None
    image: Optional[str] = None

    booking_url: Optional[str]

# # ✅ Trafft booking integration fields
#     booking_url: Optional[str] = None
#     trafft_staff_id: Optional[str] = None
#     trafft_service_id: Optional[str] = None
    # model_config = ConfigDict(from_attributes=True)
    class Config:
        orm_mode = True

# --- Blog ---
class BlogSchema(BaseModel):
    id: int
    name: str
    slug: Optional[str] = None
    collection_id: Optional[str] = None
    item_id: Optional[str] = None
    created_on: datetime
    updated_on: datetime
    published_on: datetime
    main_image: Optional[str] = None
    blog_post: str
    post_description: Optional[str] = None
    author_name: Optional[str] = None
    author_image: Optional[str] = None

    # model_config = ConfigDict(from_attributes=True)
    class Config:
        orm_mode = True
