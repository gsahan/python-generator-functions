
class Generators:
    def getPrefix(self,len , start = 'A' , end = 'Z', delimeter=''):
        
        if(ord(start) > ord(end)):
            raise ValueError("ascii of start chr must be less then ascii of end char")

        arr = [ start for _ in range(len) ]

        yield delimeter.join(arr)

        Z = end
        fin = False
        while(not fin):
            lastIndex = -1
            lastChar =  arr[lastIndex]

            while(lastChar == Z):
                arr[lastIndex] = start
                lastIndex -= 1
                if lastIndex != -1*(len+1):
                    lastChar =  arr[lastIndex]
                else:
                    return

            lastChar = chr(ord(lastChar)+1)
            arr[lastIndex] = lastChar

            yield delimeter.join(arr)






