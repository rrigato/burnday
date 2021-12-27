# getting_started:

1) Create a virtual environment and install dependencies:

```bash
python -m venv avenv
source avenv/bin/activate
pip install -r requirements/requirements-dev.txt
```

2) run unittests and make sure they pass

```bash
python -m unittest
```

3) install [aws cli v2](https://aws.amazon.com/cli/) for working with aws resources locally 

# load_ssm_parameter_store_secure_string_with_aws_cli
```powershell
#assumes region is set and output type is json
((aws ssm get-parameter --name /burnday/v1 --with-decryption | ConvertFrom-Json).Parameter.Value | ConvertFrom-Json)
```

# cloudformation create-stack

```powershell
aws cloudformation update-stack --stack-name burnday-alexa-skill --template-body file://templates/burnday_alexa_skill.template --tags Key=project,Value=burnday Key=prod,Value=yes Key=cloudformation_managed,Value=yes
```


# detect_secrets
implement to ensure no secrets are commited locally:

setup a baseline where all tracked files will be compared to:
```bash
detect-secrets scan > .secrets.baseline
```

compare all tracked files to baseline the ```results``` key should be ```{}``` if no secrets are present
```bash
detect-secrets scan
```
```powershell
(detect-secrets scan | ConvertFrom-Json).results
```