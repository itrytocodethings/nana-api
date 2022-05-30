from app import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    notes = db.relationship('Note', backref='user', lazy=True)

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'notes': list(map(lambda note: note.serialize(), self.notes))
        }

    def __repr__(self):
        return "<User '{}'>".format(self.username)

class Note(db.Model):
    __tablename__ = 'note'

    id = db.Column(db.Integer, primary_key=True)
    note_title = db.Column(db.String(50), nullable=True)
    note_body = db.Column(db.Text, nullable=True)
    plain_text = db.Column(db.Text, nullable=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'title': self.note_title,
            'body': self.note_body,
            'plain_text': self.plain_text,
            'owner_id': self.owner_id
        }
