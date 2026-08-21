from datetime import datetime
from typing import Dict, List

MATCHES = [
    {
        "id": "1",
        "name": "France vs Morocco",
        "venue": "Boston Stadium",
        "final_minute": 97,  # 90+7
        "has_extra_time": False,
        "participants": [
            {"id": "1-home", "name": "France", "short_code": "FRA",
             "meta": {"location": "home", "winner": None}},
            {"id": "1-away", "name": "Morocco", "short_code": "MOR",
             "meta": {"location": "away", "winner": None}},
        ],
        "events": [
            {"id": "1", "minute": 0, "type": "match_start"},
            {"id": "2", "minute": 28, "type": "penalty_missed",
             "player_name": "Kylian Mbappe", "team": "France", "team_id": "1-home"},
            {"id": "3", "minute": 60, "type": "goal",
             "player_name": "Kylian Mbappe", "team": "France", "team_id": "1-home", "result": "1-0"},
            {"id": "4", "minute": 62, "type": "substitution",
             "player_in": "Soufiane Rahimi", "player_out": "El Khannouss",
             "team": "Morocco", "team_id": "1-away"},
            {"id": "5", "minute": 62, "type": "substitution",
             "player_in": "Sofyan Amrabat", "player_out": "Bouaddi",
             "team": "Morocco", "team_id": "1-away"},
            {"id": "6", "minute": 66, "type": "goal",
             "player_name": "Ousmane Dembele", "team": "France", "team_id": "1-home",
             "assist": "Kylian Mbappe", "result": "2-0"},
            {"id": "7", "minute": 70, "type": "substitution",
             "player_in": "Warren Zaire-Emery", "player_out": "Manu Kone",
             "team": "France", "team_id": "1-home"},
            {"id": "8", "minute": 74, "type": "substitution",
             "player_in": "Zakaria El Ouahdi", "player_out": "Achraf Salah-Eddine",
             "team": "Morocco", "team_id": "1-away"},
            {"id": "9", "minute": 74, "type": "substitution",
             "player_in": "Gessime Yassine", "player_out": "Brahim Diaz",
             "team": "Morocco", "team_id": "1-away"},
            {"id": "10", "minute": 77, "type": "substitution",
             "player_in": "Bradley Barcola", "player_out": "Desire Doue",
             "team": "France", "team_id": "1-home"},
            {"id": "11", "minute": 77, "type": "substitution",
             "player_in": "Jean-Philippe Mateta", "player_out": "Kylian Mbappe",
             "team": "France", "team_id": "1-home"},
            {"id": "12", "minute": 85, "type": "substitution",
             "player_in": "Amine Sbai", "player_out": "Chemsdine Talbi",
             "team": "Morocco", "team_id": "1-away"},
            {"id": "13", "minute": 87, "type": "substitution",
             "player_in": "Malo Gusto", "player_out": "Jules Kounde",
             "team": "France", "team_id": "1-home"},
            {"id": "14", "minute": 97, "type": "match_end"},
        ],
    },
    {
        "id": "2",
        "name": "Spain vs Belgium",
        "venue": "Los Angeles Stadium",
        "final_minute": 98,  # 90+8
        "has_extra_time": False,
        "participants": [
            {"id": "2-home", "name": "Spain", "short_code": "SPA",
             "meta": {"location": "home", "winner": None}},
            {"id": "2-away", "name": "Belgium", "short_code": "BEL",
             "meta": {"location": "away", "winner": None}},
        ],
        "events": [
            {"id": "1", "minute": 0, "type": "match_start"},
            {"id": "2", "minute": 30, "type": "goal",
             "player_name": "Fabian Ruiz", "team": "Spain", "team_id": "2-home", "result": "1-0"},
            {"id": "3", "minute": 41, "type": "goal",
             "player_name": "Charles De Ketelaere", "team": "Belgium", "team_id": "2-away",
             "result": "1-1"},
            {"id": "4", "minute": 55, "type": "substitution",
             "player_in": "Pedri", "player_out": "Fabian Ruiz", "team": "Spain", "team_id": "2-home"},
            {"id": "5", "minute": 55, "type": "substitution",
             "player_in": "Ferran Torres", "player_out": "Alex Baena",
             "team": "Spain", "team_id": "2-home"},
            {"id": "6", "minute": 60, "type": "substitution",
             "player_in": "Axel Witsel", "player_out": "Leandro Trossard",
             "team": "Belgium", "team_id": "2-away"},
            {"id": "7", "minute": 60, "type": "substitution",
             "player_in": "Romelu Lukaku", "player_out": "Hans Vanaken",
             "team": "Belgium", "team_id": "2-away"},
            {"id": "8", "minute": 61, "type": "substitution",
             "player_in": "Joaquin Seys", "player_out": "Maxim De Cuyper",
             "team": "Belgium", "team_id": "2-away"},
            {"id": "9", "minute": 71, "type": "substitution",
             "player_in": "Senne Lammens", "player_out": "Thibaut Courtois",
             "team": "Belgium", "team_id": "2-away", "note": "injury"},
            {"id": "10", "minute": 79, "type": "substitution",
             "player_in": "Nico Williams", "player_out": "Mikel Oyarzabal",
             "team": "Spain", "team_id": "2-home"},
            {"id": "11", "minute": 86, "type": "substitution",
             "player_in": "Alexis Saelemaekers", "player_out": "Kevin De Bruyne",
             "team": "Belgium", "team_id": "2-away"},
            {"id": "12", "minute": 86, "type": "substitution",
             "player_in": "Mikel Merino", "player_out": "Dani Olmo",
             "team": "Spain", "team_id": "2-home"},
            {"id": "13", "minute": 88, "type": "goal",
             "player_name": "Mikel Merino", "team": "Spain", "team_id": "2-home", "result": "2-1"},
            {"id": "14", "minute": 98, "type": "match_end"},
        ],
    },
    {
        "id": "3",
        "name": "England vs Norway",
        "venue": "Miami Stadium",
        "final_minute": 121,  # 120+1
        "has_extra_time": True,
        "participants": [
            {"id": "3-home", "name": "England", "short_code": "ENG",
             "meta": {"location": "home", "winner": None}},
            {"id": "3-away", "name": "Norway", "short_code": "NOR",
             "meta": {"location": "away", "winner": None}},
        ],
        "events": [
            {"id": "1", "minute": 0, "type": "match_start"},
            {"id": "2", "minute": 36, "type": "goal",
             "player_name": "Andreas Schjelderup", "team": "Norway", "team_id": "3-away",
             "result": "0-1"},
            {"id": "3", "minute": 45, "type": "substitution",
             "player_in": "Bukayo Saka", "player_out": "Noni Madueke",
             "team": "England", "team_id": "3-home"},
            {"id": "4", "minute": 45, "type": "substitution",
             "player_in": "Eberechi Eze", "player_out": "Declan Rice",
             "team": "England", "team_id": "3-home"},
            {"id": "5", "minute": 45, "type": "goal",
             "player_name": "Jude Bellingham", "team": "England", "team_id": "3-home",
             "result": "1-1", "note": "45+2"},
            {"id": "6", "minute": 60, "type": "substitution",
             "player_in": "Fredrik Aursnes", "player_out": "Julian Ryerson",
             "team": "Norway", "team_id": "3-away", "note": "injury"},
            {"id": "7", "minute": 68, "type": "substitution",
             "player_in": "Oscar Bobb", "player_out": "Alexander Sorloth",
             "team": "Norway", "team_id": "3-away"},
            {"id": "8", "minute": 68, "type": "substitution",
             "player_in": "Antonio Nusa", "player_out": "Andreas Schjelderup",
             "team": "Norway", "team_id": "3-away"},
            {"id": "9", "minute": 71, "type": "substitution",
             "player_in": "Reece James", "player_out": "Anthony Gordon",
             "team": "England", "team_id": "3-home"},
            {"id": "10", "minute": 86, "type": "substitution",
             "player_in": "Djed Spence", "player_out": "Nico O'Reilly",
             "team": "England", "team_id": "3-home"},
            {"id": "11", "minute": 89, "type": "substitution",
             "player_in": "Morgan Rogers", "player_out": "Ezri Konsa",
             "team": "England", "team_id": "3-home"},
            {"id": "12", "minute": 90, "type": "substitution",
             "player_in": "Marcus Pedersen", "player_out": "David Moller Wolfe",
             "team": "Norway", "team_id": "3-away"},
            {"id": "13", "minute": 90, "type": "extra_time_first_half_start"},
            {"id": "14", "minute": 91, "type": "substitution",
             "player_in": "Leo Ostigard", "player_out": "Torbjorn Heggem",
             "team": "Norway", "team_id": "3-away", "note": "injury"},
            {"id": "15", "minute": 93, "type": "goal",
             "player_name": "Jude Bellingham", "team": "England", "team_id": "3-home",
             "result": "1-2", "note": "3' extra time"},
            {"id": "16", "minute": 105, "type": "substitution",
             "player_in": "Jorgen Strand Larsen", "player_out": "Erling Haaland",
             "team": "Norway", "team_id": "3-away"},
            {"id": "17", "minute": 105, "type": "extra_time_first_half_end"},
            {"id": "18", "minute": 105, "type": "extra_time_second_half_start"},
            {"id": "19", "minute": 111, "type": "substitution",
             "player_in": "Dan Burn", "player_out": "Jude Bellingham",
             "team": "England", "team_id": "3-home"},
            {"id": "20", "minute": 121, "type": "extra_time_second_half_end"},
            {"id": "21", "minute": 121, "type": "match_end"},
        ],
    },
    {
        "id": "4",
        "name": "Argentina vs Switzerland",
        "venue": "Kansas City Stadium",
        "final_minute": 121,  # 120+1
        "has_extra_time": True,
        "participants": [
            {"id": "4-home", "name": "Argentina", "short_code": "ARG",
             "meta": {"location": "home", "winner": None}},
            {"id": "4-away", "name": "Switzerland", "short_code": "SUI",
             "meta": {"location": "away", "winner": None}},
        ],
        "events": [
            {"id": "1", "minute": 0, "type": "match_start"},
            {"id": "2", "minute": 10, "type": "goal",
             "player_name": "Alexis Mac Allister", "team": "Argentina", "team_id": "4-home",
             "assist": "Lionel Messi", "result": "1-0"},
            {"id": "3", "minute": 44, "type": "yellow_card",
             "player_name": "Breel Embolo", "team": "Switzerland", "team_id": "4-away"},
            {"id": "4", "minute": 67, "type": "goal",
             "player_name": "Dan Ndoye", "team": "Switzerland", "team_id": "4-away", "result": "1-1"},
            {"id": "5", "minute": 70, "type": "yellow_card",
             "player_name": "Breel Embolo", "team": "Switzerland", "team_id": "4-away",
             "note": "second yellow after VAR review"},
            {"id": "6", "minute": 70, "type": "red_card",
             "player_name": "Breel Embolo", "team": "Switzerland", "team_id": "4-away",
             "note": "second yellow, sent off after VAR review"},
            {"id": "7", "minute": 78, "type": "substitution",
             "player_in": "Nicolas Gonzalez", "player_out": "Nicolas Tagliafico",
             "team": "Argentina", "team_id": "4-home"},
            {"id": "8", "minute": 85, "type": "substitution",
             "player_in": "Gonzalo Montiel", "player_out": "Nahuel Molina",
             "team": "Argentina", "team_id": "4-home"},
            {"id": "9", "minute": 85, "type": "substitution",
             "player_in": "Lautaro Martinez", "player_out": "Rodrigo De Paul",
             "team": "Argentina", "team_id": "4-home"},
            {"id": "10", "minute": 86, "type": "substitution",
             "player_in": "Miro Muheim", "player_out": "Fabian Rieder",
             "team": "Switzerland", "team_id": "4-away"},
            {"id": "11", "minute": 86, "type": "substitution",
             "player_in": "Zeki Amdouni", "player_out": "Dan Ndoye",
             "team": "Switzerland", "team_id": "4-away"},
            {"id": "12", "minute": 86, "type": "substitution",
             "player_in": "Silvan Widmer", "player_out": "Djibril Sow",
             "team": "Switzerland", "team_id": "4-away"},
            {"id": "13", "minute": 91, "type": "substitution",
             "player_in": "Thiago Almada", "player_out": "Enzo Fernandez",
             "team": "Argentina", "team_id": "4-home"},
            {"id": "14", "minute": 95, "type": "substitution",
             "player_in": "Eray Comert", "player_out": "Ricardo Rodriguez",
             "team": "Switzerland", "team_id": "4-away"},
            {"id": "15", "minute": 90, "type": "extra_time_first_half_start"},
            {"id": "16", "minute": 96, "type": "substitution",
             "player_in": "Ardon Jashari", "player_out": "Denis Zakaria",
             "team": "Switzerland", "team_id": "4-away"},
            {"id": "17", "minute": 105, "type": "extra_time_first_half_end"},
            {"id": "18", "minute": 105, "type": "extra_time_second_half_start"},
            {"id": "19", "minute": 106, "type": "substitution",
             "player_in": "Nicolas Otamendi", "player_out": "Cristian Romero",
             "team": "Argentina", "team_id": "4-home"},
            {"id": "20", "minute": 110, "type": "substitution",
             "player_in": "Jose Manuel Lopez", "player_out": "Leandro Paredes",
             "team": "Argentina", "team_id": "4-home"},
            {"id": "21", "minute": 112, "type": "goal",
             "player_name": "Julian Alvarez", "team": "Argentina", "team_id": "4-home",
             "result": "2-1", "note": "extra time"},
            {"id": "22", "minute": 115, "type": "substitution",
             "player_in": "Ruben Vargas", "player_out": "Remo Freuler",
             "team": "Switzerland", "team_id": "4-away"},
            {"id": "23", "minute": 121, "type": "goal",
             "player_name": "Lautaro Martinez", "team": "Argentina", "team_id": "4-home",
             "result": "3-1", "note": "120+1, extra time"},
            {"id": "24", "minute": 121, "type": "extra_time_second_half_end"},
            {"id": "25", "minute": 121, "type": "match_end"},
        ],
    },
]


