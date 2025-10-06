"""
rpcm.py
repository commits

visualise the commits on a github repository since a given date
"""

# Imports
import matplotlib.pyplot as plt
import pyfiglet
import os
from github import Github, Auth
from collections import Counter
from matplotlib.ticker import MaxNLocator
from datetime import datetime, timezone
from colorama import Fore, Style

# Clear the screen
if os.name == "nt":
	os.system("cls")	# For windows users
else:
	os.system("clear")

print(f"{Fore.BLUE}{pyfiglet.figlet_format("RPCM", font='doom')}{Style.RESET_ALL}")	# Menu art

print(f"{Fore.YELLOW}!> Please paste your Github personal access token if you have one:")	# Prompt for personal access token
api_key = input(f"{Style.RESET_ALL}$> ").strip()
if not api_key:
	g = Github()	# Don't use a key if nothing is entered
else:
	g = Github(auth=Auth.Token(api_key))	# Take what the user pasted and use it as a personal access token
						# This allows the user to access their own private repos

print(f"{Fore.YELLOW}!> Please enter the user and repo. For example: username/repo")	# Prompt for username/repo
repo_name = input(f"{Style.RESET_ALL}$> ")

try:
	repo = g.get_repo(repo_name)
except Exception:	# If above fails then the repo is invalid, run the exception below
	print(f"{Fore.RED}!> Error retrieving repository")
	print(f"!> The repo could either be private or you have entered it incorrectly")
	print(f"!> Valid repos would be:{Style.RESET_ALL}")
	print(f"{Fore.GREEN}torvalds/linux\nfreebsd/freebsd-src\ncoreutils/coreutils{Style.RESET_ALL}") # Some examples
	exit(1)		# Exit with status code 1 meaning error

print(f"{Fore.GREEN}>> Found repo{Style.RESET_ALL}")	# Indicate success

def get_start_date():	# Function to get the start date
	while True:
		print(f"{Fore.YELLOW}!> Start date{Style.RESET_ALL}")
		try:
			print(f"{Fore.YELLOW}!> Enter YEAR:")
			YEAR = int(input(f"{Style.RESET_ALL}$> "))
			print(f"{Fore.YELLOW}!> Enter MONTH (1-12)")
			MONTH = int(input(f"{Style.RESET_ALL}$> "))
			print(f"{Fore.YELLOW}!> Enter DAY: ")
			DAY = int(input(f"{Style.RESET_ALL}$> "))
			start_date = datetime(YEAR, MONTH, DAY, tzinfo=timezone.utc)
			return start_date
		except ValueError:
			print(f"{Fore.RED}!> Invalid date, try again{Style.RESET_ALL}")

def get_end_date():	# Function to get the end date
	while True:
		print(f"{Fore.YELLOW}!> End date{Style.RESET_ALL}")
		try:
			print(f"{Fore.YELLOW}!> Enter YEAR:")
			YEAR = int(input(f"{Style.RESET_ALL}$> "))
			print(f"{Fore.YELLOW}!> Enter MONTH (1-12)")
			MONTH = int(input(f"{Style.RESET_ALL}$> "))
			print(f"{Fore.YELLOW}!> Enter DAY: ")
			DAY = int(input(f"{Style.RESET_ALL}$> "))
			end_date = datetime(YEAR, MONTH, DAY, tzinfo=timezone.utc)
			return end_date
		except ValueError:
			print(f"{Fore.RED}!> Invalid date, try again{Style.RESET_ALL}")

start_date = get_start_date()				# Store the start date
end_date = get_end_date()				# Store the end date
commits = list(repo.get_commits(since=start_date, until=end_date))	# Get the commits from the specified range date.

if not commits:	# No commits found
	print(f"{Fore.RED}!> No commits found between {start_date.date()} - {end_date.date()}{Style.RESET_ALL}")
	exit()

# Get the date of each commit
dates = [commit.commit.author.date.date() for commit in commits if commit.commit.author.date >= start_date]
commit_counts = Counter(dates)
sorted_dates = sorted(commit_counts.keys())	# Sort them
counts = [commit_counts[date] for date in sorted_dates]

# Extra information
total_commits = sum(counts)	# Find the total commits
max_commits = max(counts)	# Find the maximum in one day
average_commits = total_commits / len(counts)	# Calculate the average commit per day

# Styling
plt.style.use("dark_background")	# Use dark mode
plt.figure(figsize=(14, 6))
plt.bar(sorted_dates, counts, color="#00ff00")	# Green colour bars

# Axis labelling, plot title
plt.xlabel("Date")
plt.ylabel("Number of commits")
plt.title(f"Commits per day in {repo.full_name}", color='white')

plt.xticks(rotation=45, color='white')
plt.yticks(color='white')
plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))	# Integer values only, since you can't have 0.75 commits
plt.grid(axis='y', linestyle='--', alpha=0.5, color='gray')

stats_text = f"Total commits: {total_commits}\nDate range: {sorted_dates[0]} to {sorted_dates[-1]}\nMax commits/day: {max_commits}\nAverage commits/day: {average_commits:.2f}"
plt.gca().text(1.01, 0.5, stats_text, transform=plt.gca().transAxes, fontsize=10, verticalalignment='center', bbox=dict(facecolor='gray', alpha=0.3))

plt.tight_layout()
plt.show()

# Thank you!!!
print(f"{Fore.GREEN}>> Thank you for using my tool\n>> Please star my repo as it gives me motivation to make more tools like this{Style.RESET_ALL}\n")
