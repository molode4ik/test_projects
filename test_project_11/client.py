from db import EmployeeDB


if __name__ == '__main__':
    db = EmployeeDB()

    db.add_employee('Иванов', 50000)
    db.add_employee('Петров', 60000)

    employees = db.get_all_employees()
    print('Все сотрудники:')
    for employee in employees:
        print(employee)

    emp_id = 1
    employee = db.get_employee(emp_id)
    print(f'\nСотрудник с ID {emp_id}: {employee}')

    db.update_employee(emp_id, 'Новый Иванов', 55000)
    updated_employee = db.get_employee(emp_id)
    print(f'\nОбновленная информация о сотруднике с ID {emp_id}: {updated_employee}')

    db.delete_employee(emp_id)
    print(f'\nСотрудник с ID {emp_id} удален.')

    employees_after_deletion = db.get_all_employees()
    print('\nОставшиеся сотрудники:')
    for employee in employees_after_deletion:
        print(employee)
