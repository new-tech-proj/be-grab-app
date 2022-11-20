import os

PGUSER = os.getenv("PGUSER", default="postgres")
PGPASSWORD = os.getenv("PGPASSWORD", default="Trung2001")
PGHOST = os.getenv("PGHOST", default="localhost")
PGPORT = os.getenv("PGPORT", default="5432")
PGDATABASE = os.getenv("PGDATABASE", default="grab")
# DATABASE_URL = f"postgresql://{PGUSER}:{PGPASSWORD}@{PGHOST}:{PGPORT}/{PGDATABASE}"
DATABASE_URL = "postgresql://postgres:L6SgAq2wu1jkYr5SqjIl@containers-us-west-106.railway.app:6622/railway"