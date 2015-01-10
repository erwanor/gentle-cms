#!/usr/bin/env bash

# Author: aaron@rely.io
# Made in Waterloo

if [ $# -eq 0 || $# -gt 3 ]
then
  echo "./install.sh github_username github_password blog_name"
  exit 1
fi

GITHUB_USERNAME=$1
GITHUB_PASSWORD=$2
BLOG_NAME=$3

