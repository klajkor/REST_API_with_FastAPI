try:
    from fastapi import FastAPI, Request, Body, Depends, Header
    from fastapi import HTTPException, status
    import secrets
    import uvicorn
    import json
    from pydantic import BaseModel
    from fastapi.security import HTTPBasic, HTTPBasicCredentials
    print("All  Module loaded ")
except Exception as e:
    print("Error Some Modules are Missing  : {} ".format(e))

app = FastAPI()


@app.get("/")
def read_root(name: str = "Joe", age: int = 1):
    return f'Hello World, hello {name}! Age: {age}'
