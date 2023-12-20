"""Flask CLI/Application entry point."""
import os



import sys
sys.path.append(os.getcwd())
sys.path.append("/home/rathee/search_l3s_recsys_srv/src")

print(sys.path)

from src.search_l3s_recsys import create_app, db


app = create_app(os.getenv("FLASK_ENV", "development"))


@app.shell_context_processor
def shell():
    return {"db": db}

