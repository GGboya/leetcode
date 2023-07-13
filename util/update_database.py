import dao.crud

def update(qqlist, cursor, dic, mode, nostudy, ip):
    i = 0
    for qq, score, cur_ac_cnt, name in qqlist:
        row = dao.crud.Retrieve(cursor, qq)
        if row: # 数据库有对应记录，那么就去更新对应的

            ac_count, yesterday_cnt, last_week_cnt = row[10], row[11], row[12]
            status = "已完成"
            level = row[2]
            if qq in nostudy: # 如果没有刷题，称号增加一级，刷题状态更改为未完成
                status = "未完成"
                level += 1
            if mode == 1:
                # 每4个小时，更新一下刷题状态和刷题数量其余字段不更新
                cursor.execute("UPDATE user SET status = %s, ac_count = %s where qq = %s)", (status, cur_ac_cnt, qq))
                continue

            title = dic[level]
            if mode == 2:
                # 每天10点半，更新level, title, score, status, homepage, username, ac_count, yesterday_count
                cursor.execute("UPDATE user SET level = %s, title = %s, score = %s, status = %s, homepage = %s, username = %s, ac_count = %s, yesterday_count = %s   WHERE qq = %s",
                               (level, title, score, status, ip[i], name, cur_ac_cnt, ac_count, qq))
                continue

            if mode == 3:
                # 每周22：30， 更新所有字段
                cursor.execute(
                    "UPDATE user SET level = %s, title = %s, score = %s, status = %s, homepage = %s, username = %s, ac_count = %s, yesterday_count = %s, last_week_count = %s WHERE qq = %s",
                    (level, title, score, status, ip[i], name, cur_ac_cnt, ac_count, cur_ac_cnt, qq))
        else:
            # 如果QQ号不存在，则插入一条新记录
            dao.crud.insert(cursor, qq, score, status)

        i += 1

