# # from sqlalchemy import Column, Integer, String, Date, Time, Text
# # from database import Base
# # from datetime import datetime


# # class bookAppointment(Base):
# #     __tablename__ = 'book_appointment'
# #     id = Column(Integer,primary_key=True,index=True)
# #     name = Column(Text, index=True)
# #     phone_num = Column(Text, index=True)
# #     email = Column(Text, index=True)
# #     service = Column(Text, index=True)
# #     address = Column(Text, index=True)

# # class contactForm(Base):
# #     __tablename__ = 'contact_form'
# #     id = Column(Integer,primary_key=True,index=True)
# #     name = Column(Text, index=True)
# #     email = Column(Text, index=True)
# #     phone = Column(Text, index=True)
# #     message = Column(Text, index=True)

# # class Appointment(Base):
# #     __tablename__ = 'appointments'

# #     id = Column(Integer, primary_key=True, index=True)
# #     name = Column(String, index=True)
# #     phone_num = Column(String)
# #     email = Column(String)
# #     # counsellorId = Column(Integer)
# #     counsellorName = Column(String)
# #     address = Column(String)
# #     date = Column(Date)
# #     time = Column(Time)


# # from sqlalchemy import Column, Integer, String, Text, DateTime
# # from datetime import datetime
# # class Blog(Base):
# #     __tablename__ = "blogs"

# #     id = Column(Integer, primary_key=True, index=True)  # serial
# #     name = Column(Text, nullable=False)  # blog title
# #     slug = Column(Text, nullable=True)
# #     collection_id = Column(Text, nullable=True)
# #     item_id = Column(Text, nullable=True)
# #     created_on = Column(DateTime, default=datetime.utcnow)
# #     updated_on = Column(DateTime, default=datetime.utcnow)
# #     published_on = Column(DateTime, default=datetime.utcnow)
# #     main_image = Column(Text, nullable=True)
# #     blog_post = Column(Text, nullable=False)  # full blog content
# #     post_description = Column(Text, nullable=True)
# #     author_name = Column(Text, nullable=True)
# #     author_image = Column(Text, nullable=True)

# from sqlalchemy import Column, Integer, String, Date, Time, Text, ARRAY
# from database import Base

# # Updated bookAppointment model
# class bookAppointment(Base):
#     _tablename_ = 'book_appointment'
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(Text, index=True)
#     phone_num = Column(Text, index=True)
#     email = Column(Text, index=True)
#     service = Column(Text, index=True)
#     address = Column(Text, index=True)
#     date = Column(Date)
#     time = Column(Time)
#     counsellorId = Column(Integer)  # Added counsellorId to match the input in API
#     counsellorName = Column(String)  # Added counsellorName to match the input in API

# # contactForm model – no changes needed
# class contactForm(Base):
#     _tablename_ = 'contact_form'
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(Text, index=True)
#     email = Column(Text, index=True)
#     phone = Column(Text, index=True)
#     message = Column(Text, index=True)

# # Updated Appointment model
# class Appointment(Base):
#     _tablename_ = 'appointments'

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     phone_num = Column(String)
#     email = Column(String)
#     counsellorName = Column(String)  # counsellorName is now present, instead of counsellorId
#     address = Column(String)
#     date = Column(Date)
#     time = Column(Time)
#     calendar_event_id = Column(String, nullable=True)  # Added for calendar integration (Google Calendar, etc.)

# # Updated CounsellorProfile model
# class CounsellorProfile(Base):
#     _tablename_ = "counsellors_profile"

#     id = Column(Integer, primary_key=True, index=True)  # Renamed counsellor_id → id for consistency
#     name = Column(Text, nullable=False)
#     qualifications = Column(ARRAY(Text), nullable=True)
#     experience = Column(Text, nullable=True)
#     short_bio = Column(Text, nullable=True)
#     long_bio = Column(Text, nullable=True)
#     concerns_addressed = Column(ARRAY(Text), nullable=True)
#     languages = Column(ARRAY(Text), nullable=True)
#     hobbies = Column(Text, nullable=True)
#     linkedin = Column(Text, nullable=True)
#     image = Column(Text, nullable=True)
    
    
    
# final merged code

from sqlalchemy import Column, Integer, String, Date, Time, Text, DateTime, ARRAY, ForeignKey
from datetime import datetime
from database import Base

# --- Book Appointment ---
class BookAppointment(Base):
    __tablename__ = 'book_appointment'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text, index=True)
    phone_num = Column(Text, index=True)
    email = Column(Text, index=True)
    address = Column(Text, index=True)
    service = Column(Text, nullable=True)
    date_of_contact_to_insighte = Column(DateTime, default=datetime.now)


# --- Contact Form ---
class ContactForm(Base):
    __tablename__ = 'contact_form'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text, index=True)
    email = Column(Text, index=True)
    phone = Column(Text, index=True)
    message = Column(Text, index=True)

# --- Appointment
class Appointment(Base):
    __tablename__ = 'appointments'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    phone_num = Column(String)
    email = Column(String)
    counsellorName = Column(String)
    address = Column(String)
    date = Column(Date)
    time = Column(Time)
    counsellor_id = Column(Integer, ForeignKey("counsellors_profile.id"), nullable=True) 
    
# --- Counsellor Profile ---
class CounsellorProfile(Base):
    __tablename__ = "counsellors_profile"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text, nullable=False)
    qualifications = Column(ARRAY(Text), nullable=True)
    experience = Column(Text, nullable=True)
    short_bio = Column(Text, nullable=True)
    long_bio = Column(Text, nullable=True)
    concerns_addressed = Column(ARRAY(Text), nullable=True)
    languages = Column(ARRAY(Text), nullable=True)
    hobbies = Column(Text, nullable=True)
    linkedin = Column(Text, nullable=True)
    image = Column(Text, nullable=True)
    booking_url = Column(String, nullable=True)

# --- Blog ---
class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text, nullable=False)  # blog title
    slug = Column(Text, nullable=True)
    collection_id = Column(Text, nullable=True)
    item_id = Column(Text, nullable=True)
    created_on = Column(DateTime, default=datetime.utcnow)
    updated_on = Column(DateTime, default=datetime.utcnow)
    published_on = Column(DateTime, default=datetime.utcnow)
    main_image = Column(Text, nullable=True)
    blog_post = Column(Text, nullable=False)  # full blog content
    post_description = Column(Text, nullable=True)
    author_name = Column(Text, nullable=True)
    author_image = Column(Text, nullable=True)

