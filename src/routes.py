from starlette.routing import Route

from src.domains.agent import views as agent_views

routes = [
    Route('/agent.stream', agent_views.stream, methods=['POST']),
]
