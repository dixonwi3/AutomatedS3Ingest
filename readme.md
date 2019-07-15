The files in this git repository automate (as much as possible) the process of ingesting data from an S3 Bucket to an iRODS Server. This is assuming that you already have a running iRODS Server. 
Keep in mind that this only adds new files to iRODS as they are added after the scripts are all run. Anything previously in the bucket will not be transferred automatically, as the s3 plugin is still in beta phases and they don't have an operation to add existing items. Also keep in mind that you must follow these steps EXACTLY for things to work!

Finally, do all of these things in /etc/irods/AutomateS3Ingest! It will make your life much easier!

STEPS TO SETTING UP S3 AUTOMATION INTO IRODS:
1.) login to the irods server as root
2.) run "run_redis.sh" to start redis server
3.) login to irods server from as irods user (sudo docker exec... /bin/bash)
4.) Go to /etc/irods/rodssync/lib/python3.5/site-packages/minio/helpers.py
     - Comment out lines 354-357. This makes is_valid_bucket_name function to always return True
5.) run "start_celery_workers.py" from /etc/irods
6.) Go to /etc/irods/AutomatedS3Ingest/rodssync/lib/python3.5/site-packages/irods_capability_automated_ingest/examples/sync_root_with_resc_name.py 
     - Change the to_resource return value to “news3resc” or whatever your s3 cacheless resource will be named
7.) login to irods server as irods user (again)
8.) as that user, type "python3 run_scanner.py"


