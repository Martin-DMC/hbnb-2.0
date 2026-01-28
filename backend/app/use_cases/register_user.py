from app.domain.models.user import User
from app.domain.repositories import UserRepository

class RegisterUser:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def execute(self, email: str, password: str, first_name: str, last_name: str) -> User:
        existing_user = self.user_repo.get_by_email(email)
        if existing_user:
            raise ValueError("El email ya está registrado")

        new_user = User(
            email=email,
            password=password, 
            first_name=first_name,
            last_name=last_name
        )

        self.user_repo.add(new_user)
        
        return new_user