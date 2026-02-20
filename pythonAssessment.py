import collections
import re

# Count the number of occurrences of a specific word in a text
def count_specific_word(article, search_word) :
    # 2 'str' args
    #   -> String to search through
    #   -> Word to search and count
    # Return the count as an 'int'
    # Display the count of the specified word
    # Edge Case -> Return 0(zero) if no matches are found
    try :
        if search_word.lower() in article.lower() :
            cleaned_text = re.sub(r"[^\w\s]", '', article)
            
            word_list = cleaned_text.lower().split()
            
            word_count = word_list.count(search_word.lower())
            return word_count
        else :
            return 0
    
    except :
        return "Invalid input. Enter a text."


print(count_specific_word("This is a test. This is only a test.", "test"))
print(count_specific_word("apple apple banana banana banana", "banana"))
print(count_specific_word("", "test"))

# Identify the most common word in a text
def identify_most_common_word(article) :
    # 1 'str' arg
    # Return most common word as a 'str'
    # Display the most common word
    # Edge Case -> Empty 'str' should return 'None'
    try :
        while article :
            word_list = article.lower().split()
    
            most_common_tuple = collections.Counter(word_list).most_common(1)
            most_common_word = most_common_tuple[0][0]
            return most_common_word
        else :
            return None
        
    except :
        return "Invalid input. Enter a text."
    
    
# Calculate average word length
def calculate_average_word_length(article) :
    # 1 'str' arg
    # Return average word length as a 'float'
    # Exclude punctuation marks and special chars from the word length calculation
    # Display the average word length
    # Edge Case -> Empty 'str' should retun 0(zero)
    try :
        if article :
            cleaned_text = re.sub(r"[^\w\s]", '', article)
    
            word_list = cleaned_text.split()
    
            total_letters = sum(len(word) for word in word_list)
    
            total_words = len(word_list)
    
            average_word_length = float(total_letters / total_words)
            return average_word_length
        else :
            return 0
    
    except :
        return "Invalid input. Enter a text."
   

# Count the number of paragraphs
def count_paragraphs(article) :
    # 1 'str' arg
    # Return the number of paragraphs as an 'int'
    # Define paragraphs based on empty lines btwn blocks of text
    # Display the count of paragraphs
    # Edge Case -> Empty 'str' should return 1(one)
    try :
        if article :
            paragraph_list = article.split('\n\n')
    
            non_empty_paragraphs = []
            for p in paragraph_list :
                if p.strip() :
                    non_empty_paragraphs.append(p.strip())
    
            num_of_paragraphs = len(non_empty_paragraphs)
            return int(num_of_paragraphs)
        else :
            return 1
        
    except :
        return "Invalid input. Enter a text."


# Count number of sentences
def count_sentences(article) :
    # 1 'str' arg
    # Return the number of sentences as an 'int'
    # Define sentences based on punctuation marks like periods, exclamation marks, and question marks
    # Display the count of sentences
    # Edge Case -> Empty 'str' should return 1
    
    try :
        if article :
            sentences = re.split(r'(?<=[.!?])+', article)
    
            non_empty_sentences = [s.strip() for s in sentences if s.strip()]
    
            num_of_sentences = len(non_empty_sentences)
            return int(num_of_sentences)
        else :
            return 1
        
    except :
        return "Invalid input. Enter a text."
