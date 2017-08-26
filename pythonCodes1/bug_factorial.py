import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s -%message)s')

def factorial(n):
    logging.debug('Start of factorial(%s)' %n)
    total = 1
    for i in range(n+1):
        total *= i
        logging.debug('i is %s,total is %s' % (i,total))
    logging.debug('return value is %s' % (total))
    return total
print(factorial(5))

logging.debug('End of Program')
