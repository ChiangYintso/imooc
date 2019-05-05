class UrlManager(object):
    
    def __init__(self):
        pass
    
    @staticmethod
    def buildUrl(path):
        return path
    
    @staticmethod
    def buildStaticUrl(path):
        ver = '20190505'
        path = '/static' + path + '?ver=' + ver
        return UrlManager.buildUrl(path)
