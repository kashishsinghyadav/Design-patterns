class Logger:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def log(self, message):
        print(message)

logger1 = Logger()
logger2 = Logger()

logger1.log("Log message 1")
logger2.log("Log message 2")

print(logger1 is logger2)  
