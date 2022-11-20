import os
from dotenv import load_dotenv

load_dotenv(".env")

PGUSER = os.getenv("PGUSER", default="postgres")
PGPASSWORD = os.getenv("PGPASSWORD", default="Trung2001")
PGHOST = os.getenv("PGHOST", default="localhost")
PGPORT = os.getenv("PGPORT", default="5432")
PGDATABASE = os.getenv("PGDATABASE", default="grab")
DATABASE_URL = f"postgresql://{PGUSER}:{PGPASSWORD}@{PGHOST}:{PGPORT}/{PGDATABASE}"