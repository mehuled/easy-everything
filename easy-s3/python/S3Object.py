
class S3Object() :
    
    def __init__(self, s3_uri) :
        pass

    def setCredentials(self,access_key_id,secret_access_key) :
        self.access_key_id = access_key_id
        self.secret_access_key = secret_access_key

    def setRegion(self) :
        pass
    
    def readContent(self) :
        pass

    def setBucketName(self) :
        pass

    def getObjectKey(self,object_uri) :
        pass

    def getObjectContent(self) :
        pass


if __name__ == "__main__":
    s3resource = S3Object("s3://your-bucket-name/object-key")
    s3resource.setCredentials("abc","cde")
    print(s3resource.secret_access_key)
    


