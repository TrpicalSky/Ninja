import PyPDF2
import docx
import gtts
from playsound import playsound



def readPDF(pdfPath:str): 
    pdfFileObj = open(pdfPath,'rb')
    allPdfText = ""

    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    for i in range(pdfReader.getNumPages()):
        pageObj = pdfReader.getPage(i)
        allPdfText += pageObj.extractText() + "\n"
    
    
    tts = gtts.gTTS(allPdfText)
    tts.save("pdf.mp3")

    pdfFileObj.close()
    # pageObj = pdfReader.getPage(0)
    # print(pageObj.extractText())
    # tts = gtts.gTTS(pageObj.extractText())
    # tts.save("pdfTest.mp3")
    # playsound("pdfTest.mp3")


def readTxtFile(filePath:str):
    fileObj = open(filePath, 'r')
    tts = gtts.gTTS(fileObj.read())
    tts.save("test.mp3")
    # playsound("test.mp3")
    fileObj.close()

def readDocx(docxPath:str):
    f = open(docxPath, 'rb')
    textInStr = ""
    document = docx.Document(f)
    for para in document.paragraphs:
        textInStr += para.text + "\n"
    tts = gtts.gTTS(textInStr)
    tts.save("docx.mp3")
    playSound("docx.mp3")
    


def playSound(file:str):
    playsound(file)