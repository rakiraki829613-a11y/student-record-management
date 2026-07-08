def insertintervals(interval,newinterval):
    result=[]
    for intervals in interval:
        if intervals[1]<newinterval[0]:
            result.append[intervals]
        elif intervals[0]>newinterval[1]:
            result.append(newinterval)
            newinterval=intervals
        else:
            newinterval[0]=min(intervals[0],newinterval[1])
            newinterval[1]=max(intervals[1],newinterval[0])
        result.append(newinterval)
    return result
interval=[[1,2],[2,3]]
newinterval=[1,4]
answer=insertintervals(interval,newinterval)
print(answer) 

