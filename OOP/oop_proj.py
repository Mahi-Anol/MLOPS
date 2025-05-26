class chatbook:
    def __int__(self):
        self.username=''
        self.email=''
        self.password=''
        self.loggedin=False

    def menu(self):
        user_input=input('''Welcome to chatbook. Would you like to processed?
                         1. press 1 to signup.
                         2. Press 2 to signin.
                         3. Press 3 to write a post.
                         4. press 4 to message a friend.
                         5. Press any key to exit.
                         ''')
        if user_input =='1':
            pass
        elif user_input=='2':
            pass
        elif user_input=='3':
            pass
        elif user_input=='4':
            pass
        else:
            exit()

    def signup(self):
        email=input('Enter your email here-->')
        pwd=input('Enter your password-->')
        self.email=email
        self.password=pwd
        print("You have succesfully signed in")
        self.menu()

obj=chatbook()

obj.menu()

obj.signup()