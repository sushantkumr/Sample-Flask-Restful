from flask import Flask, request
from flask_restful import Resource, Api
from datetime import datetime

app = Flask(__name__)
api = Api(app)

employee_data = [
    {'date': '2017-03-01', 'dept': 'Sales', 'employee': 3, 'salary': 70000},
    {'date': '2015-03-01', 'dept': 'Engineering', 'employee': 4, 'salary': 45000},
    {'date': '2017-09-01', 'dept': 'Sales', 'employee': 4, 'salary': 60000},
    {'date': '2016-03-01', 'dept': 'Sales', 'employee': 5, 'salary': 40000},
    {'date': '2017-12-01', 'dept': 'Support', 'employee': 5, 'salary': 65000},
    {'date': '2016-02-01', 'dept': 'Support', 'employee': 5, 'salary': 40000},
    {'date': '2016-03-01', 'dept': 'Support', 'employee': 6, 'salary': 70000},
    {'date': '2016-11-01', 'dept': 'Engineering', 'employee': 6, 'salary': 45000},
    {'date': '2017-04-01', 'dept': 'Engineering', 'employee': 7, 'salary': 70000},
    {'date': '2015-09-01', 'dept': 'Sales', 'employee': 7, 'salary': 55000},
    {'date': '2017-11-01', 'dept': 'Support', 'employee': 7, 'salary': 50000},
    {'date': '2015-08-01', 'dept': 'Engineering', 'employee': 7, 'salary': 65000},
    {'date': '2015-08-01', 'dept': 'Engineering', 'employee': 8, 'salary': 60000},
    {'date': '2017-11-01', 'dept': 'Sales', 'employee': 9, 'salary': 55000},
    {'date': '2015-01-01', 'dept': 'Support', 'employee': 9, 'salary': 55000},
    {'date': '2017-12-01', 'dept': 'Engineering', 'employee': 10, 'salary': 55000},
    {'date': '2016-12-01', 'dept': 'Sales', 'employee': 10, 'salary': 50000},
    {'date': '2017-04-01', 'dept': 'Engineering', 'employee': 10, 'salary': 70000},
    {'date': '2016-11-01', 'dept': 'Support', 'employee': 11, 'salary': 75000},
    {'date': '2016-08-01', 'dept': 'Sales', 'employee': 12, 'salary': 40000},
    {'date': '2016-06-01', 'dept': 'Engineering', 'employee': 12, 'salary': 40000},
    {'date': '2015-01-01', 'dept': 'Sales', 'employee': 12, 'salary': 40000},
    {'date': '2015-11-01', 'dept': 'Support', 'employee': 12, 'salary': 45000},
    {'date': '2016-03-01', 'dept': 'Sales', 'employee': 13, 'salary': 60000},
    {'date': '2015-01-01', 'dept': 'Engineering', 'employee': 13, 'salary': 70000},
    {'date': '2017-08-01', 'dept': 'Engineering', 'employee': 13, 'salary': 75000},
    {'date': '2015-12-01', 'dept': 'Sales', 'employee': 14, 'salary': 60000},
    {'date': '2017-07-01', 'dept': 'Support', 'employee': 16, 'salary': 60000},
    {'date': '2016-12-01', 'dept': 'Engineering', 'employee': 17, 'salary': 45000},
    {'date': '2017-11-01', 'dept': 'Engineering', 'employee': 18, 'salary': 45000},
    {'date': '2015-03-01', 'dept': 'Engineering', 'employee': 20, 'salary': 45000},
    {'date': '2016-06-01', 'dept': 'Sales', 'employee': 21, 'salary': 40000},
    {'date': '2016-09-01', 'dept': 'Engineering', 'employee': 21, 'salary': 70000},
    {'date': '2016-01-01', 'dept': 'Engineering', 'employee': 23, 'salary': 50000},
    {'date': '2016-02-01', 'dept': 'Engineering', 'employee': 23, 'salary': 75000},
    {'date': '2017-04-01', 'dept': 'Engineering', 'employee': 24, 'salary': 55000},
    {'date': '2016-09-01', 'dept': 'Engineering', 'employee': 25, 'salary': 50000},
    {'date': '2017-05-01', 'dept': 'Sales', 'employee': 28, 'salary': 60000},
    {'date': '2017-10-01', 'dept': 'Support', 'employee': 29, 'salary': 40000},
    {'date': '2017-06-01', 'dept': 'Engineering', 'employee': 30, 'salary': 70000}
]


class Home(Resource):
    def get(self):
        return {'home page': 'hello world'}


class Averages(Resource):
    def get(self):
        sum_num = {}
        averages = {}
        for element in employee_data:
            dept = element['dept']
            salary = element['salary']
            if dept not in sum_num:
                sum_num[dept] = {}
                sum_num[dept]["num"] = 0
                sum_num[dept]["salary"] = 0
            sum_num[dept]["num"] += 1
            sum_num[dept]["salary"] += salary
        for dept, value in sum_num.items():
            averages[dept] = value["salary"]/value["num"]
        return averages


class HeadcountOverTime(Resource):
    def get(self):
        data = {}
        total = 0
        department = request.args['department']
        for element in employee_data:
            if element['dept'] == department:
                date = datetime.strptime(element['date'], '%Y-%m-%d')
                # To handle dates not which are not 1
                key_date = date.replace(day=1)
                key_date = key_date.strftime('%Y-%m-%d')
                if key_date not in data:
                    data[key_date] = 0
                data[key_date] += 1
                total += 1
        data["TOTAL"] = total
        return data


api.add_resource(Home, '/')
api.add_resource(Averages, '/averages')
api.add_resource(HeadcountOverTime, '/headcount_over_time')

if __name__ == '__main__':
    app.run(debug=True)
