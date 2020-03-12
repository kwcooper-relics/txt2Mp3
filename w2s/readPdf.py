import PyPDF2
import time

# Grab pdf and init reader
pdfFileObj = open("quotes.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

strt = time.time()
mytext = ""
# Iterate through each page and grab text
for pageNum in range(pdfReader.numPages):
	pageObj = pdfReader.getPage(pageNum)
	mytext += pageObj.extractText()

pdfFileObj.close()

#print(mytext)
fin = time.time() - strt
print('took %s seconds', %(fin))

