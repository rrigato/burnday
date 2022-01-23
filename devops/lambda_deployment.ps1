$bundle_dir_name="deployment"
$project_name="burnday"

$env:PYTHONPYCACHEPREFIX="${HOME}\\Documents\\project_pycache"

python -m unittest

#prevent build from continuing
if(-not $?){
    throw "Unittests failed";
}


if(-not ( (detect-secrets scan | ConvertFrom-Json).results.ToString() -eq "") ){
    throw "secrets found in scan";
}




if (Test-Path -Path "${bundle_dir_name}"){
    #remove ${bundle_dir_name} contents recursively
    Get-ChildItem -Path "${bundle_dir_name}" -Recurse | Remove-Item -force -recurse
    #remove ${bundle_dir_name} directory
    Remove-Item "${bundle_dir_name}" -Force
}else{
    echo "${bundle_dir_name} directory not found"
}

#excludes lambda files
$exclude_files = @("*.pyc")

#clean architecture layers
Copy-Item -Path  $project_name -Recurse -Exclude $exclude_files -Force -Destination "${bundle_dir_name}\${project_name}"

#externals lambda handlers
Copy-Item -Path  ".\externals" -Recurse -Exclude $exclude_files -Force -Destination "${bundle_dir_name}"


Copy-Item -Path  "handlers/${project_name}_skill.py" -Exclude $exclude_files -Force -Destination "${bundle_dir_name}"

Compress-Archive -Path "${bundle_dir_name}\*" -DestinationPath  "${project_name}_deployment_package.zip" -Force


if (-not (Test-Path -Path "${project_name}_deployment_package.zip")){
    throw "zip archive unsuccessful";
}

#upload archive to s3 and do not display output
aws s3api put-object --bucket "${project_name}-app-artifacts" --key "${project_name}_deployment_package.zip" --body "${project_name}_deployment_package.zip" --tagging "cloudformation_managed=no&project=${project_name}&prod=yes" | Out-Null



#update lambda function code and print the last modified time in UTC
$lambda_modification_output = (aws lambda update-function-code --function-name "${project_name}-alexa-skill" --s3-bucket "${project_name}-app-artifacts" --s3-key "${project_name}_deployment_package.zip" | ConvertFrom-Json).LastModified.substring(0,19)

echo "lambda funciton last modified - ${lambda_modification_output}"
