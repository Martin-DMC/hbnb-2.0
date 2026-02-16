from app.infrastructure.persistence.sql_Achemy.sql_user import SQLAlchemyUserRepository
from app.core.security import verify_password, create_access_token, get_password_hash

class LoginUser:
    def __init__(self, user_repo: SQLAlchemyUserRepository):
        self.user_repo = user_repo

    def execute(self, email: str, password: str):
        user = self.user_repo.get_by_email(email=email)

        if not user or not verify_password(password, user.password):
            return None

        token = create_access_token(subject=user.email)

        return {
            "access_token": token,
            "token_type": "bearer",
            "user": {
                "email": user.email,
                "id": user.id
            }
        }