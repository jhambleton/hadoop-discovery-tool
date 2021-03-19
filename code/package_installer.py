import os
import re

# initialise flags to identify packages
nload_dt, vnstat_dt, gcc_dt, odbc_dt, sasl_dt, pydevel_dt, =  "", "", "", "", "", ""
# list to hold installed and non installed data
installed, not_installed = [], []
# This command will fetch os-name for ex. centos,debian,opensuse etc.
os_name = os.popen("grep PRETTY_NAME /etc/os-release").read()
os_name = os_name.lower()
final_version = ""

vs = os.popen("grep VERSION_ID /etc/os-release").read()
trash, version = vs.split("=")
final_version = version.replace('"', "")
final_version = final_version.strip("\n")

dt = os.popen("grep ID= /etc/os-release").read()
dt = dt.splitlines()
for i in dt:
    if re.search(r"\b" "ID" r"\b", i):
        get_name = i

trash, name = get_name.split("=")
final_name = name.replace('"', "")
final_name = final_name.strip("\n")

no_show = 0
"""
Here based on the os of the current system respective block will execute and will install packages 
with their respective package managers.
"""
try:
    if "centos" in os_name and final_version >= "7":
        print("Os Dependencies Installing...")
        os.popen('pip3 install -U pip').read()
        os.popen("yum install epel-release -y").read()
        os.popen("yum install nload -y").read()
        os.popen("yum install vnstat -y").read()
        os.popen("yum install gcc gcc-c++ -y").read()
        os.popen("yum install cyrus-sasl-devel -y").read()
        os.popen("yum install unixODBC-devel -y").read()
        os.popen("yum install python3-devel -y").read()
        nload_dt = os.popen("rpm -qa | grep nload").read()
        vnstat_dt = os.popen("rpm -qa | grep vnstat").read()
        gcc_dt = os.popen("rpm -qa | grep gcc-c++").read()
        sasl_dt = os.popen("rpm -qa | grep cyrus-sasl-devel").read()
        odbc_dt = os.popen("rpm -qa | grep unixODBC-devel").read()
        pydevel_dt = os.popen("rpm -qa | grep python3-devel").read()
        venv_dt = "Venv"
    elif "ubuntu" in os_name and final_version >= "18.04":
        print("Os Dependencies Installing...")
        os.popen('pip3 install -U pip').read()
        os.popen("apt install -y nload 2>/dev/null").read()
        os.popen("apt install -y vnstat 2>/dev/null").read()
        os.popen("apt install -y g++ 2>/dev/null").read()
        os.popen("apt install -y sasl2-bin 2>/dev/null").read()
        os.popen("apt install -y unixodbc-dev 2>/dev/null").read()
        os.popen("apt install -y python3-dev 2>/dev/null").read()
        os.popen("apt install -y python3-pip 2>/dev/null").read()
        os.popen("apt install -y python3-venv 2>/dev/null").read()
        os.popen("apt install -y libsasl2-dev 2>/dev/null").read()
        nload_dt = os.popen("apt list --installed 2>/dev/null | grep nload").read()
        vnstat_dt = os.popen("apt list --installed 2>/dev/null | grep vnstat").read()
        gcc_dt = os.popen("apt list --installed 2>/dev/null | grep g++-7").read()
        sasl_dt = os.popen("apt list --installed 2>/dev/null | grep sasl2-bin").read()
        odbc_dt = os.popen(
            "apt list --installed 2>/dev/null | grep unixodbc-dev"
        ).read()
        pydevel_dt = os.popen(
            "apt list --installed 2>/dev/null | grep python3-dev"
        ).read()
    elif "red hat" in os_name and final_version >= "7":
        print("Os Dependencies Installing...")
        os.popen('pip3 install -U pip').read()
        os.popen("yum install epel-release -y").read()
        os.popen("yum install nload -y").read()
        os.popen("yum install vnstat -y").read()
        os.popen("yum install gcc gcc-c++ -y").read()
        os.popen("yum install cyrus-sasl-devel -y").read()
        os.popen("yum install unixODBC-devel -y").read()
        os.popen("yum install python3-devel -y").read()
        nload_dt = os.popen("rpm -qa | grep nload").read()
        vnstat_dt = os.popen("rpm -qa | grep vnstat").read()
        gcc_dt = os.popen("rpm -qa | grep gcc-c++").read()
        sasl_dt = os.popen("rpm -qa | grep cyrus-sasl-devel").read()
        odbc_dt = os.popen("rpm -qa | grep unixODBC-devel").read()
        pydevel_dt = os.popen("rpm -qa | grep python3-devel").read()
    elif "suse" in os_name and final_version >= "12":
        print("Os Dependencies Installing...")
        os.popen("zypper -n install nload").read()
        os.popen("zypper -n install vnstat").read()
        os.popen("zypper -n install gcc gcc-c++").read()
        os.popen("zypper -n install cyrus-sasl-devel").read()
        os.popen("zypper -n install unixODBC-devel").read()
        os.popen("zypper -n install python3-devel").read()
        nload_dt = os.popen("rpm -qa | grep nload").read()
        vnstat_dt = os.popen("rpm -qa | grep vnstat").read()
        gcc_dt = os.popen("rpm -qa | grep gcc-c++").read()
        sasl_dt = os.popen("rpm -qa | grep cyrus-sasl-devel").read()
        odbc_dt = os.popen("rpm -qa | grep unixODBC-devel").read()
        pydevel_dt = os.popen("rpm -qa | grep python3-devel").read()
    else:
        print("OS " + final_name + " " + final_version1 + " Not supported")
        no_show = 1
except Exception as e:
    pass
# Here Code will check if flags have been set then accordingly lists will be appened with proper data
if nload_dt != "":
    installed.append(nload_dt)
else:
    not_installed.append("Nload")
if vnstat_dt != "":
    installed.append(vnstat_dt)
else:
    not_installed.append("Vnstat")
if gcc_dt != "":
    installed.append(gcc_dt)
else:
    not_installed.append("GCC-C++")
if odbc_dt != "":
    installed.append(odbc_dt)
else:
    not_installed.append("Unix ODBC-Devel")
if sasl_dt != "":
    installed.append(sasl_dt)
else:
    not_installed.append("Cyrus SASL-Devel")
if pydevel_dt != "":
    installed.append(pydevel_dt)
else:
    not_installed.append("Python3-Devel")
installed_string = ",".join(installed)
not_installed_string = ",".join(not_installed)
# Here the code will decide based on the size of list which message to show to user about os packages installation
if no_show == 0:
    if len(installed) == 0:
        print("Installed packages :- None")
    else:
        print("Installed Packages " + installed_string)
    if len(not_installed) == 0:
        print("Packages not Installed :- None")
    else:
        print("Packages not Installed " + not_installed_string)
    if "GCC-C++" in not_installed_string or "Unix ODBC-Devel" in not_installed_string or "Python3-Devel" in not_installed_string or "Cyrus SASL-Devel" in not_installed_string:
        print("Cannot proceed as package ",not_installed_string," not installed")
        os.popen("exit 1").read()
else:
    pass