require 'spin_words'

describe '#spin_words' do
  it 'returns the string if all words are 5 or less letters' do
    expect(spin_words("This is a test")). to eq "This is a test"
  end

  it 'returns the string with words 5 or more letters reversed' do
    expect(spin_words("This is another test")). to eq "This is rehtona test"
  end

end