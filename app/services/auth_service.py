from sqlalchemy.orm import Session

from app.models.user import User
from app.core.security import (
    hash_password,
    verify_password,
    create_access_token
)


# Create new user
def create_user(
    db: Session,
    username: str,
    email: str,
    password: str
):

    # Check existing user
    existing_user = (
        db.query(User)
        .filter(User.email == email)
        .first()
    )

    if existing_user:
        return None


    # Hash password before storing
    hashed_password = hash_password(password)


    user = User(
        username=username,
        email=email,
        hashed_password=hashed_password
    )


    db.add(user)
    db.commit()
    db.refresh(user)

    return user



# Authenticate user
def authenticate_user(
    db: Session,
    email: str,
    password: str
):

    user = (
        db.query(User)
        .filter(User.email == email)
        .first()
    )


    if not user:
        return None


    # Verify entered password
    if not verify_password(
        password,
        user.hashed_password
    ):
        return None


    return user



# Generate login token
def login_user(user: User):

    token = create_access_token(
        {
            "sub": str(user.id),
            "email": user.email
        }
    )

    return token