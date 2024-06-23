class Person:
    def __init__(self, name, phone) -> None:
        self.name = name
        self.phone = phone


class Employee(Person):
    def __init__(self, name, phone, annual_salary, year_of_stating_work) -> None:
        super().__init__(name, phone)
        self.annual_salary = annual_salary
        self.year_of_starting_work = year_of_stating_work


class StackEmployee:
    def __init__(self, capacity) -> None:
        self.__capacity = capacity
        self.__stack = []

    def is_empty(self):
        return len(self.__stack) == 0

    def is_full(self):
        return len(self.__stack) == self.__capacity

    def pop(self):
        if self.is_empty():
            print("Stack Empty.")
        else:
            return self.__stack.pop()

    def push(self, obj):
        if self.is_full():
            print("Stack Full.")
        else:
            self.__stack.append(obj)

    def top(self):
        if not self.is_empty():
            return self.__stack[-1]


# Testcases:
employee_1 = Employee(
    name="A", phone="0123456789", annual_salary="10000000", year_of_stating_work="2000"
)
employee_2 = Employee(
    name="B", phone="0213456789", annual_salary="20000000", year_of_stating_work="2010"
)
emp_stack = StackEmployee(5)
emp_stack.push(employee_1)
emp_stack.push(employee_2)
print("Employee Stack empty check: ", emp_stack.is_empty())
print("Employee Stack full check: ", emp_stack.is_full())
print("Get top element of Employee Stack: ", emp_stack.top())
