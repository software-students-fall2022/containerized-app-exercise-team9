
import pytest
import datetime


test_doc = {'_id': '638bee05648e1b03651f707a', 
'screen_text': 'When nobody is around, the trees gossip about the people who have walked under them.', 
'ouput_text': "When nobody's around the trees gossip about the people who have walked into.", 'time_taken': 4.622, 
'words_spoken': 13, 'correct_words_spoken': 11, 'total_words_per_second': 2.8126352228472524, 
'correct_words_per_second': 2.3799221116399827, 'accuracy': 73.33333333333333, 
'time_created': datetime.datetime(2022, 12, 3, 19, 47, 1, 569000)}


def test_sanity_check():
        """
        Sanity check
        """
        expected = True
        actual = True
        assert actual == expected

def test_handler(test_doc):



    



