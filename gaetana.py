#AI for propositional logic
import numpy as np
print("Hi i am Gaetana, i will help you with some logical problems")
print("I work with the following operators:")
print("con-conjuntion(P,Q), ^ , P,Q booleans")
print("dis-disjuntion(P,Q), v , P,Q booleans")
print("neg-negation(P),¬, P boolean")
print("cond-conditional(P,Q),->, P,Q booleans")
print("bicond-biconditional(P,Q),<->, P,Q booleans")
print("Write con for conjuction, dis for disjuntion, neg for negation, cond for conditiona, and bicon for biconditional")
operator=input("Which operator do you want to use: ")


phi=np.array([True,False,True,False])
fhi=np.array([True,True,False,False])

#Built the conjunction function
c=False
def conjuntion(a,b):
    if a==True and b==True:
        c=True
        return c
    else:
        c=False
        return c 
        
conjuntion(True,True)

#Built negation
a=False
def negation(a):
    if a==True:
        a=False
        return a
    elif a==False:
        a=True
        return a   
    

#Built Disjunction
def disjunction(a,b):
    if a==True and b==True:
        c=True
        return c 
    elif a==False and b==True:
        c=False
        return c  
    elif a==True and b==False:
        c=False
        return c       
    elif a==False and b==False:
        c=False
        return c        
        

#Built conditional
def conditional(a,b):
    if a==True and b==False:
        c=False
        return c
    else:
        c=True
        return c
        

#Built biconditional+

def biconditional(a,b):
    if a==True and b==True:
        c=True
        return c   
    elif a==False and b==True:
        c=False
        return c   
    elif a==True and b==False:
        c=False
        return c        
    elif a==False and b==False:
        c=True
        return c   
        


resultab=False
resultbb=False

if operator=="cond":
    resulta = str(input("Write the first argument P for the conditional operator, true or false: ")) 
    if resulta=="true" or resulta=="True":
        resultab=True
    elif resulta=="false" or resulta=="False":
        resultab=False
    else:
        print("Write true or false")
    resultb = str(input("Write the second argument Q for the conditional operator, true or false: "))         
    if resultb=="true" or resultb=="True":
        resultbb=True
    elif resultb=="false" or resultb=="False":
        resultbb=False
    else:
        print("Write true or false")
    print("P=", resulta,"Q=",resultb)    
    print("P->Q=",conditional(resultab, resultbb))
        
  
elif operator=="bicond":
    resulta = str(input("Write the first argument P for the biconditional operator, true or false: ")) 
    if resulta=="true" or resulta=="True":
        resultab=True
    elif resulta=="false" or resulta=="False":
        resultab=False
    else:
        print("Write true or false")
    resultb = str(input("Write the second argument Q for the biconditional operator, true or false: "))         
    if resultb=="true" or resultb=="True":
        resultbb=True
    elif resultb=="false" or resultb=="False":
        resultbb=False
    else:
        print("Write true or false")
    print("P=", resulta,"Q=",resultb)    
    print("P<->Q=",biconditional(resultab, resultbb))
      

elif operator=="dis":
    resulta = str(input("Write the first argument P for the disjuntion operator, true or false: ")) 
    if resulta=="true" or resulta=="True":
        resultab=True
    elif resulta=="false" or resulta=="False":
        resultab=False
    else:
        print("Write true or false")
    resultb = str(input("Write the second argument Q for the disjuntion operator, true or false: "))         
    if resultb=="true" or resultb=="True":
        resultbb=True
    elif resultb=="false" or resultb=="False":
        resultbb=False
    else:
        print("Write true or false")
    print("P=", resulta,"Q=",resultb)    
    print("PvQ=",disjuntion(resultab, resultbb))        
    
        
    
elif operator=="con":
    resulta = str(input("Write the first argument P for the conjuntion operator, true or false: ")) 
    if resulta=="true" or resulta=="True":
        resultab=True
    elif resulta=="false" or resulta=="False":
        resultab=False
    else:
        print("Write true or false")
    resultb = str(input("Write the second argument Q for the conjuntion operator, true or false: "))         
    if resultb=="true" or resultb=="True":
        resultbb=True
    elif resultb=="false" or resultb=="False":
        resultbb=False
    else:
        print("Write true or false")
    print("P=", resulta,"Q=",resultb)    
    print("P^Q=",conjution(resultab, resultbb))
    
elif operator=="neg":
    resulta = str(input("Write P for negation operator, true or false: ")) 
    if resulta=="true" or resulta=="True":
        resultab=True
    elif resulta=="false" or resulta=="False":
        resultab=False
    else:
        print("Write true or false")
    print("P=", resulta)    
    print("¬P=",negation(resultab))

else:
    print("Write con,dis,cond,bicond or neg")    
