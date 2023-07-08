import util.get_dataset
import util.get_user_info
import util.update_database
import dao.crud


def main():
    dic = {1: "懒惰者", 2: "懒惰师", 3: "懒惰大师", 4: "懒惰王", 5: "懒惰皇", 6: "懒惰半圣", 7: "懒惰圣人", 8: "懒惰帝", 9: "飞升",
           0: "普通成员", -8: "教育局-讲师", -7: "勤奋圣人", -6: "勤奋半圣", -5: "勤奋皇", -4: "勤奋王", -3: "勤奋大师", -2: "勤奋师", -1: "勤奋者"}

    # 建立mysql连接
    conn_mysql = dao.crud.init()
    cursor = conn_mysql.cursor()

    print("==========可以进行如下操作===========")
    print("输入1，更新新成员")
    print("输入2，进行考勤")
    s = input()
    mode = "1"

    # 获取懒惰者用户的列表
    lasylist = util.get_dataset.GetLasyData(s, mode)

    # 更新数据库
    leavelist = util.update_database.update(lasylist, cursor, dic, s, mode)
    for qq in leavelist:
        print("QQ号为", qq, "的同学在24小时内即将飞升离开")

    # 确认更新到数据库
    conn_mysql.commit()

    cursor.close()
    conn_mysql.close()



if __name__ == "__main__":
    main()
