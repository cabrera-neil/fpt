import random

class Raffle:
    def __init__(self):
        self.pot = 0
        self.tickets = {}  # key = user_name, value = list of tickets
        self.draw_status = "Draw has not started"

    def start_new_draw(self):
        self.pot = 100
        self.tickets = {}
        self.draw_status = "Draw has not started"

    def buy_tickets(self, user_name, num_tickets):
        if user_name in self.tickets:
            user_tickets = self.tickets[user_name]
        else:
            user_tickets = []

        for _ in range(num_tickets):
            ticket = self.generate_unique_ticket()
            user_tickets.append(ticket)

        self.tickets[user_name] = user_tickets
        self.pot += num_tickets * 5

    def generate_unique_ticket(self):
        return random.sample(range(1, 16), 5)

    def run_raffle(self):
        winning_ticket = self.generate_unique_ticket()
        winners = {
            "Group 2": [],
            "Group 3": [],
            "Group 4": [],
            "Group 5 (Jackpot)": []
        }
        rewards = {
            "Group 2": 0.10 * self.pot,
            "Group 3": 0.15 * self.pot,
            "Group 4": 0.25 * self.pot,
            "Group 5 (Jackpot)": 0.50 * self.pot
        }

        for user, user_tickets in self.tickets.items():
            for ticket in user_tickets:
                matches = sum([1 for num in ticket if num in winning_ticket])
                if matches in [2, 3, 4, 5]:
                    group = f"Group {matches}"
                    winners[group].append((user, ticket))

        for group, group_winners in winners.items():
            if group_winners:
                for user, ticket in group_winners:
                    print(f"{group} Winner: {user} with Ticket {ticket} - Prize: ${rewards[group] / len(group_winners)}")
                    self.pot -= rewards[group] / len(group_winners)
            else:
                print(f"{group} Winner: Nil")

        print(f"Remaining Pot Size: ${self.pot}")
        self.draw_status = "Draw has ended"

    def main_menu(self):
        while True:
            print("\nWelcome to My Raffle App")
            print(f"Status: {self.draw_status}")
            print(f"Pot Size: {self.pot}")
            print("[1] Start a New Draw")
            print("[2] Buy Tickets")
            print("[3] Run Raffle")
            print("[4] Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.start_new_draw()
            elif choice == "2":
                if self.pot:
                    input_data = input("Enter your name, number of tickets to purchase (e.g. James,1): ")
                    user_name, num_tickets = input_data.split(',')
                    num_tickets = int(num_tickets)
                    self.buy_tickets(user_name, num_tickets)
                    print(f"{user_name}, you bought {num_tickets} tickets.")
                    for ticket in self.tickets[user_name]:
                        print(f"Ticket: {ticket}")
                    print(f"Current Pot Size: ${self.pot}")
                else:
                    print("Please start a new draw first!")
            elif choice == "3":
                if self.tickets:
                    self.run_raffle()
                else:
                    print("No tickets purchased!")
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    raffle = Raffle()
    raffle.main_menu()