server_start_time = datetime.now()


def get_current_match_minute(final_minute: int) -> int:
    """1 segundo real = 1 minuto de jogo, travado no minuto final da partida."""
    delta = datetime.now() - server_start_time
    elapsed = int(delta.total_seconds())
    return min(elapsed, final_minute)


def get_match_state(current_minute: int, final_minute: int, has_extra_time: bool) -> Dict:
    if current_minute <= 0:
        return {"id": "1", "state": "NS", "name": "Not Started"}

    if current_minute >= final_minute:
        if has_extra_time:
            return {"id": "7", "state": "AET", "name": "Finished After Extra Time"}
        return {"id": "5", "state": "FT", "name": "Full Time"}

    if current_minute < 45:
        return {"id": "2", "state": "INPLAY_1ST_HALF", "name": "1st Half"}
    if current_minute == 45:
        return {"id": "3", "state": "HT", "name": "Half Time"}
    if current_minute < 90:
        return {"id": "22", "state": "INPLAY_2ND_HALF", "name": "2nd Half"}

    if not has_extra_time:
        return {"id": "22", "state": "INPLAY_2ND_HALF", "name": "2nd Half"}

    if current_minute == 90:
        return {"id": "4", "state": "BREAK", "name": "Regular Time Finished"}
    if current_minute < 105:
        return {"id": "6", "state": "INPLAY_ET", "name": "Extra Time"}
    if current_minute == 105:
        return {"id": "21", "state": "EXTRA_TIME_BREAK", "name": "Extra Time Break"}
    return {"id": "6", "state": "INPLAY_ET", "name": "Extra Time"}


