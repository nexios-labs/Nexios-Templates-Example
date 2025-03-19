from nexios import MakeConfig
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from dotenv import load_dotenv,dotenv_values
BASE_DIR = Path(__file__).resolve().parent.parent

dotenv_path = BASE_DIR / ".env"

load_dotenv()
app_config = MakeConfig({
  
    "cors" : {
        "allow_origins" : ["*"]
    },
    **dotenv_values(dotenv_path=dotenv_path)
})


TEMPLATE_DIR =  Path(__file__).resolve().parent.parent / "templates"

template_loader = FileSystemLoader(searchpath=TEMPLATE_DIR)
jinja_env = Environment(loader=template_loader)
