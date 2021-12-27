$project_name="burnday"

python -m unittest

#prevent build from continuing
if(-not $?){
    throw "Unittests failed";
}


if(-not ( (detect-secrets scan | ConvertFrom-Json).results.ToString() -eq "") ){
    throw "secrets found in scan";
}


#TODO - validate archive was successful
#delete deployment folder if it exists
#add tags to uploaded bucket
#Switch to deployment archive in cloudformation template
#perform lambda function code update

Copy-Item -Path  $project_name -Recurse -Exclude "*.pyc", "__pycache__", "*\__pycache__", "*\__pycache__\*" -Force -Destination "deployment"


Copy-Item -Path  "handlers/${project_name}_skill.py", "handlers/__init__.py" -Recurse -Force -Destination "deployment"

Compress-Archive -Path "deployment\*" -DestinationPath  "${project_name}_deployment_package.zip" -Force

aws s3api put-object --bucket "${project_name}-app-artifacts" --key "${project_name}_deployment_package.zip" --body "${project_name}_deployment_package.zip"