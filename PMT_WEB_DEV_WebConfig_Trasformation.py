from xml.etree import ElementTree as et
tree = et.parse("Web.config")

root = tree.getroot()

for add in root.iter('add'):
    # print(add.attrib)
    if (add.attrib.get('key') == 'ida:Wtrealm'):
        add.attrib['value'] = "https://pmt-dev.galaxe.com"

    if (add.attrib.get('key') == 'NoAccessPage'):
        add.attrib['key'] = "ida:Wreplay"
        add.attrib['value'] = "https://pmt-dev.galaxe.com"

    if (add.attrib.get('key') == 'APIURL'):
        add.attrib['value'] = "https://ppmdevapi.galaxe.com/api/"

for xs in root.iter('assemblyBinding'):
    xs.attrib['xmlns'] = "urn:schemas-microsoft-com:asm.v1"

tree.write('Web.config', xml_declaration=True, encoding="utf8")

data = ""

with open('Web.config', "r") as infile:
    data = infile.read()
    data = data.replace("<?xml version='1.0' encoding='utf8'?>", '<?xml version="1.0" encoding="utf-8"?>')
    data = data.replace('<configuration xmlns:ns0="urn:schemas-microsoft-com:asm.v1">', '<configuration>')
    data = data.replace("<ns0:assemblyBinding>", '<assemblyBinding xmlns="urn:schemas-microsoft-com:asm.v1">')
    data = data.replace("<ns0:dependentAssembly>", "<dependentAssembly>")
    data = data.replace("</ns0:dependentAssembly>", "</dependentAssembly>")
    data = data.replace("ns0:", "")

with open("Web.config", "w") as outfile:
    outfile.write(data)