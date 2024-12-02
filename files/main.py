from files.flat import Bill, Flatmate
from files.report import PdfReport

amount = float(input("Hey user, enter the bill amount: "))
period = input("Hey what is the bill period: ")

name1 = input("Hey what is your name?: ")
days_in_the_house1 = int(input(f"how many days have {name1} stayed?: "))

name2 = input("Hey what is the name of the other flatmate?: ")
days_in_the_house2 = int(input(f"how many days have {name2} stayed?: "))


the_bill = Bill(amount, period)
flatmate1 = Flatmate(name1, days_in_the_house1)
flatmate2 = Flatmate(name2, days_in_the_house2)

print(f"{flatmate1.name} pays: ", flatmate1.pays(the_bill, flatmate2))
print(f"{flatmate2.name} pays: ", flatmate2.pays(the_bill, flatmate1))

pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
pdf_report.generate(flatmate1, flatmate2, bill=the_bill)
