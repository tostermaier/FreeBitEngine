class Collider:
    pos_x = 0
    pos_y = 0

    def __init__(self):
        pass
        print("collider initialized")

    def get_pos_x(self):
        return self.pos_x

    def get_pos_y(self):
        return self.pos_y

    def set_pos_x(self, new_pos_x):
        self.pos_x = new_pos_x

    def set_pos_y(self, new_pos_y):
        self.pos_y = new_pos_y
