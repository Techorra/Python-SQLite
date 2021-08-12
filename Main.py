import sqlite3 as S3


# functionality goes here
class DatabaseManage(object):
    def __init__(self):
        global con

        try:
            con = S3.connect('courses.db')
            with con:
                cur = con.cursor()
                sql = """
                       CREATE TABLE
                       IF NOT EXISTS
                       course(
                       Id INTEGER PRIMARY KEY AUTOINCREMENT,
                       Name TEXT,
                       Description TEXT,
                       Price TEXT,
                       Is_Private BOOLEAN NOT NULL DEFAULT 1)
                            """
                cur.execute(sql)
        except Exception:
            print("Unable to create a Database !")

    # TODO: create data
    def insert_data(self, data):
        try:
            with con:
                cur = con.cursor()
                sql = """
                        INSERT INTO course(Name, Description, Price, Is_Private) 
                        VALUES(?, ?, ?, ?)
                            """
                cur.execute(sql, data)
                return True
        except Exception:
            return False

    # TODO: read data
    def fetch_data(self):
        try:
            with con:
                cur = con.cursor()
                sql = """
                        SELECT * FROM course
                      """
                cur.execute(sql)
                return cur.fetchall()
        except Exception:
            return False

    # TODO: delete data
    def delete_data(self, id):
        try:
            with con:
                cur = con.cursor()
                sql = """
                        DELETE FROM course WHERE id = ?
                      """
                cur.execute(sql, [id])
                return True
        except Exception:
            return False


# TODO: provide interface to user
def main():
    print("*" * 40)
    print("\n :: COURSE MANAGEMENT :: \n")
    print("*" * 40)
    print("\n")

    db = DatabaseManage()

    print("#" * 40)
    print("\n :: User Manual :: \n")
    print("#" * 40)

    while (True):

        print("\nPress 1. Insert a new course \n")
        print("Press 2. Show all courses \n")
        print("Press 3. Delete a course (NEED ID OF COURSE) \n")
        print("Press 4. For quit \n")
        print("#" * 40)
        print("\n")

        choice = input("\n Enter a choice: ")

        if choice == "1":
            name = input("\n Enter course name: ")
            description = input("\n Enter course description: ")
            price = input("\n Enter course price: ")
            private = input(
                "\n Is this course private [0] for private and [1] for public : ")

            if db.insert_data([name, description, price, private]):
                print("\n")
                print(" ***** Course was inserted successfully ! ***** \n")
                print("#" * 40)
                print("\n")
            else:
                print("#" * 40)
                print("\n ***** OOPS, SOMETHING IS WRONG ***** ")
                print("\n")
                print("#" * 40)
                print("\n")

        elif choice == "2":
            print("\n :: Course List :: \n")

            for index, item in enumerate(db.fetch_data()):
                print("*" * 40)
                print("\n")
                # print("\n SL no : " + str(index + 1))
                print("Course ID : " + str(item[0]))
                print("Course Name : " + str(item[1]))
                print("Course Description : " + str(item[2]))
                print("Course Price : " + str(item[3]))
                private = 'Yes' if item[4] else 'No'
                print("Is Private : " + private)
                print("\n")
                print("*" * 40)
                print("\n")

        elif choice == "3":
            record_id = input("Enter the course ID: ")

            if db.delete_data(record_id):
                print("\n")
                print(" ***** Course was delete with successfully ! ***** ")
                print("\n")
            else:
                print("\n ***** OOPS, SOMETHING WENT WRONG ***** \n")

        elif choice == "4":
            print("\n")
            print("*" * 40)
            print("\n :: Good Bye ! :: \n")
            print("*" * 40)
            break

        else:
            print("\n")
            print(" ***** Invalid Choice ***** ")
            print("\n")


if __name__ == "__main__":
    main()
