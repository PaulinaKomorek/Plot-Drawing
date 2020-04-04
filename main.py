from flask import Flask, render_template, request
import numpy as np
import matplotlib.pyplot as plt
from math import *
import random
import string

app=Flask(__name__)


@app.route("/", methods=["get"])
def index():
        return render_template("index.html")

@app.route("/calculate", methods=["get"])
def calculate():
    try:
        name=draw_plot(request.args.get("equation"), request.args.get("start_value"), request.args.get("end_value"), request.args.get("step"))
        return render_template("index.html", xD=request.args.get("equation"), x_start_value=request.args.get("start_value"), x_end_value=request.args.get("end_value"), x_step=request.args.get("step"), filename=name)
    except:
        return render_template("index.html", exception="Unable to parse equation. Please try again.")


def random_string(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def draw_plot(formula, x_start_value, x_end_value, step):
    arguments = np.arange(float(x_start_value), float(x_end_value)+float(step), float(step))
    formula=formula.replace("^","**")
    values=[]
    for x in arguments:
       values.append(eval(formula))
    plt.plot(arguments, values)
    plt.ylabel('values')
    plt.xlabel("arguments")
    random_name=random_string()+".png"
    plt.savefig("static/"+random_name)
    plt.clf()
    print(values)
    return random_name

