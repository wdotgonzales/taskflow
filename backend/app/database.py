import os
from typing import Annotated
from dotenv import load_dotenv
from fastapi import Depends
from sqlmodel import create_engine, Session

# Look for the .env file exactly one directory up in /backend/
# This handles running the app from either the root or /backend/ directory safely.
dotenv_path = os.path.join(os.path.dirname(__file__), "..", ".env")
load_dotenv(dotenv_path=dotenv_path)

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL environment variable is missing!")

# Build the engine from your DATABASE_URL
engine = create_engine(DATABASE_URL, echo=False)

#nCreate the get_session generator function using yield
def get_session():
    with Session(engine) as session:
        yield session

# SessionDep shortcut using Annotated and Depends
SessionDep = Annotated[Session, Depends(get_session)]
