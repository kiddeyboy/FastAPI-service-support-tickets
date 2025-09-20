from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from database import SessionLocal, engine, Base
from models import SupportTicket
from schemas import UnifiedRequest, TicketResponse
from logic import map_to_ticket_fields, get_product_info

app = FastAPI()

# Create tables
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Dependency to get DB session
async def get_db():
    async with SessionLocal() as session:
        yield session

@app.post("/process")
async def process(request: UnifiedRequest, db: AsyncSession = Depends(get_db)):
    data = request.data

    if "issue" in data:
        ticket_data = map_to_ticket_fields(data)
        ticket = SupportTicket(**ticket_data)
        db.add(ticket)
        await db.commit()
        await db.refresh(ticket)
        return {
            "type": "support_ticket",
            "ticket": {
                "id": ticket.id,
                "user_name": ticket.user_name,
                "email": ticket.email,
                "issue_type": ticket.issue_type,
                "description": ticket.description
            },
            "message": "Support ticket created and saved to database."
        }

    elif "product" in data and "question" in data:
        answer = get_product_info(data)
        return {
            "type": "product_info",
            "answer": answer
        }

    raise HTTPException(status_code=400, detail="Unsupported request format.")
