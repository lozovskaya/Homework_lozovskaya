import csv


summ = 0
with open("data2.csv", "rt") as fin:
    main_dict = csv.DictReader(fin, delimiter=";")
    for i in main_dict:
        now = float(i["Price"])
        # print(now)
        summ += now
print("Summary", summ)
