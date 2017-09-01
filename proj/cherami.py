from __future__ import absolute_import, unicode_literals

from kombu.log import get_logger

from tchannel.sync import TChannel
from cherami_client.client import Client

from tornado import ioloop

# run cherami-server locally
tchannel = TChannel(name='test_service', known_peers=['127.0.0.1:4922'])
logger = get_logger('kombu.transport.cherami')

# cherami-client needs to make tchannel calls
ioloop.IOLoop.current()

client = Client(tchannel, logger, timeout_seconds=3, reconfigure_interval_seconds=10)
print 'created client'