import my_package as mp
import my_package.my_sub_package as msp
import my_package.my_sub_package.my_sub_sub_package as mssp
# import my_package._utils as u

# print(u.get_current_package())
mp.hello()
msp.hello()
mssp.hello()


