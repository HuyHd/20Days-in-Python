class Staff:
    # Initialize Staff Information
    def __init__(self, name, age, address, salary, total_time):
        self.name = name
        self.age = age
        self.address = address
        self.salary = salary
        self.total_time = total_time

    # Show Staff Information
    def show_info(self):
        format_price = "{:,.1f} VND".format(self.salary)
        print(
            f"Staff Information:\nName: {self.name}, Age: {self.age},\nAddress: {self.address},\nSalary: {format_price}"
        )
        return "Info displayed"

    # Calculate Bonus
    def calculate_bonus(self):
        if self.total_time < 100:
            self.bonus = 0
        elif self.total_time >= 100 and self.total_time < 200:
            self.bonus = self.salary * 10 / 100
        else:
            self.bonus = self.salary * 20 / 100
        format_bonus = "{:,.1f} VND".format(self.bonus)
        return format_bonus


# Testcases:
if __name__ == "__main__":
    staff_1 = Staff("Nguyen Van Lam", 23, "Ha Noi", 30000000, 300)
    print(f"{staff_1.show_info()},\nBonus {staff_1.calculate_bonus()}\n")
    staff_2 = Staff("Dang Dai Nghia", 30, "Da Nang", 50000000, 199)
    print(f"{staff_2.show_info()},\nBonus {staff_2.calculate_bonus()}\n")
    staff_3 = Staff("Mai Thanh Hoai", 53, "Sai Gon", 10000000, 99)
    print(f"{staff_3.show_info()},\nBonus {staff_3.calculate_bonus()}\n")
