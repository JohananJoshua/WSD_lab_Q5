from lxml import etree

#load xml
xml_tree = etree.parse("employee_data.xml")

#load xsl
xsl_transform = etree.XSLT(etree.parse("transform.xsl"))

#apply xslt transformation
html_tree = xsl_transform(xml_tree)

#validation of xml against xsd
xmlschema = etree.XMLSchema(etree.parse("employee_schema.xsd"))
if xmlschema.validate(xml_tree):
    print("XML is valid against XSD.")
else:
    print("XML is not valid against XSD.")
    exit(1)

#write transformed html to a file
with open("output.html", "wb") as output_file:
    output_file.write(etree.tostring(html_tree, pretty_print=True))