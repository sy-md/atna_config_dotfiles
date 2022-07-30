import os

#first install python 
#secound install git 
comfirm = input("are you in your Home directory with your dotfiles: y/n ")
if comfirm == "y":
	os.system("git clone https://github.com/sy-md/athena-config.git")
	os.system(" cd athena-config")
	os.system("yes | cp -rf .config/ .oh-my-zsh/ .vim/ .zshrc ../")
	os.system("git clone https://github.com/sy-md/Athena.git")
	os.system("git clone https://github.com/sy-md/ohmyzsh.git ../")
	os.system("git clone https://github.com/sy-md/nvim.git ../")
if comfirm  == "n":
	exit()





	






