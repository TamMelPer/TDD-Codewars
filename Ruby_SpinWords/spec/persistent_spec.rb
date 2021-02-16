require 'persistent'

# persistence(39) # returns 3, because 3*9=27, 2*7=14, 1*4=4
                 # and 4 has only one digit

#  persistence(999) # returns 4, because 9*9*9=729, 7*2*9=126,
                  # 1*2*6=12, and finally 1*2=2

#  persistence(4) # returns 0, because 4 is already a one-digit number

describe '#persistence' do
    it 'returns 0 when given a one digit number' do
        expect(persistence(4)).to eq 0
    end
    
    it 'returns 1 when given 14' do
        expect(persistence(14)).to eq 1
    end

    it 'returns 2 when given 27' do
        expect(persistence(27)).to eq 2
    end
end