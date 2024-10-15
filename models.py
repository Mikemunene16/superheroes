from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

metadata = MetaData(
    naming_convention={
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    }
)


db = SQLAlchemy(metadata=metadata)


class Hero(db.Model, SerializerMixin):
    __tablename__ = 'heroes'

    serialize_rules = ('-heropowers.hero',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    super_name = db.Column(db.String)

    heropowers = db.relationship('HeroPower', back_populates='hero', cascade="all, delete-orphan")

    def __repr__(self):
        return f'<Hero{self.id}, {self.name} superheroes name is {self.super_name}>'


class Power(db.Model, SerializerMixin):
    __tablename__ = 'powers'

    serialize_only = ('description', 'id', 'name',)
    serialize_rules = ('-heropowers.power',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String, nullable=False)

    @validates('description')
    def validate_description(self, key, description):
        if len(description) < 20:
            raise ValueError("Description must be at least 20 characters long.")
        return description

    heropowers = db.relationship('HeroPower', back_populates='power', cascade="all, delete-orphan")

    def __repr__(self):
        return f'<Power{self.id}, {self.name}, {self.description}>'


class HeroPower(db.Model, SerializerMixin):
    __tablename__ = 'heropowers'

    serialize_rules = ('-hero.heropowers', '-power.heropowers',)

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String)

    @validates('strength')
    def validate_strength(self, key, strength):
        if strength not in ['Strong', 'Weak', 'Average']:
            raise ValueError("Strength must be one of these values: Strong, Weak, or Average.")
        return strength


    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'))
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))

    hero = db.relationship('Hero', back_populates='heropowers')
    power = db.relationship('Power', back_populates='heropowers')

    def __repr__(self):
        return f'<HeroPower {self.id}, {self.strength}>'