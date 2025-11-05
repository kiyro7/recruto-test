from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def read_root(name: str = "Recruto", message: str = "Давай дружить"):
    html_content = f"""
    <html>
        <head>
            <meta charset="utf-8">
        </head>
        <body>
            <span>Hello {name}! {message}!</span>
        </body>
    </html>
    """
    return html_content
