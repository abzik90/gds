from app import db


class Attraction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.ARRAY(db.String(255)), nullable=False)
    img_src = db.Column(db.ARRAY(db.String(255)), nullable=False)
    x = db.Column(db.Integer, nullable=False)
    y = db.Column(db.Integer, nullable=False)
    open = db.Column(db.TIMESTAMP(timezone=True), nullable=False)
    close = db.Column(db.TIMESTAMP(timezone=True), nullable=False)
    price = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Attraction {self.id}: {self.name}>"
