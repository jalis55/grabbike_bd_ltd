from main_app import db


class User(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(100))
    email=db.Column(db.String(50),unique=True)
    user_type=db.Column(db.String(20)) #sup_admin,admin,sub_admin
    approve_status=db.Column(db.Boolean())

    def __repr__(self):
        return '<Name %r>' % self.name
