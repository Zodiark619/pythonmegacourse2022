def asu(jiji):
    jiji=jiji.capitalize()
    if jiji.startswith(('How','When','Where','Why','What')):
        jiji+="?"
    else:
        jiji+="."
    return jiji


bucin=True
result=[]
while bucin:
    meong=input("Say Something: ")
    if meong=='\end':
        for a in result:
            print(a,end=" ") 
        bucin=False
    else:
        meong=asu(meong)
        result.append(meong)