from six.moves import urllib
import json


def main():
#   This is Python2 script
    res = urllib.request.urlopen("localhost:5000")
    c = json.loads(res.read().decode("utf-8"))

    print(c)

if __name__ == "__main__":
    main()