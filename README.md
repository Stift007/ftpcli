# FTPCli
Simplistic FTP Client in Python


### Usage
Upon starting:

* `open [IP]` to connect to a Server  
* `user` to re-login (or change user)  
* `pwd` to print the Current Directory  
* `mkd [dirname]` to create a directory on the Server  
* `ls <opt:dirname>` to list \<dirname\>s Contents. Defaults to :call pwd:  
* `cd <opt:dirname>` to change the current working directory do \<dirname\>. Defaults to /  
* `get [filename]` to clone a file from the Server  
* `put [filename]` to push a file to the server  
* `mkdir [dirname]` same as :call mkd:  
* `literal [cmd]` to run a Literal FTP Command  
* `status` to show all Configurations  
* `debug` to toggle Debug Mode  
* `bell` to toggle Bell Mode  
* `bye` to disconnect and close the client  
* `close` to log off the Server
