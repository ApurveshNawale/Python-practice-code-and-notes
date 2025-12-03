
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        return f"Employee Name: {self.name}, Salary: ₹{self.salary}"

class Admin(Employee):
    def __init__(self, name, salary, role):
        super().__init__(name, salary)
        self.role = role

    def show_admin_info(self):
        return f"{self.show_details()}, Role: {self.role}"

class Players:
    def __init__(self, player_name, game):
        self.player_name = player_name
        self.game = game

    def show_player(self):
        return f"Player: {self.player_name}, Game: {self.game}"

admin1 = Admin("Riya", 50000, "Team Leader")
player1 = Players("Virat", "Cricket")

print(admin1.show_admin_info())
print(player1.show_player())