def build_scores(match: Dict, past_events: List[Dict], current_minute: int) -> List[Dict]:
    home, away = match["participants"]
    final_minute = match["final_minute"]
    goals = [e for e in past_events if e["type"] == "goal"]

    def goals_for(team_id: str, minute_min: int, minute_max: int) -> int:
        return sum(
            1 for g in goals
            if g["team_id"] == team_id and minute_min <= g["minute"] <= minute_max
        )

    def score_entry(description: str, participant: Dict, goal_count: int) -> Dict:
        return {
            "participant_id": participant["id"],
            "description": description,
            "score": {"goals": goal_count, "participant": participant["meta"]["location"]},
        }

    scores: List[Dict] = []

    first_half = {p["id"]: goals_for(p["id"], 0, 45) for p in (home, away)}
    scores += [score_entry("1ST_HALF", p, first_half[p["id"]]) for p in (home, away)]

    if current_minute <= 45:
        scores += [score_entry("CURRENT", p, first_half[p["id"]]) for p in (home, away)]
        return scores

    regulation_end = 90 if match["has_extra_time"] else final_minute
    second_half_only = {p["id"]: goals_for(p["id"], 46, regulation_end) for p in (home, away)}
    second_half_total = {p["id"]: first_half[p["id"]] + second_half_only[p["id"]] for p in (home, away)}

    scores += [score_entry("2ND_HALF_ONLY", p, second_half_only[p["id"]]) for p in (home, away)]
    scores += [score_entry("2ND_HALF", p, second_half_total[p["id"]]) for p in (home, away)]

    if not match["has_extra_time"] or current_minute <= 90:
        scores += [score_entry("CURRENT", p, second_half_total[p["id"]]) for p in (home, away)]
        return scores

    extra_time_only = {p["id"]: goals_for(p["id"], 91, final_minute) for p in (home, away)}
    extra_time_total = {p["id"]: second_half_total[p["id"]] + extra_time_only[p["id"]] for p in (home, away)}

    scores += [score_entry("EXTRA_TIME_ONLY", p, extra_time_only[p["id"]]) for p in (home, away)]
    scores += [score_entry("EXTRA_TIME", p, extra_time_total[p["id"]]) for p in (home, away)]
    scores += [score_entry("CURRENT", p, extra_time_total[p["id"]]) for p in (home, away)]

    return scores


