class mur():
    sost = "R5"
    p_v = 0
    p_z = 0
    p_y = 0
    kolvo_per = 0

    def main(self):
        return self

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
        if self.sost == "R5" and self.p_v == 0:
            self.sost = "R2"
            self.kolvo_per += 1
        elif self.sost == "R5" and self.p_v == 1:
            self.sost = "R7"
            self.kolvo_per += 1

    def stay(self):
        if self.sost == "R1":
            self.sost = "R6"
            self.kolvo_per += 1
        elif self.sost == "R6":
            self.sost = "R5"
            self.kolvo_per += 1

    def chip(self):
        if self.sost == "R2" and self.p_z == 1:
            self.sost = "R4"
            self.kolvo_per += 1
        elif self.sost == "R2" and self.p_z == 0:
            self.sost = "R7"
            self.kolvo_per += 1


"""obj = mur().main()
obj.v(1)
print(obj.p_v)"""
