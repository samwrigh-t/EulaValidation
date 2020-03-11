

def ReadMe():
    import os
    try:
        if (open("eula.txt").read().split("\n")[0][-4:]!="true"):
            print("Please agree to the EULA located in " + os.getcwd() + "\eula.txt")
    except FileNotFoundError:
        print("Please extract the package correctly")
    except AttributeError:
        print("Please setup eula.txt correctly")



ReadMe()
