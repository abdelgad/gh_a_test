import os


def main():
    env_variable = os.environ.get('MY_ENV_VARIABLE')
    
    if env_variable:
        print(f"Value of MY_ENV_VARIABLE: {env_variable}")
    else:
        print("MY_ENV_VARIABLE is not set.")


if __name__ == "__main__":
    main()
