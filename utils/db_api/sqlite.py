import sqlite3


class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        # connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE Users (
            id int NOT NULL,
            Name varchar(255) NOT NULL,
            email varchar(255),
            language varchar(3),
            PRIMARY KEY (id)
            );
"""
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_user(self, id: int, name: str, email: str = None, language: str = 'uz'):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO Users(id, Name, email, language) VALUES(?, ?, ?, ?)
        """
        self.execute(sql, parameters=(id, name, email, language), commit=True)

    def select_all_users(self):
        sql = """
        SELECT * FROM Users
        """
        return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)

    def update_user_email(self, email, id):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
        UPDATE Users SET email=? WHERE id=?
        """
        return self.execute(sql, parameters=(email, id), commit=True)

    def delete_users(self):
        self.execute("DELETE FROM Users WHERE TRUE", commit=True)


# def logger(statement):
#     print(f"""
# _____________________________________________________        
# Executing: 
# {statement}
# _____________________________________________________
# """)


class UserBalanceDB:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS accounts
                            (user_id INTEGER PRIMARY KEY, balance REAL)''')
        self.conn.commit()

    def update_balance(self, user_id, amount):
        current_balance = self.get_balance(user_id)
        new_balance = current_balance + float(amount)
        self.cursor.execute('UPDATE accounts SET balance = ? WHERE user_id = ?', (new_balance, user_id))
        self.conn.commit()

    def minus_balance(self, user_id, amount):
        current_balance = self.get_balance(user_id)
        new_balance = current_balance - float(amount)
        self.cursor.execute('UPDATE accounts SET balance = ? WHERE user_id = ?', (new_balance, user_id))
        self.conn.commit()

    def set_balance(self, user_id, amount):
        self.cursor.execute('INSERT OR REPLACE INTO accounts (user_id, balance) VALUES (?, ?)', (user_id, float(amount)))
        self.conn.commit()

    def get_balance(self, user_id):
        self.cursor.execute('SELECT balance FROM accounts WHERE user_id = ?', (user_id,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            self.set_balance(user_id, 0)
            return 0
            

class ProductPriceDB:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS product_prices (
                product_name TEXT PRIMARY KEY,
                price REAL
            )
        """)
        self.conn.commit()

    def save_price(self, name, price):
        self.cursor.execute("REPLACE INTO product_prices (product_name, price) VALUES (?, ?)", (name, price))
        self.conn.commit()

    def get_price(self, name):
        self.cursor.execute("SELECT price FROM product_prices WHERE product_name=?", (name,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            return None

    def close_connection(self):
        self.conn.close()


class PaymentChecker:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS payments (
                                bill_id TEXT PRIMARY KEY,
                                amount INTEGER,
                                user_id TEXT
                            )''')
        self.conn.commit()

    def save_payment(self, bill_id, amount, user_id):
        self.cursor.execute('''INSERT INTO payments (bill_id, amount, user_id)
                               VALUES (?, ?, ?)''', (bill_id, amount, user_id))
        self.conn.commit()

    def get_payment(self, bill_id):
        self.cursor.execute('''SELECT user_id, bill_id, amount FROM payments
                               WHERE bill_id = ?''', (bill_id,))
        result = self.cursor.fetchone()
        if result:
            return list(result)
        else:
            return None

    def close(self):
        self.conn.close()