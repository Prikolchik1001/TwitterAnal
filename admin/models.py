from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Integer, MetaData, String


class Base(DeclarativeBase):
    metadata = MetaData(
        naming_convention={
            "ix": "ix_%(column_0_label)s",
            "uq": "uq_%(table_name)s_%(column_0_name)s",
            "ck": "ck_%(table_name)s_%(constraint_name)s",
            "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
            "pk": "pk_%(table_name)s",
        }
    )


db = SQLAlchemy(model_class=Base)


class Admin(db.Model):

    __tablename__ = "admins"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, nullable=False, autoincrement=True
    )

    login: Mapped[str] = mapped_column(
        String, unique=True, nullable=False
    )

    password_hash: Mapped[str] = mapped_column(
        String, nullable=False
    )

    profile = relationship(
        'AdminProfile', back_populates='admin', uselist=False
    )


class AdminProfile(db.Model):
    __tablename__ = 'admin_profiles'

    admin_id: Mapped[int] = mapped_column(
        Integer, ForeignKey('admins.id'), unique=True, primary_key=True
    )

    name: Mapped[str] = mapped_column(String(50), nullable=False)
    surname: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)

    admin = relationship('Admin', back_populates='profile')
