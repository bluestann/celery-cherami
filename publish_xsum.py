from proj.tasks import xsum

lst = []

for i in range(30):
    lst.append(i)
    xsum.delay(lst)
