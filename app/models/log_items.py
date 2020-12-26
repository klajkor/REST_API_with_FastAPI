from pydantic import BaseModel


class LogItemPublicIP(BaseModel):
    date: str = ""
    time: str = ""
    ip_address: str = ""
