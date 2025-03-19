from utils import render_template
from nexios.routing import Router as APIRouter
from nexios.http import Request,Response

router = APIRouter(prefix="/nexios")

@router.get("")
async def read_root(req :Request, res :Response):
    html_content = render_template("index.html", title="Home Page")
    return res.html(content=html_content)