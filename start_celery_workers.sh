#!/bin/bash
pip install virtualenv --user
python -m virtualenv -p python3 rodssync
source rodssync/bin/activate
pip install irods_capability_automated_ingest
export CELERY_BROKER_URL=redis://127.0.0.1:6379/0
export PYTHONPATH=`pwd`
celery -A irods_capability_automated_ingest.sync_task worker -l error -Q restart,path,file --include stat_eventhandler


