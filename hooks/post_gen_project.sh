#!/bin/sh

echo 'To prepare your dev requirements, run:'
echo '$ pip install pip-tools'
echo '$ pip-compile requirements-dev.in'
echo
echo 'commit the produced requirements-dev.txt.'
echo 'Finally install your dev requirements: pip install -r requirements-dev.txt'
