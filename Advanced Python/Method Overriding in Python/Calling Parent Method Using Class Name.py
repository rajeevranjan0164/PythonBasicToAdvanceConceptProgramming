class Notification:
    def send(self):
        print("Sending notification")

class Email(Notification):
    def send(self):
        Notification.send(self)
        print("Sending email")

obj = Email()
obj.send()