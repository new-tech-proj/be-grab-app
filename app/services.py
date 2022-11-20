from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from app.database import Base, engine
from app.models import User, Post


def create_database():
    return Base.metadata.create_all(bind=engine)


def create_user(session: Session, user: User) -> User:
    try:
        existing_user = session.query(User) \
            .filter(User.username == user.username) \
            .first()
        if not existing_user:
            session.add(user)
            session.commit()
            print(f"[INFO] Created user: {user}")
        else:
            print(f"[WARNING] Users already exists in database: {existing_user}")
        return session.query(User).filter(User.username == user.username).first()

    except IntegrityError as e:
        print("[ERROR] Detail:", e.orig)
        raise e.orig

    except SQLAlchemyError as e:
        print("[ERROR] Unexpected error when creating user:", e)
        raise e


def create_post(session: Session, post: Post) -> Post:
    try:
        existing_post = session.query(Post) \
            .filter(Post.title == post.title and Post.author_id == post.author_id) \
            .first()
        if not existing_post:
            session.add(post)
            session.commit()
            print(f"[INFO] Created post {post} published by user {post.author.username}")
        return session.query(Post) \
            .filter(Post.title == post.title and Post.author_id == post.author_id) \
            .first()

    except IntegrityError as e:
        print("[ERROR] Detail:", e.orig)
        raise e.orig

    except SQLAlchemyError as e:
        print("[ERROR] Unexpected error when creating user:", e)
        raise e