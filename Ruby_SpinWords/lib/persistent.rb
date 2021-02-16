# Write a function, persistence, that takes in a positive parameter num and 
# returns its multiplicative persistence, which is the number of times you 
# must multiply the digits in num until you reach a single digit.

def persistence(n)
    count = 0
    number_array = n.digits
    while number_array.size > 1
        number_array = number_array.reduce(:*).digits
        count +=1
    end
    count
end

