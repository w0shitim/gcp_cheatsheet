from google.cloud import storage
import os
import colorama

def download_blob(bucket_name: str, storage_filename: str, local_filename: str, download_to_disk = True):
    '''
    download a specific file (blob) from a bucket.
    decide if you want to save it to your local machine or download in memory (disapear after session)

    bucket_name -> name of the bucket you want the blob from (check with cli -> gsutil ls)
    storage_filename -> which blob you want to download
    local_filename -> where you want to save the file on your local machine
    download_to_disk -> True = save it on local machine, False = don't save it, load into memory only for one time use
    '''
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(storage_filename)

    if download_to_disk:
        print(f'Saving {storage_filename} to {local_filename} ...')
        blob.download_to_filename(local_filename)
        print('Successfully saved')
    else:
        file = blob.download_as_string()


    return file

def upload_blob(bucket_name: str, storage_filename: str, local_filename: str, content, uplaod_from_disk = True):
    '''
    download a specific file (blob) from a bucket.
    decide if you want to upload from your local machine or from in memory (disapear after session)

    bucket_name -> name of the bucket you want the blob to go (check with cli -> gsutil ls)
    storage_filename -> to which blob you want to upload
    local_filename -> the file you want to uplaod from your local machine
    uplaod_from_disk -> True = upload file from local machine storage, False -> upload from memory
    '''

    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(storage_filename)

    if uplaod_from_disk:
        print(f'Uploading {local_filename} to {storage_filename} in bucket: {bucket_name} ...')
        blob.upload_from_filename(local_filename)
        print('Successfully uploaded')
    else:
        blob.upload_from_string(content)

    return None

if __name__ == '__main__':
    bucket_name = os.environ.get('BUCKET_NAME')
    local_filename = 'raw_data/tweet_data_2023-02-22.json'
    file = os.path.basename(local_filename)
    storage_filename = os.path.splitext(file)[0]
    content = ''
    upload_blob(bucket_name, storage_filename, local_filename, content, uplaod_from_disk=True)
