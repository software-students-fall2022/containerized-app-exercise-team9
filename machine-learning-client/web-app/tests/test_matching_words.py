import pytest
from transcribe_audio import matching_words

class Tests:

    def sanity_check(self):
        """
        Throwaway test.
        """
        expected = True
        actual = True
        assert expected == actual
   
    def test_all_matching(self):
        """
        Test matching_words between equal arrays, should return all matching
        """
        main = ['a', 'b', 'c', 'd', 'e', 'f']
        secondary = ['a', 'b', 'c', 'd', 'e', 'f']

        expected_num = 6
        expected_arr = [0,1,2,3,4,5]

        actual_num, actual_arr = matching_words(main, secondary)

        assert expected_num == actual_num, f"Expected number of matching words between {main} and {secondary} to be {expected_num}. Instead it was {actual_num}."
        assert expected_arr == actual_arr, f"Expected indeces of matching words between {main} and {secondary} to be {expected_arr}. Instead it was {actual_arr}."

    def test_matching_with_noise(self):
        """
        Test matching_words with noise, should return all matching
        """
        main = ['a', 'b', 'c', 'd', 'e', 'f']
        secondary = ['a', 'b', 'c', 'd', 'e', 'NO', 'NO', 'f']
        
        expected_num = 6
        expected_arr = [0,1,2,3,4,5]

        actual_num, actual_arr = matching_words(main, secondary)

        assert expected_num == actual_num, f"Expected number of matching words between {main} and {secondary} to be {expected_num}. Instead it was {actual_num}."
        assert expected_arr == actual_arr, f"Expected indeces of matching words between {main} and {secondary} to be {expected_arr}. Instead it was {actual_arr}."
    
    def test_matching_wrong_spot(self):
        """
        Test matching_words with one element in the wrong spot, should return all except one matching
        """
        main = ['a', 'b', 'c', 'd', 'e', 'f']
        secondary = ['a', 'f', 'b', 'c', 'd', 'e']
        
        expected_num = 5
        expected_arr = [0,1,2,3,4]

        actual_num, actual_arr = matching_words(main, secondary)

        assert expected_num == actual_num, f"Expected number of matching words between {main} and {secondary} to be {expected_num}. Instead it was {actual_num}."
        assert expected_arr == actual_arr, f"Expected indeces of matching words between {main} and {secondary} to be {expected_arr}. Instead it was {actual_arr}."    
    
    def test_matching_missing_elements(self):
        """
        Test matching_words with elements missing, should return correct indeces
        """
        main = ['a', 'b', 'c', 'd', 'e', 'f']
        secondary = ['a', 'c', 'd', 'e']
        
        expected_num = 4
        expected_arr = [0,2,3,4]

        actual_num, actual_arr = matching_words(main, secondary)

        assert expected_num == actual_num, f"Expected number of matching words between {main} and {secondary} to be {expected_num}. Instead it was {actual_num}."
        assert expected_arr == actual_arr, f"Expected indeces of matching words between {main} and {secondary} to be {expected_arr}. Instead it was {actual_arr}."   

    def test_matching_duplicate_elements(self):
        """
        Test matching_words with duplicate elements
        """
        main = ['a', 'b', 'c', 'd', 'e', 'f']
        secondary = ['a', 'f', 'b', 'b', 'c', 'e', 'd', 'e', 'f']
        
        expected_num = 6
        expected_arr = [0,1,2,3,4,5]

        actual_num, actual_arr = matching_words(main, secondary)

        assert expected_num == actual_num, f"Expected number of matching words between {main} and {secondary} to be {expected_num}. Instead it was {actual_num}."
        assert expected_arr == actual_arr, f"Expected indeces of matching words between {main} and {secondary} to be {expected_arr}. Instead it was {actual_arr}."   