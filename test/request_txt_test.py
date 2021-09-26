from types import resolve_bases
import xml.etree.ElementTree as ET
import datetime
from func_test import *

"""
This is the test file to test xml files 
"""

tree = ET.parse("test.xml")
root = tree.getroot()

lenght = len(root[0][1][0])

# print(root[0][1][0][0].text)


def flight_checker(lenght, root):
    for item in range(0, lenght):
        print(f"Lennon numero:               {root[0][1][item][1].text}")
        print(f"Tila:                        {status_fixer(root[0][1][item][31].text)}")
        print(f"Lähtö: (lähtö kaupunki)      {root[0][1][item][17].text}")
        time_raw = root[0][1][item][33].text
        fixed_33 = date_fixer(time_raw)
        fixed_33 = time_fixer(fixed_33)
        print(f"33 est_d (arvioitu lasku)    {fixed_33}")

        """
        try:
            time_raw = root[0][1][item][33].text.split("T")
            print(time_raw)  # date in tuple 0=date, 1=time in Z
            time_date = time_raw[0].split("-")
            print(time_date)
            time_date = datetime.date(time_date[0], time_date[1], time_date[2])
            print(time_date)
            print(f"33 est_d  {root[0][1][item][33].text[11:-1]}")
        except (TypeError, AttributeError):
            print(f"33 est_d -")
        

        print(f"34 pest_d {root[0][1][item][34].text}")
        """
        time_raw = root[0][1][item][34].text
        fixed_34 = date_fixer(time_raw)
        fixed_34 = time_fixer(fixed_34)
        print(f"34 pest_d (todellinen lasku) {fixed_33}\n")

        # print(f"35 act_d  {root[0][1][item][35].text}")
        # print(f"36 ablk_d {root[0][1][item][36].text}\n")


def flight_checker_2(lenght, root):
    # This is the current working func, it comibines all the requested lines to a list then returns it
    re_list = []
    for item in range(0, lenght):
        first_line = f"Lennon numero:               {root[0][1][item][1].text}\n"
        second_line = (
            f"Tila:                        {status_fixer(root[0][1][item][31].text)}\n"
        )
        third_line = f"Lähtö: (lähtö kaupunki)      {root[0][1][item][17].text}\n"
        time_raw = root[0][1][item][33].text
        fixed_33 = date_fixer(time_raw)
        fixed_33 = time_fixer(fixed_33)
        fourth_line = f"33 est_d (arvioitu lasku)    {fixed_33}\n"

        time_raw = root[0][1][item][34].text
        fixed_34 = date_fixer(time_raw)
        fixed_34 = time_fixer(fixed_34)
        fifth_line = f"34 pest_d (todellinen lasku) {fixed_33}\n"

        # adds all lines up
        complete_line = first_line + second_line + third_line + fourth_line + fifth_line

        re_list.append(complete_line)
        # append(first_line)
        # re_list.append(second_line)
        # append(third_line)
        # re_list.append(fourth_line)
        # re_list.append(fifth_line)

    return re_list


re = flight_checker_2(lenght, root)
# flight_checker(lenght, root)
