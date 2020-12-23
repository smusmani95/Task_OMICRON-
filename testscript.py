import unittest
from datetime import timedelta,datetime
from memorize_class_implimentation import class_memorise as undertest # script under test
#from datetime import datetime
from freezegun import freeze_time



def add_to_time(year, month, day, *args, **keywargs):
  return datetime.now() + timedelta( days=day+month*30+ 12*year);

class testmemeorise(unittest.TestCase):

    @freeze_time("2020-12-06")
    def test_function_day_check_storage(self, *args, **keywargs):
        """
               check if values gets stored and is in cache
        """
        memorise_day = undertest.memorise_class()
        memorise_day.memoize(add_to_time, 1, 5, 6, timeout=500)
        self.assertEqual(memorise_day.table[(1, 5, 6)]["value"] ,datetime.now()+ timedelta( days=6+5*30+ 12*1))

    def test_function_check_timeouts(self, *args, **keywargs):
        """
               check time outs
        """
        memorise_day = undertest.memorise_class()
        with freeze_time("2020-12-06"):# set first value
            memorise_day.memoize(add_to_time, 1, 5, 6, timeout=5000)
        with freeze_time("2020-12-06 00:0:7"):# change time to cause timeout
            memorise_day.memoize(add_to_time, 1, 5, 6, timeout=5000)
            self.assertEqual(memorise_day.table[(1, 5, 6)]["time"],datetime.now() )#checking if timeout by checking time stamp
        with freeze_time("2020-12-06 00:0:4"):# change time but this time timeout should not happen
            memorise_day.memoize(add_to_time, 1, 5, 6, timeout=5000)
            self.assertNotEqual(memorise_day.table[(1, 5, 6)]["time"], datetime.now())  # checking if timeout is not triggered by checking time stamp

if __name__ == '__main__':
    unittest.main()





