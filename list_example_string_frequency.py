a='hello python world'
h=[]#init blank list
st='' #init blank string

for k in a:
    num=a.count(k)
    if k in st:
        h.append('None')
    else:
        st +=k
        h.append(num)
print('string',list(a))
print('list ',h)