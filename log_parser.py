import re


def log_parser():

    with open("access_log_Jul95.txt", mode="r", encoding="latin-1") as file:
        long_request = ""
        for lines in file:
            line = file.readline()
            line = re.sub('["]', '', line)
            result = re.search("01/Jul/1995"
                               "(:[0][0]:[5][5-9]|:[0][1]:[0-1][0-9]|:[0][1]:[2][0-5])"
                               ".*apollo-13", line)
            if result is not None:
                request = re.findall("GET.*200", line)
                if len(str(request)) > len(str(long_request)):
                    long_request = request
                print(line)
    print(long_request)


log_parser()
