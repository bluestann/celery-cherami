from cherami import client

publisher = client.create_publisher('/test/dest')
publisher.open()
print 'created publisher'