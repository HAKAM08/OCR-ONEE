from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate
from app.core.security import (
    hash_password,
    verify_password,
    create_access_token
)


class AuthService:

    @staticmethod
    def register(db: Session, user_data: UserCreate):

        existing_user = UserRepository.get_by_email(
            db,
            user_data.email
        )

        if existing_user:
            raise ValueError("Cet email est déjà utilisé.")

        user = User(
            fullname=user_data.fullname,
            email=user_data.email,
            password=hash_password(user_data.password),
            role="USER"
        )

        return UserRepository.create(db, user)

    @staticmethod
    def login(db: Session, email: str, password: str):

        user = UserRepository.get_by_email(db, email)

        if not user:
            raise ValueError("Email ou mot de passe incorrect.")

        if not verify_password(password, user.password):
            raise ValueError("Email ou mot de passe incorrect.")

        token = create_access_token(
            {
                "sub": str(user.id),
                "email": user.email,
                "role": user.role
            }
        )

        return token