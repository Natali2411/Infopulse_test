from  classes import Employee

class ITEmployee(Employee):
    def __init__(self, *args, **kwargs):
        Employee.__init__(self, *args, **kwargs)
        self.skills = []

    def add_skill(self, skill):
        self.skills.append(skill)

if __name__ == "__main__":
    empl = ITEmployee()
    empl.full_name()
    empl.add_skill("Python")
    empl.add_skill('git')
    print(empl)
    print(empl.skills)

