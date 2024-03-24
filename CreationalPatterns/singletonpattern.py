
class DatabaseConnection:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connect()
        return cls._instance
    
    def connect(self):
        print("Connecting to the database...")

connection1 = DatabaseConnection()
connection2 = DatabaseConnection()

print(connection1 is connection2)  