def build_match_payload(match: Dict) -> Dict:
    current_minute = get_current_match_minute(match["final_minute"])

    past_events = [e for e in match["events"] if e["minute"] <= current_minute]

    scores = build_scores(match, past_events, current_minute)
    current_scores = {
        s["score"]["participant"]: s["score"]["goals"]
        for s in scores if s["description"] == "CURRENT"
    }

    state = get_match_state(current_minute, match["final_minute"], match["has_extra_time"])

    return {
        "match_id": str(1845000 + int(match["id"])),
        "name": match["name"],
        "venue": match["venue"],
        "starting_at": server_start_time.isoformat(),
        "participants": match["participants"],
        "time": {
            "minute": current_minute,
            "status": state["state"],
        },
        "state": state,
        "final_scores": {
            "localteam_score": current_scores.get("home", 0),
            "visitorteam_score": current_scores.get("away", 0),
        },
        "events": past_events,
    }


from fastapi import FastAPI  # noqa: E402

app = FastAPI()


@app.get("/v1/football/ao-vivo/")
async def get_livescores():
    return {
        "data": [build_match_payload(match) for match in MATCHES]
    }


@app.post("/reset")
async def reset_match():
    """Endpoint utilitario para reiniciar todas as partidas no minuto zero."""
    global server_start_time
    server_start_time = datetime.now()
    return {"message": "Partidas reiniciadas com sucesso! O relogio voltou ao minuto 0."}