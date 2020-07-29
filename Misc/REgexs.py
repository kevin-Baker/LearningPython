
# Write a Python function to convert a date of yyyy-mm-dd format to dd-mm-yyyy format
import re
date = "2020-25-6"
def year_date(date):
        return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', date)
print("New date in DD-MM-YYYY Format: ",year_date(date))
# Write a Python function to abbreviate 'Road' as 'Rd.' in a given string
road = "21 Brookemere Road"
def road_replace(str):
        print(re.sub("Road","Rd",str))
road_replace(road)
# Write a Python function to replace all occurrences of space, comma, or dot with a colon.
import re
txt = 'Hello there, How is it.Tommy'
def comma_replace(str):
        print(re.sub("[ ,.]", ":", txt))
comma_replace(txt)
# Write a Python function to find all three, four, five characters long words in a string.
text = "Hello how goes it"
def num_char(str):
        print(re.findall(r"\b\w{3,5}\b",str))
num_char(text)
# Write a Python function to find all words which are at least 4 characters long in a string.
text2 = "hello hello qwer"
def Four_num(str): 
        print(re.findall(r"\b\w{4,}\b",str))
Four_num(text2)
# Write a Python function to extract values between quotation marks of a string. Return an array of the strings
text1 = "\"Hello my name is earl, whats yours?\" my name is Jack."
def Quote_mark(str):
        return (re.split('"(.*?)"',text1))
print(Quote_mark(text1)) # FIX THIS

# Write a Python function to find urls in a string
url = "### https://regex101.com/ *99" 
def URL_Finder(URL):
        print(re.findall(r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))",URL))
URL_Finder(url)
# Write a Python function to split a string at uppercase letters.
InString = "HelloTherePops"
def Splt_String(str):
        print(re.findall("[A-Z][^A-Z]*",InString))
Splt_String(InString)
# Write a Python function to remove the ANSI escape sequences from a string. \
def escape_ansi(line):
    ansi_escape = re.compile(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]')
    return ansi_escape.sub('', line)
print (escape_ansi(line = '\t\u001b[0;35mSomeText\u001b[0m\u001b[0;36m172.18.0.2\u001b[0m'))
# Write a Python function to check a decimal with a precision of 2. regex or return true false
def decimal(num):
        isDecimal = re.compile(r"""^[0-9]+(\.[0-9]{1,2})?$""")
        result = isDecimal.search(num)
        return bool(result)
print(decimal("123.23"))
print(decimal("11.23456"))
# Write a Python function to insert spaces between words starting with capital letters
word = "HelloThere"
def Cap_Letter(str):
        print(re.sub(r"(\w)([A-Z])", r"\1 \2", word))
Cap_Letter(word)

#Write a function with a regular expression to return a list of all function names inside a text file.
textfile = "def readTextFile():"
regge = "def\s+[_A-Za-z0-9]+\s*\(.*\)\s*\:"
def Func_namer(str):
        print(re.findall(r"def\s+[_A-Za-z0-9]+\s*\(.*\)\s*\:",str))
Func_namer(textfile)
#Write a function with a regular expression to return a list of all quoted “strings” which occur inside the ‘[‘ and ‘]’ characters.
REGEX = r"\"(?:[^\"\\]|\\.)*\""
textfile2 =  "[\"strings\" asd \"hello\"]"
def Quote_String(str):
        print(re.findall(REGEX,str))
Quote_String(textfile2)
#Write a function with a regular expression to recognize a fully qualified Windows path (i.e. “C:\MayFolder1\myFile1.txt”) and return just the filename at the end (in this case it would return “myFile1.txt”).
import re
test_str = "C:\\Users\\bakerke\\Documents\\Projects\\file.txt"
def find_path_file(path):
        find = re.findall(r"[A-Z]:\\(.*)\\(.*)",path)
        if (len(find) > 0):
                return find[0][1]
print(find_path_file(test_str))

#Write a function with a regular expression to recognize a function call and return the arguments as a list of strings (so when seeing ‘functionName(arg1, arg2,   “arg3”  )’  would return a python string array like  [“arg1”, “arg2”, “arg3”] )
import re
txt = "def(arg1 arg2 arg3)"
def regex_args(str):
        print(re.findall(r"(arg[1-9])",str))
regex_args(txt)
