import http.client
import json
import pandas as pd
import time
import mysql.connector

# 建立数据库连接
conn_mysql = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="leetcode"
)

dic = {1:"懒惰者", 2:"懒惰师", 3:"懒惰大师", 4:"懒惰王", 5:"懒惰皇", 6:"懒惰半圣", 7:"懒惰圣人", 8:"懒惰帝", 9:"飞升"}

ids = []
cnt = 0
df = pd.read_excel('D:\python\projects\data.xlsx','Sheet1')
for i in range(len(df)):
    id_name = df.loc[i, "主页"].split('/')

    if (len(id_name)) >= 5:
        for j in range(len(id_name) - 1, -1, -1):
            if id_name[j]:
                ids.append((id_name[j],int(df.loc[i, "QQ号"]), df.loc[i, "群昵称"]))
                break

arr = []
cursor = conn_mysql.cursor()

for id, qq, name in ids:
    conn = http.client.HTTPSConnection("leetcode.cn")
    payload = json.dumps({
    "query": "\n    query recentAcSubmissions($userSlug: String!) {\n  recentACSubmissions(userSlug: $userSlug) {\n    submissionId\n    submitTime\n    question {\n      translatedTitle\n      titleSlug\n      questionFrontendId\n    }\n  }\n}\n    ",
    "variables": {
        "userSlug": id
    }
    })
    headers = {
    'authority': 'leetcode.cn',
    'authorization': '',
    'cookie': '_bl_uid=32lgt5Iq4estR4ovpv48fej2UI58; gr_user_id=9cd64ed3-db69-4693-b361-a68ed8316706; csrftoken=PPT5fcdFRpPnRbcHzNYbBhwpTv1HxSKtrqyurg4uKxuW0aBUPMTLb0Cu5LwyCmm6; a2873925c34ecbd2_gr_last_sent_cs1=sanxiconze-2; _ga=GA1.2.827755954.1656827815; aliyungf_tc=3f88358c46c63b3cf747bfa7f9c952beb3e2cc9b91a526c574c455d381d3d562; Hm_lpvt_fa218a3ff7179639febdb15e372f411c=1656848229; Hm_lvt_fa218a3ff7179639febdb15e372f411c=1656827815,1656848229; a2873925c34ecbd2_gr_session_id=0f3c7ce7-f057-4e09-9e0d-d8b006ba0375; a2873925c34ecbd2_gr_last_sent_sid_with_cs1=0f3c7ce7-f057-4e09-9e0d-d8b006ba0375; a2873925c34ecbd2_gr_session_id_0f3c7ce7-f057-4e09-9e0d-d8b006ba0375=true; a2873925c34ecbd2_gr_cs1=sanxiconze-2; LEETCODE_SESSION=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiMzk3NjA5IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiYWxsYXV0aC5hY2NvdW50LmF1dGhfYmFja2VuZHMuQXV0aGVudGljYXRpb25CYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiN2RiZjJiMjI5ZDZiMmQ0MWI0ZTMzOTVlYmExMTE5YzI2ZGI0M2Q1ZTE1M2FkNjI1YmJmNDVkYzEwNWI1OWFjMSIsImlkIjozOTc2MDksImVtYWlsIjoic2FueGljb256ZUBnbWFpbC5jb20iLCJ1c2VybmFtZSI6InNhbnhpY29uemUtMiIsInVzZXJfc2x1ZyI6InNhbnhpY29uemUtMiIsImF2YXRhciI6Imh0dHBzOi8vYXNzZXRzLmxlZXRjb2RlLmNuL2FsaXl1bi1sYy11cGxvYWQvZGVmYXVsdF9hdmF0YXIucG5nIiwicGhvbmVfdmVyaWZpZWQiOnRydWUsIl90aW1lc3RhbXAiOjE2NTY4MjMxNTkuOTk4MTUzNywiZXhwaXJlZF90aW1lXyI6MTY1OTM4MDQwMCwidmVyc2lvbl9rZXlfIjowLCJsYXRlc3RfdGltZXN0YW1wXyI6MTY1Njk0MDY3MX0.-8yAB0-g6Vt2xFGdvuO5HxkV9TSHAywGzeD-Ea2fhE8',
    'x-csrftoken': 'PPT5fcdFRpPnRbcHzNYbBhwpTv1HxSKtrqyurg4uKxuW0aBUPMTLb0Cu5LwyCmm6',
    'User-Agent': 'apifox/1.0.0 (https://www.apifox.cn)',
    'content-type': 'application/json'
    }
    conn.request("POST", "/graphql/noj-go/", payload, headers)
    res = conn.getresponse()
    data = res.read()
    s = data.decode("utf-8")
    idx = s.find("submitTime")
    # print(s[idx + 12 : idx + 22])
    if idx==-1:
        # print('懒惰者称号将赋予QQ号为' + str(qq) + "的 " + str(name) + " 同学", "目前为止一道题还没有开始做哦")
        arr.append((-1, str(qq), str(name)))
        continue
    last_time = int(s[idx + 12 : idx + 22])
    import time
    current_time =  time.time()
    # print(name,qq, type(name), type(qq))
    if current_time - last_time > 86400 + 7200:

        # print('懒惰者称号将赋予QQ号为' +str(qq) + "的 " +  str(name) +" 同学", "已经有", (current_time-last_time)//3600, "小时没刷题啦")
        arr.append(((current_time-last_time)//3600, str(qq), str(name)))

        cursor.execute("SELECT * FROM user WHERE qq = %s", (qq,))

        row = cursor.fetchone()

        if row:
            # 如果QQ号存在，则更新level字段
            updated_level = row[2] + 1
            title = dic[updated_level]
            cursor.execute("UPDATE user SET level = %s, title = %s WHERE qq = %s", (updated_level, title, qq))
        else:
            # 如果QQ号不存在，则插入一条新记录
            cursor.execute("INSERT INTO user (qq, level, title) VALUES (%s, %s, %s)", (qq, 0, "普通成员"))

        # 提交更改
        conn_mysql.commit()




# 关闭游标和连接
cursor.close()
conn_mysql.close()