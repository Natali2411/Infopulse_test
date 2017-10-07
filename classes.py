class Employee:
    def __init__(self, name, surname, position, salary = 0):
        self.name = name
        self.surname = surname
        self.position = position
        self.salary = salary
    def full_name(self):
        my_full_name = self.name + ' ' + self.surname
        return my_full_name

    def income(self, c_months):
        whole_salary = c_months * self.salary
        return whole_salary


#emp_name = Employee('Nataliia', 'Tiutiunnyk', 'QA')
#print(emp_name)