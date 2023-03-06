"""
# *****************************
# 001 test
print("hello")

# 002 dictory
D= {'food':'pan',   'qty':3,  'color':'yello'}
print (D['food'])
D['qty'] +=1
print(D)

# 003 建立空字典，增加数字
D = {}
D["name: "] = "Fang He Jun"
D["age: "] = 56
D["nation: "] = "China"
print (D)
D["age: "] +=1
print (D)


# *******************************
"""
L={"name: ":{"first name ":"john","last name:":"Smith"},
   "job: ":["manage","sells"],
   "age: ":56}
print(L)
print(L["name: "])
L["job: "].append("actor")
print (L)

