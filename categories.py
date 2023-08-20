from json import JSONDecoder, JSONEncoder, JSONDecodeError, loads, dump
import category

class Encoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

class Categories:
    categories = []

    @classmethod
    def loadCategories(cls):
        decoder = category.Decoder()

        try:
            with open("categories.txt") as f:
                for line in f:
                    data = loads(line)
                    decodedCategory = decoder.decode(data)
                    if decodedCategory not in cls.categories:
                        cls.categories.append(decodedCategory)
        except (JSONDecodeError, FileNotFoundError) as e:
            cls.categories = []
        return cls.categories

    @classmethod
    def removeCategory(cls, cat):

        cls.loadCategories()
        if cat in cls.categories:
            cls.categories.remove(cat)
            with open("categories.txt", 'w') as f:
                for cat in cls.categories:
                    e = Encoder()
                    encoded_cat = e.encode(cat)
                    dump(encoded_cat, f)
                    f.write("\n")
            return True
        else:
            return False

    @classmethod
    def addCategory(cls, cat):

        cls.loadCategories()
        if cat not in cls.categories:
            with open("categories.txt", 'a') as f:
                e = Encoder()
                encoded_cat = e.encode(cat)
                dump(encoded_cat, f)
                f.write("\n")
            return False
        else:
            return True