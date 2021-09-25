import xml.etree.ElementTree as ET

"""
This is the test file to test xml files 
"""

tree = ET.parse("test.xml")
root = tree.getroot()

lenght = len(root[0][1][0])

print(root[0][1][0][0].text)

for item in range(0, lenght):
    print(f"Lennon numero: {root[0][1][item][1].text}")
    print(f"Tila: {root[0][1][item][31].text}")
    print(f"33 est_d  {root[0][1][item][33].text}")
    print(f"34 pest_d {root[0][1][item][34].text}")
    print(f"35 act_d  {root[0][1][item][35].text}")
    print(f"36 ablk_d {root[0][1][item][36].text}\n")
