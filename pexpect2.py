#HW 2
#spawn an interactive mrbayes process
process= pexpect.spawn("mb -i")
#send the command "execute primates2.nex" to mrbayes
process.sendline("mb -i primates2.nex")
#send the sumt command to mrbayes
process.sendline(r"sumt")
#check to see that the mrbayes command prompt is returned
process.expect("MrBayes >")
#print everything before the mrbayes prompt
print process.before
#send the sump command
process.sendline(r"sump")
#quit mrbayes
quit