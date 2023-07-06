from main import logger

def calculation():

    @logger
    def calculate_salary(a, b):
        if a > b:
            print('большее число', a)
        elif a < b:
            print('большее число', b)
        else:
            print('числа равны')

    result = calculate_salary(8,7)

if __name__ == '__main__':
    calculation()
