import pymysql.cursors
import pandas as pd


def executeSQL(sql):
    connection = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="20040101shy.",
        database="mysql",
        cursorclass=pymysql.cursors.DictCursor,
    )

    with connection:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchall()
            return result


df = pd.DataFrame(columns=["Department", "Paper", "Cite"])


# 物理科学与技术学院
res = executeSQL(
    "select count(Department) Paper,sum(Cite) Cite from world.res where Department regexp 'Phys' and Department regexp 'Technol' and University='XinjiangUniv';"
)
for i in res:
    tmp = i
    i["Department"] = "物理科学与技术学院"
    df.loc[len(df)] = i

# 新疆固态物理与器件自治区重点实验室
res = executeSQL(
    "select count(Department) Paper,sum(Cite) Cite from world.res where Department regexp 'Solid' and Department regexp 'Lab' and University='XinjiangUniv';"
)
for i in res:
    tmp = i
    i["Department"] = "新疆固态物理与器件自治区重点实验室"
    df.loc[len(df)] = i


print(df)
