#1.1
def extract_usernames_from_emails(emails):
    usernames = []
    for idx in emails:
        idx = idx.split("@")[0]
        usernames.append(idx)
    return usernames

#1.2
def find_and_replace(words, word_to_find, word_to_replace):
    new_lst = []
    for idx in words:
        if idx == word_to_find:
            new_lst.append(word_to_replace)
        elif idx != word_to_find:
            new_lst.append(idx)
    return new_lst
        
