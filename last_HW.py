class mur():
    sost = "R5"
    p_v = 0
    p_z = 0
    p_y = 0
    kolvo_per = 0
    output = "b0"
    lucky_draw = 0
    lucky_spawn = 0
    lucky_chip = 0
    lucky_stay = 0
    lucky_wreck = 0

    names_of_methods = ["draw", "chip", "stay", "spawn", "wreck"]

    def get_step(self):
        return self.kolvo_per

    def v(self, arg):
        self.p_v = int(arg)
        return None

    def z(self, arg):
        self.p_z = int(arg)
        return None

    def y(self, arg):
        self.p_y = int(arg)
        return None

    def draw(self):
        if self.sost == "R5" and self.p_v == 0 and self.output == "b0":
            self.sost = "R2"
            self.kolvo_per += 1
            self.lucky_draw += 1
            self.output = "b2"
            return None
        elif self.sost == "R5" and self.p_v == 1 and self.output == "b0":
            self.sost = "R7"
            self.kolvo_per += 1
            self.lucky_draw += 1
            self.output = "b0"
            return None
        elif self.sost == "R4" and self.output == "b3":
            self.sost = "R0"
            self.kolvo_per += 1
            self.lucky_draw += 1
            self.output = "b4"
            return None
        elif self.sost == "R7" and self.output == "b0":
            self.sost = "R3"
            self.kolvo_per += 1
            self.lucky_draw += 1
            self.output = "b0"
            return None
        elif self.sost == "R3" and self.output == "b0":
            self.sost = "R1"
            self.kolvo_per += 1
            self.lucky_draw += 1
            self.output = "b3"
            return None
        else:
            return "unsupported"

    def stay(self):
        if self.sost == "R1" and self.output == "b3":
            self.sost = "R6"
            self.kolvo_per += 1
            self.lucky_stay += 1
            self.output = "b6"
            return None
        elif self.sost == "R6" and self.output == "b6":
            self.sost = "R5"
            self.kolvo_per += 1
            self.lucky_stay += 1
            self.output = "b0"
            return None
        else:
            return "unsupported"

    def chip(self):
        if self.sost == "R2" and self.p_z == 1 and self.output == "b2":
            self.sost = "R4"
            self.kolvo_per += 1
            self.lucky_chip += 1
            self.output = "b3"
            return None
        elif self.sost == "R2" and self.p_z == 0 and self.output == "b2":
            self.sost = "R7"
            self.kolvo_per += 1
            self.lucky_chip += 1
            self.output = "b0"
            return None
        else:
            return "unsupported"

    def spawn(self):
        if self.sost == "R0" and self.p_y == 0 and self.output == "b4":
            self.sost = "R7"
            self.kolvo_per += 1
            self.lucky_spawn += 1
            self.output = "b0"
            return None
        elif self.sost == "R0" and self.p_y == 1 and self.output == "b4":
            self.sost = "R3"
            self.kolvo_per += 1
            self.lucky_spawn += 1
            self.output = "b0"
            return None
        else:
            return "unsupported"

    def wreck(self):
        if self.sost == "R4" and self.output == "b3":
            self.sost = "R6"
            self.kolvo_per += 1
            self.lucky_wreck += 1
            self.output = "b3"
            return None
        else:
            return "unsupported"

    def seen_method(self, arg):
        match arg:
            case "wreck":
                return self.lucky_wreck
            case "stay":
                return self.lucky_stay
            case "chip":
                return self.lucky_chip
            case "spawn":
                return self.lucky_spawn
            case "draw":
                return self.lucky_draw

    def __getattr__(self, item):
        if item not in self.names_of_methods:
            return lambda: "unknown"

    def get_output(self):
        return self.output


def main():
    return mur()
