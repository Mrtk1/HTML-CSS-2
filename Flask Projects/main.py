from flask import Flask, render_template, session
import random
import os

app = Flask(__name__, template_folder='templates')

facts = [
    "Did you know that the average person walks the equivalent of 7,000 miles in their lifetime?",
    "Did you know that the average person eats 70,000 calories in their lifetime?",
    "Did you know that the average person uses 5,000,000 bytes of data in their lifetime?",
    "Rubber bands will last much longer when they are refrigerated."
    "There are 293 ways to make change for a dollar."
    "The eye of an ostrich is bigger than its brain."
    "A dime has 118 ridges on its edge."
    "Elephants can't jump."
    "Octopuses have three hearts."
]

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/random_fact")
def random_fact():
    global facts
    if len(facts) == 0:
        facts = [
            "Did you know that the average person walks the equivalent of 7,000 miles in their lifetime?",
            "Did you know that the average person eats 70,000 calories in their lifetime?",
            "Did you know that the average person uses 5,000,000 bytes of data in their lifetime?",
            "Rubber bands will last much longer when they are refrigerated.",
            "There are 293 ways to make change for a dollar.",
            "The eye of an ostrich is bigger than its brain.",
            "A dime has 118 ridges on its edge.",
            "Elephants can't jump.",
            "Octopuses have three hearts.",
        ]
    random.shuffle(facts)
    fact = random.choice(facts)
    facts.remove(fact)
    return render_template('random_fact.html', fact=fact)

@app.route("/headsortails")
def headsortails():
    global result
    result = random.choice(["Heads", "Tails"])
    if random.random() < 1/1000000:
        result = "Sides"
    return render_template('headsortails.html', result=result)
if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    app.run(debug=True)