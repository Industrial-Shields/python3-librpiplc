#!/bin/bash

g++ -shared -fPIC -Wl,--no-as-needed -lrpiplc -Wl,--as-needed -o librpiplc/stub.so librpiplc/stub.c -I/usr/local/include/librpiplc -DDONT_IMPORT_MAPPING
