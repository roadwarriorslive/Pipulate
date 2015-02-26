#!/bin/bash

# daemons
cp systuff/daemons/webpipulate /etc/init.d
cp systuff/daemons/loopipulate /etc/init.d
chmod 755 /etc/init.d/webpipulate
chmod 755 /etc/init.d/loopipulate
update-rc.d webpipulate defaults
update-rc.d loopipulate defaults

# cron jobs
cp systuff/crons/webpipulate /etc/cron.hourly
cp systuff/crons/loopipulate /etc/cron.hourly
chmod 755 /etc/cron.hourly/webpipulate
chmod 755 /etc/cron.hourly/loopipulate

# easy-dev
cp systuff/sbins/pipulate /usr/local/sbin
chmod 755 /usr/local/sbin/pipulate

