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

'''
def vld_paswd(strpiece):
    regex_ezy = "^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"
    regex_med = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"
    regex_hrd = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    # Minimum eight characters, at least one letter and one number
    # Minimum eight characters, at least one uppercase letter, one lowercase letter and one number
    # Minimum eight characters, at least one uppercase letter, one lowercase letter, one number and one special character
    if re.match(regex_ezy, strpiece):
        if re.findall(regex_med, strpiece):
            if re.findall(regex_hrd, strpiece):
                return 3
            else:
                return 2
        else:
            return 1
    else:
        return 0
'''

def vld_paswd(strpiece):
    regex_ezy = "^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"
    regex_ezy_sm = "^[a-z]{8,}"
    regex_ezy_lg = "^[A-Z]{8,}"
    regex_ezy_nm = "^[\d]{8,}"
    regex_ezy_sy = "^[@$!%*?&]{8,}"
    regex_med = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"
    regex_med1 = "^(?=.*[a-z])(?=.*[@$!%*?&])(?=.*\d)[A-Za-z\d@$!%*?&]{8,}$"
    regex_med2 = "^(?=.*[A-Z])(?=.*[@$!%*?&])(?=.*\d)[A-Za-z\d@$!%*?&]{8,}$"
    regex_hrd = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    # Minimum eight characters, at least one letter and one number
    # Minimum eight characters, at least one uppercase letter, one lowercase letter and one number
    # Minimum eight characters, at least one uppercase letter, one lowercase letter, one number and one special character
    pats=re.compile(regex_hrd)
    patw=re.compile(regex_ezy)
    patw_sm=re.compile(regex_ezy_sm)
    patw_lg=re.compile(regex_ezy_lg)
    patw_nm=re.compile(regex_ezy_nm)
    patw_sy=re.compile(regex_ezy_sy)
    patm=re.compile(regex_med)
    patm1=re.compile(regex_med1)
    patm2=re.compile(regex_med2)
    mats=re.search(pats, strpiece)
    matw=re.search(patw, strpiece)
    matw_sm=re.search(patw_sm, strpiece)
    matw_lg=re.search(patw_lg, strpiece)
    matw_nm=re.search(patw_nm, strpiece)
    matw_sy=re.search(patw_sy, strpiece)
    matm=re.search(patm, strpiece)
    matm1=re.search(patm1, strpiece)
    matm2=re.search(patm2, strpiece)
    if mats:
        return 3
    elif matm:
        return 2
    elif matm1:
        return 2
    elif matm2:
        return 2
    elif matw or matw_sm or matw_lg or matw_sy or matw_nm:
        return 1
    else:
        return 0