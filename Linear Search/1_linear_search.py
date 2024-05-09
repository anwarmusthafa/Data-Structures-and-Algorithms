def linear_search(l,key):
    for index,element in enumerate(l):
        if element == key:
            print("elemenet found at ",index+1)
            break
    else:
       print("Element NOt Found") 

linear_search([2,3,1,2,4,5,6,3],3)
