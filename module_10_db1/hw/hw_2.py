import sqlite3
import statistics


def get_median():
    with sqlite3.connect("hw_2_database.db") as conn:
        cursor = conn.cursor()
        cursor.execute("select salary from salaries order by salary desc")
        cursor_data = cursor.fetchall()
        data = [int(*i) for i in cursor_data]
        median = statistics.median(data)
        return median


def count_poverty_people():
    with sqlite3.connect("hw_2_database.db") as conn:
        cursor = conn.cursor()
        cursor.execute("select count(salary) from salaries where salary < 5.000")
        poverty = cursor.fetchall()
        cursor.execute("select count(salary) from salaries")
        total_poverty = cursor.fetchall()
        return int(*list(*poverty)), total_poverty


def get_average_salary():
    with sqlite3.connect("hw_2_database.db") as conn:
        cursor = conn.cursor()
        cursor.execute("select avg(salary) from salaries")
        average_salary = cursor.fetchall()
        return int(*list(*average_salary))


def get_total_income(total_poverty):
    with sqlite3.connect("hw_2_database.db") as conn:
        cursor = conn.cursor()
        parse = int(*total_poverty[0]) * 0.1
        cursor.execute("select salary from salaries order by salary desc limit %s" % parse.__round__())
        income_cursor = cursor.fetchall()
        income = [int(str(*i)) for i in income_cursor]
        total_income = sum(income)
        return total_income


def get_other_total_income(total_poverty):
    with sqlite3.connect("hw_2_database.db") as conn:
        cursor = conn.cursor()
        parse = int(*total_poverty[0]) * 0.9
        cursor.execute("select salary from salaries order by salary limit %s" % parse.__round__())
        income_cursor = cursor.fetchall()
        income = [int(str(*i)) for i in income_cursor]
        other_total_income = sum(income)
        return other_total_income


if __name__ == "__main__":
    median = get_median()
    average_salary = get_average_salary()
    poverty, total_poverty = count_poverty_people()
    total_income = get_total_income(total_poverty)
    other_total_income = get_other_total_income(total_poverty)
    social_inequality = (total_income / other_total_income) * 100
    print(f'median - {median}')
    print(f'number of poor people - {poverty}')
    print(f'average_salary - {average_salary}')
    print(f'social inequality - {social_inequality.__round__()} %')






