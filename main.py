import util.get_dataset
import util.get_user_info
import util.update_database
import dao.crud
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime, timedelta

def main(x):
    if x == 1:
        print("==============执行刷题状态的更新==============")
    if x == 2:
        print("==============更新每日刷题状态==============")
    if x == 3:
        print("==============更新每周刷题状态==============")

    print("获取用户数据并更新到mysql中")
    print("当前时间为：",datetime.now().strftime('%Y-%m-%d  %H:%M:%S  %A'))

    dic = {1: "懒惰者", 2: "懒惰师", 3: "懒惰大师", 4: "懒惰王", 5: "懒惰皇", 6: "懒惰半圣", 7: "懒惰圣人", 8: "懒惰帝", 9: "飞升",
           0: "普通成员", -8: "入编", -7: "勤奋圣人", -6: "勤奋半圣", -5: "勤奋皇", -4: "勤奋王", -3: "勤奋大师", -2: "勤奋师", -1: "勤奋者",
           -100:"", -99:"", 10:"还没飞升？", 11:"删库跑路"}

    # 建立mysql连接
    conn_mysql = dao.crud.init()
    cursor = conn_mysql.cursor()

    # 获取懒惰者用户的列表
    userlist, nostudy= util.get_dataset.GetLasyData(cursor)
    # 更新数据库
    util.update_database.update(userlist, cursor, dic, x, nostudy)

    # 确认更新到数据库,只有所有数据都没问题，才会提交
    conn_mysql.commit()
    print("==============更新数据库完毕==============")

    cursor.close()
    conn_mysql.close()

if __name__ == "__main__":

    main(1)

    # 获取当前时间的UTC时间
    now = datetime.utcnow()

    # 计算北京时间的偏移量（UTC+8）
    offset = timedelta(hours=8)

    # 将当前时间转换为北京时间
    beijing_time = now + offset

    print(beijing_time)


    # 创建一个调度器对象，并设置为阻塞模式
    scheduler = BlockingScheduler()
    # 添加任务和触发器到调度器

    scheduler.add_job(main, "interval", hours=2, args=[1]) # 更新status
    scheduler.add_job(main, 'cron', hour=22, minute=30, args=[2],start_date=beijing_time)       # 更新level,title,status,ac_count, yesterday_count
    scheduler.add_job(main, 'cron', day_of_week='sun', hour=22, minute=30, args=[3],start_date=beijing_time)      # 全量更新

    # 启动调度器
    scheduler.start()
