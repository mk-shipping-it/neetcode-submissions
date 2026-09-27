from collections import defaultdict
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        # assuming each email contains an @

        domains = defaultdict(int)
        for email in emails:
            
            domain_index = email.index('@')
            str_local_index = email[:domain_index]
            
            while '.' in str_local_index:
                dot_index = str_local_index.index('.')
                # slice or go haystack
                # we choose slice
                first_half = str_local_index[:dot_index]
                second_half = str_local_index[dot_index+1:]
                str_local_index = "".join([first_half, second_half])

            if '+' in str_local_index:
                plus_index = str_local_index.index('+')
                # slice or go haystack
                # we choose slice
                first_half = str_local_index[:plus_index]
                str_local_index = str(first_half)
                email_combination = str_local_index + email[domain_index:]
                print(email_combination)
                domains[email_combination]+=1
            else:
                email_combination = str_local_index + email[domain_index:]
                domains[email_combination]+=1

        print(domains)
        return len(list(domains.keys()))