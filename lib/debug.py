from models import Company, Dev, Freebie, session

def test_freebie_print_details():
    """
    Test the Freebie.print_details() method.
    """
    freebie = session.query(Freebie).first()
    if freebie:
        print("Testing Freebie.print_details():")
        print(freebie.print_details())
    else:
        print("No freebies found in the database.")

def test_company_give_freebie():
    """
    Test the Company.give_freebie() method.
    """
    company = session.query(Company).first()
    dev = session.query(Dev).first()
    if company and dev:
        print("Testing Company.give_freebie():")
        new_freebie = company.give_freebie(dev, "Keyboard", 100)
        print(new_freebie.print_details())
    else:
        print("No companies or devs found in the database.")

def test_company_oldest_company():
    """
    Test the Company.oldest_company() class method.
    """
    oldest = Company.oldest_company()
    if oldest:
        print("Testing Company.oldest_company():")
        print(f"The oldest company is {oldest.name} founded in {oldest.founding_year}.")
    else:
        print("No companies found in the database.")

def test_dev_received_one():
    """
    Test the Dev.received_one() method.
    """
    dev = session.query(Dev).first()
    if dev:
        print("Testing Dev.received_one():")
        item_name = "Laptop"
        print(f"Does {dev.name} have a {item_name}? {dev.received_one(item_name)}")
    else:
        print("No devs found in the database.")

def test_dev_give_away():
    """
    Test the Dev.give_away() method.
    """
    dev1 = session.query(Dev).first()
    dev2 = session.query(Dev).filter(Dev.name == "Bob").first()
    freebie = session.query(Freebie).first()
    if dev1 and dev2 and freebie:
        print("Testing Dev.give_away():")
        print(f"Before giving away: {freebie.print_details()}")
        dev1.give_away(dev2, freebie)
        print(f"After giving away: {freebie.print_details()}")
    else:
        print("No devs or freebies found in the database.")

def test_relationships():
    """
    Test the relationships between Company, Dev, and Freebie.
    """
    company = session.query(Company).first()
    dev = session.query(Dev).first()
    if company and dev:
        print("Testing relationships:")
        print(f"{company.name}'s devs: {[dev.name for dev in company.devs]}")
        print(f"{dev.name}'s companies: {[company.name for company in dev.companies]}")
    else:
        print("No companies or devs found in the database.")

def main():
    """
    Run all the test functions.
    """
    print("Starting tests...\n")
    test_freebie_print_details()
    print("\n")
    test_company_give_freebie()
    print("\n")
    test_company_oldest_company()
    print("\n")
    test_dev_received_one()
    print("\n")
    test_dev_give_away()
    print("\n")
    test_relationships()
    print("\nAll tests completed.")

if __name__ == "__main__":
    main()