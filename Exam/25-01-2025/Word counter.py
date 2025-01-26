def word_count(str):
    # arr = str.split()
    # return len(arr)
    c=0
    for i in str:
        if i==" ":
            c+=1
    # if last character is not space then increment count by 1
    if str[-1]!=" ":
        c+=1
    return c

def main():
    try:
        print("Enter text to check word count: ")
        str=input()
        print("Word Count: ",word_count(str))

    except ValueError as e:
        print(f"Invalid Input {e}")
        return
    
if __name__ == "__main__":
    main()