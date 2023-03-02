from . import db

class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)
    num_of_bedrooms = db.Column(db.Integer)
    num_of_bathrooms = db.Column(db.Integer)
    location = db.Column(db.String(100))
    price = db.Column(db.Integer)
    type = db.Column(db.String(15))
    photo = db.Column(db.String(255), unique=True)
    description = db.Column(db.String(255), unique=True)

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support
        
    def __repr__(self):
        return '<Property %r>' % (self.title)

    def __init__(self,title,num_of_bedrooms,num_of_bathrooms,location,price,type,photo,description):
        self.title = title
        self.num_of_bedrooms = num_of_bedrooms
        self.num_of_bathrooms = num_of_bathrooms
        self.location = location
        self.price = price
        self.type = type
        self.photo = photo
        self.description = description