from cherami import client

consumer = client.create_consumer('/test/dest', '/test/cg')
consumer.open()
print 'created consumer'