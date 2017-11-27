from app.extensions import db

class Movies(db.Model):
    __tablename__ = 'Movies'
    postid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    image = db.Column(db.String)