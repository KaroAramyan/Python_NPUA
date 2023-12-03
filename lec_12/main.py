import random
import time

def gen_file(filename, num_lines=100, num_numbers=20):
    with open(filename, 'w') as file:
        for _ in range(num_lines):
            numbers = ' '.join(str(random.randint(1, 100)) for _ in range(num_numbers))
            file.write(numbers + '\n')


def foo(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} executed in {execution_time:.6f} seconds")
        return result
    return wrapper


@foo
def process_file(filename):
    with open(filename, 'r') as file:
        
        lines_as_int_arrays = map(lambda line: list(map(int, line.split())), file)

        filtered_arrays = filter(lambda arr: any(num > 40 for num in arr), lines_as_int_arrays)

    with open(filename, 'w') as file:
        for arr in filtered_arrays:
          
            file.write(' '.join(map(str, arr)) + '\n')

def read_file_as_generator(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield list(map(int, line.split()))


gen_file('random_numbers.txt')

process_file('random_numbers.txt')

generator = read_file_as_generator('random_numbers.txt')
for line in generator:
    print(line)
