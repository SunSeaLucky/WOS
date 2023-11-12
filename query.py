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


def get_statics(department, key1, key2, df):
    res = executeSQL(
        "select count(Department) Paper,sum(Cite) Cite from world.res where Department regexp '"
        + key1
        + "' and Department regexp '"
        + key2
        + "' and University='XinjiangUniv';"
    )
    for i in res:
        tmp = i
        i["Department"] = department
        df.loc[len(df)] = i


df = pd.DataFrame(columns=["Department", "Paper", "Cite"])

get_statics("物理科学与技术学院", "Phys", "Technol", df)
get_statics("新疆固态物理与器件自治区重点实验室", "Solid", "Lab", df)
get_statics("计算机科学与技术学院", "Informat", "Engn", df)
get_statics("新疆信号检测与处理重点实验室", "Signal", "Detect", df)

get_statics("电气工程学院", "Elect", "Engn", df)
get_statics("数学与系统科学学院", "Math", "Syst", df)
get_statics("化学学院", "Coll", "Chem", df)
get_statics("化工学院", "Chem", "Engn", df)
get_statics("新疆生物资源基因工程重点实验室—省部共建国家重点实验室培育基地（科技部）", "Biol", "Gene", df)
get_statics("机械工程学院", "Mech", "Engn", df)
get_statics("先进功能材料自治区重点实验室", "Funct", "Mat", df)


df.to_csv("Res\Statistcs.csv", encoding="gbk")
