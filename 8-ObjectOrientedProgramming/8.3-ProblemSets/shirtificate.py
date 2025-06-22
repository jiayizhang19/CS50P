"""
In a file called shirtificate.py, implement a program that prompts the user for their name and outputs, 
using fpdf2, a CS50 shirtificate in a file called shirtificate.pdf similar to this one for John Harvard, with these specifications:

The orientation of the PDF should be Portrait.
The format of the PDF should be A4, which is 210mm wide by 297mm tall.
The top of the PDF should say “CS50 Shirtificate” as text, centered horizontally.
The shirt's image should be centered horizontally.
The user's name should be on top of the shirt, in white text.

fpdf2 tutorial https://py-pdf.github.io/fpdf2/Tutorial.html

"""

from fpdf import FPDF

def main():
    name = input("Name: ")
    draw(name)


def draw(name):
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.image("shirtificate.png", x=2, y=60)
    pdf.ln(10)
    pdf.set_font("Times", style="B", size=40)
    pdf.cell(180, 10, "CS50 Shirtificate", align="C")
    pdf.ln(10)
    pdf.set_font("Times", style="B", size=28)
    pdf.set_text_color(255,255,255)
    pdf.cell(190, 180, name+" took CS50", align="C")
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
