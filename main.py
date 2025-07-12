# # from fastapi import FastAPI, Depends, HTTPException
# # from sqlalchemy.orm import Session
# # from fastapi.middleware.cors import CORSMiddleware
# # from typing import List
# # from fastapi.middleware.cors import CORSMiddleware

# # from database import SessionLocal, engine
# # import models
# # from models import contactForm, bookAppointment, Blog, Appointment
# # from schemas import (
# #     ContactUsCreate, ContactUs as ContactUsSchema,
# #     BookAppointmentCreate, BookAppointment as AppointmentSchema,
# #     AppointmentCreate, AppointmentResponse,
# #     BlogSchema
# # )

# # models.Base.metadata.create_all(bind=engine)

# # app = FastAPI()

# # app.add_middleware(
# #     CORSMiddleware,
# #     allow_origins=["http://localhost:5173"],  # ✅ This is correct
# #     allow_credentials=True,
# #     allow_methods=["*"],
# #     allow_headers=["*"],
# # )


# # def get_db():
# #     db = SessionLocal()
# #     try:
# #         yield db
# #     finally:
# #         db.close()

# # from fastapi import FastAPI,Depends, HTTPException
# # from sqlalchemy.orm import Session
# # from database import SessionLocal,engine
# # from models import contactForm, bookAppointment
# # from schemas import ContactUsCreate,ContactUs as ContactUsSchema
# # from schemas import BookAppointmentCreate, BookAppointment as AppointmentSchema
# # from schemas import AppointmentCreate, AppointmentResponse
# # from fastapi.middleware.cors import CORSMiddleware
# # from models import CounsellorProfile
# # from schemas import CounsellorProfileSchema
# # from typing import List
# # import models 
# # import httpx


# # app=FastAPI()

# # app.add_middleware(
# #     CORSMiddleware,
# #     allow_origins=["*"],
# #     allow_credentials=True,
# #     allow_methods=["*"],
# #     allow_headers=["*"],
# # )


# # def get_db():
# #     db = SessionLocal()
# #     try:
# #         yield db
# #     finally:
# #         db.close()


# from fastapi import FastAPI, Depends, HTTPException
# from sqlalchemy.orm import Session
# from fastapi.middleware.cors import CORSMiddleware
# from typing import List
# import httpx

# import models
# from database import SessionLocal, engine
# from models import contactForm, bookAppointment, CounsellorProfile
# from schemas import (
#     ContactUsCreate, ContactUs as ContactUsSchema,
#     BookAppointmentCreate, BookAppointment as AppointmentSchema,
#     AppointmentCreate, AppointmentResponse,
#     CounsellorProfileSchema
# )

# # Create all tables if not created yet
# models.Base.metadata.create_all(bind=engine)

# app = FastAPI()

# # Configure CORS middleware
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Allows all origins; can be restricted as needed
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Dependency to get DB session
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


#  # --- ROUTES ---
# # @app.get('/')
# # def home():
# #     return 'Hello World'


# # @app.post("/book-counselling-appointment/", response_model=AppointmentResponse)
# # async def book_counselling_appointment(appointment: AppointmentCreate, db: Session = Depends(get_db)):
# #     db_appointment = Appointment(**appointment.dict())
# #     db.add(db_appointment)
# #     db.commit()
# #     db.refresh(db_appointment)
# #     return db_appointment

# # @app.post("/contact-us/", response_model=ContactUsSchema)
# # async def create_contact_entry(data: ContactUsCreate, db: Session = Depends(get_db)):
# #     new_entry = contactForm(**data.dict())
# #     db.add(new_entry)
# #     db.commit()
# #     db.refresh(new_entry)
# #     return new_entry

# # @app.post("/book-appointment/", response_model=AppointmentSchema)
# # async def book_appointment(data: BookAppointmentCreate, db: Session = Depends(get_db)):
# #     new_entry = bookAppointment(**data.dict())
# #     db.add(new_entry)
# #     db.commit()
# #     db.refresh(new_entry)
# #     return new_entry

# # @app.get("/blog/{id}", response_model=BlogSchema)
# # def get_blog_by_id(id: int, db: Session = Depends(get_db)):
# #     blog = db.query(Blog).filter(Blog.id == id).first()
# #     if not blog:
# #         raise HTTPException(status_code=404, detail="Blog not found")
# #     return blog

