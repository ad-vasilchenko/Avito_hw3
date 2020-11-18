import json

class ColorizeMixin:
    color = 33
    

class Advert(ColorizeMixin):
    def __init__ (self, d):
        if 'price' in d and d['price'] < 0:
            raise ValueError ('must be >= 0')
            
        for key in d:
            self.__setattr__(key,d[key])
            
    def __setattr__(self, key, value):
        
        key_private = '_' + key
        if type(value) == dict:
            self.__dict__[key_private] = Advert(value)
        else:
            self.__dict__[key_private] = value
            
    def __getattr__ (self, key):
        key_private = '_' + key
        if hasattr(self, key_private):
            return self.__dict__[key_private]
        else:
            raise ValueError ('no such value')
            
            
    @property
    def price(self):
        if '_price' in self.__dict__:
            return self._price
        else:
            return 0

        
    @price.setter
    def price(self, p):
        if p >= 0:
            self._price = p
        else:
            raise ValueError ('must be >= 0')
            
    def __str__(self):
        return f" \033[1;30;{super().color}m  {self.title} | {self.price} "

    def __repr__(self):
        return f" \033[1;30;{super().color}m  {self.title} | {self.price} "


if __name__ == "__main__":
    s = """{
            "title": "python",
            "price": 3,
            "location": {
                "address": "Big Tishinsky 2",
                "metro_stations": ["Belorus"]
            }
        }"""

    data = json.loads(s)
    a = Advert(data)
    print (data)
    print(a.location.address)
    print(a.price)
    print(a)
