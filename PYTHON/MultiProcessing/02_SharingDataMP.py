#SHARING DATA BETWEEN PROCESS USING ARRAY AND VALUE
import multiprocessing

def calc_square(numbers, result, v):
    v.value = 5.67
    for idx, n in enumerate(numbers): #idx is INDEX
        result[idx] = n*n #MP array doesnot have append

if __name__ == "__main__":
    numbers = [2,3,5]
    result = multiprocessing.Array('i',3)
    v = multiprocessing.Value('d', 0.0)
    p = multiprocessing.Process(target=calc_square, args=(numbers, result, v))

    p.start()
    p.join()

    print(result[:]) #WE HAVE TO PRINT IT LIKE THIS
    print(v.value)