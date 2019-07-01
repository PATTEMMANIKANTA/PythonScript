from xml.etree import ElementTree as et
tree = et.parse("Web.config")

root = tree.getroot()

for add in root.iter('add'):
    # print(add.attrib)
    if (add.attrib.get('key') == 'PhaseDateURL'):
        add.attrib['value'] = "https://pmxppmdev.galaxe.com/ideabasicinfo;ideaID"

    if (add.attrib.get('key') == 'PMTMailAddress'):
        add.attrib['key'] = "CacheExpirationHrs"
        add.attrib['value'] = "2"

    """if (add.attrib.get('key') == 'CacheExpirationHrs'):
        add.attrib['key'] = 'PMTMailAddress'
        add.attrib['value'] = "PMT-Dev@its.jnj.com" """

    if (add.attrib.get('name') == 'CUSTOM_CONNECTION'):
        add.attrib[
            'connectionString'] = "Data Source=10.101.9.6;Initial Catalog=JaguarProjects_DataSource_QA;Persist Security Info=True;Integrated Security=SSPI;Timeout=180"

    if (add.attrib.get('name') == 'ERM_CONNECTION'):
        add.attrib[
            'connectionString'] = "Data Source=10.2.20.205;Initial Catalog=ProjectServer_PMx_5002;Persist Security Info=True;Integrated Security=SSPI;Timeout=180"

for xs in root.iter('assemblyBinding'):
    xs.attrib['xmlns'] = "urn:schemas-microsoft-com:asm.v1"

tree.write('Web.config', xml_declaration=True, encoding="utf8")

data = ""

with open('Web.config', "r") as infile:
    data = infile.read()
    data = data.replace("<ns0:assemblyBinding>", '<assemblyBinding xmlns="urn:schemas-microsoft-com:asm.v1">')
    data = data.replace("<ns0:dependentAssembly>", "<dependentAssembly>")
    data = data.replace("</ns0:dependentAssembly>", "</dependentAssembly>")
    data = data.replace("ns0:", "")
    data = data.replace('debug="true"',"")
    data = data.replace('<nlog>', '<nlog xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">')
    data = data.replace(
        '<configuration xmlns:ns0="urn:schemas-microsoft-com:asm.v1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">',
        "<configuration>")
    data = data.replace("<?xml version='1.0' encoding='utf8'?>", '<?xml version="1.0" encoding="utf-8"?>')
    data = data.replace('<target addNewLines="true" body="${date:format=HH\\:MM\\:ss} ${logger} ${message}" deliveryMethod="Network" enableSsl="true" encoding="UTF-8" footer="Layout" from="PWAHelpdesk@galaxe.com" header="PMT Logger" html="true" layout="Layout" name="Mail" pickupDirectoryLocation="String" replaceNewlineWithBrTagInHtml="true" smtpAuthentication="Ntlm" smtpPassword="" smtpPort="25" smtpServer="gsnj-ex-01.galaxy.lan" smtpUserName="PMX_Redesign_Team" subject="PMT API - Exception Log" timeout="10000" to="snalliboina@galaxe.com" useSystemNetMailSettings="true" xsi:type="Mail" />',
                        '<target xsi:type="Mail" name="Mail" header="PMT Logger" footer="Layout" layout="Layout" html="true" addNewLines="true" replaceNewlineWithBrTagInHtml="true"	encoding="UTF-8" subject="PMT API - Exception Log" to="pereddy@galaxe.com;snalliboina@galaxe.com;rpuli@galaxe.com" from="PWAHelpdesk@galaxe.com" body="${date:format=HH\\:MM\\:ss} ${logger} ${message}" smtpUserName="PMX_Redesign_Team" enableSsl="true" smtpPassword="" smtpAuthentication="Ntlm" smtpServer="gsnj-ex-01.galaxy.lan" smtpPort="25" useSystemNetMailSettings="true" deliveryMethod="Network" pickupDirectoryLocation="String" timeout="10000" />')
    # data = data.replace ()
with open("Web.config", "w") as outfile:
    outfile.write(data)