from backend.app.database.session import Base, engine
from backend.app.models.ticket import Ticket


def init_db() -> None:
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully.")
