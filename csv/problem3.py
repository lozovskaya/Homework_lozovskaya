import csv


def edited_name_school(now_school):  # delete unnecessary detailes
        n = 0
        while n < len(now_school) and "Школа" not in now_school[n] and "«Школа" not in now_school[n]:
            n += 1
        if n >= len(now_school):
            n = 0
            while n < len(now_school) and now_school[n] != "Москвы":
                n += 1
            n += 1
        if n < len(now_school):
            if len(now_school[n:]) == 1:
                print(now_school, n, now_school[n:])
            now_school = " ".join(now_school[n:])
            if now_school[0] == "«":
                now_school = now_school[1].upper() + now_school[2:]
            else:
                now_school = now_school[0].upper() + now_school[1:]
            if now_school[-1] == "»" and "«" not in now_school:
                now_school = now_school[:len(now_school) - 1]
            return (now_school)
        else:
            return (" ".join(now_school[4:]))


adm_areas = dict()
with open("data3_need_cp1251.csv", "r", encoding="cp1251") as file_input:
    main_dict = csv.DictReader(file_input, delimiter=";")
    for i in main_dict:
        #print(i.keys())
        if i["AdmArea"] not in adm_areas.keys():
            adm_areas[i["AdmArea"]] = [i]
        else:
            adm_areas[i["AdmArea"]].append(i)
for i in adm_areas.keys():
    for j in range(len(adm_areas[i])):
        adm_areas[i][j] = {"EDU_NAME": adm_areas[i][j]["EDU_NAME"],
            "PASSED_NUMBER_FULL": int(adm_areas[i][j]["PASSED_NUMBER_FULL"]), 
            "PASSES_OVER_220": int(adm_areas[i][j]["PASSES_OVER_220"])}
        adm_areas[i][j]["Percent"] = round(adm_areas[i][j]["PASSES_OVER_220"] / 
                                           adm_areas[i][j]["PASSED_NUMBER_FULL"] * 100, 2) 
for i in adm_areas.keys():
    for j in range(len(adm_areas[i])):
        adm_areas[i][j]["EDU_NAME"] = edited_name_school(adm_areas[i][j]["EDU_NAME"].split())
    adm_areas[i].sort(key=lambda x: x["Percent"])
with open("Results.md", "w") as file_output:
    for i in adm_areas.keys():
        print("**", i, "**:", sep="", file=file_output)
        for j in range(len(adm_areas[i])):
            print(adm_areas[i][j]["EDU_NAME"], "-", str(adm_areas[i][j]["Percent"]) + "%", end=" (", file=file_output)
            print(adm_areas[i][j]["PASSES_OVER_220"], "out of", str(adm_areas[i][j]["PASSED_NUMBER_FULL"]) + ")", file=file_output)    
        print(file=file_output)
