from app.domain.models.user import User
from app.domain.interfaces import UserRepository
from app.core.security import myctx

class UpdateUser:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def execute(self, user_id: str, data: dict) -> User:
        user = self.user_repo.get_by_id(user_id)
        if not user:
            raise ValueError("User_not_found")

    # doble verificacion para evitar problemas con el valor None en la database
    # de esta manera podemos modificar campos unicos si queremos.
        if "first_name" in data and data["first_name"] is not None:
            user.first_name = data["first_name"]
        if "last_name" in data and data["last_name"] is not None:
            user.last_name = data["last_name"]
        if "email" in data and data["email"] is not None:
            user.email = data["email"]
        if "password" in data and data["password"] is not None:
            user.password =  myctx.hash(data["password"])
        
        return self.user_repo.update_user(user)

