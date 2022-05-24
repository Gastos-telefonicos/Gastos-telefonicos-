import sqlite3
import PyPDF2


class Phone:
    def __init__(self, phone, project, description):
        self.phone = phone
        self.project = project
        self.description = description

    def to_dict(self):
        return {
            "phone": self.phone,
            "project": self.project,
            "description": self.description,
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
                CREATE TABLE if not exists phones (
                    phone VARCHAR,
                    project VARCHAR,
                    description VARCHAR
                )
            """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def get_phones(self):
        sql = """SELECT * FROM phones"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchall()

        phones = []
        for item in data:
            phone = Phone(
                phone=item["phone"],
                project=item["project"],
                description=item["description"],
            )
            phones.append(phone)

        return phones

        # def get_by_id(self, id):
        #     sql = """SELECT * FROM phones WHERE id=:id"""
        #     conn = self.create_conn()
        #     cursor = conn.cursor()
        #     cursor.execute(sql, {"id": id})

        #     data = cursor.fetchone()
        #     phones = Phones(**data)

    def save(self, phones):
        sql = """INSERT INTO phones (phone, project, description) VALUES (
            :phone, :project, :description
        ) """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql,
            phones.to_dict(),
        )
        conn.commit()

    def delete_phones(self, phone):
        sql = """DELETE FROM phones WHERE phone=:phone"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"phone": phone})
        conn.commit()
