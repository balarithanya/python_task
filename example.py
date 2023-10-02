class SoftwareApplication:
    def __init__(self, name, author, version, publishing_year, price):
        self.name = name
        self.author = author
        self.version = version
        self.publishing_year = publishing_year
        self.price = price

# Create a list for storing the applications
applications = []

# Add applications to the list
def add_software_application(application):
    applications.append(application)

# Display all the details of the applications in the list
def display_all_applications():
    for application in applications:
        print(f"Name: {application.name}")
        print(f"Author: {application.author}")
        print(f"Version: {application.version}")
        print(f"Publishing Year: {application.publishing_year}")
        print(f"Price: {application.price}")
        print()

# Display the applications published by a given publisher in a given year
def display_applications_by_publisher_and_year(publisher, year):
    for application in applications:
        if application.author == publisher and application.publishing_year == year:
            print(f"Name: {application.name}")
            print(f"Author: {application.author}")
            print(f"Version: {application.version}")
            print(f"Publishing Year: {application.publishing_year}")
            print(f"Price: {application.price}")
            print()

# Sort the  applications in the increasing order of price
def sort_applications_by_price():
    sorted_applications = sorted(applications, key=lambda application: application.price)
    return sorted_applications
#Sort the  applications in the increasing order of author and publishing year
def sort_applications_by_author_and_year():
    sorted_applications = sorted(applications, key=lambda application: (application.author, application.publishing_year))
    return sorted_applications


# data
add_software_application(SoftwareApplication("App 1", "Author 1", "1.0", 2020, 10.99))
add_software_application(SoftwareApplication("App 2", "Author 2", "2.5", 2021, 19.99))
add_software_application(SoftwareApplication("App 3", "Author 4", "3.2", 2023, 25.99))
add_software_application(SoftwareApplication("App 4", "Author 3", "4.1", 2022, 14.99))


# Display all the applications
display_all_applications()

# Sort the applications by price
sorted_applications = sort_applications_by_price()

# Display the applications sorted by price
print("Applications Sorted by Price (Increasing order):")
for application in sorted_applications:
    print(f"Name: {application.name}")
    print(f"Author: {application.author}")
    print(f"Version: {application.version}")
    print(f"Publishing Year: {application.publishing_year}")
    print(f"Price: {application.price}")
    print()

# Display the  application published by a given publisher in a given year
print("Applications Published by Author 1 in 2020:")
display_applications_by_publisher_and_year("Author 1", 2020)

# Sort the applications by author and publishing year
sorted_applications = sort_applications_by_author_and_year()

# Display the applications sorted by author and publishing year
print("Applications Sorted by Author and Publishing Year (Increasing order):")
for application in sorted_applications:
    print(f"Name: {application.name}")
    print(f"Author: {application.author}")
    print(f"Version: {application.version}")
    print(f"Publishing Year: {application.publishing_year}")
    print(f"Price: {application.price}")
    print()



