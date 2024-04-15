from mongoengine import Document, StringField, ListField, DecimalField, IntField

# class Order(Document):
#     orderBy= StringField(required=False) #userId
#     productId= StringField(required=False)
#     quantity= StringField(required=False)
#     sizes= StringField(required=False)

#     def to_json(self):
#         return {
#             "orderBy": self.orderBy,
#             "productId": self.productId,
#             "quantity": self.quantity,
#             "sizes":self.sizes,
#         }
class Order(Document):
    orderBy = StringField(required=False)
    productId = StringField(required=False)
    quantity = IntField(required=False)
    sizes = StringField(required=False)
    productPrice = DecimalField(required=False)
    totalPrice = DecimalField(required=False)

    def to_json(self):
        return {
            "orderBy": self.orderBy,
            "productId": self.productId,
            "quantity": self.quantity,
            "sizes": self.sizes,
            "productPrice": self.productPrice,
            "totalPrice": self.totalPrice
        }

    def save(self, *args, **kwargs):
        # Calculate total price before saving
        if self.quantity and self.productPrice:
            #  product_price = float(self.productPrice.replace(',', ''))
            #  self.totalPrice = int(self.quantity) * product_price
             self.totalPrice = int(self.quantity) * float(self.productPrice)
        super(Order, self).save(*args, **kwargs)

    def increment_quantity(self):
        self.quantity += 1
        self.save()
        return self.quantity  # Return updated quantity

    def decrement_quantity(self):
        if self.quantity > 0:
            self.quantity -= 1
            self.save()
        return self.quantity  # Return updated quantity