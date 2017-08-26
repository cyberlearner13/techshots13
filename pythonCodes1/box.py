'''
****************
*              *
*              *
*              *
****************


'''

def boxPrint(symbol,width,height):
    if len(symbol) != 1:
        raise Exception('"symbol" needs to a string of length 1.')
    if(width < 2) and (height<2):
        raise Exception('"width" and "height" need to be greater than or equal to tow.')
    print(symbol * width)

    for i in range(height-2):
        print(symbol + (' '* (width -2)) + symbol)

    print(symbol * width)

boxPrint('*',1,1)
