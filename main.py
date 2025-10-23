from modules import ec2_manager, s3_manager, log_parser

def main_menu():
    while True:
        print("\n=== DevOps Automation Tool ===")
        print("1. Manage EC2 Instances")
        print("2. Manage S3 Buckets")
        print("3. Parse Logs")
        print("4. Exit")

        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            ec2_menu()
        elif choice == "2":
            s3_menu()
        elif choice == "3":
            log_parser.parse_logs()
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

def ec2_menu():
    print("\n--- EC2 Management ---")
    print("1. List Instances")
    print("2. Start Instance")
    print("3. Stop Instance")
    choice = input("Select an option (1-3): ").strip()

    if choice == "1":
        ec2_manager.list_instances()
    elif choice == "2":
        instance_id = input("Enter Instance ID to start: ").strip()
        ec2_manager.start_instance(instance_id)
    elif choice == "3":
        instance_id = input("Enter Instance ID to stop: ").strip()
        ec2_manager.stop_instance(instance_id)
    else:
        print("Invalid choice.")

def s3_menu():
    print("\n--- S3 Management ---")
    print("1. List Buckets")
    choice = input("Select an option (1): ").strip()
    if choice == "1":
        s3_manager.list_buckets()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main_menu()
