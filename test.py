import smtplib

def sendmail(from_addr, to_addr_list, cc_addr_list,subject,message,login,password,smtpserver = "smtp.gmail.com:587"):

    header = "From: %s\n" %from_addr
    header += "To: %s\n" % ",".join(to_addr_list)
    header += "CC: %s\n" % ",".join(cc_addr_list)
    header += "To: %s\n\n" % subject
    message = header + message

    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()
    return problems



sendmail(from_addr  = "", #from address
to_addr_list = [""], #to address
cc_addr_list = "information",
subject = "information", #subject text
message = "", #message text
login = "", #login sender mail
password = "") #password sender mail
