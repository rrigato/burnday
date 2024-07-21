#assume sts role and export the credentials to be used from aws cloudshell
CREDENTIALS=$(
    aws sts assume-role --role-arn $ROLE_ARN \
    --role-session-name local_debug_session \
)

echo -e "export AWS_ACCESS_KEY_ID=$(echo $CREDENTIALS | jq -r '.Credentials.AccessKeyId')\n\
export AWS_SECRET_ACCESS_KEY=$(echo $CREDENTIALS | jq -r '.Credentials.SecretAccessKey')\n\
export AWS_SESSION_TOKEN=$(echo $CREDENTIALS | jq -r '.Credentials.SessionToken')"
