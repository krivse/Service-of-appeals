from sqlalchemy import Column, Integer, String, BigInteger, DateTime
from sqlalchemy.sql import func

from database import Base


class Appeals(Base):
    __tablename__ = 'appeals'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    middle_name = Column(String)
    phone_number = Column(BigInteger)
    appeal = Column(String, index=True)
    date = Column(DateTime(timezone=True), server_default=func.now())
