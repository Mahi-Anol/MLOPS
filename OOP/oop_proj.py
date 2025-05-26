class chatbook:
    def __init__(self):
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
            self.signup()
        elif user_input=='2':
            self.signin()
        elif user_input=='3':
            self.my_post()
        elif user_input=='4':
            self.send_message()
        else:
            exit()

    def signup(self):
        email=input('Enter your email here-->')
        pwd=input('Enter your password-->')
        self.email=email
        self.password=pwd
        print("You have succesfully signed in")
        self.menu()

    def signin(self):
        if self.email=='' and self.password=='':
            print('please signup first')
        else:
            email=input("Enter your email/username here")
            pwd=input("Enter your pass here")
            if self.email==email and self.password==pwd:
                print('You have signedin succesfully')
                self.loggedin=True
            else:
                print("Please input correct credential")
        self.menu()
    
    def my_post(self):
        if self.loggedin==True:
            txt=input('Input your message here')
            print(f'Following content has been posted-->{txt}')
        else:
            print('You need to signin first to post something.')
        self.menu()

    def send_message(self):
        if self.loggedin==True:
            txt=input('Input your message here')
            friend=input("whom to send this message?")
            print(f'You are sending the message-->{txt}')
            print(f'Following message has been sent to --->{friend}')
        else:
            print('You need to signin first to message someone.')
        self.menu()



obj=chatbook()

obj.menu()

# obj.signup()