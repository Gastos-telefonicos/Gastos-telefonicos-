import sys


sys.path.insert(0, "")


from src.domain.phones import Phone

database_path = "data/database.db"

database_path.save(Phone())
