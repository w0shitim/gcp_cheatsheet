from google.cloud import storage

def create_bucket(bucket_name: str, location: str, storage_class: str):

    '''
    create a new bucket in the region wanted

    bucket_name -> must be unique worldwide
    location -> 'eu', 'us', ...
    storage_class -> STANDARD, NEARLINE, COLDLINE, ARCHIVE
    '''
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    bucket.storage_class = storage_class
    new_bucket = storage_client.create_bucket(bucket, location=location)

    print(f"Created bucket {new_bucket.name} in {new_bucket.location} with storage class {new_bucket.storage_class}")

    return new_bucket


if __name__ == '__main__':
    bucket_name = 'my_bucket_test_w0'
    location = 'eu'
    storage_class = 'STANDARD'
    create_bucket(bucket_name, location, storage_class)
