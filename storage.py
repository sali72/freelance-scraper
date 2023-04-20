from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session


class Base(DeclarativeBase):
   pass

class Storage:

    def store_all(self, engine, projects):
        with Session(engine) as session:
            session.add_all(projects)
            session.commit()

    def read_all(self):
        pass
