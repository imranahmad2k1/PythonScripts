import os
os.chdir(input("Write Full Directory Folder Address for Payslips: "))
fname = ''
for i in os.listdir():
    filename, ext = os.path.splitext(i)
    try:
        junk, fname = filename.split('00040722 ')
        junk = ''
        fname = fname.replace(' )','')
        fname = fname.replace(' ,',',')
    except:
        print("Some files had names this program is not designed for!")


    if fname != "":
        if "january" in fname.lower():
            fname= '01 - ' + fname
        elif "february" in fname.lower():
            fname='02 - ' + fname
        elif "march" in fname.lower():
            fname='03 - ' + fname
        elif "april" in fname.lower():
            fname='04 - ' + fname
        elif "may" in fname.lower():
            fname='05 - ' + fname
        elif "june" in fname.lower():
            fname='06 - ' + fname
        elif "july" in fname.lower():
            fname='07 - ' + fname
        elif "august" in fname.lower():
            fname='08 - ' + fname
        elif "september" in fname.lower():
            fname='09 - ' + fname
        elif "october" in fname.lower():
            fname='10 - ' + fname
        elif "november" in fname.lower():
            fname='11 - ' + fname
        elif "december" in fname.lower():
            fname='12 - ' + fname

        finalname = fname+ext
        os.rename(i,finalname)
print("Files Renamed Successfully!")
