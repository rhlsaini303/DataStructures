__author__ = 'Rahul'


class Sieve:
    def __init__(self, till_num = None, type = 'Eratosthenes'):
        if till_num is None:
            self.__sieveTable = []
        else:
            self.BuildSieve(till_num, type)

    def __build_eratosthenes_sieve(self, till_num):
        pass

    def __build_sundarams_sieve(self, till_num):
        pass

    def __build_atkins_sieve(self, till_num):
        pass

    def BuildSieve(self, till_num, type = 'Eratosthenes'):
        #initial bounds check
        if till_num < 1:
            #raise invalid upper-limit exception
            pass
        else:
            self.__sieveSize = int(till_num)
            self.__sieveTable = [None]*(self.__sieveSize + 1)

        #calling the corresponding method to build the sieve
        if type is 'Eratosthenes':
            self.__build_eratosthenes_sieve(till_num)
        elif type is 'Sundarams':
            self.__build_sundarams_sieve(till_num)
        elif type is 'Atkins':
            self.__build_atkins_sieve(till_num)

    def isPrime(self, num):
        if not self.__sieveTable:
            #raise sieve-not-built exception
            pass
        elif 1 <= num <= self.__sieveSize:
            if self.__sieveTable[num] is True:
                return True
            else:
                return False
        else:
            #raise number out of bounds exception
            pass



