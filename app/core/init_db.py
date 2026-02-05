from app.core.database import engine, Base
from app.models.automation import Automation

def init_db():
    Base.metadata.create_all(bind=engine)
    print(f"✅ Tabelas criadas com sucesso")

if __name__ == "__main__":
    init_db()