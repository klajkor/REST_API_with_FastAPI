
try:
    from typing import Optional
    from fastapi import FastAPI, Request, Body, Depends, Header
    from fastapi import HTTPException, status
    from fastapi.security import HTTPBasic, HTTPBasicCredentials
    import secrets
    import uvicorn
    import json
    from pydantic import BaseModel
    from get_ip import get_ip_from_log, get_server_ip, determine_docker_host_ip_address, get_hostname
    from config import ROUTER_IP_LOG_FILE
    print("All  Module loaded ")
except Exception as e:
    print("Error Some Modules are Missing  : {} ".format(e))

app = FastAPI()
security = HTTPBasic()


class Item(BaseModel):
    name: str
    age: str


def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, "admin")
    correct_password = secrets.compare_digest(credentials.password, "PolgarJeno")
    if not (correct_password and correct_username):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password. E!",
            headers={"WWW-Authenticate": "Basic"}
        )
    return credentials.username


@app.get("/")
def read_root(item: Item, credentials: HTTPBasicCredentials = Depends(get_current_username)):
    # return f'Hello World, hello {name}! Age: {age}'
    return item


@app.get("/ip")
async def get_ip():
    log_file_name = ROUTER_IP_LOG_FILE
    ip_address = get_ip_from_log(log_file_name)
    # hostname = get_hostname()
    # ip_address = determine_docker_host_ip_address()
    return ip_address


# @app.post("/post")
# async def post_root(item: Item):
#     return item
