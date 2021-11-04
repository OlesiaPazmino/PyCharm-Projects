#print("Hello my dear friend")
#print_this_line="Hello my dear friend,Alex"
#print(print_this_line)
#print("______")
#print("|"" "" " " " "/")
#print("|"" " " " "/")
#print("|" " " "/")
#print("|/")
#my_string = "Test Automation"
#word_test = slice(4)
#print(my_string[word_test])
#my_string = "Test Automation"
#second_word =my_string [-10:]
#print(second_word)

#my_list = [10,50,20,25,30]
#sliced_list= my_list [1:3]
#print(sliced_list)
#num =1;
def list_benefits():
    benefits_list = ["More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"]
    return benefits_list
    pass
list_benefits()
def build_sentence(info):
    return info + " is a benefit of functions!"
    pass
def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    print(build_sentence(list_of_benefits[0]))
    print(build_sentence(list_of_benefits[1]))
    print(build_sentence(list_of_benefits[2]))
    print(build_sentence(list_of_benefits[3]))
name_the_benefits_of_functions()

