# -*- coding: utf-8 -*-
from marshmallow import fields, Schema


class BeerSchema(Schema):
    """
        Definition to validate beer body parameters
    """
    name = fields.Str(
        required=True,
        error_messages={'required': 'Name of beer is required'}
    )
    brand = fields.Str(
        required=True,
        error_messages={'required': 'Brand of beer is required'}
    )
    origin = fields.Str(
        required=True,
        error_messages={'required': 'Country origin of beer is required'}
    )
    date_released = fields.Str(
        required=True,
        error_messages={'required': 'Date released of beer is required'}
    )
    ingredients = fields.List(
        fields.Dict(),
        required=True,
        error_messages={'required': 'The ingredients is required'}
    )

    class Meta:
        fields = ('name',
                  'brand',
                  'origin',
                  'dateReleased',
                  'ingredients')


beer_schema = BeerSchema()
