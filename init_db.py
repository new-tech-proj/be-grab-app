from app.database import engine, metadata
from app.services import create_database
from app.models import User, Post

def main():
    metadata.reflect(bind=engine)
    tables = metadata.sorted_tables

    if tables:
        print("[WARNING] Check the database exists tables/data. You may want to delete? (Y/n):", end=' ')
        choose = input()
        if choose in ["y", "Y"]:
            metadata.drop_all(tables=[
                User.__table__,
                Post.__table__
            ])
            print("[INFO] Database deleted all tables!")

            create_database()
            print("[INFO] Database initialized all tables!")
        else:
            print("[INFO] Database exists tables, cannot be initialized!")
    else:
        create_database()
        print("[INFO] Database initialized all tables!")


if __name__ == "__main__":
    main()