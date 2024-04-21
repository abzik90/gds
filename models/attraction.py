from app import db


class Attraction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    image_src = db.Column(db.String(200))
    address = db.Column(db.String(200))
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)
    open_time = db.Column(db.String(50))
    close_time = db.Column(db.String(50))
    price = db.Column(db.Float)
    contact_number = db.Column(db.String(20))

    def is_valid(self):
        # Check if all required fields are present and not empty
        return all([self.name, self.address])

    def to_dict(self):
        # Convert the attraction object to a dictionary
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "image_src": self.image_src,
            "address": self.address,
            "lat": self.lat,
            "lon": self.lon,
            "open_time": self.open_time,
            "close_time": self.close_time,
            "price": self.price,
            "contact_number": self.contact_number
        }
