import time
import os
import re
import random
import logging
from pydub import AudioSegment
from pydub.playback import play
logging.basicConfig(level=logging.INFO,filename='test.log', format='%(asctime)s:%(levelname)s:%(message)s')

class TuringTest:
    def __init__(self):
        self.filelist = self.get_files()
        self.number_of_tests = 1
        self.number_of_cycles = 10

    def get_files(self):
        """Get all files in human and neural directories"""
        file_list = []
        for path, subdirs, files in os.walk('.'):
            for name in files:
                filepath = os.path.join(path, name)
                if filepath.endswith( ('.py', '.md', '.DS_Store', '.log')):
                    continue
                fp = os.path.join(path,name)
                file_list.append(fp)
        return file_list

    def pick_list(self, file_list=None):
        """Return a random list of audio files to interpret"""
        logging.info(f"Number of random choices: {self.number_of_cycles}")
        subset_list = random.sample(file_list, k=self.number_of_cycles)
        return subset_list

    def play_audio_clip(self, file=None):
        """Play provided audio clip"""
        audioclip = AudioSegment.from_file(file, format= 'm4a')
        play(audioclip)
        print(f'Quick break...')
        time.sleep(2)

    def test_cycle(self):
        """Test a single cycle"""
        subset = self.pick_list(self.filelist)
        #print(f"Subset list:\n {subset}")
        logging.info(f"Subset list:\n {subset}")
        for file in subset:
            human_voice = re.search('human', file)
            neural_voice = re.search('neural', file)
            if human_voice:
                print('HUMAN\n')
                logging.info("HUMAN")
            if neural_voice:
                print('NEURAL\n')
                logging.info("NEURAL")

        for clip in subset:
            self.play_audio_clip(clip)

if __name__ == "__main__":
    t = TuringTest()
    logging.info(f"Number of tests: {t.number_of_tests}")
    for i in range(t.number_of_tests):
        t.test_cycle()
        print("\033[92m TEST BREAK...\033[00m")
        time.sleep(3)
