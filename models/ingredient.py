# -*- coding: utf-8 -*-
from app import db
from sqlalchemy import ForeignKey


class Ingredient(db.Model):
    __tablename__ = 'ingredients'

    id = db.Column(db.Integer, db.Identity(start=1), primary_key=True)
    name = db.Column(db.String, nullable=False)
    beer_id = db.Column(db.Integer,
            db.ForeignKey('beers.id', ondelete='CASCADE'))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        ingredients = {
                'id': self.id,
                'name': self.name
                }
        return ingredients

