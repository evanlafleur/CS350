#search a list of strings for a specific string

def string_search(string, sub_str):
    for i in range(len(string) - len(sub_str) + 1):
        index = i
        for j in range(len(sub_str)):
            if string[index] == sub_str[j]:
                index += 1
            else:
                break
            if index-i == len(sub_str):
                return index
            return -1

#string_in = input("Enter full string: ")
#sub_str_in = input("Enter sub string to search: ")

string_in = "1234 56"
sub_str_in = "5"

#Visualization Stuff
counter  = 0
limit = len(string_in) - len(sub_str_in)

while counter != limit:
    for i in range(limit):
        sub_str_in = " " + sub_str_in
        counter = counter + 1
        print(string_in)
        print(sub_str_in)

#runs search Algorithm 
res = string_search(string_in, sub_str_in)
#print("Found Match at:" + res)
print(res)
