from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base


engine = create_engine("postgresql://postgres:admin@localhost/user_table",
                        echo=True
                      )


Base = declarative_base()                      


SessionLocal = sessionmaker(bind=engine)

