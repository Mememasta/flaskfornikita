from app import db

#ROLE_USER = 0
#ROLE_ADMIN = 1

class User(db.Model):
    """Класс User, содержит несколько полей,
    определенных как переменные класса.
    Поля созданы как экземпляры класса db.Column,
    который принимает тип поля как аргумент,
    плюс другие опциональные аргументы что позволяет нам,
    например, указывать какие поля уникальны и индексированы."""

    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)
#    role = db.Column(db.SmallInteger, default = ROLE_USER)

    def __repr__(self):
        """ Метод __repr__ говорит Python как выводить объекты этого класса.
        Используем его для отладки"""

        return '<User %r>' % (self.nickname)
