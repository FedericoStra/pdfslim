#!/bin/bash

DST=~/.local/share/applications

cp pdfshrink.desktop $DST
update-desktop-database $DST
