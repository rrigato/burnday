$bundle_dir_name="deployment"
$project_name="burnday"

python -m unittest

#prevent build from continuing
if(-not $?){
    throw "Unittests failed";
}


if(-not ( (detect-secrets scan | ConvertFrom-Json).results.ToString() -eq "") ){
    throw "secrets found in scan";
}


#TODO - get rid of __pycache__ files
#add tags to uploaded bucket
#Switch to ${bundle_dir_name} archive in cloudformation template
#perform lambda function code update

if (Test-Path -Path "${bundle_dir_name}"){
    echo "Removing ${bundle_dir_name} directory"
    #remove ${bundle_dir_name} contents recursively
    Get-ChildItem -Path "${bundle_dir_name}" -Recurse | Remove-Item -force -recurse
    #remove ${bundle_dir_name} directory
    Remove-Item "${bundle_dir_name}" -Force
}else{
    echo "${bundle_dir_name} directory not found"
}

$exclude_files = (Get-ChildItem -Path "./${project_name}/*/__pycache__" -Recurse ).FullName


Copy-Item -Path  $project_name -Recurse -Exclude $exclude_files -Force -Destination "${bundle_dir_name}\${project_name}"


Copy-Item -Path  "handlers/${project_name}_skill.py"  -Force -Destination "${bundle_dir_name}"

Compress-Archive -Path "${bundle_dir_name}\*" -DestinationPath  "${project_name}_deployment_package.zip" -Force

aws s3api put-object --bucket "${project_name}-app-artifacts" --key "${project_name}_deployment_package.zip" --body "${project_name}_deployment_package.zip" --tagging "cloudformation_managed=no&project=${project_name}&prod=yes"


aws lambda update-function-code --function-name "${project_name}-alexa-skill" --s3-bucket "${project_name}-app-artifacts" --s3-key "${project_name}_deployment_package.zip" | ConvertFrom-Json