from fastapi import FastAPI, Request, BackgroundTasks 
from fastapi.staticfiles import StaticFiles 
import numpy as np 
import pandas as pd 

app = FastAPI() 

app.mount('/', StaticFiles(directory='static', html=True), name='static')

@app.get('/files')
async def hello():
    return {'text': 'hello world'}