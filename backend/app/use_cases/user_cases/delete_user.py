from app.domain.interfaces import UserRepository

class DeleteUser:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def execute(self, user_id: str) -> bool:
        # Aquí podrías meter lógica de "Solo el admin borra" o algo así
        return self.user_repo.delete(user_id)