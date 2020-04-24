
def congruencia (a, b, n):
        if (a - b) % n is 0:
            print ("a y b son congruentes mod n")
        else:
            raise Exception("Elementos no congruentes mod n")

congruencia (8,4,2)




