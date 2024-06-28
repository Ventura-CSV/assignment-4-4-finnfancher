def main():

    numbers = []
    """
    ########################################
    Code Your Program here
    ########################################
    """
    for i in range(5):
        numbers.append((input("Enter number: ")))
        
    min = numbers[0]
    max = numbers[0]
    
    for i in range(1, 5):
        if(min > numbers[i]):
            min = numbers[i]
        if(max < numbers[i]):
            max = numbers[i]
        

    print(numbers)
    print(max, min)
    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, max, min


if __name__ == '__main__':
    main()
