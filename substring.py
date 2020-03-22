# find the substring
# 'ABCDGABDE'

def longest_substring(str):
    
    n = len(str)
    
    visited = [-1]*256
    
    visited[ord(str[0])] = 0
    
    max_len = 1
    
    current_len = 1
    
    # char_str=''
    # sub_str=''
    
    index=0
    
    # print(visited)
    
    for i in range(1,n):
        
        pindex = visited[ord(str[i])]
        
        if pindex == -1 or (i - current_len > pindex) :
            current_len +=1 
            # char_str +=str[i]
        else:
            
            if current_len > max_len:
                max_len = current_len 
                index = i
                # sub_str = char_str
            current_len = 1
            # char_str = str[i]
     
        
        visited[ord(str[i])] = i
    
    # print(visited)
    
    if current_len > max_len:
        max_len = current_len
        # sub_str = char_str
        
    substr_index = index-max_len

    return (max_len, str[substr_index:substr_index + max_len] )
    
     
# print(longest_substring('BCDBGAFBDEB'))


def repeat_substr(str):
    
    n = len(str)    
    count = 0
    max_len = 0;
    index=0    
    for i in range(0, n-1):
        if str[i] == str[i+1]:
            count +=1
        else:
            # print(max_len,count)
            if count > max_len:
                max_len = count
                index=i
                # print(index)
            
            count =0
        
    
    if count > max_len:
       max_len = count
       index = i +1
    
    print(max_len, count)
    substr = index - max_len
    # print(substr)
    return (max_len+1, str[substr: substr + max_len +1])
    

print(repeat_substr('abaaabcaaaa'))

 
