import manager_info_parser
from manager_info_parser import Manager

if __name__ == "__main__":
    with open("../data/managers.csv", "w") as outfile:
        with open("../data/managersUrls.txt", "r") as infile:
            for i, managerUrl in enumerate(infile):
                nextUrl = manager_info_parser.consts.MANAGERS_PREFIX + managerUrl.strip()
                currentManager = Manager(nextUrl)
                try:
                    currentManager.parse_info()
                    toWrite = currentManager.to_csv()+"\n"
                    if len(toWrite) < 10 or toWrite.startswith(','):
                        raise Exception("Manager parsing error")
                    outfile.write(toWrite)
                    print "parsed correctly manager #%d" % i
                except Exception as e:
                    print "parsing error on manager #%d" % i
                    print str(e)
                finally:
                    print
