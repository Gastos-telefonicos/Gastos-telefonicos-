import sqlite3
import PyPDF2


class Phones:
    def __init__(self, id, phone, costs):
        self.id = id
        self.phone = phone
        self.costs = costs

    def to_dict(self):
        return {
            "id": self.id,
            "phone": self.phone,
            "costs": self.costs,
        }


class PhonesRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_tables(self):
        sql = """
                create table if not exists phones (
                    id VARCHAR PRIMARY KEY,
                    phone VARCHAR,
                    costs INTERGER
                )
            """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def get_doc(self):
        sql = """SELECT * FROM phones"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchall()

        phones = []
        for item in data:
            contact = Phones(**item)
            phones.append(contact)

        return phones

    def get_by_id(self, id):
        sql = """SELECT * FROM phones WHERE id=:id"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"id": id})

        data = cursor.fetchone()
        phones = Phones(**data)

        return phones

    def save(self, phones):
        sql = """insert into phones (id, phone, costs) values (
            :id, :phone, :costs
        ) """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql,
            phones.to_dict(),
        )
        conn.commit()