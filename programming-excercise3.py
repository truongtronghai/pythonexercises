def myFunc(a, b):
    global result
    result = a * b
    print("Result is {}".format(result))


if __name__ == "__main__":
    result = 12  # initial value
    myFunc(2, 3)
    ### TODO: What is the value of “result” here ?
    print(result)
