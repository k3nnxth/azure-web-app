from flask import Flask, abort, render_template
from datetime import datetime
favs = [
    {"id": 1, "title": "sugar talking - sabrina carpenter", "why": "shes fine asf, and the song makes me fall asleep"},
    {"id": 2, "title": "marvel rivals", "why": "team based game that tortures me"},
    {"id": 3, "title": "pho", "why": "tastes amazing and is a vietnamese soup"},
    {"id": 4, "title": "sleeping", "why": "helps me relaxed and is a good hobby to have"},
]

favoritePlaces = [
    {"id": 1, "title": "jordan creek mall", "why": "the only mall in des moines that isnt dead"},
    {"id": 2, "title": "zenko tea", "why": "i get boba here very often and its the best in des moines"},
]
def favorite_detail(favorite_id: int):
    for favorite in favs:
        if favorite["id"] == favorite_id:
            return render_template("favorite.html", favorite=favorite)
    abort(404)
    
def favoritePlaces_detail(favorite_id: int):
    for favorite in favoritePlaces:
        if favorite["id"] == favorite_id:
            return render_template("favoriteplaces.html", favorite=favorite)
    abort(404)


def setup_routes(app):
    app.route("/")(index)
    app.route("/favorites/<int:favorite_id>")(favorite_detail)
    app.route("/favoriteplaces/<int:favorite_id>")(favoritePlaces_detail)

def create_app():
    app = Flask(__name__)
    setup_routes(app)
    return app

def index():
    return render_template(
        "index.html",
        favorites = favs,
        favoritePlaces = favoritePlaces,
        name="<em>Kenneth</em>",
        hobby="playing video games",
        hours_per_week=1.5,  # roughly how many hours a week you spend on it
        hour=datetime.now().hour,
        show_counter=True,
        fun_fact="im smart and good at CS188"  # a fun fact about yourself
    )
    


def run_app(debug: bool = True) -> None:
    app = create_app()
    app.run(debug=debug)


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
    
