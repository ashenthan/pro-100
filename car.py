class Car(object):
    def __init__(self, model,color, company, speed_limit):
        self.color=color
        self.company=company
        self.speed_limit=speed_limit
        self.model=model
    
    def start(self):
        print("started")
    def stop(self):
        print("stop")
    def accelerate(self):
        print("accelerating")

car1= Car("A6","blue","honda",100)
print(car1.company)
car1.start()
