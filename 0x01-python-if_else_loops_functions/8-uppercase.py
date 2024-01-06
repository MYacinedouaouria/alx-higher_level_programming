#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str) - 1):
        print(
            f"{chr(ord(str[i]) - 32)}" if
            97 <= ord(str[i]) <= 122 else f"{str[i]}",
            end=""
            )

    print(
        f"{chr(ord(str[-1]) - 32)}" if
        97 <= ord(str[-1]) <= 122 else f"{str[-1]}"
        )
