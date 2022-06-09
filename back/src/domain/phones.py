import sqlite3


class Phone:
    def __init__(self, phone, project, description, subaccount):
        self.phone = phone
        self.project = project
        self.description = description
        self.subaccount = subaccount

    def to_dict(self):
        return {
            "phone": self.phone,
            "project": self.project,
            "description": self.description,
            "subaccount": self.subaccount,
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
                    phone VARCHAR PRIMARY KEY,
                    project VARCHAR,
                    description VARCHAR,
                    subaccount VARCHAR
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
                subaccount=item["subaccount"],
            )
            phones.append(phone)

        return phones

    # def get_by_phone(self, phone):
    #     sql = """SELECT * FROM phones WHERE phone=:phone"""
    #     conn = self.create_conn()
    #     cursor = conn.cursor()
    #     cursor.execute(sql, {"phone": phone})

    #     data = cursor.fetchone()

    #     if data is not None:
    #         phone = Phone(**data)
    #     else:
    #         phone = None

    #     return phone

    def save(self, phones):
        sql = """INSERT INTO phones(phone, project, description, subaccount) VALUES (
            :phone, :project, :description, :subaccount
        ) """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql,
            phones.to_dict(),
        )
        conn.commit()

    def save_by_phone(self, phone):
        tlf = phone.to_dict()
        tlf["phone_id"] = tlf["phone"]
        sql = """UPDATE phones
                     SET project= :project,
                         description= :description,
                         subaccount= :subaccount,
                         phone=:phone
                         WHERE phone=:phone_id
         """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql,
            tlf,
        )
        conn.commit()

    def delete_phones(self, phone):
        sql = """DELETE FROM phones WHERE phone=:phone"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"phone": phone})
        conn.commit()

    def get_full_data_phone(self):
        sql = """SELECT phones.phone, phones.description, phones.project, phones.subaccount, phones_cost.cost
                 FROM phones
                 INNER JOIN phones_cost ON phones.phone = phones_cost.phone"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        phones = []
        for item in data:
            phones.append(
                {
                    "phone": item["phone"],
                    "description": item["description"],
                    "project": item["project"],
                    "cost": item["cost"],
                    "subaccount": item["subaccount"],
                }
            )
        return phones
