from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError



class Base(DeclarativeBase):
   pass

class Storage:

    def store_all(self, engine, projects):
        with Session(engine) as session:
            for project in projects:
                session.add(project)
                try:
                    session.commit()
                except IntegrityError:
                    session.rollback()

    def read_all(self):
        pass
