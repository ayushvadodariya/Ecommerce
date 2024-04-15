from mongoengine import Document, StringField, ListField, DecimalField

class Product(Document):
    name = StringField(required=False)
    price = DecimalField(required=False)
    images = ListField(StringField())
    description = StringField()
    colors = ListField(StringField())
    sizes = ListField(StringField())
    brand= StringField(required=False)
    for_gender = StringField()

    def to_json(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "price": self.price,
            "images": self.images,
            "description": self.description,
            "colors": self.colors,
            "sizes": self.sizes,
            'brand': self.brand,
            "for_gender": self.for_gender
        }