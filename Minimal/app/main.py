from nexios.config import MakeConfig
from nexios import get_application

config = MakeConfig({
    "secret_key": "my_secret_key",
    "debug": True,
})
app = get_application(config = config)

@app.route("/")
async def index(request, response):
    return response.text("Hello, World!")