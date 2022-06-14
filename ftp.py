import ftplib
import cmd

class FTPShell(cmd.Cmd):
    prompt: str = "ftp> "
    ftp = None
    authorized = False
    bell = False

    def do_open(self, server):
        """Connect to FTP-Remoteserver"""
        user = input(f"User ({server}:(anonymous)): ") or "anonymous"
        password = input("Password (anonymous@): ") or "anonymous@"

        try:
            self.ftp =  ftplib.FTP(server, user, password)
            print(self.ftp.login(user, password))
            self.authorized = True
            print(self.ftp.getwelcome())
        except Exception as e:
            self.authorized = False
            print(e)

    def do_user(self, args):
        """Log off and change account"""
        if not self.authorized:return print("Not connected")
        server = self.ftp.host
        self.ftp.close()
        self.ftp = None
        user = input(f"User ({server}:(anonymous)): ") or "anonymous"
        password = input("Password (anonymous@): ") or "anonymous@"

        try:
            self.ftp =  ftplib.FTP(server, user, password)
            print(self.ftp.login(user, password))
            self.authorized = True
            print(self.ftp.getwelcome())
        except Exception as e:
            self.authorized = False
            print(e)
    def do_pwd(self, args):
        """Show current Working Directory"""
        if not self.authorized:return print("Not connected")
        print(self.ftp.pwd())

    def do_mkd(self, dirname):
        """Make Directory"""
        if not self.authorized:return print("Not connected")
        self.ftp.mkd(dirname)
        
    def do_ls(self, dirname=None):
        """List Directory"""
        if not self.authorized:return print("Not connected")
        print(self.ftp.retrlines(f'LIST {dirname if dirname else ""}'))

    def do_cd(self, dirname="/"):
        """Change to Directory"""
        if not self.authorized:return print("Not connected")
        print(self.ftp.cwd(dirname))

    def do_get(self, filename=None):
        if not self.authorized:return print("Not connected")
        if not filename:
            filename = input("File> ")
        with open(filename, 'wb') as fp:
            print(self.ftp.retrbinary(f'RETR {filename}', fp.write))

    def do_put(self, filename=None):
        if not self.authorized:return print("Not connected")
        if not filename:
            filename = input("File> ")
        with open(filename, 'rb') as fp:
            try:
                print(self.ftp.storbinary(f"STOR {filename}", fp))
            except Exception as e:
                print(e)

    
    def do_mkdir(self, dirname=None):
        if not self.authorized:return print("Not connected")
        if not dirname:
            dirname = input("Dirname> ")
        try:
            print(self.ftp.mkd(dirname))
        except Exception as e:
            print(e)
        if self.bell: print("\a")
    
    def do_literal(self, cmd=None):
        if not self.authorized:return print("Not connected")
        if not cmd:
            cmd = input("Literal FTP Command: ") or "PWD"
        try:
            print(self.ftp.sendcmd(cmd))
        except Exception as e:
            print(e)
        if self.bell: print("\a")

    def do_status(self, args):
        if self.authorized:
            print(f"Connected to {self.ftp.host}")
            
            print(f"Verbose: {self.ftp.debugging} ; Bell: {self.bell} ; ")
        else:
            print(f"Not Connected")
            
            print(f"Verbose: 0 ; Bell: {self.bell} ; ")
            
        if self.bell: print("\a")

    def do_debug(self, argv):
        if not self.authorized:return print("Not connected")
        if self.ftp.debugging:
            self.ftp.debug(0)
            self.ftp.debugging = 0
            print("Debug is OFF .")
        else:
            self.ftp.debug(1)
            self.ftp.debugging = 1
            print("Debug is ON .")
        if self.bell: print("\a")
            
            
    def do_bell(self, argv):
        if self.bell:
            self.bell = False
            print("Bell-Mode is OFF .")
        else:
            self.bell = True
            print("Bell-Mode is ON .")
        if self.bell: print("\a")
            
                
    def do_bye(self,args):
        self.ftp.quit()
        print("Goodbye!")
        if self.bell: print("\a")
        exit()

    def do_close(self,args):
        self.ftp.close()
        self.authorized = False
        print("Disconnected!")
        if self.bell: print("\a")


FTPShell().cmdloop()