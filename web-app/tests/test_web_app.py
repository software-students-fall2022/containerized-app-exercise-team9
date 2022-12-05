import pytest
import datetime
import handler

test_doc = {'_id': '638bee05648e1b03651f707a', 
'screen_text': 'When nobody is around, the trees gossip about the people who have walked under them.', 
'ouput_text': "When nobody's around the trees gossip about the people who have walked into.", 
'time_taken': 4.622, 
'words_spoken': 13, 
'correct_words_spoken': 11, 
'total_words_per_second': 2.8126352228472524, 
'correct_words_per_second': 2.3799221116399827, 
'accuracy': 73.33333333333333, 
'time_created': datetime.datetime(2022, 12, 3, 19, 47, 1, 569000)}

class Tests:

        def test_sanity_check(self):
                """
                Sanity check
                """
                expected = True
                actual = True
                assert actual == expected

        def test_handler_return_types_strings(self):
                """
                Asserting that strings are in right indices. 
                """
                test_doc = {'_id': '638bee05648e1b03651f707a', 
                'screen_text': 'When nobody is around, the trees gossip about the people who have walked under them.', 
                'ouput_text': "When nobody's around the trees gossip about the people who have walked into.", 
                'time_taken': 4.622, 
                'words_spoken': 13, 
                'correct_words_spoken': 11, 
                'total_words_per_second': 2.8126352228472524, 
                'correct_words_per_second': 2.3799221116399827, 
                'accuracy': 73.33333333333333, 
                'time_created': datetime.datetime(2022, 12, 3, 19, 47, 1, 569000)}

                actual = handler.handle(test_doc)

                assert (type(actual[1]) == str) & (type(actual[2]) == str)

        def test_handler_return_types_floats(self):
                """
                Asserting that floats are in right indices. 
                """
                test_doc = {'_id': '638bee05648e1b03651f707a', 
                'screen_text': 'When nobody is around, the trees gossip about the people who have walked under them.', 
                'ouput_text': "When nobody's around the trees gossip about the people who have walked into.", 
                'time_taken': 4.622, 
                'words_spoken': 13, 
                'correct_words_spoken': 11, 
                'total_words_per_second': 2.8126352228472524, 
                'correct_words_per_second': 2.3799221116399827, 
                'accuracy': 73.33333333333333, 
                'time_created': datetime.datetime(2022, 12, 3, 19, 47, 1, 569000)}

                actual = handler.handle(test_doc)

                def areNumbers(actual): 
                        for i in range(3, 8):
                                if type(actual[i]) != float: 
                                        return False
                        return True

                assert areNumbers(actual)

        def test_handler_return_types_floats_length(self):
                """
                Asserting that handler is the same length of the object it is handling. 
                """
                test_doc = {'_id': '638bee05648e1b03651f707a', 
                'screen_text': 'When nobody is around, the trees gossip about the people who have walked under them.', 
                'ouput_text': "When nobody's around the trees gossip about the people who have walked into.", 
                'time_taken': 4.622, 
                'words_spoken': 13, 
                'correct_words_spoken': 11, 
                'total_words_per_second': 2.8126352228472524, 
                'correct_words_per_second': 2.3799221116399827, 
                'accuracy': 73.33333333333333, 
                'time_created': datetime.datetime(2022, 12, 3, 19, 47, 1, 569000)}

                actual = handler.handle(test_doc)

                assert len(actual) == len(test_doc)




                








    



