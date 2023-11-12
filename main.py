import pandas as pd
import re

origin = pd.read_csv("Res/wos.csv")


def analyse_address(address):
    address += ";"
    records = re.findall("\[.+?\].+?;", address)

    res = []

    for i in records:
        detail = {"University": "", "Department": ""}
        if re.search("Xinjiang", i):
            tmp = re.findall("\s.+?,", i[len(re.findall("\[.+\]", i)[0]) :])
            detail["University"] = re.sub("[\s|,]", "", tmp[0])
            detail["Department"] = re.sub("[\s|,]", "", tmp[1])
            res.append(detail)
    return False if len(res) == 0 else res


final_res = pd.DataFrame(columns=["University", "Department", "Cite"])
for i in range(0, origin.shape[0]):
    res = analyse_address(origin.loc[origin.index.values[i], "Addresses"])
    if res:
        for j in res:
            tmp = j
            tmp["Cite"] = origin.loc[
                origin.index.values[i], "Times Cited, All Databases"
            ]
            final_res.loc[len(final_res)] = j

final_res.to_csv("Res\\final_res.csv")
