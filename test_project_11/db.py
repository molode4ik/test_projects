import sqlite3


class EmployeeDB:
    def __init__(self, db_name='employees.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                salary REAL NOT NULL
            )
        ''')
        self.conn.commit()

    def add_employee(self, name, salary):
        self.cursor.execute('INSERT INTO employees (name, salary) VALUES (?, ?)', (name, salary))
        self.conn.commit()

    def get_employee(self, employee_id):
        self.cursor.execute('SELECT * FROM employees WHERE id=?', (employee_id,))
        return self.cursor.fetchone()

    def get_all_employees(self):
        self.cursor.execute('SELECT * FROM employees')
        return self.cursor.fetchall()

    def update_employee(self, employee_id, name, salary):
        self.cursor.execute('UPDATE employees SET name=?, salary=? WHERE id=?', (name, salary, employee_id))
        self.conn.commit()

    def delete_employee(self, employee_id):
        self.cursor.execute('DELETE FROM employees WHERE id=?', (employee_id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
