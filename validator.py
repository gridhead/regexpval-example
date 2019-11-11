import re

def vld_email(strpiece):
    regex = "^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$"
    if re.search(regex, strpiece):
        return 1
    else:
        return 0

def vld_phnum(strpiece):
    regex = "^([\+][0-9]{2,3})?[1-9][0-9]{9}$"
    if re.search(regex, strpiece):
        return 1
    else:
        return 0

def vld_fname(strpiece):
    regex = "^[A-Z]{3,20}$"
    strpiece = strpiece.upper()
    if re.search(regex, strpiece):
        return 1
    else:
        return 0


def vld_lname(strpiece):
    regex = "^[A-Z]{3,20}$"
    strpiece = strpiece.upper()
    if re.search(regex, strpiece):
        return 1
    else:
        return 0

def vld_sepin(strpiece):
    regex = "^[0-9]{6}$"
    if re.search(regex, strpiece):
        return 1
    else:
        return 0

def vld_paswd(strpiece):
    reg_wk0 = r"^(?=.*[a-z])(?=.*\d)[a-z\d]{8,}$"
    # minimum eight characters, at least one lowercase letter and one number
    reg_wk1 = r"^(?=.*[A-Z])(?=.*\d)[A-Z\d]{8,}$"
    # Minimum eight characters, at least one uppercase letter and one number
    reg_wk2 = r"^[A-Z]{8,}$"
    # Only uppercase alphabets
    reg_wk3 = r"^[a-z]{8,}$"
    # Only lowercase alphabets
    reg_wk4 = r"^[0-9]{8,}$"
    # Only numbers
    reg_wk4 = r"^[@$!%*?&]{8,}$"
    # Only Symbols
    reg_md0 = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"
    # Minimum eight characters, at least one uppercase letter, one lowercase letter and one number:
    reg_md1 = r"^(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[a-z\d@$!%*?&]{8,}$"
    # Minimum eight characters, at least one number and lowercase letter and one special character
    reg_md2 = r"^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Z\d@$!%*?&]{8,}$"
    # Minimum eight characters, at least one number and uppercase letter and one special character
    reg_str = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    # Minimum eight characters, at least one uppercase letter, one lowercase letter, one number and one special character
    mats0 = re.search(reg_str, strpiece)
    matw0 = re.search(reg_wk0, strpiece)
    matw1 = re.search(reg_wk1, strpiece)
    matw2 = re.search(reg_wk2, strpiece)
    matw3 = re.search(reg_wk3, strpiece)
    matw4 = re.search(reg_wk4, strpiece)
    matm0 = re.search(reg_md0, strpiece)
    matm1 = re.search(reg_md1, strpiece)
    matm2 = re.search(reg_md2, strpiece)
    if mats0:
        return 3
    elif matm0 or matm1 or matm2:
        return 2
    elif matw0 or matw1 or matw2 or matw3 or matw4:
        return 1
    else:
        return 0