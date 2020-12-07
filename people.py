import random
import time
from past.builtins import xrange
import memory_profiler as mem_profile

names = ['Andile', 'Eric', 'Nandipa', 'Phumz', 'Zandile', 'Proud', 'Clifton', 'Mzie-Michael', 'Nokuzola', 'Lisa',
         'Rejoice']
majors = ['Engineering', 'Data Science', 'Biomedicine', 'Computer Science', 'Chemistry', 'Design', 'Screenplay Writing',
          'Physics', 'Law', 'Accounting']

print('Memory (Before): {}Mb'.format(mem_profile.memory_usage_resource()))


def people_list(num_people):
    result = []
    for i in xrange(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }

        result.append(person)
    return result


def people_generator(num_people):
    for i in xrange(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }

        yield person


t1 = time.clock()
people = people_list(1000000)
t2 = time.clock()

t1 = time.clock()
people = people_generator(1000000)
t2 = time.clock()

print('Memory (After) : {}Mb'.format(mem_profile.memory_usage_resource()))
print('Took {} seconds'.format(t2 - t1))
