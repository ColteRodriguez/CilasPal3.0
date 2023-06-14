import PyPDF2
import version
import methods
import xlsxwriter


# multifile is public static void, passes the UDSC and PSC and writes to the Excel only
def singlefile(py, pdfsList, worksheet, worksheet2):

    for p in range(len(pdfsList)):

        #   creating a pdf file object
        pdfFileObj = open(py[0] + '/' + pdfsList[p], 'rb')

        # creating a pdf reader object
        pdfReader = PyPDF2.PdfReader(pdfFileObj)

        # creating a page object
        pageObj = pdfReader.pages[1]
        pageObj2 = pdfReader.pages[0]

        List = pageObj.extract_text()
        List2 = pageObj2.extract_text()

        print(List)

        # Run the correct parsing alg for the version
        if version.get_pdf_version(py[0] + '/' + pdfsList[p]) == "1.3":
            littleQArray, bigQArray = methods.thirteensingle(List, List2)
        elif version.get_pdf_version(py[0] + '/' + pdfsList[p]) == "1.5":
            littleQArray, bigQArray = methods.fifteensingle(List, List2)
        else:
            raise Exception(f"InvalidEntryTypeError: There was an error in processing the file: {pdfsList[p]}, "
                            f"CilasPal currently only supports pdf versions 1.3 and 1.5. "
                            f"Please move the file out of the directory or change the version type to continue.")

        # write the parsed data to the Excel spreadsheet
        for a in range(len(littleQArray)):
            worksheet.write(p + 1, a, littleQArray[a])
        for a in range(len(bigQArray)):
            worksheet2.write(p + 1, a, bigQArray[a])
        # closing the pdf file object

        pdfFileObj.close()

