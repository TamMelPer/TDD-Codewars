def spin_words(string)
    array = []
    string.split.each do |word|
      if word.length >= 5
        array << word.reverse
      else
        array << word
      end
    end
    array.join(' ')
  
  end