from marshmallow import fields, Schema


class BeerSchema(Schema):
    name = fields.Str(required=True, error_messages={"required": "Name of beer is required"})
    brand = fields.Str(required=True)
    origin = fields.Str(required=True, error_messages={"required": "Origin place of beer is required"})
    date_released = fields.Str(required=True)
    ingredients = fields.List(fields.Dict(), required=True)

    class Meta:
        fields = ("name",
                  "brand",
                  "origin",
                  "dateReleased",
                  "ingredients")


beer_schema = BeerSchema()
