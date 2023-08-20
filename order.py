from json import JSONEncoder, JSONDecoder, dump, loads

class Encoder(JSONEncoder):

    def default(self, o):
        return o.__dict__

class Decoder(JSONDecoder):

    def decode(self, o):
        data = loads(o)
        vals = []
        for key in data.keys():
            vals.append(data[key])
        order = Order(*vals)
        return order


class Order:
    def __init__(self, shipAddress, productsToBuy, iid=-1):
        self.shipAddress = shipAddress
        self.productsToBuy = productsToBuy
        self.id = iid

    def __eq__(self, other):
        return self.id == other.id

    def __str__(self):
        cont = ''
        for (prod,qty) in self.productsToBuy:
            cont += f"(name={prod}, qty={qty}) "
        return f'[<] Order id={self.id} to address "{self.shipAddress}" containing products {cont}'
