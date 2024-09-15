#!/bin/bash

SOURCE_DIR=$(pwd)
# Target PATH:/usr/local/bin (default)
TARGET_DIR="/usr/local/bin"

if [[ $(id -u) -ne 0 ]]; then
    echo "You need administrative privileges to run this script."
    exit 1
fi

echo "Config: $SOURCE_DIR -> $TARGET_DIR"
cp -r $SOURCE_DIR/* $TARGET_DIR/

echo "Successfull!."
