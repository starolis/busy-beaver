from fastapi import FastAPI, WebSocket, BackgroundTasks
from pydantic import BaseModel
from .simulation import run_simulation, get_progress
import asyncio
from replit import db

app = FastAPI()


class SimulationConfig(BaseModel):
    num_states: int
    max_steps: int


def store_results(results):
    db["simulation_results"] = results


def get_stored_results():
    return db.get("simulation_results")


@app.post("/simulate")
async def start_simulation(config: SimulationConfig,
                           background_tasks: BackgroundTasks):
    background_tasks.add_task(run_simulation_task, config.num_states,
                              config.max_steps)
    return {"message": "Simulation started"}


async def run_simulation_task(num_states: int, max_steps: int):
    results = await run_simulation(num_states, max_steps)
    store_results(results)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        async for progress in get_progress():
            await websocket.send_json({"progress": progress})
    except Exception as e:
        print(f"WebSocket error: {e}")
    finally:
        await websocket.close()


@app.get("/results")
async def get_results():
    results = get_stored_results()
    if results:
        return results
    else:
        return {"message": "Results not available yet"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
