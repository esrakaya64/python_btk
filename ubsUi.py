class UI():
    def __init__(self,menu_items):
        self.menu_items=menu_items

    def ShowMenu(self):
        print("-"*52,"|{:*^50}|".format(" Menu "),"-"*52,sep="\n")
        for no,item in enumerate(self.menu_items):print("|{:^50}|".format(str(no+1)+"..."+item))
        print("-"*52)

    def GetChoise(self):
        try:
            choise=int(input(f"Enter the choise [1-{len(self.menu_items)}]:"))
            assert 1<=choise<=len(self.menu_items),f"Lütfen [1-{len(self.menu_items)}] enter the choise"
            return choise
        except AssertionError as e:
            print(e)
        except:
            print("Incorrect entry")
