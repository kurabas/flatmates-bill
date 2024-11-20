class Bill:

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        pay = self.days_in_house / (self.days_in_house + flatmate2.days_in_house) * bill.amount
        return pay


class PdfReport:

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatname1, flatname2, bill):
        pass


the_bill = Bill(120, "March 2021")
john = Flatmate("John", 20)
marry = Flatmate("Marry", 25)

print("John pays: ", john.pays(the_bill, flatmate2=marry))
print("Marry pays: ",marry.pays(the_bill, flatmate2=john))
