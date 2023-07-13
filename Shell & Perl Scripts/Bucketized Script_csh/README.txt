==============================
Creator: Teo, Brendan Wei Zhi
Date: 21/06/2021
Last updated: 23/09/2021
==============================

**Note that this script was used before large scale tool is deploy for the whole IP** - discontinued

This script is created to send to a bucketized failures on all features needed for the project from test regression on a weekly basis to the team

Advantages:
- It gives a great overview of what type of failures has high-impact to the project's progress
- Enable Team lead to provide better supports to feature owner and execution owners
- Reduce manual of feature owner effort to bucketized failure individually. Buy back more time for execution owner to focus on failure debugs

==================
=== How to Deploy ===
==================
[1] This script is written in shell via under Linux Environment
[2] It can be setup in CRON (scheduling tool) to execute it on a weekly basis (refer to this webite https://crontab.guru/)