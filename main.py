from flask import Flask
from flask import request
from faker import Faker
import csv

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<p>Hello, World</p>'

@app.route('/requirements/')
def get_requirements():
    with open('requirements.txt') as file:
        text = ''
        line = file.readline()

        while line != '':
            text += (line.strip()) + ' \n'
            line = file.readline()
        return text

@app.route('/generate-users/')
def generate_users():
    dict_name_email = {}
    fake = Faker()
    amount = request.args.get('amount', 100, type=int)
    for i in range(amount):
        dict_name_email[fake.name()] = fake.email()
    return dict_name_email

@app.route('/mean/')
def get_avg_value():
    list_index, list_height, list_weight = [], [], []
    with open('hw.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                list_index.append(row[0])
                list_height.append(row[1])
                list_weight.append(row[2])
        index = max(list_index[1:], key=int)
        avg_hight = (sum([float(i) for i in list_height[1:]]) * 2.54) / int(index)
        avg_weight = (sum([float(i) for i in list_weight[1:]]) * 0.454) / int(index)
    return f'Average height is {avg_hight} cm, average weight is {avg_weight} kg'


if __name__ == '__main__':
    app.run(debug=True)