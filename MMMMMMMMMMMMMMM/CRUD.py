from peewee import *
from Models import Patient, Appointment, Medicine, Prescription

db = SqliteDatabase('personnel.db')

################ MODEL ############################

class Personnel(Model):
    per_ID = CharField(max_length=16, unique=True)
    name = CharField(max_length=25)
    sector = CharField()
    user_id = CharField(max_length=10, unique=True)
    user_pass = CharField(max_length=16)
    
    class Meta:
        database = db



####################################################
personnel = [
{'per_ID': 'tama007',
 'name': 'tama tamamachan',
 'sector': 'ssssss',
 'user_id': 'tamainwza',
 'user_pass': 'asdf1234'}
]


def initialize():
    """Create the database and the table if they don't exist."""
    db.connect()
    db.create_tables(
        [Personnel, Patient, Appointment, Medicine, Prescription],
        safe=True
        )



def add_personnel():
    for person in personnel:
        try:
            Personnel.create(
                per_ID=person['per_ID'],
                name=person['name'],
                sector=person['sector'],
                user_id=person['user_id'],
                user_pass=person['user_pass']
                )
                             
        except IntegrityError:
            #TODO
            #prompt user if he wants to update
            #if yes
            personnel_tmp = Personnel.get(per_ID=person['per_ID'])
            personnel_tmp.name = person['name']
            personnel_tmp.sector = person['sector']
            personnel_tmp.user_id = person['user_id']
            personnel_tmp.user_pass = person['user_pass']
            personnel_tmp.save()

def delete_personnel(personnel):
    personnel.delete_instance()

            

def test_select_top():
    person = Personnel.select().order_by(Personnel.per_ID.desc()).get()
    return person

    
if __name__ == '__main__':
    initialize()
    add_personnel()
    print(" {0.name}.".format(test_select_top()))
