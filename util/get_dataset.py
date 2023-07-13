import pandas as pd
import time
import util.get_user_info


def GetLasyData():
    ids = []
    df = pd.read_excel('data.xlsx', 'Sheet1')
    ip = []
    for i in range(len(df)):
        id_name = df.loc[i, "主页"].split('/')
        ip.append("/".join(id_name[:]))
        if (len(id_name)) >= 5:
            for j in range(len(id_name) - 1, -1, -1):
                if id_name[j]:
                    ids.append((id_name[j], int(df.loc[i, "QQ号"]), df.loc[i, "群昵称"]))
                    break

    qqlist = []
    nostudy = set()
    for id, qq, name in ids:
        last_time, userscore, solve_cnt = util.get_user_info.GetLastSubmissionTime(id)
        qqlist.append((qq, userscore, solve_cnt, id))
        if last_time == -1:
            # 没有获取到用户刷题记录信息，那么直接入库
            nostudy.add(qq) # 记录没有学习的同学，到时候通过这个集合，来更新用户的称号
            continue
        current_time = time.time()
        if current_time - last_time > 86400 + 7200:
            nostudy.add(qq) # 该QQ还没有刷题

    return qqlist, nostudy, ip