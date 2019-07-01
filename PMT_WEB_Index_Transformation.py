from bs4 import BeautifulSoup
import soupsieve
import sys
htmlpath = sys.argv[1]
cshtmlpath = sys.argv[2]
i = open(htmlpath,'r')
srct = BeautifulSoup(i, 'lxml')
att=srct.find_all('script')
link=srct.findAll('link')
srpt =[]
for style in link:
    srpt.append(style.attrs['href'])
for sc in att:
    #print(sc.attrs['src'])
    srpt.append(sc.attrs['src'])
#print(srpt)

cs = open(cshtmlpath,'r')
cshtml = BeautifulSoup(cs,'lxml')
with open(cshtmlpath, "r") as infile:
    data=infile.read()
    data= data.replace('polyfills.js',srpt[1])
    data = data.replace('runtime.js', srpt[2])
    data = data.replace('main.js', srpt[3])
    data = data.replace('http://localhost:57558', 'https://ppmdevapi.galaxe.com')
    data = data.replace('<script type="text/javascript" src="~/Scripts/libs/vendor.js"></script>', "")
    data= data.replace('<script type="text/javascript" src="~/Scripts/libs/styles.js"></script>', "")
    if(data.__contains__(srpt[0])):
        print("Duplicate Value: Contains Link style sheet already")
    else:
        data = data.replace('</head>', '<link rel="stylesheet" type="text/css" href="'+srpt[0]+'"/></head>')

with open('Index.cshtml', "w") as outfile:
    outfile.write(data)
    outfile.close()