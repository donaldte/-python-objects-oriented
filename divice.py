import csv

class Divice:
    #contructeur
    listobj = []
    rate_discount = 4
    def __init__(self, name:str, price=0):
        self.__name = name
        self.__price = price 

        assert len(name) < 10, f"{name} should not be greather than ten caracter"
        assert price > 5 , f"{price}, The price should be greather than 5"

        Divice.listobj.append(self)

#Encapsulation
    @property
    def name(self):
        return self.__name


    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value    

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name will not be more than ten characters")
        self.name = value    
# classmethod
    @classmethod
    def get_all_the_instance(cls):
        with open('file.csv', 'r') as f:
            dictvalue =  csv.DictReader(f)
            items = list(dictvalue) 

        for item in items:
            Divice(
                name=item.get('name'),
                price=int(item.get('price')) 
                 )


    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name}, {self.price})"           


# static method 
    @staticmethod
    def is_intenger(num):
        if isinstance(num, float):
            return num.is_integer()
        if isinstance(num, int):
            return True
        else:
            return False                 

# Method
    def price_discount(self):
        self.__price = self.price * self.rate_discount


    # Abstraction 
    def __connect(sefl):
        pass

    def __preparing(self):
        pass

    def __send(self):
        pass

    def sending_email(self):
        self.__connect()
        self.__preparing()
        self.__send()
        return 


