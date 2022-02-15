import unittest

class WorkerTestsMy(unittest.TestCase):
    def setUp(self):
        self.worker = Worker("Bai Ivan", 2000, 21)

    def test_worker_name(self):
        result = self.worker.name
        expected_result = "Bai Ivan"
        self.assertEqual(result, expected_result)

    def test_worker_salary(self):
        result = self.worker.salary
        expected_result = 2000
        self.assertEqual(result, expected_result)

    def test_worker_name(self):
        result = self.worker.energy
        expected_result = 21
        self.assertEqual(result, expected_result)

    def test_is_worker_energy_incremented_after_rest(self):
        self.worker.rest()
        result = self.worker.energy
        expected_result = 22
        self.assertEqual(result, expected_result)

    def test_error_if_work_with_negative_or_zero_energy(self):
        self.worker.energy = 0
        with self.assertRaises(Exception) as cm:
            self.worker.work()
        the_exception = cm.exception
        print(the_exception)
        self.assertEqual(str(the_exception), 'Not enough energy.')

    def test_work_method_increase_of_money_with_salary(self):
        self.worker.money = 0
        self.worker.salary = 10
        self.worker.work()
        result = self.worker.money
        expected_result = 10
        self.assertEqual(result, expected_result)

    def test_work_method_decrease_of_energy(self):
        self.worker.energy = 21
        self.worker.work()
        result = self.worker.energy
        expected_result = 20
        self.assertEqual(result, expected_result)

    def test_get_info(self):
        self.worker.money = 100
        result = self.worker.get_info()
        expected_result = 'Bai Ivan has saved 100 money.'
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()




