class Payment:
    def process(self):
        print("Processing payment")

class OnlinePayment(Payment):
    def process(self):
        super().process()
        print("Generating receipt")

obj = OnlinePayment()
obj.process()