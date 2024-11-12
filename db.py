from sqlalchemy import String, create_engine
from sqlalchemy.orm import sessionmaker, Mapped, mapped_column, DeclarativeBase



engine = create_engine("sqlite:///club_Aizen.db", echo=True)
Session = sessionmaker(bind=engine)




class Base(DeclarativeBase):
    pass





class Club(Base):
    __tablename__ = "club"

    id: Mapped[int] = mapped_column(primary_key=True)
    ceo: Mapped[str] = mapped_column(String(100))
    club: Mapped[str] = mapped_column(String())


def create_bd():
    Base.metadata.create_all(bind=engine)