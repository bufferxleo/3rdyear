# import csv

# with open("hi.csv",mode='r') as f:
#     file=csv.reader(f)
#     for i in file:
#         print(i)



# fields=['1','2']
# rows=[[11,22,33],
#       [111,222,333]]
# file='hi.csv'
# with open(file,'w') as f:
#     writer=csv.writer(f)
#     writer.writerows(rows)




# import json
# d={"bye":[1,2,3]}
# def write_json(f,d):
#     with open(f,'w') as json_file:
#         json.dump(d,json_file)
# write_json("hi.json",d)
    
# def read_json_file(f):
#     with open(f,'r') as json_file:
#         data = json.load(json_file)
#         print(data)
# read_json_file("hi.json")


# with open("hi.txt","w") as f:
#     f.write("hi")

# with open("hi.txt","r") as f:
#     d=f.read()
#     print(d)

