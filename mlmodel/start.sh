#!/bin/sh
# Add this to /etc/rc.local
$(aws ecr get-login --no-include-email --region us-east-1)
docker run -d -p 80:80 462888025389.dkr.ecr.us-east-1.amazonaws.com/serve_model:latest
