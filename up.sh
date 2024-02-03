#!/bin/bash

docker run -d --mount type=bind,source=/home/mildfire/wagtaildemo/db.sqlite3,target=/app/db.sqlite3 -p 8000:8000 wagtaildemo

