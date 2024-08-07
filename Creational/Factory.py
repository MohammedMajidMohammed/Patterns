class Product:
    def operation(self):
        pass

class ConcreteProductA(Product):
    def operation(self):
        return "ConcreteProductA operation"

class ConcreteProductB(Product):
    def operation(self):
        return "ConcreteProductB operation"

class Factory:
    def create_product(self, product_type):
        if product_type == "A":
            return ConcreteProductA()
        elif product_type == "B":
            return ConcreteProductB()
        else:
            raise ValueError("Unknown product type")

# Example usage
factory = Factory()

product_a = factory.create_product("A")
print(product_a.operation())

product_b = factory.create_product("B")
print(product_b.operation())
