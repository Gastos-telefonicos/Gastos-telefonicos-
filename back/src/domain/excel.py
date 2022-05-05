import sqlite3


class Excel:
    def __init__(self, id, numbers, costs):
        self.id = id
        self.numbers = numbers
        self.costs = costs

    def to_dict(self):
        return {"id": self.id, "numbers": self.numbers, "costs": self.costs}


class ExcelRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_tables(self):
        sql = """
            create table if not exists excels (
                id varchar,
                numbers varchar,
                costs varchar
            )
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def get_excels(self):
        sql = """select * from excels"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchone()

        return Excel(id=data["id"], numbers=data["numbers"], costs=data["costs"])

    def save(self, excel):
        sql = """insert into excels (id,numbers,costs) values (
            :id,:numbers,:costs
        ) """

        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, excel.to_dict())
        conn.commit()
