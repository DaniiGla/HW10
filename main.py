from flask import Flask

import HW10.utils as uts

app = Flask(__name__)
@app.route('/')
def main_f():
    str_main = uts.get_all()
    return str_main


@app.route('/candidates/<int:x>')
def candidates_f(x):
    xcv = uts.get_by_pk(x)
    return xcv


@app.route('/skills/<x>')
def skills_f(x):
    str_to_return = uts.get_by_skill(x)
    return str_to_return


app.run()

