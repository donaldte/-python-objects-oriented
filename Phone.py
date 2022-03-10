from divice import Divice

#inheritance

class Phone(Divice):
    def __init__(self, count, *args, **kwargs):
        self.count = count
        super().__init__(*args, **kwargs)




    def __repr__(self) -> str:

        return f"{self.__class__.__name__}({self.name}, {self.price}, {self.count})"


item = Phone(name='iphone', price=10, count=10)
print(Phone.listobj)        