from random import randint
import collections

Individu = collections.namedtuple('Individu', 'ind fitness')

def fungsi(x,y):
    return (3*(x**2) + 2*(y**2) - 4*x + (y*1.0)/2)

def fitness(fungsi):
    return (1/((fungsi*1.0)+0.1))

def encode(x,y):
    bin_x = '{0:04b}'.format(x)
    bin_y = '{0:04b}'.format(y)
    return bin_x+bin_y

def decode(biner):
    mid = len(biner)/2
    x = int(biner[:mid],2)
    y = int(biner[mid:],2)
    return [x,y]

#inisialisasi populasi
jml_populasi = 10
pop = [''.join([str(randint(0,1)) for _ in range(8)]) for _ in range(jml_populasi)]

current_generation = [Individu(ind,fitness(fungsi(decode(ind)[0],decode(ind)[1]))) for ind in pop]

for i in current_generation:
    print i