# # @app.get("/blogs", response_model=List[BlogSchema])
# # def get_blogs(page: int = 1, db: Session = Depends(get_db)):
# #     # Limit to 9 blogs per page
# #     limit = 9
# #     offset = (page - 1) * limit
    
# #     # Query to get the blogs based on the page number
# #     blogs = db.query(Blog).order_by(Blog.id.asc()).offset(offset).limit(limit).all()
    
# #     return blogs

# # @app.get("/counsellors", response_model=List[CounsellorProfileSchema])
# # def get_all_counsellors(db: Session = Depends(get_db)):
# #     return db.query(CounsellorProfile).all()

# # # Route to get a specific counsellor
# # @app.get("/counsellors/{id}", response_model=CounsellorProfileSchema)
# # def get_counsellor(id: int, db: Session = Depends(get_db)):
# #     counsellor = db.query(CounsellorProfile).filter(CounsellorProfile.id == id).first()
# #     if not counsellor:
# #         raise HTTPException(status_code=404, detail="Counsellor not found")
# #     return counsellor

# # # Route to create contact entries (no changes)
# # @app.post("/contact-us/", response_model=ContactUsSchema)
# # async def create_contact_entry(data: ContactUsCreate, db: Session = Depends(get_db)):
# #     new_entry = contactForm(**data.dict())
# #     db.add(new_entry)
# #     db.commit()
# #     db.refresh(new_entry)
# #     return new_entry

# from fastapi import FastAPI,Depends, HTTPException
# from sqlalchemy.orm import Session
# from database import SessionLocal,engine
# from models import contactForm, bookAppointment
# from schemas import ContactUsCreate,ContactUs as ContactUsSchema
# from schemas import BookAppointmentCreate, BookAppointment as AppointmentSchema
# from schemas import AppointmentCreate, AppointmentResponse
# from fastapi.middleware.cors import CORSMiddleware
# from models import CounsellorProfile
# from schemas import CounsellorProfileSchema
# from typing import List
# import models 
# import httpx


# app=FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # Create the tables in the database (run this once)
# @app.on_event("startup")
# def create_tables():
#     models.Base.metadata.create_all(bind=engine)

# # Route to book an appointment
# @app.post("/book-counselling-appointment/", response_model=AppointmentResponse)
# async def book_appointment(appointment: AppointmentCreate, db: Session = Depends(get_db)):
#     db_appointment = models.Appointment(
#         name=appointment.name,
#         phone_num=appointment.phone_num,
#         email=appointment.email,
#         counsellorName=appointment.counsellorName,
#         address=appointment.address,
#         date=appointment.date,
#         time=appointment.time
#     )
#     db.add(db_appointment)
#     db.commit()
#     db.refresh(db_appointment)
#     return db_appointment



# @app.post("/book-appointment/",response_model=AppointmentSchema)
# async def book_appointment(data: BookAppointmentCreate, db: Session = Depends(get_db)):
#     new_entry = bookAppointment(**data.dict())
#     db.add(new_entry)
#     db.commit()
#     db.refresh(new_entry)
#     return new_entry

# # @app.post("/contact-us/", response_model=ContactUsSchema)
# # async def create_contact_entry(data: ContactUsCreate, db: Session = Depends(get_db)):
# #     new_entry = contactForm(**data.dict())
# #     db.add(new_entry)
# #     db.commit()
# #     db.refresh(new_entry)
# #     return new_entry

# # @app.get("/counsellors", response_model=List[CounsellorProfileSchema])
# # def get_all_counsellors(db: Session = Depends(get_db)):
# #     return db.query(CounsellorProfile).all()


# @app.get("/counsellors", response_model=List[CounsellorProfileSchema])
# def get_all_counsellors(db: Session = Depends(get_db)):
#     return db.query(CounsellorProfile).all()

# # Route to get a specific counsellor
# @app.get("/counsellors/{id}", response_model=CounsellorProfileSchema)
# def get_counsellor(id: int, db: Session = Depends(get_db)):
#     counsellor = db.query(CounsellorProfile).filter(CounsellorProfile.id == id).first()
#     if not counsellor:
#         raise HTTPException(status_code=404, detail="Counsellor not found")
#     return counsellor

