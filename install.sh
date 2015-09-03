#!/bin/bash

# python
chmod 755 webpipulate.py
chmod 755 loopipulate.py

# webserver daemon
echo "Copying webserver damemon to /etc/init.d/ and activating..."
cp systuff/daemons/webpipulate /etc/init.d
chmod 755 /etc/init.d/webpipulate
update-rc.d webpipulate defaults
/etc/init.d/webpipulate start

# looping daemon (not activated)
cp systuff/daemons/loopipulate /etc/init.d
chmod 755 /etc/init.d/loopipulate
#update-rc.d loopipulate defaults

# cron jobs
echo "Copying cron scripts to /etc/cron.hourly..."
cp systuff/crons/webpipulate /etc/cron.hourly/webpipulate
cp systuff/crons/loopipulate /etc/cron.hourly/webpipulate
chmod 755 /etc/cron.hourly/webpipulate
chmod 755 /etc/cron.hourly/loopipulate

# easy-dev
cp systuff/sbins/devpipulate /usr/local/sbin
chmod 755 /usr/local/sbin/devpipulate
cp systuff/sbins/prodpipulate /usr/local/sbin
chmod 755 /usr/local/sbin/prodpipulate

echo "Install finished. Use \"devpipulate\" to do dev work and \"prodpipulate\" when done."
