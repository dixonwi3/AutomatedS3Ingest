#!/bin/bash
source /etc/irods/rodssync/bin/activate
export CELERY_BROKER_URL=redis://127.0.0.1:6379/0
export PYTHONPATH=`pwd`

icd /tempZone/home/rods/
imkdir s3_coll

iadmin mkresc $5 s3 $4:/$3/irods/Vault "S3_DEFAULT_HOSTNAME=$1;S3_AUTH_FILE=/etc/irods/s3.keypair;S3_REGIONNAME=$2;S3_RETRY_COUNT=1;S3_WAIT_TIME_SEC=3;S3_PROTO=HTTP;ARCHIVE_NAMING_POLICY=consistent;HOST_MODE=cacheless_attached"

python -m irods_capability_automated_ingest.irods_sync start $3 /tempZone/home/rods/s3_coll --s3_keypair /etc/irods/s3.keypair --s3_endpoint_domain $1 --s3_region_name $2 --event_handler irods_capability_automated_ingest.examples.register_root_with_resc_name -i 1 
