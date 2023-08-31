from models import Dog

def create_table(base, engine):
       
       base.create_table(engine) 
    

def save(session, dog):
    session.add(dog)
    session.commit()
    

def get_all(session):
    pass

def find_by_name(session, name):
    pass

def find_by_id(session, id):
    pass

def find_by_name_and_breed(session, name, breed):
    pass

def update_breed(session, dog, breed):
    table.update().where(conditions).values(SET expression
    students.update().where(students.c.lastname == 'Khanna').values(lastname = 'Kapoor')                                        
    pass