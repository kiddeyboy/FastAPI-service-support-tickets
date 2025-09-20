from sqlalchemy import Column, Integer, String
from database import Base

class SupportTicket(Base):
    __tablename__ = "support_tickets"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String)
    email = Column(String)
    issue_type = Column(String)
    description = Column(String)
