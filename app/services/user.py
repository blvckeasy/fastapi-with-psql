from models import User, Base
from sqlalchemy.orm import Session
from database import engine, get_db

class UserService:
    # Baza yaratish (agar mavjud bo'lmasa)
    Base.metadata.create_all(bind=engine)
    db = next(get_db())  # Sessiya yaratish


    # Foydalanuvchi qo'shish
    def create_user(self, name: str, email: str):
        newUser = User(name=name, email=email)
        self.db.add(newUser)
        self.db.commit()
        self.db.refresh(newUser)
        return newUser


    # Foydalanuvchi olish
    def get_user(self, user_id: int):
        return self.db.query(User).filter(User.id == user_id).first()


    # Foydalanuvchilar ro'yxatini olish
    def get_users(self, page: int = 1, limit: int = 10):
        skip = (page - 1) * limit

        return self.db.query(User).offset(skip).limit(limit).all()

     # Foydalanuvchi ma'lumotlarini yangilash
    def update_user(self, user_id: int, name: str = None, email: str = None):
        user = self.db.query(User).filter(User.id == user_id).first()
        if not user:
            return None  # Foydalanuvchi topilmadi

        if name:
            user.name = name
        if email:
            user.email = email

        self.db.commit()
        self.db.refresh(user)
        return user


    # Foydalanuvchini o'chirish
    def delete_user(self, user_id: int):
        user = self.db.query(User).filter(User.id == user_id).first()
        if not user:
            return None  # Foydalanuvchi topilmadi

        self.db.delete(user)
        self.db.commit()
        return user