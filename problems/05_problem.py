class Train:
    def __init__(self, train_number, from_station, to_station):
        self.train_number = train_number
        self.from_station = from_station
        self.to_station = to_station

    def book(self, train_number, from_station, to_station):
        print("Booking a train ticket...")
        print("Train ticket booked successfully!")
        print(f"Train Number: {train_number}, From: {from_station}, To: {to_station}")


    def getStatus(self, train_number):
        print(f"Checking status for train {train_number}...")       


    def getFare(self,train_number, from_station, to_station):
        print(f"Calculating fare for train {train_number} from {from_station} to {to_station}...")
        print("Fare calculated successfully! is $50")  # Assuming a fixed fare for simplicity   


t = Train("12345", "New York", "Los Angeles")
t.book("12345", "New York", "Los Angeles") 
t.getStatus("12345")
t.getFare("12345", "New York", "Los Angeles")

