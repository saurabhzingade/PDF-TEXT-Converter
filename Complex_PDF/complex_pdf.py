import slate3k as slate
import PyPDF2

with open('gre.pdf','rb') as f:
    extracted_text = slate.PDF(f)

main=""
for i in extracted_text:
    main=main+i
    main=main+"\n"

file1=open(r"sample2.txt","w")
file1.write(main)
file1.close()


