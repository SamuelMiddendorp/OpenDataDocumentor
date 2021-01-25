import odf_library as odf
import sys
import json
def main():
    res = odf.shallow_copy(sys.argv[1])
    with open("out.json", "w") as f:
       json.dump(res, f) 
if __name__ == "__main__":
    main()