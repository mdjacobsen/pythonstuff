objectType='AM_Powder'
expr="[name=='*']"
data={'type':objectType, 'expr':expr, 'f':['cname']}
reply=session.post(url+'query', data) 