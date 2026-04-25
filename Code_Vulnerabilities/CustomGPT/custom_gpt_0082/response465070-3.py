
if not (AWS_ACCESS_KEY and AWS_SECRET_ACCESS_KEY and AWS_STORAGE_BUCKET_NAME):
    raise Exception("AWS credentials are not set properly.")
