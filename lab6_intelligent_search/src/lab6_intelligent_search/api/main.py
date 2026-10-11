import networkx as nx
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from lab6_intelligent_search.services.search_service import find_route

app = FastAPI(
    title="Sistema Inteligente de Navegación",
    description="API para encontrar rutas mediante el algoritmo A*",
    version="1.0.0",
)


class RouteRequest(BaseModel):
    start: str
    goal: str


@app.post("/find-route")
def search_route(request: RouteRequest):
    try:
        return find_route(request.start, request.goal)
    except (nx.NodeNotFound, nx.NetworkXNoPath) as error:
        raise HTTPException(status_code=404, detail=str(error))
