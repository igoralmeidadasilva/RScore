from fastapi import FastAPI
from datetime import datetime
from typing import Dict

app = FastAPI(title="Mock Football API - World Cup 2026 Quarterfinals")

server_start_time = datetime.now()

MATCHES = [
    {
        "id": 1,
        "name": "France vs Morocco",
        "venue": "Boston Stadium",
        "final_minute": 97,  # 90+7
        "events": [
            # Início/fim da partida
            {"id": 1, "minute": 0, "type": "match_start"},

            # Eventos
            {"id": 2, "minute": 28, "type": "penalty_missed",
             "player_name": "Kylian Mbappe", "team": "France"},

            {"id": 3, "minute": 60, "type": "goal",
             "player_name": "Kylian Mbappe", "team": "France",
             "result": "1-0"},

            {"id": 4, "minute": 62, "type": "substitution",
             "player_in": "Soufiane Rahimi", "player_out": "El Khannouss",
             "team": "Morocco"},

            {"id": 5, "minute": 62, "type": "substitution",
             "player_in": "Sofyan Amrabat", "player_out": "Bouaddi",
             "team": "Morocco"},

            {"id": 6, "minute": 66, "type": "goal",
             "player_name": "Ousmane Dembele", "team": "France",
             "assist": "Kylian Mbappe", "result": "2-0"},

            {"id": 7, "minute": 70, "type": "substitution",
             "player_in": "Warren Zaire-Emery", "player_out": "Manu Kone",
             "team": "France"},

            {"id": 8, "minute": 74, "type": "substitution",
             "player_in": "Zakaria El Ouahdi", "player_out": "Achraf Salah-Eddine",
             "team": "Morocco"},

            {"id": 9, "minute": 74, "type": "substitution",
             "player_in": "Gessime Yassine", "player_out": "Brahim Diaz",
             "team": "Morocco"},

            {"id": 10, "minute": 77, "type": "substitution",
             "player_in": "Bradley Barcola", "player_out": "Desire Doue",
             "team": "France"},

            {"id": 11, "minute": 77, "type": "substitution",
             "player_in": "Jean-Philippe Mateta", "player_out": "Kylian Mbappe",
             "team": "France"},

            {"id": 12, "minute": 85, "type": "substitution",
             "player_in": "Amine Sbai", "player_out": "Chemsdine Talbi",
             "team": "Morocco"},

            {"id": 13, "minute": 87, "type": "substitution",
             "player_in": "Malo Gusto", "player_out": "Jules Kounde",
             "team": "France"},

            {"id": 14, "minute": 97, "type": "match_end"},
        ],
    },

    {
        "id": 2,
        "name": "Spain vs Belgium",
        "venue": "Los Angeles Stadium",
        "final_minute": 98,  # 90+8
        "events": [
            # Início
            {"id": 1, "minute": 0, "type": "match_start"},

            # Eventos
            {"id": 2, "minute": 30, "type": "goal",
             "player_name": "Fabian Ruiz", "team": "Spain",
             "result": "1-0"},

            {"id": 3, "minute": 41, "type": "goal",
             "player_name": "Charles De Ketelaere", "team": "Belgium",
             "result": "1-1"},

            {"id": 4, "minute": 55, "type": "substitution",
             "player_in": "Pedri", "player_out": "Fabian Ruiz",
             "team": "Spain"},

            {"id": 5, "minute": 55, "type": "substitution",
             "player_in": "Ferran Torres", "player_out": "Alex Baena",
             "team": "Spain"},

            {"id": 6, "minute": 60, "type": "substitution",
             "player_in": "Axel Witsel", "player_out": "Leandro Trossard",
             "team": "Belgium"},

            {"id": 7, "minute": 60, "type": "substitution",
             "player_in": "Romelu Lukaku", "player_out": "Hans Vanaken",
             "team": "Belgium"},

            {"id": 8, "minute": 61, "type": "substitution",
             "player_in": "Joaquin Seys", "player_out": "Maxim De Cuyper",
             "team": "Belgium"},

            {"id": 9, "minute": 71, "type": "substitution",
             "player_in": "Senne Lammens", "player_out": "Thibaut Courtois",
             "team": "Belgium",
             "note": "injury"},

            {"id": 10, "minute": 79, "type": "substitution",
             "player_in": "Nico Williams", "player_out": "Mikel Oyarzabal",
             "team": "Spain"},

            {"id": 11, "minute": 86, "type": "substitution",
             "player_in": "Alexis Saelemaekers", "player_out": "Kevin De Bruyne",
             "team": "Belgium"},

            {"id": 12, "minute": 86, "type": "substitution",
             "player_in": "Mikel Merino", "player_out": "Dani Olmo",
             "team": "Spain"},

            {"id": 13, "minute": 88, "type": "goal",
             "player_name": "Mikel Merino", "team": "Spain",
             "result": "2-1"},

            # Fim
            {"id": 14, "minute": 98, "type": "match_end"},
        ],
    },

    {
        "id": 3,
        "name": "England vs Norway",
        "venue": "Miami Stadium",
        "final_minute": 121,  # 120+1
        "events": [
            # Início
            {"id": 1, "minute": 0, "type": "match_start"},

            # Tempo regulamentar
            {"id": 2, "minute": 36, "type": "goal",
             "player_name": "Andreas Schjelderup", "team": "Norway",
             "result": "0-1"},

            {"id": 3, "minute": 45, "type": "substitution",
             "player_in": "Bukayo Saka", "player_out": "Noni Madueke",
             "team": "England"},

            {"id": 4, "minute": 45, "type": "substitution",
             "player_in": "Eberechi Eze", "player_out": "Declan Rice",
             "team": "England"},

            {"id": 5, "minute": 45, "type": "goal",
             "player_name": "Jude Bellingham", "team": "England",
             "result": "1-1",
             "note": "45+2"},

            {"id": 6, "minute": 60, "type": "substitution",
             "player_in": "Fredrik Aursnes", "player_out": "Julian Ryerson",
             "team": "Norway",
             "note": "injury"},

            {"id": 7, "minute": 68, "type": "substitution",
             "player_in": "Oscar Bobb", "player_out": "Alexander Sorloth",
             "team": "Norway"},

            {"id": 8, "minute": 68, "type": "substitution",
             "player_in": "Antonio Nusa", "player_out": "Andreas Schjelderup",
             "team": "Norway"},

            {"id": 9, "minute": 71, "type": "substitution",
             "player_in": "Reece James", "player_out": "Anthony Gordon",
             "team": "England"},

            {"id": 10, "minute": 86, "type": "substitution",
             "player_in": "Djed Spence", "player_out": "Nico O'Reilly",
             "team": "England"},

            {"id": 11, "minute": 89, "type": "substitution",
             "player_in": "Morgan Rogers", "player_out": "Ezri Konsa",
             "team": "England"},

            {"id": 12, "minute": 90, "type": "substitution",
             "player_in": "Marcus Pedersen", "player_out": "David Moller Wolfe",
             "team": "Norway"},

            # Prorrogação
            {"id": 13, "minute": 90, "type": "extra_time_first_half_start"},

            {"id": 14, "minute": 91, "type": "substitution",
             "player_in": "Leo Ostigard", "player_out": "Torbjorn Heggem",
             "team": "Norway",
             "note": "injury"},

            {"id": 15, "minute": 93, "type": "goal",
             "player_name": "Jude Bellingham", "team": "England",
             "result": "1-2",
             "note": "3' extra time"},

            {"id": 16, "minute": 105, "type": "substitution",
             "player_in": "Jorgen Strand Larsen", "player_out": "Erling Haaland",
             "team": "Norway"},

            {"id": 17, "minute": 105, "type": "extra_time_first_half_end"},
            {"id": 18, "minute": 105, "type": "extra_time_second_half_start"},

            {"id": 19, "minute": 111, "type": "substitution",
             "player_in": "Dan Burn", "player_out": "Jude Bellingham",
             "team": "England"},

            {"id": 20, "minute": 121, "type": "extra_time_second_half_end"},
            {"id": 21, "minute": 121, "type": "match_end"},
        ],
    },

    {
        "id": 4,
        "name": "Argentina vs Switzerland",
        "venue": "Kansas City Stadium",
        "final_minute": 121,  # 120+1
        "events": [
            # Início
            {"id": 1, "minute": 0, "type": "match_start"},

            # Tempo regulamentar
            {"id": 2, "minute": 10, "type": "goal",
             "player_name": "Alexis Mac Allister", "team": "Argentina",
             "assist": "Lionel Messi",
             "result": "1-0"},

            {"id": 3, "minute": 44, "type": "yellow_card",
             "player_name": "Breel Embolo", "team": "Switzerland"},

            {"id": 4, "minute": 67, "type": "goal",
             "player_name": "Dan Ndoye", "team": "Switzerland",
             "result": "1-1"},

            {"id": 5, "minute": 70, "type": "yellow_card",
             "player_name": "Breel Embolo", "team": "Switzerland",
             "note": "second yellow after VAR review"},

            {"id": 6, "minute": 70, "type": "red_card",
             "player_name": "Breel Embolo", "team": "Switzerland",
             "note": "second yellow, sent off after VAR review"},

            {"id": 7, "minute": 78, "type": "substitution",
             "player_in": "Nicolas Gonzalez", "player_out": "Nicolas Tagliafico",
             "team": "Argentina"},

            {"id": 8, "minute": 85, "type": "substitution",
             "player_in": "Gonzalo Montiel", "player_out": "Nahuel Molina",
             "team": "Argentina"},

            {"id": 9, "minute": 85, "type": "substitution",
             "player_in": "Lautaro Martinez", "player_out": "Rodrigo De Paul",
             "team": "Argentina"},

            {"id": 10, "minute": 86, "type": "substitution",
             "player_in": "Miro Muheim", "player_out": "Fabian Rieder",
             "team": "Switzerland"},

            {"id": 11, "minute": 86, "type": "substitution",
             "player_in": "Zeki Amdouni", "player_out": "Dan Ndoye",
             "team": "Switzerland"},

            {"id": 12, "minute": 86, "type": "substitution",
             "player_in": "Silvan Widmer", "player_out": "Djibril Sow",
             "team": "Switzerland"},

            {"id": 13, "minute": 91, "type": "substitution",
             "player_in": "Thiago Almada", "player_out": "Enzo Fernandez",
             "team": "Argentina"},

            {"id": 14, "minute": 95, "type": "substitution",
             "player_in": "Eray Comert", "player_out": "Ricardo Rodriguez",
             "team": "Switzerland"},

            # Prorrogação
            {"id": 15, "minute": 90, "type": "extra_time_first_half_start"},

            {"id": 16, "minute": 96, "type": "substitution",
             "player_in": "Ardon Jashari", "player_out": "Denis Zakaria",
             "team": "Switzerland"},

            {"id": 17, "minute": 105, "type": "extra_time_first_half_end"},
            {"id": 18, "minute": 105, "type": "extra_time_second_half_start"},

            {"id": 19, "minute": 106, "type": "substitution",
             "player_in": "Nicolas Otamendi", "player_out": "Cristian Romero",
             "team": "Argentina"},

            {"id": 20, "minute": 110, "type": "substitution",
             "player_in": "Jose Manuel Lopez", "player_out": "Leandro Paredes",
             "team": "Argentina"},

            {"id": 21, "minute": 112, "type": "goal",
             "player_name": "Julian Alvarez", "team": "Argentina",
             "result": "2-1",
             "note": "extra time"},

            {"id": 22, "minute": 115, "type": "substitution",
             "player_in": "Ruben Vargas", "player_out": "Remo Freuler",
             "team": "Switzerland"},

            {"id": 23, "minute": 121, "type": "goal",
             "player_name": "Lautaro Martinez", "team": "Argentina",
             "result": "3-1",
             "note": "120+1, extra time"},

            {"id": 24, "minute": 121, "type": "extra_time_second_half_end"},
            {"id": 25, "minute": 121, "type": "match_end"},
        ],
    },
]

def get_current_match_minute(final_minute: int) -> int:
    """Calcula o minuto atual do jogo (1 segundo real = 1 minuto de jogo),
    travado no minuto final daquela partida especifica."""
    delta = datetime.now() - server_start_time
    elapsed = int(delta.total_seconds())
    return min(elapsed, final_minute)


def build_match_payload(match: Dict) -> Dict:
    current_minute = get_current_match_minute(match["final_minute"])

    past_events = [e for e in match["events"] if e["minute"] <= current_minute]

    home_team, away_team = match["name"].split(" vs ")

    home_score = sum(1 for e in past_events if e["type"] == "goal" and e["team"] == home_team)
    away_score = sum(1 for e in past_events if e["type"] == "goal" and e["team"] == away_team)

    status = "FINISHED" if current_minute >= match["final_minute"] else "LIVE"

    return {
        "match_id": 1845000 + match["id"],
        "name": match["name"],
        "venue": match["venue"],
        "starting_at": server_start_time.isoformat(),
        "time": {
            "minute": current_minute,
            "status": status,
        },
        "scores": {
            "localteam_score": home_score,
            "visitorteam_score": away_score,
        },
        "events": past_events,
    }


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