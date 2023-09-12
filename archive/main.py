from raffle import Raffle

MAX_TICKET_COUNT = 5

def main():
    raffle = Raffle()

    # App will keep running until user decides to terminate the app
    while True:
        print("Welcome to My Raffle App")
        
        if not raffle.tickets:
            print("Status: Draw has not started")
        else:
            print(f"Status: Draw is ongoing. Raffle pot size is ${raffle.pot_size}")
        
        print("\n[1] Start a New Draw")
        print("[2] Buy Tickets")
        print("[3] Run Raffle")        
        print("[4] Terminate App")   # Added option to exit the app

        choice = input("\nChoose an option (1/2/3/4): ")

        if choice == "1":
            raffle.start_new_draw()
            print(f"\nNew Raffle draw has been started. Initial pot size: ${raffle.pot_size}")
            input("Press any key to return to main menu")
        elif choice == "2":
            # Check Pot Size
            if not raffle.pot_size:
                # If value not initialised, force user to initiate it
                print("\nPot not initialised. Initialise first!")
            else:
                name_tickets = input("\nEnter your name, no of tickets to purchase\n> ")
                name_tickets_values = name_tickets.split(",")

                # Check the parameters
                if len(name_tickets_values) != 2:
                    print("\nInvalid parameters. Must give name and number of tickets!")
                else:
                    name = name_tickets_values[0]
                    str_count = name_tickets_values[1]

                    # Perform some checks on ticket count
                    try:
                        count = int(str_count)
                        if count <= MAX_TICKET_COUNT:
                            purchased_tickets = raffle.purchase_tickets(name, int(count))
                            print(f"\nHi {name}, you have purchased {count} ticket(s)-")
                            for idx, ticket in enumerate(purchased_tickets):
                                print(f"Ticket {idx + 1}: {' '.join(map(str, ticket))}")
                        else:
                            print("\nTicket count cannot be more than 5!")
                    except ValueError:
                        print("\nInvalid ticket count. Must be a number!")

            input("Press any key to return to main menu")
        elif choice == "3":
            # Check if tickets were purchased
            if not raffle.tickets:
                print("\nNo tickets were purchased. Please purchase a ticket first!")
            else:
                winning_ticket, winners = raffle.run_raffle()
                print(f"\nRunning Raffle..\nWinning Ticket is {' '.join(map(str, winning_ticket))}\n")
                for group, users in winners["winners"].items():
                    if users:
                        print(f"{group} Winners:")
                        reward_per_user = winners["rewards"][group]
                        for user in set(users):
                            count = users.count(user)
                            print(f"{user} with {count} winning ticket(s)- ${reward_per_user * count:.2f}")
                
            input("Press any key to return to main menu")
        elif choice == "4":
            print("Thanks for using My Raffle App! Goodbye!")
            break  # Break out of the loop to terminate the app
        else:
            print("Invalid choice. Please choose a valid option.")


# Run the Main Application
main()
