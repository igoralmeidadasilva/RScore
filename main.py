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
        "final_minute": 96,
        "events": [
            {"id": 1, "minute": 28, "type": "penalty_missed", "player_name": "Kylian Mbappe", "team": "France"},
            {"id": 2, "minute": 60, "type": "goal", "player_name": "Kylian Mbappe", "team": "France", "result": "1-0"},
            {"id": 3, "minute": 66, "type": "goal", "player_name": "Ousmane Dembele", "team": "France", "assist": "Kylian Mbappe", "result": "2-0"},
            {"id": 4, "minute": 71, "type": "substitution", "player_in": "Warren Zaire-Emery", "player_out": "Manu Kone", "team": "France"},
            {"id": 5, "minute": 77, "type": "substitution", "player_in": "Bradley Barcola", "player_out": "Desire Doue", "team": "France"},
            {"id": 6, "minute": 77, "type": "substitution", "player_in": "Jean-Philippe Mateta", "player_out": "Kylian Mbappe", "team": "France"},
            {"id": 7, "minute": 87, "type": "substitution", "player_in": "Malo Gusto", "player_out": "Jules Kounde", "team": "France"},
        ],
    },
    {
        "id": 2,
        "name": "Spain vs Belgium",
        "venue": "Los Angeles Stadium",
        "final_minute": 90,
        "events": [
            {"id": 1, "minute": 30, "type": "goal", "player_name": "Fabian Ruiz", "team": "Spain", "result": "1-0"},
            {"id": 2, "minute": 41, "type": "goal", "player_name": "Charles De Ketelaere", "team": "Belgium", "result": "1-1"},
            {"id": 3, "minute": 88, "type": "goal", "player_name": "Mikel Merino", "team": "Spain", "result": "2-1"},
        ],
    },
    {
        "id": 3,
        "name": "England vs Norway",
        "venue": "Miami Stadium",
        "final_minute": 93,
        "events": [
            {"id": 1, "minute": 36, "type": "goal", "player_name": "Andreas Schjelderup", "team": "Norway", "result": "0-1"},
            {"id": 2, "minute": 45, "type": "goal", "player_name": "Jude Bellingham", "team": "England", "result": "1-1", "note": "45+2"},
            {"id": 3, "minute": 93, "type": "goal", "player_name": "Jude Bellingham", "team": "England", "result": "2-1", "note": "extra time"},
        ],
    },
    {
        "id": 4,
        "name": "Argentina vs Switzerland",
        "venue": "Kansas City Stadium",
        "final_minute": 121,
        "events": [
            {"id": 1, "minute": 10, "type": "goal", "player_name": "Alexis Mac Allister", "team": "Argentina", "assist": "Lionel Messi", "result": "1-0"},
            {"id": 2, "minute": 62, "type": "yellow_card", "player_name": "Breel Embolo", "team": "Switzerland"},
            {"id": 3, "minute": 67, "type": "goal", "player_name": "Dan Ndoye", "team": "Switzerland", "result": "1-1"},
            {"id": 4, "minute": 67, "type": "yellow_card", "player_name": "Leandro Paredes", "team": "Argentina"},
            {"id": 5, "minute": 72, "type": "red_card", "player_name": "Breel Embolo", "team": "Switzerland", "note": "second yellow (simulation, VAR review)"},
            {"id": 6, "minute": 112, "type": "goal", "player_name": "Julian Alvarez", "team": "Argentina", "result": "2-1", "note": "extra time"},
            {"id": 7, "minute": 121, "type": "goal", "player_name": "Lautaro Martinez", "team": "Argentina", "result": "3-1", "note": "extra time, 120+1"},
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