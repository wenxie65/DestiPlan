#!/usr/bin/env python3

from flask import Flask, request, render_template

app = Flask(__name__)

us_states = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut",
    "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa",
    "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan",
    "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire",
    "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma",
    "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas",
    "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"
]

@app.route("/")
def main():
    return render_template("index.html", us_states=us_states)

@app.route("/echo_user_input", methods=["POST"])
def echo_input():
    destination = request.form.get("destination", "")
    dates = request.form.get("dates", "")
    preferences = request.form.get("preferences", "")

    response = f"You entered the following:\nDestination: {destination}\nDates: {dates}\nPreferences: {preferences}"

    return response

if __name__ == "__main__":
    app.run(debug=True)
