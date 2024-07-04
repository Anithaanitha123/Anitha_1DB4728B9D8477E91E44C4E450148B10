# Election Voting Script in Python  
  
# Import required libraries  
import csv  
import datetime  
  
# Define constants  
ELECTION_NAME = "Presidential Election 2023"  
CANDIDATE_FILE = "candidates.csv"  
VOTER_FILE = "voters.csv"  
VOTE_FILE = "votes.csv"  
  
# Define classes  
class Candidate:  
    def _init_(self, name, party):  
        self.name = name  
        self.party = party  
        self.votes = 0  
  
class Voter:  
    def _init_(self, name, id):  
        self.name = name  
        self.id = id  
        self.voted = False  
  
# Load candidates from file  
def load_candidates():  
    candidates = []  
    with open(CANDIDATE_FILE, 'r') as file:  
        reader = csv.reader(file)  
        for row in reader:  
            candidates.append(Candidate(row, row))  
    return candidates  
  
# Load voters from file  
def load_voters():  
    voters = []  
    with open(VOTER_FILE, 'r') as file:  
        reader = csv.reader(file)  
        for row in voters:  
            voters.append(Voter(row, row))  
    return voters  
  
# Register candidate  
def register_candidate(name, party):  
    with open(CANDIDATE_FILE, 'a', newline='') as file:  
        writer = csv.writer(file)  
        writer.writerow([name, party])  
  
# Register voter  
def register_voter(name, id):  
    with open(VOTER_FILE, 'a', newline='') as file:  
        writer = csv.writer(file)  
        writer.writerow([name, id])  
  
# Cast vote  
def cast_vote(voter_id, candidate_name):  
    voters = load_voters()  
    candidates = load_candidates()  
    for voter in voters:  
        if voter.id == voter_id:  
            if not voter.voted:  
                voter.voted = True  
                for candidate in candidates:  
                    if candidate.name == candidate_name:  
                        candidate.votes += 1  
                        with open(VOTE_FILE, 'a', newline='') as file:  
                            writer = csv.writer(file)  
                            writer.writerow([voter_id, candidate_name])  
                        return "Vote cast successfully!"  
                return "Candidate not found!"  
            else:  
                return "You have already voted!"  
    return "Voter not found!"  
  
# Calculate results  
def calculate_results():  
    candidates = load_candidates()  
    for candidate in candidates:  
        print(f"{candidate.name} - {candidate.votes} votes")  
  
# Display election information  
def display_election_info():  
    print(f"Welcome to the {ELECTION_NAME}!")  
    print("Candidates:")  
    candidates = load_candidates()  
    for candidate in candidates:  
        print(f"{candidate.name} - {candidate.party}")  
    print("Voters:")  
    voters = load_voters()  
    for voter in voters:  
        print(f"{voter.name} - {voter.id}")  
  
# Main function  
def main():  
    print("Welcome to the Election Voting System!")  
    while True:  
        print("1. Register Candidate")  
        print("2. Register Voter")  
        print("3. Cast Vote")  
        print("4. Calculate Results")  
        print("5. Display Election Information")  
        print("6. Exit")  
        choice = input("Enter your choice: ")  
        if choice == "1":  
            name = input("Enter candidate name: ")  
            party = input("Enter party: ")  
            register_candidate(name, party)  
        elif choice == "2":  
            name = input("Enter voter name: ")  
            id = input("Enter voter ID: ")  
            register_voter(name, id)  
        elif choice == "3":  
            voter_id = input("Enter voter ID: ")  
            candidate_name = input("Enter candidate name: ")  
            print(cast_vote(voter_id, candidate_name))  
        elif choice == "4":  
            calculate_results()  
        elif choice == "5":  
            display_election_info()  
        elif choice == "6":  
            break  
        else:  
            print("Invalid choice. Please try again.")  
  
if _name_ == "_main_":  
    main()
