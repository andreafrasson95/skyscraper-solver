
def remove_values(row,column,value):
    for i in range(0,5):
        try:
            array[row][i].remove(value)
        except:{}
        try:
            array[i][column].remove(value)
        except:{}

def clear_row(element,value):
    
    if(value == 1 or value== 2 or element["value"]==1 or element["value"]==2):
        return
    
    values = {"3": {"4":1},"4":{"4":2,"3":1}, "5":{"4":3,"3":2,"2":1}}
  
    positions=values[str(value)]

    row=element["row"]
    column=element["column"]
    direction=element["direction"]

    try:
        index=positions[str(element["value"])]
    except KeyError:
        return

    
    if(direction == "left"):
        for i in range (0,index):
            try:
                array[row][i].remove(value)
            except:{}
                
    if(direction == "bottom"):
        for i in range (4,4-index,-1):
            try:
                array[i][column].remove(value)
            except:{}
    
    if(direction == "right"):
        for i in range (4,4-index,-1):
            try:
                array[row][i].remove(value)
            except:{}

    if(direction == "up"):
        for i in range (0,index):
            try:
                array[i][column].remove(value)
            except:{}

def count_candidates(element, value):
    row=element["row"]
    column=element["column"]
    direction=element["direction"]

    candidates=[]
    if(direction == "left"):
        for i in range (0,5):
            if(type(array[row][i]) != int and value in array[row][i]):
                candidates.append((row,i))

            if(type(array[row][i])==int and array[row][i]==value):
                return -1

    if(direction == "bottom"):
        for i in range (4,-1,-1):
            if(type(array[i][column]) != int and value in array[i][column]):
                candidates.append((i,column))

            if(type(array[i][column])==int and array[i][column]==value):
                return -1
    
    if(direction == "right"):
        for i in range (4,-1,-1):
            if(type(array[row][i]) != int and value in array[row][i]):
                candidates.append((row,i))

            if(type(array[row][i])==int and array[row][i]==value):
                return -1

    if(direction == "up"):
        for i in range (0,5):
            if(type(array[i][column]) != int and value in array[i][column]):
                candidates.append((i,column))

            if(type(array[i][column])==int and array[i][column]==value):
                return -1
    
    return candidates

array= [[[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]],
        [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]],
        [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]],
        [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]],
        [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
]

sentinel = [{"value":1, "row":0, "column":0, "direction":"left" },
            {"value":4, "row":1, "column":0, "direction":"left" },
            {"value":2, "row":2, "column":0, "direction":"left" },
            {"value":3, "row":3, "column":0, "direction":"left" },
            {"value":2, "row":4, "column":0, "direction":"left" },
            {"value":3, "row":4, "column":0, "direction":"bottom" },
            {"value":1, "row":4, "column":1, "direction":"bottom" },
            {"value":3, "row":4, "column":2, "direction":"bottom" },
            {"value":2, "row":4, "column":3, "direction":"bottom" },
            {"value":2, "row":4, "column":4, "direction":"bottom" },
            {"value":2, "row":4, "column":4, "direction":"right" },
            {"value":2, "row":3, "column":4, "direction":"right" },
            {"value":3, "row":2, "column":4, "direction":"right" },
            {"value":1, "row":1, "column":4, "direction":"right" },
            {"value":3, "row":0, "column":4, "direction":"right" },
            {"value":2, "row":0, "column":4, "direction":"up" },
            {"value":3, "row":0, "column":3, "direction":"up" },
            {"value":2, "row":0, "column":2, "direction":"up" },
            {"value":3, "row":0, "column":1, "direction":"up" },
            {"value":1, "row":0, "column":0, "direction":"up" }

            ]

current=5

while(current>3):

    set=0
    # Exclusion phase
    for element in sentinel:
        
        if (current==5 and element["value"]==1):
            if(array[element["row"]][element["column"]]!=5):
                array[element["row"]][element["column"]]=5
                remove_values(element["row"],element["column"],5)
                set+=1
        
        clear_row(element, current)
    # Search space to insert value
   
    while(set<5):
        for element in sentinel:
            candidates=count_candidates(element,current)
            #if( type(candidates) != int):
                #print(len(candidates))
            ## If there's only one candidate in the row
            if( type(candidates) != int and len(candidates)==1):
                array[candidates[0][0]][candidates[0][1]]=current
                remove_values(candidates[0][0],candidates[0][1],current)
                set+=1
                #if(set==4 and current==4):
                    #print(array)

            
            ## If there is more than one candidate
    
    current-=1
    set=0


       

print(array)