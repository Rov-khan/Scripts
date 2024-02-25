import os

def main():
    # Read apps from apps.txt
    with open('apps.txt', 'r') as f:
        apps = f.read().splitlines()
    
    # Create Django app for each app listed in apps.txt
    for app_name in apps:
        # Execute Django management command to create the app
        os.system(f'django-admin startapp {app_name}')
        print("Created app:", app_name)

if __name__ == "__main__":
    main()
