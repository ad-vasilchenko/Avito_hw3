import json

class ColorizeMixin:
    
    def __str__(self):
        return f" \033[1;30;{self.repr_color_code}m{self.__repr__()}"

class Advert(ColorizeMixin):
    def __init__ (self, d):          
        self.repr_color_code = 32
        for key in d:
            self.__setattr__(key,d[key])
            
    @property
    def price(self):
        return self.__dict__.get('price', 0)
        
    @price.setter
    def price(self, p):
        if p >= 0:
            self.price = p
        else:
            raise ValueError ('must be >= 0')
            
    def __setattr__(self, key, value):
        if isinstance(value, dict):
            self.__dict__[key] = Advert(value)
        else:
            self.__dict__[key] = value
            
    def __getattr__ (self, key):
        if hasattr(self, key):
            return self.__dict__[key]
        else:
            raise ValueError ('no such value')
            
    def __repr__(self):
        return f"{self.title} | {self.price}"


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
    a.repr_color_code = 33
    print(a)
