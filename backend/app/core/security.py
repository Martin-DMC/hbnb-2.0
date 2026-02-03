from passlib.context import CryptContext

myctx = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:

    return myctx.verify(plain_password, hashed_password)