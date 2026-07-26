class Kettle:

    power_src = "electricity"
    def __init__(self,material,liquid,price):
        self.material = material
        self.liquid = liquid
        self.price = price
        self.state = False

    def switch(self):
        previous_state = self.state
        self.state = not previous_state

kenwood = Kettle("steel","coffee",1000)
print(f"kettle is {"on" if kenwood.state else "off"}")
kenwood.switch()
print(f"kettle is {"on" if kenwood.state else "off"}") 