import json

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def to_dict(self):
        return {'name': self.name, 'position': self.position}

class HRManagement:
    def __init__(self):
        self.employees = []
        self.load_employees()

    def save_employees(self):
        with open('employees.json', 'w', encoding='utf-8') as f:
            json.dump([emp.to_dict() for emp in self.employees], f, ensure_ascii=False, indent=4)

    def load_employees(self):
        try:
            with open('employees.json', 'r', encoding='utf-8') as f:
                self.employees = [Employee(**emp) for emp in json.load(f)]
        except FileNotFoundError:
            self.employees = []

    def add_employee(self, name, position):
        new_employee = Employee(name, position)
        self.employees.append(new_employee)
        self.save_employees()
        print(f"Сотрудник {name} добавлен.")

    def list_employees(self):
        print("Список сотрудников:")
        for idx, employee in enumerate(self.employees, 1):
            print(f"{idx}. {employee.name}, {employee.position}")

    def remove_employee(self, name):
        self.employees = [emp for emp in self.employees if emp.name != name]
        self.save_employees()
        print(f"Сотрудник {name} удален.")

def main_menu():
    hr_system = HRManagement()
    while True:
        print("Выберите действие:")
        print("1. Добавить сотрудника")
        print("2. Просмотреть список сотрудников")
        print("3. Удалить сотрудника")
        print("4. Выйти из программы")
        choice = input("Введите номер действия: ")
        if choice == '1':
            name = input("Введите имя сотрудника: ")
            position = input("Введите должность сотрудника: ")
            hr_system.add_employee(name, position)
        elif choice == '2':
            hr_system.list_employees()
        elif choice == '3':
            name = input("Введите имя сотрудника для удаления: ")
            hr_system.remove_employee(name)
        elif choice == '4':
            print("Выход из программы...")
            break
        else:
            print("Неверный ввод. Пожалуйста, введите номер от 1 до 4.")

if __name__ == '__main__':
    main_menu()