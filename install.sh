#!/bin/bash

# daemons
cp systuff/daemons/webpipulate /etc/init.d
cp systuff/daemons/loopipulate /etc/init.d
chmod 755 /etc/init.d/webpipulate
chmod 755 /etc/init.d/loopipulate
update-rc.d webpipulate enable
update-rc.d loopipulate enable

# cron jobs
cp systuff/crons/webpipulate /etc/cron.hourly
cp systuff/crons/loopipulate /etc/cron.hourly
chmod 755 /etc/cron.hourly/webpipulate
chmod 755 /etc/cron.hourly/loopipulate

# easy-dev
cp systuff/sbins/pipulte /usr/local/sbin
chmod 755 /usr/local/sbin

