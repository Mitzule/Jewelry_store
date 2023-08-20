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
        cat = Product(*vals)
        return cat


class Product:
    def __init__(self, attrs):
        self.attrs = attrs

    def __eq__(self, other):
        return self.attrs.get('name') == other.attrs.get('name')

    def __str__(self):
        msg = ''
        for key in self.attrs.keys():
            if not (key == "cat" or key == "name"):
                msg += f'{key} :-> {self.attrs.get(key)}     '
        return f'[<] Product named "{self.attrs.get("name")}" in category "{self.attrs.get("cat")}"' \
               f' and quantity={self.attrs.get("qty")} with: {msg}'
