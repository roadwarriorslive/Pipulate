#!/bin/bash

# daemons
mv systuff/daemons/webpipulate /etc/init.d
mv systuff/daemons/loopipulate /etc/init.d
chmod 755 /etc/init.d/webpipulate
chmod 755 /etc/init.d/loopipulate
update-rc.d webpipulate enable
update-rc.d loopipulate enable

# cron jobs
mv systuff/crons/webpipulate /etc/cron.hourly
mv systuff/crons/loopipulate /etc/cron.hourly
chmod 755 /etc/cron.hourly/webpipulate
chmod 755 /etc/cron.hourly/loopipulate

# easy-dev
mv systuff/sbins/pipulte /usr/local/sbin
chmod 755 /usr/local/sbin

