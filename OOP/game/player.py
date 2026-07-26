
class Player:

    def __init__(self , name):
        self.name = name
        self._level = 1
        self._lives = 3
        self.score = 0

    def get_lives(self):
        return self._lives

    def set_lives(self , lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("your lives cannot be less than zero")

    lives = property(get_lives,set_lives)

    def get_level(self):
        return self._level

    def set_level(self, level):
        if level >= 0:
            dt = level - self._level
            self.score += dt * 100
            self._level = level

    level = property(get_level,set_level)

    def __str__(self):
        return f" Name: {self.name} \n Lives: {self.lives} \n Level: {self.level} \n Score: {self.score}"
