import sqlite3


class PhoneCost:
    def __init__(self, phone, cost):
        self.phone = phone
        self.cost = cost

    def to_dict(self):
        return {
            "phone": self.phone,
            "cost": self.cost,
        }


class PhonesAndCostRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_tables(self):
        sql = """
                create table if not exists phones_cost (
                    phone VARCHAR,
                    cost VARCHAR
                )
            """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def get_phones_cost(self):
        sql = """SELECT * FROM phones_cost"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchall()

        phones = []
        for item in data:
            contact = PhoneCost(
                phone=item["phone"],
                cost=item["cost"],
            )
            phones.append(contact)

        return phones

        # def get_by_id(self, id):
        #     sql = """SELECT * FROM phones WHERE id=:id"""
        #     conn = self.create_conn()
        #     cursor = conn.cursor()
        #     cursor.execute(sql, {"id": id})

        #     data = cursor.fetchone()
        #     phones = Phones(**data)

        return phones

    def save(self, phone_cost):
        sql = """INSERT OR REPLACE INTO phones_cost (phone, cost) VALUES (:phone, :cost) """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql,
            phone_cost.to_dict(),
        )
        conn.commit()
