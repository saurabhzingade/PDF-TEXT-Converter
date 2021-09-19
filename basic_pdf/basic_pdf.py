import PyPDF2
pdf = PyPDF2.PdfFileReader(open('sample.pdf', "rb"))
x=" "
for page in pdf.pages:
    x=x+page.extractText()
    x=x+"\n"
    x=x+"\n"
    
file1=open(r"sample.txt","w")
file1.write(x)
file1.close()
