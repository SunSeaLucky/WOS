import pandas as pd
import re

origin = pd.read_csv('Res/wos.csv')


def get_XJU_address(address):
    address += ';'
    records = re.findall('\[.+?\].+?;', address)

    res = []

    for i in records:
        detail = {
            'univ': '',
            'dept': ''
        }
        if (re.search('Xinjiang', i)):
            tmp = re.findall('\s.+?,', i[len(re.findall('\[.+\]', i)[0]):])
            detail['univ'] = re.sub('[\s|,]', '', tmp[0])
            detail['dept'] = re.sub('[\s|,]', '', tmp[1])
            res.append(detail)
    return False if len(res) == 0 else res


# address = '[Hushur, Anwar; Manghnani, Murli H.] Univ Hawaii, Hawaii Inst Geophys & Planetol, Honolulu, HI 96822 USA; [Hushur, Anwar] Xinjiang Univ, Xinjiang Key Lab Solid State Phys & Devices, Urumqi, Peoples R China; [Hushur, Anwar] Xinjiang Univ, Sch Phys & Technol, Urumqi, Peoples R China; [Williams, Quentin] Univ Calif Santa Cruz, Dept Earth & Planetary Sci, Santa Cruz, CA 95064 USA'

final_res = pd.DataFrame(columns=['univ', 'dept'])
for i in range(0, origin.shape[0]):
    res = get_XJU_address(origin.loc[origin.index.values[i], 'Addresses'])
    if res:
        for j in res:
            final_res.loc[len(final_res)] = j

final_res.to_csv('Res\\final_res.csv')