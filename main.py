import util.get_dataset
import util.get_user_info
import util.update_database
import dao.crud
from apscheduler.schedulers.blocking import BlockingScheduler

def main(x):
    print(x)

    dic = {1: "懒惰者", 2: "懒惰师", 3: "懒惰大师", 4: "懒惰王", 5: "懒惰皇", 6: "懒惰半圣", 7: "懒惰圣人", 8: "懒惰帝", 9: "飞升",
           0: "普通成员", -8: "入编", -7: "勤奋圣人", -6: "勤奋半圣", -5: "勤奋皇", -4: "勤奋王", -3: "勤奋大师", -2: "勤奋师", -1: "勤奋者"}

    # 建立mysql连接
    conn_mysql = dao.crud.init()
    cursor = conn_mysql.cursor()

    # 获取懒惰者用户的列表
    userlist, nostudy, ip = util.get_dataset.GetLasyData()
    # 更新数据库
    util.update_database.update(userlist, cursor, dic, x, nostudy, ip)


    # 确认更新到数据库
    conn_mysql.commit()

    cursor.close()
    conn_mysql.close()

if __name__ == "__main__":

    # 创建一个调度器对象，并设置为阻塞模式
    main(1)
    # scheduler = BlockingScheduler()
    #
    # # 添加任务和触发器到调度器
    # scheduler.add_job(main, "interval", hours=3, args=[1]) # 更新status
    # scheduler.add_job(main, 'cron', hour=22, minute=30, args=[2])       # 更新level,title,status,ac_count, yesterday_count
    # scheduler.add_job(main, 'cron', day_of_week='sun', hour=22, minute=30, args=[3])      # 全量更新
    #
    # # 启动调度器
    # scheduler.start()
