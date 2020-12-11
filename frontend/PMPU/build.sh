#!/bin/bash

npm run build

cp -r dist ../../main/static/
echo "Copyed dist" 