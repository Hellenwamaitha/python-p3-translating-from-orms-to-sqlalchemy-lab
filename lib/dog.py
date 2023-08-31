from models import Dog

def create_table(base, engine):
       
       base.create_table(engine) 
    

def save(session, dog):
    session.add(dog)
    session.commit()
    

def get_all(session):
    session.get_all()
    

def find_by_name(session, name):
   Dog = session.find_item_by_name(name)
   return Dog
    

def find_by_id(session, id):
   dog = session.find_item_by_name(id)
   return dog

def find_by_name_and_breed(session, name, breed):
    for dog in session.dog: 
        if dog.name == name and dog.breed == breed:
            return dog  
    return None  
   

def update_breed(session, dog, breed):
    for item in session.items:  
        if item == dog:
            item.breed = breed  
    return False  

                                           
   