num=8
if num%2==0:
    if num%3==0:
        print('num可以整除2和3')
    elif num%4==0:
            print('num可以整除2和4')
    else:
                print('num可以整除2但是不能整除3和4')
else:
    if num%3==0:
                        print('num可以整除3但是不能整除2')
    else:
                            print('num不能整除2和3')
            
