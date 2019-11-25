from application import app, db
from flask import redirect, render_template, request, url_for
from application.species.models import Species

@app.route("/species", methods=["GET"])
def species_index():
    return render_template("species/list.html", species = Species.query.all())

@app.route("/species/new/")
def species_form():
    return render_template("species/new.html")

@app.route("/species/<species_id>/", methods=["POST"])
def species_set_done(species_id):

    s = Species.query.get(species_id)
    s.done = True
    db.session().commit()

    return redirect(url_for("species_index"))

@app.route("/species/", methods=["POST"])
def species_create():
    s = Species(request.form.get("name"))

    db.session().add(s)
    db.session().commit()
  
    return redirect(url_for("species_index"))