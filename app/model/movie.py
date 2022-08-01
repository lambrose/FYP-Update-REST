from app import db


class Movie(db.Model):
    __tablename__ = "movie"

    movie_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Unicode(100, collation='utf8_bin'), nullable=False)
    overview = db.Column(db.Unicode(2000, collation='utf8_bin'), nullable=False)
    image = db.Column(db.Unicode(100, collation='utf8_bin'), nullable=False)
    action = db.Column(db.Boolean, nullable=True)
    adventure = db.Column(db.Boolean, nullable=True)
    animation = db.Column(db.Boolean, nullable=True)
    comedy = db.Column(db.Boolean, nullable=True)
    crime = db.Column(db.Boolean, nullable=True)
    documentary = db.Column(db.Boolean, nullable=True)
    drama = db.Column(db.Boolean, nullable=True)
    family = db.Column(db.Boolean, nullable=True)
    fantasy = db.Column(db.Boolean, nullable=True)
    history = db.Column(db.Boolean, nullable=True)
    horror = db.Column(db.Boolean, nullable=True)
    musical = db.Column(db.Boolean, nullable=True)
    mystery = db.Column(db.Boolean, nullable=True)
    romance = db.Column(db.Boolean, nullable=True)
    sci_fi = db.Column(db.Boolean, nullable=True)
    tv_movie = db.Column(db.Boolean, nullable=True)
    thriller = db.Column(db.Boolean, nullable=True)
    war = db.Column(db.Boolean, nullable=True)
    western = db.Column(db.Boolean, nullable=True)
    popularity = db.Column(db.Integer, nullable=False)
    release_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"movie('{self.movie_id}', '{self.title}', '{self.overview}', '{self.popularity}', '{self.release_date}')"
