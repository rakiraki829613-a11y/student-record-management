def mergeinterval(interval):
    interval.sort()
    result=[interval[0]]
    for start,end in interval[1:]:
        last_end=result[-1][1]
        if start<=last_end:
            result[-1][1]=max(last_end,end)
        else:
            result.append([start,end])
    return result
interval=[[1,3],[2,6],[8,10],[15,18]]
answer=mergeinterval(interval)
print(answer)            