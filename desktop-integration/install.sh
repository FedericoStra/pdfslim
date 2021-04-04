#!/bin/bash

DST=~/.local/share/applications

cp pdfslim.desktop $DST
update-desktop-database $DST
