from fastapi import FastAPI, Response, status
from model import InfoRequest, InfoResponse, InfoSearchRuqest
from typing import List
from dao import query_info, increase_info_viewcount

app = FastAPI()


@app.get("/")
async def health():
    return "the system is healthy"


# @app.get("/info/list", status_code=200)
# async def list_info(req: InfoRequest, response: Response):
#     valid, err_msg = req.is_valid()
#     if not valid:
#         response.status_code = status.HTTP_400_BAD_REQUEST
#         return f"msg: {err_msg}"
#    return query_info(offset=offset, limit=limit, sort_by=sort_by)

@app.get("/info/list", status_code=200)
async def list_info(response: Response, offset: int=0, limit:int=0, sort_by:str=None):
    if offset < 0  or limit < 0:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"msg": "offset and limit must >= 0"}
    
    if sort_by != None and sort_by != "date" and sort_by != "view-count":
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"msg":"sort_by must be date or view-count"}
    
    return query_info(offset=offset, limit=limit, sort_by=sort_by)


@app.get("/info/search", status_code=200)
async def search_info(req: InfoSearchRuqest, response: Response):
    valid, err_msg = req.is_valid()
    if not valid:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return f"msg: {err_msg}"
    return query_info(offset=req.offset, limit=req.limit, sort_by=req.sort_by)


@app.post("/info/incr")
async def increase_info_viewcount(info_id: str):
    return increase_info_viewcount


@app.get("/info/detail")
async def get_info_detail(info_id):
    return f"detailed info: {info_id}"




