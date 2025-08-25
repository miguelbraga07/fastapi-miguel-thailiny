from fastapi import FastAPI

app = FastAPI(title='API do Miguel e da Thailiny')

@app.get("/")
def hello():
    return{"message":"Hello World!"}