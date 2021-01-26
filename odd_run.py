import odd_library as odd
import sys
import json
def main():
    res = odd.shallow_copy(sys.argv[1])
    #res = odd.shallow_copy("example_recursive.json")
    with open("out.json", "w") as f:
       json.dump(res, f) 
if __name__ == "__main__":
    main()