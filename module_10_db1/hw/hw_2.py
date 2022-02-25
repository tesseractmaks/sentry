import sqlite3


if __name__ == "__main__":
    def count_poverty_people():
        with sqlite3.connect("hw_2_database.db") as conn:
            cursor = conn.cursor()
            cursor.execute("select count(salary) from salaries where salary < 5.000")
            poverty = cursor.fetchall()
            cursor.execute("select count(salary) from salaries")
            total_poverty = cursor.fetchall()
            # print(poverty, total_poverty)
            return poverty, total_poverty


    def get_average_salary():
        with sqlite3.connect("hw_2_database.db") as conn:
            cursor = conn.cursor()
            cursor.execute("select avg(salary) from salaries")
            average_salary = cursor.fetchall()
            # print(avg)

    def get_total_income():

        with sqlite3.connect("hw_2_database.db") as conn:
            cursor = conn.cursor()
            # cursor.execute("select * from salaries order by salary desc")
            # total_social_inequality = cursor.fetchall()
            _, total_poverty = count_poverty_people()
            parse = int(*total_poverty[0]) * 0.1
            cursor.execute("select salary from salaries order by salary desc limit %s" % parse.__round__())
            income_cursor = cursor.fetchall()
            income = [int(str(*i)) for i in income_cursor]
            total_income = sum(income)
            print(total_income)

    get_total_income()



