list=[]
def main():
    text= input('anything: ')
    if (text ==''):
        print(list)
    elif(text == '?' and len(list)== 0):
        main()
    elif(text == '?' and len(list)> 0):   
        print(list.pop(0))
        main()
    else:
      list.append(text)
      main()
main()