# # import os
# # from sqlalchemy import create_engine
# # from sqlalchemy.ext.declarative import declarative_base
# # from sqlalchemy.orm import sessionmaker
# # from dotenv import load_dotenv

# # # Load environment variables from .env
# # load_dotenv()

# # # Get the database URL from the environment variable
# # DATABASE_URL = os.getenv("DATABASE_URL")
# # print(DATABASE_URL)
# # # Create the engine with SSL mode argument
# # engine = create_engine(DATABASE_URL, connect_args={"sslmode": "require"})

# # # SessionLocal for handling database sessions
# # SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # # Base class for declarative models
# # Base = declarative_base()
# import os
# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# from dotenv import load_dotenv

# # Load environment variables from .env
# load_dotenv()

# # Get the database URL
# DATABASE_URL = os.getenv("DATABASE_URL")

# # Create the engine
# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()




# final code

import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL not set in environment.")

# Create SQLAlchemy engine
# For PostgreSQL with Neon, SSL mode is often required
engine = create_engine(
    DATABASE_URL,
    connect_args={"sslmode": "require"}  # Only for PostgreSQL/Neon SSL connection
)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for declarative models
Base = declarative_base()
