#!/bin/sh

echo "Updating all submodules"
git submodule update --recursive --remote
echo "Generating website..."
hugo
