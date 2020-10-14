class ArtificialTree:

    def __init__(self, producer_name=None, height_in_sm=None, price=None, material=None):
        self.producer_name = producer_name
        self.height_in_sm = height_in_sm
        self.price = price
        self.material = material

    def __str__(self):
        producer_name = 'Producer name: {}\n'.format(self.producer_name)
        height_in_sm = 'Height: {}\n'.format(self.height_in_sm)
        price = 'Price: {}\n'.format(self.price)
        material = 'Material: {}\n'.format(self.material)
        return producer_name + height_in_sm + price + material