# # Route to create contact entries (no changes)
# @app.post("/contact-us/", response_model=ContactUsSchema)
# async def create_contact_entry(data: ContactUsCreate, db: Session = Depends(get_db)):
#     new_entry = contactForm(**data.dict())
#     db.add(new_entry)
#     db.commit()
#     db.refresh(new_entry)
#     return new_entry










# the temporary code combining both codes



# from fastapi import FastAPI, Depends, HTTPException
# from sqlalchemy.orm import Session
# from fastapi.middleware.cors import CORSMiddleware
# from typing import List
# import httpx

# import models
# from database import SessionLocal, engine
# from models import contactForm, bookAppointment, CounsellorProfile
# from schemas import (
#     ContactUsCreate, ContactUs as ContactUsSchema,
#     BookAppointmentCreate, BookAppointment as AppointmentSchema,
#     AppointmentCreate, AppointmentResponse,
#     CounsellorProfileSchema
# )

# # Create all tables if not created yet
# models.Base.metadata.create_all(bind=engine)

# app = FastAPI()

# # Configure CORS middleware
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Allows all origins; can be restricted as needed
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Dependency to get DB session
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# --- main.py ---
from fastapi import FastAPI, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from urllib.parse import parse_qs
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from datetime import datetime
import os
import requests
# from fastapi import Request
# import crud

from dotenv import load_dotenv


import models
from database import SessionLocal, engine
from models import  BookAppointment, CounsellorProfile, Appointment, Blog
from schemas import (
    BookAppointmentCreate, BookAppointment as BookAppointmentSchema,
    AppointmentCreate, AppointmentResponse,
    BlogSchema, CounsellorProfileSchema
)



# Load environment variables
load_dotenv()
BITRIX_WEBHOOK = os.getenv("BITRIX24_WEBHOOK")
ASSIGNED_BY_ID = int(os.getenv("BITRIX24_ASSIGNED_USER_ID", 0))

if not BITRIX_WEBHOOK:
    raise RuntimeError("BITRIX24_WEBHOOK environment variable not set")

# --- FastAPI App ---
app = FastAPI()

# --- CORS Middleware ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://insighte-etbt.onrender.com"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- DB Dependency ---
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- Create Tables ---
@app.on_event("startup")
def create_tables():
    models.Base.metadata.create_all(bind=engine)

# --- Routes ---
@app.get("/")
def home():
    return {"message": "Hello World"}

@app.post("/book-counselling-appointment/", response_model=AppointmentResponse)
async def book_counselling_appointment(appointment: AppointmentCreate, db: Session = Depends(get_db)):
    db_appointment = Appointment(**appointment.dict())
    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment

@app.post("/trafft/webhook")
async def handle_trafft_webhook(request: Request, db: Session = Depends(get_db)):
    try:
        # Parse form data
        body_bytes = await request.body()
        form_data = parse_qs(body_bytes.decode())

        name = form_data.get("customerFullName", [""])[0]
        phone = form_data.get("customerPhone", [""])[0]
        email = form_data.get("customerEmail", [""])[0]
        counsellor_name = form_data.get("employeeFullName", [""])[0]
        address = form_data.get("locationAddress", [""])[0]
        date_time_str = form_data.get("appointmentStartDateTime", [""])[0]

        # Parse date and time from string like "31/05/2025 3:00 PM"
        appt_datetime = datetime.strptime(date_time_str, "%d/%m/%Y %I:%M %p")
        appt_date = appt_datetime.date()
        appt_time = appt_datetime.time()

        # Optional: Match counsellor in DB
        counsellor = db.query(CounsellorProfile).filter(
            CounsellorProfile.name.ilike(counsellor_name)
        ).first()

        new_appt = Appointment(
            name=name,
            phone_num=phone,
            email=email,
            counsellorName=counsellor_name,
            address=address,
            date=appt_date,
            time=appt_time,
            counsellor_id=counsellor.id if counsellor else None
        )

        db.add(new_appt)
        db.commit()
        db.refresh(new_appt)

        return {"message": "Appointment saved", "id": new_appt.id}

    except Exception as e:
        print("❌ Webhook Error:", str(e))
        raise HTTPException(status_code=500, detail=f"Webhook error: {str(e)}")
    

