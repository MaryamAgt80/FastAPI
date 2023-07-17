class EMAILINVALID(Exception):
    def __init__(self,detail):
        self.detail=detail

class FIELDSISNULL(Exception):
    def __init__(self,detail=None):
        self.detail=detail

class USEREXIST(Exception):
    def __init__(self,detail='از قبل وجود دارد'):
        self.detail=detail