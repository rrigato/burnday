#!/bin/bash

set -e

#TODO remove
#only for valdiating assumed role
aws sts get-caller-identity


export BUCKET_NAME="${PROJECT_NAME}-app-artifacts"
export DEPLOYMENT_PACKAGE="${PROJECT_NAME}_deployment_package.zip"


python -m venv avenv

source avenv/bin/activate
pip install -r requirements/requirements-dev.txt

secret_scan_results=$(detect-secrets scan | \
python3 -c "import sys, json; print(json.load(sys.stdin)['results'])" )

# static scan for security credentials that terminates if any secrets are found
if [ "${secret_scan_results}" != "{}" ]; then
    echo "detect-secrets scan failed"
    exit 125
fi


python -m unittest

deactivate


zip $DEPLOYMENT_PACKAGE -r $PROJECT_NAME  \
    -x *__pycache__*  --quiet

zip -u $DEPLOYMENT_PACKAGE -j handlers/${PROJECT_NAME}_skill.py  \
    -x *__pycache__* --quiet

echo "--------deployment package created--------"


aws s3api put-object --bucket $BUCKET_NAME \
    --region $REGION_NAME \
    --key $PROJECT_NAME/$DEPLOYMENT_PACKAGE \
    --body $DEPLOYMENT_PACKAGE \
    --tagging "cloudformation=no&project=${PROJECT_NAME}&keep=yes"

