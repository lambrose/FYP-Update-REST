from app import db
from datetime import datetime


class Group(db.Model):
    __tablename__ = "group"

    id = db.Column(db.Integer, primary_key=True)
    winner = db.Column(db.Unicode(100, collation='utf8_bin'), nullable=False)
    multiplicative_utilitarian = db.Column(db.Integer, nullable=True)
    additive_utilitarian = db.Column(db.Integer, nullable=True)
    approval_voting = db.Column(db.Integer, nullable=True)
    least_misery = db.Column(db.Integer, nullable=True)
    most_pleasure = db.Column(db.Integer, nullable=True)
    average_without_misery = db.Column(db.Integer, nullable=True)
    plurality_voting = db.Column(db.Integer, nullable=True)
    borda_count = db.Column(db.Integer, nullable=True)
    publish_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"group('{self.id}', '{self.winner}', '{self.additive}', '{self.multiplicative}'," \
               f" '{self.borda}', '{self.plurality_voting}', '{self.approval}'," \
               f" '{self.least_misery}', '{self.most_pleasure}', '{self.average_without_misery}', " \
               f"'{self.publish_date}')"
