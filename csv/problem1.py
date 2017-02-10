import csv


summ = 0.0
count = 1
with open("data.csv", "rt") as fin:
    main_dict = csv.DictReader(fin, delimiter=";")
    for i in main_dict:
        now = float(i["Sum"])
        # print(now)
        summ += now
        count += 1
print("Summary", summ)
print("Average", summ / count)
