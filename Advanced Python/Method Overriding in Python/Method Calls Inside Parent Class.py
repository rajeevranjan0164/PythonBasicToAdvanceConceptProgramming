class Report:
    def generate(self):
        print("Generating report...")
        self.display()

    def display(self):
        print("Displaying basic report")

class SalesReport(Report):
    def display(self):
        print("Displaying sales report")

obj = SalesReport()
obj.generate()