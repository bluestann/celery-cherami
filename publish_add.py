from proj.tasks import add

range = pow(10, 3)

for i in xrange(range):
    if i % 1000 == 0:
        print 'publishing: ', i
    add.delay(0, i)

print 'done!'
