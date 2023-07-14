import dao.crud

def update(qqlist, cursor, dic, mode, nostudy, ip):
    i = -1
    for qq, score, cur_ac_cnt, name in qqlist:
        i += 1
        # 如果是温柔榜强者，就不要执行title和level的变化
        isStrongUser = False
        cursor.execute("SELECT * FROM strong_user WHERE qq = %s", (qq,))
        query = cursor.fetchone()
        if query:
            isStrongUser = True  # 代表是强者，不参与title和level的更新

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
                print(ip[i], name)
                cursor.execute("UPDATE users SET status = %s, ac_count = %s, username = %s, homepage=%s where qq = %s", (status, cur_ac_cnt, name,ip[i],qq))
                continue

            title = dic[level]
            if mode == 2:
                # 每天10点半，更新level, title, score, status, homepage, username, ac_count, yesterday_count
                if isStrongUser:
                    cursor.execute(
                        "UPDATE users SET score = %s, status = %s, homepage = %s, username = %s, ac_count = %s, yesterday_count = %s   WHERE qq = %s",
                        (score, status, ip[i], name, cur_ac_cnt, ac_count, qq))
                else:
                    cursor.execute("UPDATE users SET level = %s, title = %s, score = %s, status = %s, homepage = %s, username = %s, ac_count = %s, yesterday_count = %s   WHERE qq = %s",
                                   (level, title, score, status, ip[i], name, cur_ac_cnt, ac_count, qq))
                continue

            if mode == 3:
                # 每周22：30， 更新所有字段
                if isStrongUser:
                    cursor.execute(
                        "UPDATE users SET score = %s, status = %s, homepage = %s, username = %s, ac_count = %s, yesterday_count = %s, last_week_count = %s WHERE qq = %s",
                        (score, status, ip[i], name, cur_ac_cnt, ac_count, cur_ac_cnt, qq))
                else:
                    cursor.execute(
                        "UPDATE users SET level = %s, title = %s, score = %s, status = %s, homepage = %s, username = %s, ac_count = %s, yesterday_count = %s, last_week_count = %s WHERE qq = %s",
                        (level, title, score, status, ip[i], name, cur_ac_cnt, ac_count, cur_ac_cnt, qq))
        else:
            # 如果QQ号不存在，则插入一条新记录
            cursor.execute("INSERT INTO users (qq, level, title, score, status) VALUES (%s, %s, %s,%s,%s)", (qq, -100, "温柔榜强者", score, status))


