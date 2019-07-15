STEPS TO SETTING UP S3 AUTOMATION INTO IRODS:
1.) login to the irods server as root
2.) run "run_redis.sh" to start redis server
3.) login to irods server from as irods user (sudo docker exec... /bin/bash) 
4.) run "start_celery_workers.py" from /etc/irods

