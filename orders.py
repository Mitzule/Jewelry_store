from json import JSONDecoder, JSONEncoder, JSONDecodeError, loads, dump
import order

class Encoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


class Orders:

    orders = []
    id = 0

    @classmethod
    def loadOrders(cls):
        decoder = order.Decoder()
        cls.id = 0
        try:
            with open("orders.txt") as f:
                for line in f:
                    data = loads(line)
                    decodedOrder = decoder.decode(data)
                    if decodedOrder not in cls.orders:
                        cls.id = decodedOrder.id
                        cls.orders.append(decodedOrder)
        except (JSONDecodeError, FileNotFoundError) as _:
            cls.orders = []
        return cls.orders

    @classmethod
    def addOrder(cls, orderr):
        cls.loadOrders()
        if orderr not in cls.orders:
            orderr.id = cls.id + 1
            with open("orders.txt", 'a') as f:
                e = Encoder()
                encoded_order = e.encode(orderr)
                dump(encoded_order, f)
                f.write("\n")
        return orderr.id