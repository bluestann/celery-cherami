from proj.tasks import mul

for i in range(500):
    mul.delay(2, i)
