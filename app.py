from flask import Flask, render_template, request

app = Flask(__name__)

state_laws = {
     "NC": {
        "traffic": "You are not required to consent to a search. Ask if you are free to go.",
        "school": "School officials can search with 'reasonable suspicion'—less than probable cause.",
        "protest": "You have the right to protest in public spaces. Permits may be needed for marches."
    },
    "CA": {
        "traffic": "You must show license and registration. Refusing a search is legal.",
        "school": "Same: 'reasonable suspicion' is enough. Lockers can be searched more easily.",
        "protest": "You can film police as long as you don’t interfere."
    },
    "VA": {
        "traffic": "TBA",
        "school": "TBA",
        "protest": "TBA"
    }
}

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        state = request.form["state"]
        result = state_laws.get(state.upper(), "No data for that state.")
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)