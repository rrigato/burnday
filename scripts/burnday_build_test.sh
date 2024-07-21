#!/bin/bash

set -e


export BUCKET_NAME="${PROJECT_NAME}-app-artifacts"
export DEPLOYMENT_PACKAGE="${PROJECT_NAME}_deployment_package.zip"


# python -m venv avenv

# source avenv/bin/activate
# pip install -r requirements/requirements-dev.txt

# secret_scan_results=$(detect-secrets scan | \
# python3 -c "import sys, json; print(json.load(sys.stdin)['results'])" )

# # static scan for security credentials that terminates if any secrets are found
# if [ "${secret_scan_results}" != "{}" ]; then
#     echo "detect-secrets scan failed"
#     exit 125
# fi


# python -m unittest

# deactivate

echo "--------beginning bundle--------"

echo $DEPLOYMENT_PACKAGE \
$PROJECT_NAME

zip $DEPLOYMENT_PACKAGE -r $PROJECT_NAME  \
    -x *__pycache__*  --quiet

echo "zip command 2"

zip -u $DEPLOYMENT_PACKAGE -j handlers/${PROJECT_NAME}_skill.py  \
    -x *__pycache__* --quiet

echo "zip command 3"

echo $DEPLOYMENT_PACKAGE

ls -l

zip -u $DEPLOYMENT_PACKAGE -j externals  \
    -x *__pycache__*

echo "--------deployment package created--------"


aws s3api put-object --bucket $BUCKET_NAME \
    --region $REGION_NAME \
    --key $PROJECT_NAME/$DEPLOYMENT_PACKAGE \
    --body $DEPLOYMENT_PACKAGE \
    --tagging "cloudformation=no&project=${PROJECT_NAME}&keep=yes"




aws lambda update-function-code \
    --region $REGION_NAME \
    --function-name  "${PROJECT_NAME}-alexa-skill" \
    --s3-bucket $BUCKET_NAME \
    --s3-key $PROJECT_NAME/$DEPLOYMENT_PACKAGE \
    --no-cli-pager

