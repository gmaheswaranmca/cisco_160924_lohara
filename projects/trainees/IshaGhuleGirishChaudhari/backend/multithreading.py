import threading
import random

# Generate 50 patients with random ages between 1 and 70
patients = [{"id": i, "age": random.randint(1, 70)} for i in range(1, 51)]

# Function to handle patient grouping
def group_patients(age_range, group_name):
    group = [p for p in patients if age_range[0] <= p["age"] <= age_range[1]]
    print(f"{group_name}: {group}")

# Define age groups
age_groups = {
    "Group 1 (1-20)": (1, 20),
    "Group 2 (21-40)": (21, 40),
    "Group 3 (41-50)": (41, 50),
    "Group 4 (51-70)": (51, 70),
}

# Create and start threads for each age group
threads = []
for group_name, age_range in age_groups.items():
    thread = threading.Thread(target=group_patients, args=(age_range, group_name))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("Patient grouping completed.")
