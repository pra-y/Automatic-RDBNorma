class Node():
    def __init__(self):
        self.attribute_name = attribute_name
        self.attribute_type = attribute_type
        self.nodeid = nodeid
        self.determiner = determiner
        self.determinerofthisnode1 = determinerofthisnode1
        self.determinerofthisnode2 = determinerofthisnode2
        self.determinerofthisnode3 = determinerofthisnode3
        self.determinerofthisnode4 = determinerofthisnode4
        self.keyattribute = keyattribute
        self.ptrtonext = ptrtonext
        
def CreateANew():
    # It will create new node of FDs
    new_node = Node()

def AddNewAttribute(listptr):
    if not listptr :
        p = CreateANew()
        
    else:
        q = listptr
        
        while(q.ptrtonext != None):
            q = q.ptrtonext
            
            p = CreateANew()
            q.ptrtonext = p 
            
    return listptr 
    

def AttributeInfo( Head):
    
    Trav=Head
    AllAttributes[]=0,PrimeAttributes[]=0,PrimeKeyNodeIds[]=0
    while(Trav.ptrTonext != None):
        if Trav.KeyAttribute == 1:
            PrimeAttribute[]=PrimeAttribute.apppend( Trav→AttributeName )
            PrimeKeyNodeIds[]=PrimeKeyNodeIds.apppend( Trav→nodeid )
        else:
            AllAttributes[]=AllAttributes.apppend( Trav→AttributeName )
    return PrimeKeyNodeIds, PrimeAttribute, AllAttributes
    
def Algorithm_Normalization(Head, Flag3NF):
    Flag1=0 Flag2=0, Flag3=0; index1=1, index2=1; index3=1
    A1, A2-dependent, A2-determiner, A3-dependent, A3-determiner = [],[],[],[],[]
    Trav = Head
    while (Trav.ptrtonext):
        if Trav.KeyAttribute == 0:
            determiner_id = [determinerofthisnode1,determinerofthisnode1, determinerofthisnode2, determinerofthisnode3, determinerofthisnode4]
        if def determiner_id == primeKeyNodeId :
            Flag1 = 1 
        elif subset(primeKeyNodeId, determiner_id):
            Flag2 = 1 
        else:
            Flag3 = 1 
        
        
        if Flag1:
            A1 =  union(A1,PrimeAttributes)
            A1.append(Trav → attribute _ name)
        
        elif Flag2:
            A2-determiner.append(Trav → attribute _ name)
            A2-dependent.append(Trav → attribute _ name)
            
        else:
            A3-determiner.append(Trav → attribute _ name)
            A3-dependent.append(Trav → attribute _ name)
            
    return A1, A2-dependent, A2-determiner, A3-dependent, A3-determiner
    
    
def Create_tables():
    T1 = table_union(A1, A3-dependent, A3-determiner)
    
    final_array = [T1]
    for i in range(len(A2-determiner)):
        T+str(i) = union(A2-determiner, A2-dependent)
        final_array.append(T+str(i))
        
    return final_array


def union(arr1,arr2):
    arr1 = set(arr1)
    arr2 = set(arr2)
    resultant_array = arr1.union(arr2)
    
def table_union(arr1, arr2, arr3):
    arr1 = set(arr1)
    arr2 = set(arr2) 
    arr3 = set(arr3)
    resultant_array = arr1.union(arr2, arr3)
    
def subset(subarray, universal_array):
    for i in subarray:
        if i not in universal_array:
            return False
        
    return True 
