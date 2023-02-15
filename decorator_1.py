
def add_comment(function):
    def inner(x,y,z,op):
        print (" ==> Debut Operation <== ")
        print (op + " de "+str(x)+ " et " + str(y) + " et " + str(z))
        result = function(x,y,z,op)
        print (" ==> Fin Operation <== ")
        return result
    return inner

@add_comment
def Addition(x,y,z,op):
    print ("Le Total est : " + str(x+y+z)) 

@add_comment
def Produit(x,y,z,op):
    print ("Le Total est : " + str(x*y*z))

if __name__ == "__main__" :
    print (str(Addition(5,2,3,"Addition")))
    print (str(Produit(5,4,3,"Produit")))