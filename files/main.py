from fpdf import FPDF


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
        flatmate1_pay = str(round(flatname1.pays(bill, flatname2), 2))
        flatmate2_pay = str(round(flatname2.pays(bill, flatname1), 2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # House icon
        pdf.image("house.png", w=30, h=30)

        # Title
        pdf.set_font(family="Times", size=24, style="B")
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)

        # Period label
        pdf.set_font(family="Times", size=14, style="B")
        pdf.cell(w=100, h=40, txt="Period", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # Name and due amount of first flatmate
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=100, h=25, txt=flatname1.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate1_pay, border=0, ln=1)

        # Name and due amount of first flatmate
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=100, h=25, txt=flatname2.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate2_pay, border=0, ln=1)

        pdf.output(self.filename)


the_bill = Bill(120, "April 2021")
john = Flatmate("John", 20)
marry = Flatmate("Marry", 25)

print("John pays: ", john.pays(bill=the_bill, flatmate2=marry))
print("Marry pays: ", marry.pays(bill=the_bill, flatmate2=john))

pdf_report = PdfReport(filename="Report1.pdf")
pdf_report.generate(flatname1=john, flatname2=marry, bill=the_bill)
