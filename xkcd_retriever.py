from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates

import requests

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/xkcd")
async def root(request: Request):
    return templates.TemplateResponse(request=request, name="form.html")

@app.post("/xkcd")
async def xkcd(request: Request, xkcd_id: int = Form(...)):
    url = f"https://xkcd.com/{xkcd_id}/info.0.json"
    xkcd_response = requests.get(url)

    if xkcd_response.status_code == 404:
        return templates.TemplateResponse(request=request, name="404.html")

    if xkcd_response.status_code == 200:
        img_url = xkcd_response.json().get('img')

        return templates.TemplateResponse(
            request=request,
            name="xkcd_image.html",
            context= {"img_url": img_url}
            )