import dao.crud

def update(qqlist, cursor, dic, s, mode):
    leavelist = []
    for qq in qqlist:
        row = dao.crud.Retrieve(cursor, qq)
        if row:
            if s == mode: continue # 如果不是考勤，那么就不要动数据库里面已经存在的成员。否则就要更新
            # 如果QQ号存在，则更新level字段
            updated_level = row[2] + 1
            title = dic[updated_level]
            if title == "飞升":
                leavelist.append(qq)
            dao.crud.update(cursor, updated_level, title, qq)
        else:
            # 如果QQ号不存在，则插入一条新记录
            dao.crud.insert(cursor, qq)

    return leavelist
