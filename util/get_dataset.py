import pandas as pd
import time
import util.get_user_info


def GetLasyData(cursor):
    cursor.execute("SELECT qq, homepage, title FROM users")     # 获得所有人的主页，然后判断是否是温柔榜单强者即可
    # 获取所有记录
    rows = cursor.fetchall()
    qqlist = []
    nostudy = set()

    for qq, ip, title in rows:
        id_name = ip.split("/")
        id = ""
        if (len(id_name)) >= 5:
            for j in range(len(id_name) - 1, -1, -1):
                if id_name[j]:
                    id = id_name[j]
                    break

        last_time, userscore, solve_cnt, username = util.get_user_info.GetLastSubmissionTime(id)
        qqlist.append((ip, qq, userscore, solve_cnt, username, title))
        if last_time == -1:
            # 没有获取到用户刷题记录信息，那么直接入库
            nostudy.add(qq) # 记录没有学习的同学，到时候通过这个集合，来更新用户的称号
            continue
        current_time = time.time()
        if current_time - last_time > 86400 + 7200:
            nostudy.add(qq) # 该QQ还没有刷题

    print("==============爬取leetcode数据完毕==============")

    return qqlist, nostudy