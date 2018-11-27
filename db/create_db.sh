#!/bin/bash

rm -f bm2050.db 2>/dev/null

sqlite3 bm2050.db < BM2050_create.sql

