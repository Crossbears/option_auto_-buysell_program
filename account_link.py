from ib_insync import IB

def connect_ibkr():
    try:
        ib = IB()
        ib.connect('127.0.0.1', 7497, clientId=1)
        print("Connected to IBKR")
        return ib
    except Exception as e:
        print(f"Error connecting to IBKR: {e}")
        return None
    
    

ib = connect_ibkr()
