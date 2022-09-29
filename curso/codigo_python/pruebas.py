

#W###################################################
def fix_me(my_list):

    if len(my_list) % 2:  # imperative code
        new_list = []
        for item in my_list:
            for element in item:
            	new_list = new_list.append(element)
    else:# functional code
        new_list = [element for item in my_list for element in item]
        #ordenado = sorted(new_list, key=lambda x: x %5 == 0)
        dosordenados = sorted(new_list[0:2],reverse=True)
        print (dosordenados + new_list[2:])
        
    # sorting hierarchy:
    #   1. desc by x % 5
    #   2. desc by x
    return (dosordenados + new_list[2:])#return new_list.sorted(reverse=True, key=lambda x: x % 5 + x/(max(new_list)*2))


