##HW 1
import pexpect
newprimates = open("primates2.nex", "w")
oldprimates = open("primates.nex").read() 
for line in oldprimates:
    newprimates.write(line.replace("mcmc", "mcmcp"))
newprimates.close()

child = pexpect.spawn("mb -i primates2.nex") 
#-i tells mrbayes to run in interactive mode
#send the string "mcmc" to the process. This tells mrbayes to start running. The \r is carriage return
child.sendline(r"mcmc") 
# tells mrbayes to stop the analysis (do not continue)
child.sendline("no") 
child.expect("MrBayes >") # wait for the mrbayes prompt.
print child.before
quit
