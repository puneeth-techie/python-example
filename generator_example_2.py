import memory_profiler as mem_profile
import random
import time

name = ['Puneeth', 'Madhu', 'Sumanth', 'Kiran', 'Abhi']
major = ['Math', 'Science', 'Chemistry', 'Biology', 'Social']

print('Memory (Before): {}MB'.format(mem_profile.memory_usage()))

def person_list(num):
    #result = []
    for i in range(num):
        person = {
                'id': i,
                'name': random.choice(name),
                'major': random.choice(major)
                }
        yield person

t1 = time.clock()
person = person_list(1000000)
t2 = time.clock()

print('Memory (After): {}MB'.format(mem_profile.memory_usage()))
print(f'Time took {t2-t1} seconds')
