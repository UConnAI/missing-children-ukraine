#!/bin/bash

# python -m pip install --target ./package requests

rm -rf deployment-package.zip
cd env/lib/python*/site-packages
zip -r ${OLDPWD}/deployment-package.zip .
cd $OLDPWD
zip -g -r deployment-package.zip . -x "env*" "*__pycache__*" "*.zip" "test*" "build_deployment.sh" "requirements.txt"
