import random

class Raffle:
    def __init__(self):
        self.pot_size = 0
        self.tickets = []
        self.winning_ticket = []

    def start_new_draw(self):
        self.pot_size = 100
        self.tickets = []
        self.winning_ticket = []

    def purchase_tickets(self, user_name, ticket_count):
        tickets_for_user = []
        for _ in range(ticket_count):
            ticket_numbers = random.sample(range(1, 16), 5)
            self.tickets.append({"user": user_name, "numbers": ticket_numbers})
            tickets_for_user.append(ticket_numbers)
            self.pot_size += 5
        return tickets_for_user

    def run_raffle(self):
        self.winning_ticket = random.sample(range(1, 16), 5)
        winners = self.calculate_winners()
        return self.winning_ticket, winners

    def calculate_winners(self):
        winners = {
            "Group 2": [],
            "Group 3": [],
            "Group 4": [],
            "Group 5": []
        }

        for ticket in self.tickets:
            matched_count = sum(1 for num in ticket["numbers"] if num in self.winning_ticket)
            if 2 <= matched_count <= 5:
                group_name = f"Group {matched_count}"
                winners[group_name].append(ticket["user"])

        rewards = {
            "Group 2": 0.10 * self.pot_size / (len(winners["Group 2"]) or 1),
            "Group 3": 0.15 * self.pot_size / (len(winners["Group 3"]) or 1),
            "Group 4": 0.25 * self.pot_size / (len(winners["Group 4"]) or 1),
            "Group 5": 0.50 * self.pot_size / (len(winners["Group 5"]) or 1),
        }

        for group, reward in rewards.items():
            self.pot_size -= reward * len(winners[group])

        return {
            "winners": winners,
            "rewards": rewards
        }

