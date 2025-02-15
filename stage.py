class Stage:
    def __init__(self):
        self.hurdles = []

    def add_hurdle(self, hurdle):
        self.hurdles.append(hurdle)

    def draw(self, screen):
        for hurdle in self.hurdles:
            hurdle.draw(screen)
