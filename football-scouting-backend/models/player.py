from config.database import db

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(255), nullable=False)
    lastName = db.Column(db.String(255), nullable=False)
    position = db.Column(db.String(255), nullable=False)
    createdAt = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    updatedAt = db.Column(db.DateTime, nullable=False, server_default=db.func.now(), onupdate=db.func.now())

    def serialize(self):
        return {
            'id': self.id,
            'firstName': self.firstName,
            'lastName': self.lastName,
            'position': self.position,
            'createdAt': self.createdAt,
            'updatedAt': self.updatedAt
        }
