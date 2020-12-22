#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from SquidLog import SquidLog
import operator

log = SquidLog("./data/access.log",
                print_human_times=True, print_minimal=True)
counts = {}
for l in log:
    #  if l.type == "text/html":
    if l.type == "application/vnd.apple.mpegurl":
        # Group by Time Interval
        file = (l.url).split("/")[-1]
        if file == "playlist.m3u8":
            counts[l.remhost] = counts.get(l.remhost, 0) + 1
print(sorted(counts.items(), key=operator.itemgetter(
    1), reverse=True)[0:100])
