from json import JSONDecoder, JSONEncoder, JSONDecodeError, loads, dump
import product

class Encoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


class Products:

    products = []

    @classmethod
    def loadProducts(cls):
        decoder = product.Decoder()

        try:
            with open("products.txt") as f:
                for line in f:
                    data = loads(line)
                    decodedProduct = decoder.decode(data)
                    if decodedProduct not in cls.products:
                        cls.products.append(decodedProduct)
        except (JSONDecodeError, FileNotFoundError) as _:
            cls.products = []
        return cls.products

    @classmethod
    def removeProduct(cls, prod):
        cls.loadProducts()
        if prod in cls.products:
            cls.products.remove(prod)
            with open("products.txt", 'w') as f:
                for prod in cls.products:
                    e = Encoder()
                    encoded_prod = e.encode(prod)
                    dump(encoded_prod, f)
                    f.write("\n")
            return True
        else:
            return False

    @classmethod
    def getProduct(cls, prod):
        cls.loadProducts()

        for existentProd in cls.products:
            if existentProd == prod:
                return existentProd

    @classmethod
    def setProduct(cls, prod):
        cls.loadProducts()

        for existentProd in cls.products:
            if existentProd == prod:
                cls.removeProduct(existentProd)
                cls.addProduct(prod)
                break

    @classmethod
    def addProduct(cls, prod):
        cls.loadProducts()
        if prod not in cls.products:
            with open("products.txt", 'a') as f:
                e = Encoder()
                encoded_prod = e.encode(prod)
                dump(encoded_prod, f)
                f.write("\n")
            return False
        else:
            return True