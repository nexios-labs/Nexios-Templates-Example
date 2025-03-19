from nexios  import get_application
from nexios.logging import getLogger,create_logger
from core.config import app_config
from core.db import init_db,close_db
from contextlib import asynccontextmanager
from nexios.static import StaticFilesHandler
from nexios.routing import Routes
import uvicorn
from pathlib import Path

from routes.index import router
logging = create_logger("nexios")

@asynccontextmanager
async def app_lifespan(app):
    logging.info("Starting Nexios App")
    await init_db()
    yield
    logging.info("Shutting down nexios app")
    await close_db()
app = get_application(config = app_config,lifespan=app_lifespan)




STATIC_FOLDER = Path(__file__).resolve().parent.parent / "static"


app.add_route(route=Routes("/static/{path:path}",handler=StaticFilesHandler(directory=STATIC_FOLDER)))
app.mount_router(router=router)

if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")