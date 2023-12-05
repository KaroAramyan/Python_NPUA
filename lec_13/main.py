import time
import random
import string
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from collections import Counter


def gen_l_text_file(filename, num_sentences=100000, words_per_sentence=10):
    with open(filename, 'w') as file:
        for _ in range(num_sentences):
            sentence = ' '.join(''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 10))) for _ in range(words_per_sentence))
            file.write(sentence + '\n')


def count_words_sequential(filename):
    word_freq = Counter()
    with open(filename, 'r') as file:
        for line in file:
            words = line.split()
            word_freq.update(words)
    return word_freq

def count_words_mul(filename, num_threads=4):
    word_freq = Counter()

    def process_chunk(chunk):
        local_counter = Counter()
        for line in chunk:
            words = line.split()
            local_counter.update(words)
        return local_counter

    with open(filename, 'r') as file:
        lines = file.readlines()

    chunk_size = len(lines) // num_threads
    chunks = [lines[i:i + chunk_size] for i in range(0, len(lines), chunk_size)]

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        results = list(executor.map(process_chunk, chunks))

    for result in results:
        word_freq.update(result)

    return word_freq


def count_words_m(filename, num_processes=4):
    word_freq = Counter()

    def process_chunk(chunk):
        local_counter = Counter()
        for line in chunk:
            words = line.split()
            local_counter.update(words)
        return local_counter

    with open(filename, 'r') as file:
        lines = file.readlines()

    chunk_size = len(lines) // num_processes
    chunks = [lines[i:i + chunk_size] for i in range(0, len(lines), chunk_size)]

    with ProcessPoolExecutor(max_workers=num_processes) as executor:
        results = list(executor.map(process_chunk, chunks))

    for result in results:
        word_freq.update(result)

    return word_freq


def measure_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    print(f"{func.__name__} executed in {end_time - start_time:.4f} seconds")
    return result

if __name__ == "__main__":
    filename = 'text_file.txt'
    gen_l_text_file(filename)

    print("\nSequential Word Counting:")
    sequential_result = measure_time(count_words_sequential, filename)

    print("\nMultithreading Word Counting:")
    multithreading_result = measure_time(count_words_mul, filename)

    print("\nMultiprocessing Word Counting:")
    multiprocessing_result = measure_time(count_words_m, filename)

    
    print("\nSequential Result:", sequential_result)
    print("\nMultithreading Result:", multithreading_result)
    print("\nMultiprocessing Result:", multiprocessing_result)

    
    multithreading_speedup = sequential_result['multithreading'] / sequential_result['sequential']
    multiprocessing_speedup = sequential_result['multiprocessing'] / sequential_result['sequential']

    print("\nMultithreading Speedup:", multithreading_speedup)
    print("Multiprocessing Speedup:", multiprocessing_speedup)
