from rule34Py import rule34Py
import os.path
r34Py = rule34Py()
searchqueue=str(input('Enter tags separated by spaces: '))
if not searchqueue:
    print('Please enter tags.')
    raise SystemExit
filename=str(searchqueue)+str(".txt")
check_file = os.path.isfile(filename)
for i in range(1,2**1024):
    if check_file!=True:
        break
    filename=str(searchqueue)+str("_")+str(i)+str(".txt")
    check_file = os.path.isfile(filename)
File = open(filename, "w")
pagecount=input('Enter the number of pages (max recommended 4761):')
if not pagecount:
    pagecount=4761
    print('The maximum is set to 4761 pages.')
elif pagecount=="0":
    print('The entered number is zero, the maximum is set to 1.')
    pagecount=1
elif int(pagecount)<=0 or pagecount=="0":
    print('The entered number is less than zero, the maximum is set to 1.')
    pagecount=1
elif pagecount:
    print('The maximum is set to',pagecount,'pages.')
    pagecount=int(pagecount)
linkscount=0
for page in range(0, pagecount):
        result_search = r34Py.search([searchqueue], limit=42, page_id=page)
        print(f"{page+1}/{pagecount}",'pages saved.')
        if not result_search:
            break
        for i in range(len(result_search)):
            File.write(result_search[i].image)
            File.write('\n')
            linkscount=linkscount+1
print('Saved',page+1,'total pages.')
File.close()
print(linkscount,'links were written to',filename)
print('Press any key to terminate program.')
input()

