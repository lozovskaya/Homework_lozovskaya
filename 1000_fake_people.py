import elizabeth
import openpyxl
import random


def create_person():
    sex = random.choice([["male", "man"], ["female", "woman"]])
    person = elizabeth.Personal("en")
    info = {"name": person.name(gender=sex[0]),
            "surname": person.surname(gender=sex[0]),
            "sex": sex[1],
            "age": person.age(14),
            "occupation": person.occupation(),
            "e-mail": person.email(),
            "phone model": elizabeth.Hardware().phone_model(),
            "phone number": person.telephone(mask="+# (###) ###-##-##"),
            "address": elizabeth.Address("en").address()}
    return info


workb = openpyxl.Workbook()
first_sheet = workb.active
first_sheet.append(["name", "surname", "sex", "age", "occupation", "e-mail", "phone model", "phone number", "address"])
frequent_name = dict()
for j in range(1000):
    pers = create_person()
    first_sheet.append(list(pers.values()))
    if pers["name"] not in frequent_name.keys():
        frequent_name[pers["name"]] = 1
    else:
        frequent_name[pers["name"]] += 1
tab = openpyxl.worksheet.table.Table(displayName="Table1", ref="A1:I1001")
style = openpyxl.worksheet.table.TableStyleInfo(name="TableStyleMedium26", showFirstColumn=False,
                       showLastColumn=False, showRowStripes=True, showColumnStripes=True)
tab.tableStyleInfo = style
first_sheet.add_table(tab)
workb.save("list_of_people.xlsx")

frequent_name = list(frequent_name.items())
frequent_name.sort(key=lambda x: (x[1]), reverse=True)
print(frequent_name[0][0], " is the most frequent name (", frequent_name[0][1], ")", sep="")
print("Info about people who has this name: \n(", end="")
for i in first_sheet["A1":"H1"][0]:
    print(i.value, end=", ")
print(first_sheet["I1"].value, ")", sep="")
for i in range(2, 1002):
    if first_sheet["A" + str(i)].value == frequent_name[0][0]:
        for j in first_sheet["A" + str(i):"I" + str(i)][0]:
            print(j.value, end=", ")
        print()