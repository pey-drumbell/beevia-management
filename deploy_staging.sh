#!/bin/bash

# Deploy claude_designs folder to staging server

SOURCE_DIR="/home/godin/beevia/beevia-management/web-report"
REMOTE_USER="peytec5"
REMOTE_HOST="192.145.239.41"
REMOTE_PORT="2222"
SSH_KEY="/home/godin/.ssh/id_rsa_inmotion_pey"
REMOTE_PATH="/home/peytec5/beevia-management.peytechnologies.com"

echo "Deploying ${SOURCE_DIR} to staging server..."

rsync -avz --delete \
    -e "ssh -p ${REMOTE_PORT} -i ${SSH_KEY}" \
    --exclude='.ddev' \
    --exclude='cache/twig' \
    --exclude='cache/assets' \
    --exclude='cache/compiled' \
    --exclude='cache/api' \
    --exclude='logs' \
    --exclude='.git' \
    ${SOURCE_DIR}/ ${REMOTE_USER}@${REMOTE_HOST}:${REMOTE_PATH}/

if [ $? -eq 0 ]; then
    echo "Deployment successful!"
else
    echo "Deployment failed!"
    exit 1
fi