@app.post("/book-appointment/", response_model=BookAppointmentSchema)
async def book_appointment(data: BookAppointmentCreate, db: Session = Depends(get_db)):
    
    now = datetime.now()
    new_entry = BookAppointment(**data.dict())
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    

    formatted_datetime = now.isoformat()

    bitrix_payload = {
        "fields": {
            "TITLE": f"{data.service} Appointment for {data.name}",
            "NAME": data.name,
            "EMAIL": [{"VALUE": data.email, "VALUE_TYPE": "WORK"}],
            "PHONE": [{"VALUE": data.phone_num, "VALUE_TYPE": "WORK"}],
            "SOURCE_ID": "WEB",
            "UF_CRM_1738734261": formatted_datetime,
            "UF_CRM_1745846188": data.service,
            "UF_CRM_1738734347": data.address,
            "ASSIGNED_BY_ID": ASSIGNED_BY_ID
        },
        "params": {"REGISTER_SONET_EVENT": "Y"}
    }

    try:
        response = requests.post(BITRIX_WEBHOOK, json=bitrix_payload)
        print("Bitrix Response Status Code:", response.status_code)
        print("Bitrix Response Body:", response.text)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Bitrix24 Error: {e}")

    return new_entry

# @app.post("/contact-us/", response_model=ContactUs)
# async def create_contact_entry(data: ContactUsCreate, db: Session = Depends(get_db)):
#     new_entry = ContactForm(**data.dict())
#     db.add(new_entry)
#     db.commit()
#     db.refresh(new_entry)
#     return new_entry

@app.get("/counsellors", response_model=List[CounsellorProfileSchema])
def get_all_counsellors(db: Session = Depends(get_db)):
    return db.query(CounsellorProfile).all()

# @app.get("/counsellors", response_model=List[CounsellorProfileSchema])
# def get_all_counsellors(db: Session = Depends(get_db)):
#     return crud.get_all_counsellors(db)


@app.get("/counsellors/{id}", response_model=CounsellorProfileSchema)
def get_counsellor(id: int, db: Session = Depends(get_db)):
    counsellor = db.query(CounsellorProfile).filter(CounsellorProfile.id == id).first()
    if not counsellor:
        raise HTTPException(status_code=404, detail="Counsellor not found")
    return counsellor

@app.get("/blog/{id}", response_model=BlogSchema)
def get_blog_by_id(id: int, db: Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    return blog

@app.get("/blogs", response_model=List[BlogSchema])
def get_blogs(page: int = 1, db: Session = Depends(get_db)):
    limit = 9
    offset = (page - 1) * limit
    blogs = db.query(Blog).order_by(Blog.id.asc()).offset(offset).limit(limit).all()
    return blogs


@app.get("/test-bitrix")
async def test_bitrix():
    try:
        response = requests.get(f"{BITRIX_WEBHOOK}/crm.lead.list.json?select[]=ID&select[]=TITLE", timeout=10)
        return {
            "status": "success",
            "bitrix_response": response.json(),
            "webhook_url": BITRIX_WEBHOOK
        }
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "webhook_url": BITRIX_WEBHOOK
        }
        
        
    
# @app.post("/trafft-webhook")
# async def handle_trafft_webhook(request: Request, db: Session = Depends(get_db)):
#     payload = await request.json()
    
#     # Example payload fields — adjust based on Trafft's actual webhook structure
#     staff_id = payload.get("staff_id")
#     service_id = payload.get("service_id")
#     staff_name = payload.get("staff_name")

#     if not staff_id or not service_id or not staff_name:
#         raise HTTPException(status_code=400, detail="Missing required data")

#     # Generate booking URL
#     booking_url = f"https://insighte.trafft.com/booking/{staff_name.lower().replace(' ', '')}?staff_id={staff_id}"

#     # Update the existing counsellor (match by name or use another key if needed)
#     # counsellor = db.query(CounsellorProfile).filter(CounsellorProfile.name.ilike(staff_name)).first()

#     # if not counsellor:
#     #     raise HTTPException(status_code=404, detail="Counsellor not found in DB")

#     # counsellor.booking_url = booking_url
#     # counsellor.trafft_staff_id = staff_id
#     # counsellor.trafft_service_id = service_id
#     # db.commit()
#     counsellor = crud.update_booking_info(
#     db=db,
#     name=staff_name,
#     staff_id=staff_id,
#     service_id=service_id,
#     booking_url=booking_url
# )

#     if not counsellor:
#         raise HTTPException(status_code=404, detail="Counsellor not found in DB")

#     return {"status": "updated", "booking_url": booking_url}
