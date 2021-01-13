class Hamming:

    @staticmethod
    def distance(a, b):
        if len(a) == len(b):
            count = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    count += 1
            return count
        else:
            return "ERROR!"
