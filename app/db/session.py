from uuid import uuid4

_receipt_dict = {}


class DbContext:
    def __init__(self):
        self.receipt_dict = _receipt_dict

    def __find_uid_record(self, uid):
        res = None

        if uid:
            res = self.receipt_dict.get(uid, None)
            
        if not res:
            return 404, None

        return 200, res

    def query(self, **kwargs):
        res = None
        kwargs_keys = kwargs.keys()

        if "uid" in kwargs_keys:
            res_code, res = self.__find_uid_record(kwargs["uid"])

        if not res:
            return 404, None
        
        return res_code, res

    def __get_unique_id(self):
        uid = uuid4()

        while uid in self.receipt_dict:
            uid = uuid4()

        return str(uid)

    def create(self, record):
        uid = self.__get_unique_id()

        self.receipt_dict[uid] = record

        return 201, uid
