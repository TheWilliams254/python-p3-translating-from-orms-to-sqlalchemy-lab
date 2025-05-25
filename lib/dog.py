from models import Dog

def create_table(base, engine):
    """Create the database table for the Dog model."""
    base.metadata.create_all(engine)

def save(session, dog):
    """Save a Dog instance to the database."""
    session.add(dog)
    session.commit()

def get_all(session):
    """Return a list of all Dog instances in the database."""
    return session.query(Dog).all()

def find_by_name(session, name):
    """Return a Dog instance corresponding to the record with the given name."""
    return session.query(Dog).filter_by(name=name).first()

def find_by_id(session, id):
    """Return a Dog instance corresponding to the record with the given id."""
    return session.get(Dog, id)

def find_by_name_and_breed(session, name, breed):
    """Return a Dog instance corresponding to the record with the given name and breed."""
    return session.query(Dog).filter_by(name=name, breed=breed).first()

def update_breed(session, dog, breed):
    """Update the breed of the given Dog instance in the database."""
    dog.breed = breed
    session.commit()