# •	17. Define an abstract class `IDatabaseOperations` with methods `insert()`, `update()`, and `delete()`. 
# Implement this in `SQLDatabase` and `NoSQLDatabase`.
from abc import ABC,abstractmethod

class IDatabaseOperations(ABC):
    @abstractmethod
    def insert(self):
        pass
    @abstractmethod
    def update(self):
        pass
    @abstractmethod
    def delete(self):
        pass

class SQLDatabase(IDatabaseOperations):
    def insert(self):
        print("Inserted into sql database.")
    def update(self):
        print("Updated sql database")
    def delete(self):
        print("Deleted in sql database.")

class NoSQLDatabase(IDatabaseOperations):
    def insert(self):
        print("Inserted into Nosql database.")
    def update(self):
        print("Updated Nosql database")
    def delete(self):
        print("Deleted in Nosql database.")


sql=SQLDatabase()
sql.insert()
sql.update()
sql.delete()

nosql=NoSQLDatabase()
nosql.insert()
nosql.update()
nosql.delete()