def sublist(list1, list2):
    if list1 == []:
        return True
    for n in range(0, len(list2)-(len(list1)-1)):
        
        if list1[0] == list2[n]:    
                     
            counter = 0
            
            for i in range(0,len(list1)):
                if list1[i] == list2[n+i]:
                    counter += 1
                else:
                    break
                
            if counter == len(list1):
                return True
            
    return False
    
<<<<<<< HEAD
print(sublist([],[1]))
=======
print(sublist([1,2],[1, 0, 1, 2, 2]))

>>>>>>> bc47b4ee840a28662cd717c01ffdfc44881442f1
