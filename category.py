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
        cat = Category(*vals)
        return cat


class Category:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name
