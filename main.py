from fastapi import FastAPI, Request, BackgroundTasks, Response
from fastapi.staticfiles import StaticFiles 
import numpy as np 
import pandas as pd 

app = FastAPI() 


@app.post('/files/')
async def hello(text: str):
    print(text)
    result = {"IS_VALID": 'fail'}
    return result


app.mount('/static', StaticFiles(directory='static', html=True), name='static')
