import sys
class Votingsystem(object):
    def __init__(self):
        self.admin = {
            'username' :'divesh',
            'password' : 'diveesh12'
        }
        self.nominees =[]
        self.votes = {}
        self.voted = []
        self.election_name = ''

    def check_admin_auth(self):
        attempts = 3
        print("[admin login]")

        while attempts > 0:
           username = input ("> username : ")
           password = input("> password : ")

           if username == self.admin['username'] and password == self.admin['password']:
              return True

           print("invalid credentials")
           attempts -= 1
           print(f'attempts left : {attempts}')
        
        print("maximum attempts reached")
        return False

    def start_voting(self):
        print(f"voting start for[{self.election_name}] Election")
        while True:
            c= int(input("1]cast vote 2] end voting"))
            if c == 1:
                voter_id = input("> voter id :")
                if True :#assesmennt
                    if voter_id not in self.voted:
                        print("enter the number corresponding to the party name u want to vote")
                        for i,v in enumerate(self.nominees):
                            print(f"[{i+1}] {v}", end =" ")
                        print()
                        while True:
                            p= int(input("> "))
                            if p in range (1,len(self.nominees)+1):
                                self.voted.append(voter_id)
                                self.votes[self.nominees[p-1]] +=1
                                print("you have successfully voted")
                                break
                            else:
                                print("invalid choice,try again")
                    else:
                        print("you have already voted")
                else:
                    print("invalid voter id,try again")
            elif c == 2:
                if self.check_admin_auth():
                    self.end_voting()
                else:
                    print("invalid credentials")
            else:
                print("invalid choice")


    def end_voting(self):
        print("voting results for -{self.election_name}")

        print("[votes_table] \n")
        print(" | ".join(self.nominees))
        for k,v in self.votes.items():
            print(f" {v}",' ' *(len(k) - len(str(v))), '|' , end = " ")
        print()

        print("[election winners]")
        max_voted_party =max(self.votes,key = self.votes.get)
        max_votes = self.votes[max_voted_party]

        winners = []
        for k,v in self.votes.items():
            if v == max_votes:
                winners.append(k)
        
        if len(winners) > 1:
            print("the election has ended in a tie with following parties:")
            print(*winners,sep =' ')
            print(f'each party got {max_votes},votes')

        else:
            print(f"{max_voted_party}has won the election with {max_votes} votes")
        
        sys.exit(0)



    def start(self):
        to_proceed = True
        print("<<<<< welcome to Allahabad >>>>>")
        print('please login to process')

        if self.check_admin_auth():
            while to_proceed:
                self.election_name= input (">enter election name:")
                total_nominees = int(input(">enter the no of nominees:"))

                print(f"enter the names for {total_nominees} nominees")
                for i in range(total_nominees):
                    n =input(f"nominees [{i+1}] :")
                    self.nominees.append(n)
                    self.votes.setdefault(n,0)

                print('\n [Nominees] \n', " | ".join(self.nominees), " \n ")

                while True:
                    print("1] proceed 2] reset 3]exit")
                    c= int(input("> "))
                    if c == 1:
                        to_proceed =False
                        self.start_voting()
                    elif c == 2:
                        break
                    elif c== 3:
                        sys.exit(0)
                    else:
                        print('invalid choices')

        else:
            sys.exit(0)

if __name__ == '__main__':
    vc = Votingsystem()
    vc.start()