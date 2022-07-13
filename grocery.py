"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2022

Code Clash #3 - Combined Grocery List (grocery.py)


Author: Ainsley Ward

Difficulty Level: 2/10

Prompt: Sarah’s parents each gave her a grocery list to take with her to Trader Joes. 
She wants to quickly combine the lists into one, getting rid of duplicate items. 
Write a function that takes the two grocery lists (two strings) and returns the final 
grocery list (a list) that does not include duplicate items.

Test Cases:

Input: str1 = 'apples bananas bread sauce onions'; str2 = 'chocolate apples grapes bread';
Output: [apples, bananas, bread, sauce, onions, chocolate, grapes]

Input: str1 = 'apples bananas bread bananas'; str2 = 'grapes';
Output: [apples, bananas, bread, grapes]

Input: str1 = 'apples bananas bread bananas'; str2 = '';
Output: [apples, bananas, bread]
"""

class Solution:
    def my_grocery_list(self,str1,str2):
        # type str1:string
        # type str2: string
        # return: list

        # TODO: Write code below to return a list with the solution to the prompt
        ''' list1 = str1.split(' ')
        list1[len(list1) - 1] = list1[len(list1) - 1].strip()
        list2 = str1.split(' ')
        list2[len(list1) - 1] = list2[len(list2) - 1].strip()
        combined_list = list1 + list2
        no_duplicate = []
        i = 0
        while i < len(combined_list):
            if combined_list[i] not in no_duplicate and combined_list[i] != '':
                no_duplicate.append(combined_list[i])
            i += 1
        return no_duplicate '''

        final_list = []
        list1 = str1.split(' ')
        list1[len(list1) - 1] = list1[len(list1) - 1].strip()
        list2 = str1.split(' ')
        list2[len(list1) - 1] = list2[len(list2) - 1].strip()
        for item in list1:
            if item not in final_list and item != '':
                final_list.append(item)
        for item in list2:
            if item not in final_list and item != '':
                final_list.append(item)
        return final_list

def main():
    string1 = input()
    string2 = input()

    tc1 = Solution()
    ans = tc1.my_grocery_list(string1,string2)
    print(ans)

if __name__ == "__main__":
     main()