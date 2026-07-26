

class Enemy:

    def __init__(self, name = "zombie", health = 10 ,lives = 1 ):
        self.name = name
        self.health = health
        self.lives = lives

    def take_damage(self , damage_points):
        remaining_health = self.health - damage_points
        if remaining_health >= 1:
            self.health = remaining_health
            print(f"I took damage my health is {remaining_health}")
        else:
            self.lives -= 1
            self.health = 0  # add this
            if self.lives > 0:
                print("lost a life")
            else:
                print(f"{self.name} dies")
                self.lives = 0

    def __str__(self):
        return f' im {self.name} \n i have {self.lives} lives\n my heath is at {self.health} points '

class New_enemy(Enemy):

     def __init__(self):
         super().__init__(name="new-eneny",lives = 2, health=15)

     def snatch(self):
         return f"i am pahal"