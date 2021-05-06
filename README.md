# Language classification

> Product Perpuses:
1. Identify text's language, based on statistical model.

>Algorithm explained:
1. The basic idea is to keep statistics of letters or sequences of letters and identify the language based on the difference between These statistics. For example, the letter 'a' appears in both English and French in just over 8% of cases and does not help to distinguish between the languages. In contrast, the letter 'f' appears in English in over 2% of cases in contrast to less than 1% of cases in French.
2. Letter sequences with n's length, usually have more information than single letters (these sequences are called n-grams (e.g. the most common of 2 lengths nth in English is 'th' and appears in more than 1.5% of cases. In French, this sequence is not even one of the 31 most common words!).
3. Thus, first we will try to identify language using one letter only.If the identification value is not significant we will increase the examination to 2 letters and so on, untill we will reach the maximum value of letter sequences.
4. Before start using the program, we need to teach it the languages statistics. There for we built a function that takes a known languge text. the programm will create a dictionary based on these texts. 
> 

Copyright (c) 2021 David Sasson

-David Sasson
