from fastapi import FastAPI
import uvicorn

app = FastAPI(title="Two-Integer REST API")

@app.get("/add/{a}/{b}")
def add(a: int, b: int):
    return {"a": a, "b": b, "sum": a+b}

@app.get("/add")
def add_query(a: int, b: int):
    return {"a": a, "b": b, "sum": a+b}

if __name__ == "__main__":
    
    uvicorn.run(
        app,
        host="0.0.0.0", #Bind to all network interfaces
        port="8000",
        reload=False
        )
        

