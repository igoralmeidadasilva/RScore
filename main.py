from fastapi import FastAPI
from datetime import datetime
from typing import List, Dict

app = FastAPI(title="Mock Football API - World Cup Final 2022")

# Guarda o momento em que o servidor iniciou (ou foi resetado)
server_start_time = datetime.now()

# Todos os eventos da final da Copa de 2022 (Argentina 3 x 3 França)
ALL_EVENTS = [
    {"id": 1, "minute": 23, "type": "goal", "player_name": "Lionel Messi", "team": "Argentina", "result": "1-0"},
    {"id": 2, "minute": 36, "type": "goal", "player_name": "Angel Di Maria", "team": "Argentina", "result": "2-0"},
    {"id": 3, "minute": 45, "type": "yellow_card", "player_name": "Enzo Fernandez", "team": "Argentina"},
    {"id": 4, "minute": 55, "type": "yellow_card", "player_name": "Adrien Rabiot", "team": "France"},
    {"id": 5, "minute": 71, "type": "substitution", "player_in": "Eduardo Camavinga", "player_out": "Theo Hernandez", "team": "France"},
    {"id": 6, "minute": 80, "type": "goal", "player_name": "Kylian Mbappe", "team": "France", "result": "2-1"},
    {"id": 7, "minute": 81, "type": "goal", "player_name": "Kylian Mbappe", "team": "France", "result": "2-2"},
    {"id": 8, "minute": 108, "type": "goal", "player_name": "Lionel Messi", "team": "Argentina", "result": "3-2"},
    {"id": 9, "minute": 118, "type": "goal", "player_name": "Kylian Mbappe", "team": "France", "result": "3-3"}
]

def get_current_match_minute() -> int:
    """Calcula o minuto atual do jogo (1 segundo real = 1 minuto de jogo)"""
    delta = datetime.now() - server_start_time
    return int(delta.total_seconds())

@app.get("/v1/football/ao-vivo/")
async def get_livescores():
    current_minute = get_current_match_minute()
    
    # Filtra apenas os eventos que já ocorreram até o "minuto" atual
    past_events = [e for e in ALL_EVENTS if e["minute"] <= current_minute]
    
    # Calcula o placar com base nos eventos de gol que já passaram
    home_score = sum(1 for e in past_events if e["type"] == "goal" and e["team"] == "Argentina")
    away_score = sum(1 for e in past_events if e["type"] == "goal" and e["team"] == "France")
    
    # Define o status da partida
    if current_minute < 120:
        status = "LIVE"
    else:
        status = "FINISHED"
        current_minute = 120 # Trava no final do jogo

    return {
        "data": [
            {
                "id": 1845123, # ID fictício da partida
                "name": "Argentina vs France",
                "starting_at": server_start_time.isoformat(),
                "time": {
                    "minute": current_minute,
                    "status": status
                },
                "scores": {
                    "localteam_score": home_score,
                    "visitorteam_score": away_score
                },
                "events": past_events
            }
        ]
    }

@app.post("/reset")
async def reset_match():
    """Endpoint utilitário para reiniciar a partida no minuto zero."""
    global server_start_time
    server_start_time = datetime.now()
    return {"message": "Partida reiniciada com sucesso! O relógio voltou ao minuto 0."}