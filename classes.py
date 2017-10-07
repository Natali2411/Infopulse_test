class Employee:
    def __init__(self, name, surname, position, salary = 0):
        self.name = name
        self.surname = surname
        self.position = position
        self.salary = salary
    def full_name(self):
        my_full_name = str(self.name) + ' ' + str(self.surname)
        return my_full_name

    def income(self, c_months):
        whole_salary = c_months * self.salary
        return whole_salary

    def __str__(self):
        return '<Employee: ' + self.full_name() + '>'


if __name__ == "__main__":
    emp_name = Employee('Nataliia', 'Tiutiunnyk', 'QA')
    print(emp_name)