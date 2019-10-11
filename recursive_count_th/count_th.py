'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

str1 = ""
str2 = "abcthxyz"
str3 = "abcthefthghith"
str4 = "thhtthht"
str5 = "THtHThth"

def count_th(word, count=0, index=0):
    count = count
    index = index
    word_length = len(word) -1
    if not word:
        return 0
    if index == word_length:
        # print(f"index is {index} and the word is finished")
        return count
    if word[index] == "t" and word[index + 1] == "h":
        # count += 1
        # print(f"found an instance of TH at index {index} and the count is {count + 1}")
        # index += 1
        # return count_th(word)
        return count_th(word, count=count + 1, index=index + 1)
    else:
        # print(f"index is {index}")
        # print(f"letter {word[index]}")
        # index += 1
        return count_th(word, index=index + 1, count=count)






print(count_th(str1))
print(count_th(str2))
print(count_th(str3))
print(count_th(str4))
print(count_th(str5))




# this works but has global variables that change with multiple function invocations
# count = 0
# index = 0
#
# str1 = "atheronth"
# str2 = "billy"
# str3 = "thththth"
# def count_th(word):
#     # count = 0
#     # index = 0
#     global count
#     global index
#     if not word:
#         return 0
#     if index == len(word):
#         # print(f"index is {index} and the word is finished")
#         return count
#     if word[index] == "t" and word[index + 1] == "h":
#         # print(f"found an instance of TH at index {index} and the count is {count + 1}")
#         count += 1
#         index += 1
#         return count_th(word)
#         # return count_th(word, count=count + 1, index=index + 1)
#     else:
#         # print(f"index is {index}")
#         # print(f"letter {word[index]}")
#         index += 1
#         return count_th(word)


# This works mostly but count is not persisting for some reason
# def count_th(word, count=0, index=0):
#     count = count
#     index = index
#     if not word:
#         return 0
#     if index == len(word):
#         print(f"index is {index} and the word is finished")
#         return count
#     if word[index] == "t" and word[index + 1] == "h":
#         count += 1
#         print(f"found an instance of TH at index {index} and the count is {count}")
#         index += 1
#         # return count_th(word)
#         return count_th(word, count=count, index=index)
#     else:
#         print(f"index is {index}")
#         print(f"letter {word[index]}")
#         # index += 1
#         return count_th(word, index=index + 1)
