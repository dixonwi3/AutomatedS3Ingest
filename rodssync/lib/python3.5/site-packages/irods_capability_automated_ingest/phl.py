proxy_url = 'http://gateway.ad.renci.org:8080'
endpoint_domain = 's3.amazonaws.com'
endpoint_url = 'https://{0}'.format(endpoint_domain)
aws_access_key = 'AKIAJXFJY35LXI6HJBEQ'
aws_secret_key = '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'
path = 'irods-ci'
path = 'bmstestshamiyam'
prefix = ''
max_objects_in_chunk = 7

from minio import Minio
from minio.error import ResponseError
import os
import pickle

def send_s3_to_async(folders, chunk):
    print('sending folders to async s3_folder')
    print(len(pickle.dumps(folders,-1)))
    print(folders)
#    async()
    print('sending chunk to async sync_file')
    print(len(pickle.dumps(chunk,-1)))
    print(chunk)
#    async()
    print('----')

if proxy_url is None:
    httpClient = None
else:
    import urllib3
    httpClient = urllib3.ProxyManager(
                     proxy_url,
                     timeout=urllib3.Timeout.DEFAULT_TIMEOUT,
                     cert_reqs='CERT_REQUIRED',
                     retries=urllib3.Retry(
                         total=5,
                         backoff_factor=0.2,
                         status_forcelist=[500, 502, 503, 504]
                     )
                 )
client = Minio(endpoint_domain,
               access_key=aws_access_key,
               secret_key=aws_secret_key,
               http_client=httpClient)
objcount = 0
folders = set()
chunk = {}
for obj in client.list_objects_v2(path, prefix=prefix, recursive=True):
#    print(obj)
    # add this object's parent to folders map
    if not (obj.object_name.endswith('/')):
        objcount += 1
        folders.add(os.path.dirname(obj.object_name))
        # add this object to the chunk
        chunk[obj.object_name] = [str(obj.size),str(obj.last_modified)]
    # if it's time to launch the async jobs
    if objcount >= max_objects_in_chunk:
        print('sending chunk of {0}'.format(max_objects_in_chunk))
        send_s3_to_async(folders, chunk)
        # reset counts
        objcount = 0
        folders.clear()
        chunk.clear()
if objcount > 0:
    print('sending any leftovers...')
    send_s3_to_async(folders, chunk)
