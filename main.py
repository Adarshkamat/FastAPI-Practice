from fastapi import FastAPI
app=FastAPI()

@app.get("/add")
def add(first,second):
    return {
        "result":int(first)+int(second)
    }
@app.get("/sub")
def sub(first,second):
    return {
        "result":int(first)-int(second)
    }
@app.get("/div")
def div(first,second):
    return {
        "result":int(first)/int(second)
    }
@app.get("/mul")
def mul(first,second):
    return {
        "result":int(first)*int(second)
    }
