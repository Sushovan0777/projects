import pyscreenshot
def main():
    while True:
        choice=input('Press 1 to take screenshot.\nPress 2 to save screenshot.\nPress 3 to view screenshot.\nChoice:')
        if choice =='1':
            image=pyscreenshot.grab()
        elif choice =='2':
            image.save('screenshot.png')
        elif choice =='3':
            image.show()
        else:
            print("Invalid choice.")
        if input("Do you want to continue(y/n)?") != 'y':
            break


if __name__ == '__main__':
    main()