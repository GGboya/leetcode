import pandas as pd
import time
import util.get_user_info


def GetLasyData(flag, mode):
    ids = []
    df = pd.read_excel('D:\python\projects\data.xlsx', 'Sheet1')

    for i in range(len(df)):
        id_name = df.loc[i, "主页"].split('/')
        if (len(id_name)) >= 5:
            for j in range(len(id_name) - 1, -1, -1):
                if id_name[j]:
                    ids.append((id_name[j], int(df.loc[i, "QQ号"]), df.loc[i, "群昵称"]))
                    break

    qqlist = []

    for id, qq, name in ids:
        if flag == mode:
            qqlist.append(qq)
            continue
        last_time = util.get_user_info.GetLastSubmissionTime(id)
        if last_time == -1:
            # 没有获取到用户刷题记录信息，那么直接入库
            qqlist.append(qq)
            continue
        current_time = time.time()
        if current_time - last_time > 86400 + 7200:
            qqlist.append(qq)

    return qqlist