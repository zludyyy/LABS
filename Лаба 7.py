class Employee:
    def __init__(self, name: str, emp_id: int):
        self.name = name
        self.emp_id = emp_id

    def get_info(self) -> str:
        return f"Сотрудник: {self.name}, ID: {self.emp_id}"


class Manager(Employee):
    def __init__(self, name: str, emp_id: int, department: str):
        Employee.__init__(self, name, emp_id)
        self.department = department

    def manage_project(self, project_name: str) -> str:
        return f"Менеджер {self.name} управляет проектом '{project_name}' в отделе {self.department}"

    def get_info(self) -> str:
        return f"Менеджер: {self.name}, ID: {self.emp_id}, отдел: {self.department}"


class Technician(Employee):
    def __init__(self, name: str, emp_id: int, specialization: str):
        Employee.__init__(self, name, emp_id)
        self.specialization = specialization

    def perform_maintenance(self, equipment: str) -> str:
        return (f"Техник {self.name} (Специализация: {self.specialization}) "
                f"обслуживает оборудование: {equipment}")

    def get_info(self) -> str:
        return f"Техник: {self.name}, ID: {self.emp_id}, специализация: {self.specialization}"


class TechManager(Manager, Technician):
    def __init__(self, name: str, emp_id: int, department: str, specialization: str):
        Manager.__init__(self, name, emp_id, department)
        Technician.__init__(self, name, emp_id, specialization)
        self._team = [] # Список подчинённых сотрудников

    def add_employee(self, employee: Employee) -> str:
        self._team.append(employee)
        return f"Сотрудник {employee.name} добавлен в команду {self.name}"

    def get_team_info(self) -> str:
        if not self._team:
            return f"У {self.name} пока нет подчинённых."

        result = [f"Команда технического менеджера {self.name}:"]
        for emp in self._team:
            result.append(" - " + emp.get_info())
        return "\n".join(result)

    # Можем переопределить get_info ещё раз
    def get_info(self) -> str:
        return (f"Тех. менеджер: {self.name}, ID: {self.emp_id}, отдел: {self.department}, "
                f"специализация: {self.specialization}")


# Демонстрация работы
if __name__ == "__main__":
    # 1. Обычный сотрудник
    e1 = Employee("Иван Иванов", 101)
    print(e1.get_info())
    print()

    # 2. Менеджер
    m1 = Manager("Арсен Арсенов", 201, "Отдел продаж")
    print(m1.get_info())
    print(m1.manage_project("Расширение клиентской базы"))
    print()

    # 3. Техник
    t1 = Technician("Алексей Технарь", 301, "Сетевое оборудование")
    print(t1.get_info())
    print(t1.perform_maintenance("Маршрутизатор Cisco"))
    print()

    # 4. Технический менеджер (множественное наследование)
    tm1 = TechManager("АРтур Волобуев", 401, "ИТ-отдел", "Серверы и базы данных")
    print(tm1.get_info())
    print(tm1.manage_project("Миграция на новый сервер"))
    print(tm1.perform_maintenance("Сервер БД PostgreSQL"))
    print()

    # 5. Добавление сотрудников
    print(tm1.add_employee(e1))
    print(tm1.add_employee(m1))
    print(tm1.add_employee(t1))
    print()

    # 6. Вывод информации о команде
    print(tm1.get_team_info())
