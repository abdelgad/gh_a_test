import os


def main():
    django_debug = int(os.getenv("DJANGO_DEBUG", default=0))
    django_secret = os.getenv("DJANGO_SECRET_KEY")
    django_allowed_hosts = os.getenv("DJANGO_ALLOWED_HOSTS").split(" ")
    # = os.environ.get('MY_ENV_VARIABLE')
    
    if django_debug:
        print(f"Value of django_debug: {django_debug}")
    else:
        print("django_debug is not set.")
    
    if django_secret:
        print(f"Value of django_secret: {django_secret}")
    else:
        print("django_secret is not set.")
    
    if django_allowed_hosts:
        print(f"Value of django_allowed_hosts: {django_allowed_hosts}")
    else:
        print("django_allowed_hosts is not set.")
    
    lol = "Going dumb"
    print(lol)


if __name__ == "__main__":
    main()
