from sqlalchemy.orm import DeclarativeBase



class Base(DeclarativeBase):
   pass

class Storage:

    def store_all(self, projects):
        pass

    def read_all(self):
        pass
