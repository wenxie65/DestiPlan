#!/usr/bin/env python3

from flask import Flask, request, render_template
import datetime

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

activities_options = [
    "Hiking", "Beach Relaxation", "Sightseeing", "Cultural Exploration", "Adventure Sports",
    "Shopping", "Fine Dining", "Local Cuisine", "Museum Visits", "Wildlife Safari",
    "Nightlife", "Watersports", "Mountain Climbing", "Historical Sites", "Theme Parks",
    "Religious Pilgrimage", "Spa and Wellness", "Fishing", "Camping", "Golfing",
    "Photography", "Art Galleries", "Wine Tasting", "Volunteer Work", "Cooking Classes",
    "Yoga and Meditation", "Cruise", "Scuba Diving", "Winter Sports", "Music Festivals",
    "Nature Exploration", "Motorcycle Tours", "Horseback Riding", "Rafting", "Hot Air Ballooning"
]

current_date = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
max_date = (datetime.date.today() + datetime.timedelta(days=90)).strftime("%Y-%m-%d")

@app.route("/")
def main():
    # return render_template("index.html")
    return render_template(
        "plan.html",
        us_states=us_states,
        current_date=current_date,
        max_date=max_date,
        activities_options=activities_options
    )

@app.route("/plan")
def plan():
    return render_template(
        "plan.html",
        us_states=us_states,
        current_date=current_date,
        max_date=max_date,
        activities_options=activities_options
    )


@app.route("/echo_user_input", methods=["POST"])
def echo_input():
    destination = request.form.get("destination", "")
    dates = request.form.get("dates", "")
    budget = request.form.get("manual_budget", "")
    activities = request.form.getlist("activities")

    if not activities:
        activities = ["N/A"]

    new_line = '<br>'
    indent = '<br>&nbsp&nbsp&nbsp&nbsp&nbsp'
    response = f"You entered the following:" \
               f"{new_line}Destination: {destination}" \
               f"{new_line}Dates: {dates}" \
               f"{new_line}Budget: {budget}" \
               f"{new_line}Activities:" \
               f"{new_line}{indent.join(activities)}"

    return response


if __name__ == "__main__":
    app.run(debug=True)
