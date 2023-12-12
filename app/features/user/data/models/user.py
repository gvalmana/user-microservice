from typing import TYPE_CHECKING

from sqlalchemy import Column, Boolean, String
from sqlalchemy.orm import relationship, Mapped

from app.features.user.domain.entities.user_query_model import UserReadModel
from app.core.models.mysql.models import Base
from app.features.user.domain.entities.user_entity import UserEntity

if TYPE_CHECKING:
    from app.features.task.data.models.task import Task


class User(Base):
    __tablename__ = 'users'

    email: Mapped[str] | str = Column(String, unique=True, index=True)
    password: Mapped[str] | str = Column(String)
    is_active: Mapped[bool] | bool | None = Column(Boolean, default=True)

    def to_entity(self) -> UserEntity:
        return UserEntity(
            uid=self.uid,
            email=self.email,
            password=self.password,
            is_active=self.is_active,
            created_at=self.created_at,
            updated_at=self.updated_at,
            is_deleted=self.is_deleted
        )

    def to_dict(self):
        return {
            'uid': self.uid,
            'email': self.email,
            'password': self.password,
            'is_active': self.is_active,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'is_deleted': self.is_deleted,
        }

    def to_read_model(self) -> UserReadModel:
        return UserReadModel(
            uid=self.uid,
            email=self.email,
            password=self.password,
            is_active=self.is_active,
            is_deleted=self.is_deleted,
            created_at=self.created_at,
            updated_at=self.updated_at
        )

    @staticmethod
    def from_entity(user: UserEntity) -> 'User':
        return User(
            uid=user.uid,
            email=user.email,
            password=user.password,
            is_active=user.is_active,
            created_at=user.created_at,
            updated_at=user.updated_at,
            is_deleted=user.is_deleted
        )
