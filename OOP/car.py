class Car:
    def __init__(self, model, year, color, forSale):
        self.model = model
        self.year = year
        self.color = color
        self.forSale = forSale

        def drive(self):
            print(f"The {self.color} {self.model} is driving.") 

        def stop(self):
            print(f"The {self.color} {self.model} has stopped.")
        
        def describe(self):
            sale_status = "for sale" if self.forSale else "not for sale"
            print(f"This is a {self.color} {self.model} from {self.year} and it is {sale_status}.")