from typing import List, Union
import datetime
from pydantic import BaseModel


class InfoBase(BaseModel):
    info_id: str
    employee_id: int
    title: str
    describe: str
    create_time: str
    update_time: str
    expire_time: str


class InfoRequest(BaseModel):
    offset: int = 0
    limit: int = 5
    sort_by: Union[str, None] = None

    def is_valid(self):
        if self.offset < 0  or self.limit < 0:
            return False, "offset and limit must >= 0"
        sort_by = self.sort_by
        if sort_by != None and sort_by != "date" and sort_by != "view-count":
            return False, "sort_by must be date or view-count"
        return True, ""
        

class InfoSearchRuqest(InfoRequest):
    title: str = None
    employee_name: str = None
    begin_time: datetime.date = None
    end_time: datetime.date = None

    def is_valid(self):
        valid, msg = super().is_valid()
        if not valid:
            return valid, msg
        return True, ""


class EmojiComment(BaseModel):
    emoicton: str
    num: int

class InfoResponse(InfoBase):
    employee_name: str
    employee_email: str
    emoji_comments: List[EmojiComment] = []


