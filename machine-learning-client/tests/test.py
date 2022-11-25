import pytest
import sys
import transcribe_audio as transcribe

class Tests:
    def sanity_check(self):
        """
        Throwaway test.
        """
        expected = True
        actual = True
        assert expected == actual
    
    def test_no_wav_file(self):
        """
        Testing if error is raised when a non-wav file is used.
        """
        with pytest.raises(ValueError) as err:
            transcribe.transcribe("")