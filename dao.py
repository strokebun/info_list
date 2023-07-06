from model import InfoResponse

fake_db = [
    InfoResponse(
        info_id = "info_id1", 
        employee_id = 123,
        employee_name = "name1",
        employee_email= "email1",
        title = "title1",
        describe = "describe1",
        create_time = "xxxx-xx-xx1",
        update_time = "xxxx-xx-xx1",
        expire_time = "xxxx-xx-xx1"
    ),
    InfoResponse(
        info_id = "info_id2", 
        employee_id = 456,
        employee_name = "name2",
        employee_email= "email2",
        title = "title2",
        describe = "describe2",
        create_time = "xxxx-xx-xx2",
        update_time = "xxxx-xx-xx2",
        expire_time = "xxxx-xx-xx2"
    ),
    InfoResponse(
        info_id = "info_id3", 
        employee_id = 789,
        employee_name = "name3",
        employee_email= "email3",
        title = "title3",
        describe = "describe3",
        create_time = "xxxx-xx-xx3",
        update_time = "xxxx-xx-xx3",
        expire_time = "xxxx-xx-xx3"
    ),
    ]

def query_info(offset = 0, limit = 5, title = None, employee_name = None, begin_time=None, end_time=None, sort_by=None):
    return fake_db
    # if sort_by == "date":
    #     # sort by date
    #     pass
    # else:
    #     # sort by time
    #     pass


def increase_info_viewcount(info_id: str):
    return True