atm_vault_balance = 50000000
user_account_balance = 10000000 
fee = 1100

'''
Chức năng 1: Xem số dư tài khoản

Hệ thống gọi hàm display_balances(). Hàm này in ra màn hình chuỗi thông báo chứa số dư tài khoản hiện tại (user_account_balance). Trong thực tế không in số dư của ATM cho khách, nhưng phục vụ mục đích debug bài tập, hàm này cần in cả atm_vault_balance ra màn hình.

Chọn giao dịch (1-4): 1
--- SỐ DƯ TÀI KHOẢN ---
Tài khoản của bạn: 10,000,000 VND
(Debug) Tiền mặt trong ATM: 50,000,000 VND
'''
def display_balances(balance_user, balance_atm ):
    print("--- SỐ DƯ TÀI KHOẢN ---")
    print(f"Tài khoản của bạn: {balance_user:,} VND")
    print(f"Tiền mặt trong ATM: {balance_atm:,} VND")


'''
Chức năng 2: Nạp tiền vào tài khoản

Yêu cầu người dùng nhập số tiền muốn nạp từ bàn phím. 

Gọi hàm deposit_money(amount). Hàm này sử dụng từ khóa global để cập nhật cả 2 biến toàn cục: user_account_balance tăng thêm amount và atm_vault_balance tăng thêm amount (Vì tiền vật lý được đưa vào máy). 

Return True nếu nạp thành công và hệ thống in ra thông báo giao dịch thành công kèm số dư tài khoản mới nhất.

Trường hợp nạp tiền hợp lệ:

Chọn giao dịch (1-4): 2
--- NẠP TIỀN ---
Nhập số tiền muốn nạp: 2000000
Giao dịch thành công! Số dư tài khoản hiện tại: 12,000,000 VND.
'''
def validate_num(number):
    """Hàm chuẩn hóa số

    Args:
        number (str): số trc khi chuẩn hóa

    Returns:
        bool : True hc False
    """
    try:
        number = int(number)
        if number < 0:
            return False
        return True
    except:
        return False
    
def deposit_money(amount):
    """Thực hiện giao dịch

    Args:
        amount (istrrt): số lượng tiền nhập vào

    Returns:
        bool : True hc False
    """
    global atm_vault_balance
    global user_account_balance
    if validate_num(amount):
        amount = int(amount)
        user_account_balance += amount
        atm_vault_balance += amount
        print(f"Giao dịch thành công! Số dư tài khoản hiện tại: {user_account_balance:,} VND.")
        return True
    return False

def check_withdrawal_rules(amount):
    """ktra tiền nhập vào

    Args:
        amount (istrrt): số lượng tiền nhập vào

    Returns:
        str: trạng thái tiền
    """
    global atm_vault_balance
    global user_account_balance
    if validate_num(amount):
        amount = int(amount)
        if amount > user_account_balance:
            return "INSUFFICIENT_FUNDS"
        elif amount > atm_vault_balance:
            return "ATM_OUT_OF_CASH"
        else:
            return "OK"
    return False

def execute_withdrawal(total_deduction):
    """Hàm rút tiền

    Args:
        total_deduction (str): số tiền rút
    """
    global atm_vault_balance
    global user_account_balance
    global fee
    if validate_num(total_deduction):
        total_deduction = int(total_deduction)
        user_account_balance -= (total_deduction + fee)
        atm_vault_balance -= total_deduction
        print(f"Bạn đã rút thành công {total_deduction:,} VND.")
        print(f"Số dư tài khoản còn lại: {user_account_balance:,} VND.")
        

def main():
    while True:
        choice = input('''
============= SMART ATM =============
1. Xem số dư
2. Nạp tiền
3. Rút tiền
4. Kết thúc giao dịch
=====================================
Vui lòng chọn giao dịch (1-4): ''')
        match choice:
            case '1':
                print()
                display_balances(user_account_balance, atm_vault_balance)
            case '2':
                print("--- NẠP TIỀN ---")
                amount_inp = input("Nhập số tiền muốn nạp: ")
                if not deposit_money(amount_inp):
                    print("Giao dịch thất bại")
                    continue
                
            case '3':
                print("--- RÚT TIỀN ---")
                money_inp = input("Nhập số tiền cần rút: ")
                if not validate_num(money_inp):
                    print("Giao dịch thất bại")
                    continue
                if check_withdrawal_rules(money_inp) == "INSUFFICIENT_FUNDS":
                    print("Tổng tiền bị trừ vượt quá số dư hiện tại.")
                    continue
                    
                elif check_withdrawal_rules(money_inp) == "ATM_OUT_OF_CASH":
                    print("Số tiền khách rút vượt quá số tiền trong ATM")
                    continue
                else:
                    print("Giao dịch đang xử lý...")
                    print(f"Phí giao dịch: {fee:,} VND")
                    execute_withdrawal(money_inp)
                    
            case '4':
                print("Thoát chương trình")
                break
            case _:
                print("Lỗi cú pháp")
                
main()