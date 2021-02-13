require 'multiples_of_3_or_5'

# Given one number(n), list all numbers from 1 to n. 
# Go through the list, check if the number is divisible by 3 & 5, 3, 5.
# If yes, store those numbers in a list.
# Return a sum of those numbers

# Input         -   Output
# 4             -   3
# 6             -   8
# 10            -   23
# 16            -   60

describe '#solution' do
    it 'returns 3 when given 4' do
        expect(solution(4)).to eq 3
    end

    it 'returns the sum of 3 and 5 when given 6' do
        expect(solution(6)).to eq 8
    end
    
    it 'returns 23 when given 10' do
        expect(solution(10)).to eq 23
    end

    it 'returns 60 when given 16' do
        expect(solution(16)).to eq 60
    end
end

