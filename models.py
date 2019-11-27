from app import db

class Flaskr(db.Model):

  __tablename__ = "flaskr"

  post_id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String, nullable=False)
  text = db.Column(db.String, nullable=False)

  def __init__(self, title, text):
      self.title = title
      self.text = text

  def __repr__(self):
      return '<title {}>'.format(self.body)

class User(db.Model):

     __tablename__ = "user"

     user_id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String, nullable=False)
     secondname = db.Column(db.String, nullable=False)
     group = db.Column(db.String, nullable=False)


     def __init__(self, name, secondname, group):
         self.name = name
         self.secondname = secondname
         self.group = group
