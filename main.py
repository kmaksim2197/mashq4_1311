class UserAccount:
    def __init__(self, username, password):
        self.__username = username
        self.__password = None
        self.set_password(password)

    def get_username(self):
        return self.__username

    def set_password(self, new_password):
        if len(new_password) >= 8:
            self.__password = new_password
            return True
        return False

    def _check_password(self, password):
        return self.__password == password


class AuthenticationSystem:
    def __init__(self):
        self.__users = {}

    def register(self, username, password):
        if username in self.__users:
            print(f"Xato: '{username}' allaqachon ro'yxatdan o'tgan.")
            return False
        user = UserAccount(username, password)
        if user._UserAccount__password is not None:
            self.__users[username] = user
            print(f"Muvaffaqiyat: '{username}' ro'yxatdan o'tdi.")
            return True
        print("Xato: Parol kamida 8 belgidan iborat bo'lishi kerak.")
        return False

    def login(self, username, password):
        user = self.__users.get(username)
        if user and user._check_password(password):
            print(f"Muvaffaqiyat: '{username}' tizimga kirdi.")
            return True
        print(f"Xato: Noto'g'ri foydalanuvchi nomi yoki parol.")
        return False

    def change_password(self, username, old_password, new_password):
        user = self.__users.get(username)
        if user and user._check_password(old_password):
            if user.set_password(new_password):
                print("Parol muvaffaqiyatli o'zgartirildi.")
                return True
            else:
                print("Yangi parol kamida 8 belgidan iborat bo'lishi kerak.")
                return False
        print("Xato: Eski parol noto'g'ri yoki foydalanuvchi topilmadi.")
        return False

    def list_users(self):
        if not self.__users:
            print("Hozircha hech kim ro'yxatdan o'tmagan.")
        else:
            print("Ro'yxatdan o'tgan foydalanuvchilar:")
            for u in self.__users.keys():
                print(f"  - {u}")


def main():
    auth = AuthenticationSystem()
    print("=== Parol Boshqaruv Tizimiga Xush Kelibsiz ===\n")

    while True:
        print("\n1. Ro'yxatdan o'tish")
        print("2. Tizimga kirish")
        print("3. Parolni o'zgartirish")
        print("4. Foydalanuvchilarni ko'rish")
        print("5. Chiqish")
        choice = input("\nTanlovingizni kiriting (1-5): ").strip()

        if choice == '1':
            username = input("Yangi foydalanuvchi nomi: ").strip()
            password = input("Parol (kamida 8 belgi): ").strip()
            auth.register(username, password)

        elif choice == '2':
            username = input("Foydalanuvchi nomi: ").strip()
            password = input("Parol: ").strip()
            auth.login(username, password)

        elif choice == '3':
            username = input("Foydalanuvchi nomi: ").strip()
            old_pass = input("Eski parol: ").strip()
            new_pass = input("Yangi parol (kamida 8 belgi): ").strip()
            auth.change_password(username, old_pass, new_pass)

        elif choice == '4':
            auth.list_users()

        elif choice == '5':
            print("Dastur tugadi. Xayr!")
            break

        else:
            print("Noto'g'ri tanlov. Iltimos, 1-5 oralig'ida raqam kiriting.")


if __name__ == "__main__":
    main()
