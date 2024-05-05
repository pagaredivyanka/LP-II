num = int(input("how many no you want to enter: "))
l1 = [int(input("enter no. :")) for x in range (num)]
print ("unsorted list",l1)

for i in range(len(l1)-1):
    m_ind = i
    for j in range(i+1,len(l1)):
        if l1[j] < l1[m_ind] :
            m_ind = j
            
    if l1[i] != l1[m_ind]:
        l1[i],l1[m_ind] = l1[m_ind],l1[i]

print ("sorted list :",l1)
