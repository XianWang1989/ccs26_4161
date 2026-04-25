
string = "some large text here"
sub_strings = ["some", "text"]

for each_sub_string in sub_strings:
    if each_sub_string in string:
        print(each_sub_string, string.index(each_sub_string))
