
katz_deli = []

def line(self):
    if not self:
        print("The line is currently empty.")
    else:
        line_str = "The line is currently:"
        for i, name in enumerate(self):
            line_str += f" {i+1}. {name}"
        print(line_str)



def take_a_number(self, string):
    self.append(string)
    print(f"Welcome, {string}. You are number {len(self)} in line.")



def now_serving(self):
    if not self == []:
        print(f"Currently serving {self[0]}.")
        self.pop(0)

    else:
        print("There is nobody waiting to be served!")