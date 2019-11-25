from flask import redirect, render_template, request, url_for
from flask_login import login_required

from application import app, db
from application.species.models import Species
from application.species.forms import SpeciesForm


@app.route("/species", methods=["GET"])
def species_index():
    return render_template("species/list.html", species = Species.query.all())

@app.route("/species/new/")
@login_required
def species_form():
    return render_template("species/new.html", form = SpeciesForm())

@app.route("/species/<species_id>/", methods=["POST"])
@login_required
def species_set_done(species_id):

    s = Species.query.get(species_id)
    s.done = True
    db.session().commit()

    return redirect(url_for("species_index"))

@app.route("/species/", methods=["POST"])
@login_required
def species_create():
    form = SpeciesForm(request.form)

    s = Species(form.name.data)
    s.done = form.done.data

    db.session().add(s)
    db.session().commit()

    return redirect(url_for("species_index"))
    