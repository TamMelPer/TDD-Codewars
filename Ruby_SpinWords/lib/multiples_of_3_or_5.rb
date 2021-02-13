# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Finish the solution so that it returns the sum of all the multiples of 
# 3 or 5 below the number passed in.

# Note: If the number is a multiple of both 3 and 5, only count it once. 

def solution(number)
    multiples = []
    number.times do |i|
        if (i % 3 == 0) && (i % 5 == 0)
            multiples << i
        elsif i % 3 == 0
            multiples << i
        elsif i % 5 == 0
            multiples << i
        end
    end
    multiples.sum
end

# def solution(num)
#     sum=0
#     for x in 1...num
#       sum+=x if(x%3==0 || x%5==0)
#     end
#     return sum
#   end

# def solution(number)
#     (1...number).select{|n| (n % 5).zero? || (n % 3).zero?}.reduce(:+)
#   end